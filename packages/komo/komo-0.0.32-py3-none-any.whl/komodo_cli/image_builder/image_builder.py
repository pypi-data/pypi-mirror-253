import os
import uuid
from typing import Optional

import docker
from loguru import logger

import komodo_cli.printing as printing
from komodo_cli.types import ImageBuildException, ImagePushException

KOMODO_DOCKERFILE_NAME = "komodo.Dockerfile"


class ImageBuilder:
    def __init__(self, base_image, project_dir):
        self.dockerfile = f"FROM {base_image}"
        requirements_file = os.path.join(project_dir, "requirements.txt")
        if os.path.isfile(requirements_file):
            self.dockerfile += "\nCOPY requirements.txt /tmp/requirements.txt"
            if base_image.startswith("nvcr.io/nvidia"):
                # uninstall opencv to allow the user to install it without issues
                self.dockerfile += "\nRUN pip uninstall -y opencv"
                self.dockerfile += (
                    "\nRUN rm -rf /usr/local/lib/python*/dist-packages/cv2/"
                )
                self.dockerfile += "\nRUN apt update -y"
                self.dockerfile += "\nRUN apt install -y libgl1-mesa-glx"
            self.dockerfile += (
                "\nRUN pip install --no-cache-dir -r /tmp/requirements.txt"
            )
        self.project_dir = project_dir
        self.client = docker.from_env()

    def add_overlay(self, overlay_dir, dest_dir):
        self.dockerfile += f"\nCOPY {overlay_dir} {dest_dir}"

    def set_workdir(self, workdir):
        self.dockerfile += f"\nWORKDIR {workdir}"

    def add_aws_cli(self):
        self.dockerfile += '\nRUN command -v aws >/dev/null 2>&1 || { curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"; unzip awscliv2.zip; ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update; rm -rf aws; rm -rf awscliv2.zip; }'

    def add_aws_efa(self):
        self.dockerfile += "\nRUN apt update"
        self.dockerfile += "\nRUN curl -O https://efa-installer.amazonaws.com/aws-efa-installer-1.30.0.tar.gz"
        self.dockerfile += "\nRUN tar -xf aws-efa-installer-1.30.0.tar.gz && cd aws-efa-installer && ./efa_installer.sh -y --mpi=openmpi4 --skip-kmod --skip-limit-conf --no-verify"
        self.dockerfile += "\nRUN apt-get install -y libhwloc-dev"
        self.dockerfile += "\nRUN wget https://github.com/aws/aws-ofi-nccl/releases/download/v1.7.4-aws/aws-ofi-nccl-1.7.4-aws.tar.gz && tar -xf aws-ofi-nccl-1.7.4-aws.tar.gz && cd aws-ofi-nccl-1.7.4-aws && ./configure --prefix=/opt/aws-ofi-nccl --with-mpi=/opt/amazon/openmpi --with-libfabric=/opt/amazon/efa --with-cuda=/usr/local/cuda --enable-platform-aws"
        self.dockerfile += '\nENV PATH="/opt/amazon/openmpi/bin/:${PATH}"'
        self.dockerfile += "\nRUN make && make install; exit 0"

    def build_image(self, overlay_images_repository: Optional[str] = None):
        printing.info("Building image...")
        dockerfile_path = os.path.join(self.project_dir, KOMODO_DOCKERFILE_NAME)
        with open(dockerfile_path, "w") as f:
            f.write(self.dockerfile)

        uid = str(uuid.uuid4())
        if overlay_images_repository:
            tag = f"{overlay_images_repository}:{uid}"
        else:
            tag = f"komodo-overlay:{uid}"

        try:
            image, build_logs = self.client.images.build(
                path=os.path.dirname(dockerfile_path),
                tag=tag,
                quiet=False,
                rm=True,
                pull=True,
                forcerm=True,
                dockerfile=dockerfile_path,
                platform="linux/amd64",  # TODO
            )
            return image
        except (
            docker.errors.BuildError,
            docker.errors.APIError,
            TypeError,
        ) as e:
            raise ImageBuildException(str(e))
        except Exception as e:
            raise e
        finally:
            os.remove(dockerfile_path)

    def push_image(self, image, overlay_images_repository):
        printing.info("Pushing image...")
        try:
            resp = self.client.images.push(
                overlay_images_repository,
                image.tags[0].split(":")[-1],
                stream=True,
                decode=True,
            )

            for line in resp:
                if "error" in line:
                    raise ImagePushException(line["error"])
        except ImagePushException as e:
            raise e
        except Exception as e:
            raise ImagePushException(str(e))
