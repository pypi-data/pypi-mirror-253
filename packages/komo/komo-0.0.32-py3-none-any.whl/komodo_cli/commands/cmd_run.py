import os
import time
from typing import Optional

import click
from loguru import logger
from vyper import Vyper

import komodo_cli.printing as printing
from komodo_cli.backends.backend import Backend
from komodo_cli.backends.backend_factory import BackendFactory
from komodo_cli.types import JobNotFoundException, JobStatus, TooManyNodes
from komodo_cli.utils import (
    APIClient, config_args_to_dict, handle_errors,
    update_context_project_config_with_backend_override,
    update_context_with_api_client, update_context_with_project_config,
    validate_backend_config, validate_overlay_images_repository)


@click.command("run")
@click.option(
    "--backend",
    "-b",
    type=str,
    default=None,
    help="Name of the backend to use.",
)
@click.option(
    "--resource",
    "-r",
    type=str,
    default=None,
    help="Resource type to use for the job as defined in the config file. Ignored for local jobs.",
)
@click.option(
    "--num_nodes",
    "-n",
    type=int,
    default=1,
    help="Number of nodes for the job",
)
@click.option(
    "--config",
    "-c",
    type=str,
    default="",
    help=(
        "Override any parameters in the section of your project config corresponding to the specified backend."
        "Values must be provided as a comma-separated list of key=value pairs."
    ),
)
@click.option("--detach", "-d", is_flag=True)
@click.argument("args", nargs=-1)
@click.pass_context
@handle_errors
def cmd_run(
    ctx: click.Context,
    backend: Optional[str],
    resource: Optional[str],
    num_nodes: int,
    config: str,
    detach: bool,
    args,
):
    """Run a Komodo job."""
    backend_config_override = config_args_to_dict(config)
    _run_helper(
        ctx,
        backend,
        resource,
        num_nodes,
        backend_config_override,
        detach,
        args,
    )


def _run_helper(
    ctx: click.Context,
    backend_name: Optional[str],
    resource_name: Optional[str],
    num_nodes: int,
    backend_config_override: dict,
    detach: bool,
    args,
):
    update_context_with_api_client(ctx)
    update_context_with_project_config(ctx)

    project_config: Vyper = ctx.obj["project_config"]
    if backend_name is None:
        backend_name = project_config.get("default_backend")
        if backend_name is None:
            printing.error("No backend was specified", bold=True)
            exit(1)

    update_context_project_config_with_backend_override(
        ctx, backend_name, backend_config_override
    )
    project_backend_config = project_config.get("configs")[backend_name]
    try:
        validate_backend_config(backend_name, project_backend_config)
    except Exception as e:
        printing.error(f"Error while validating backend config: {str(e)}", bold=True)
        exit(1)

    api_client: APIClient = ctx.obj["api_client"]
    backend_schema = api_client.get_backend(backend_name)
    backend: Backend = BackendFactory.get_backend(
        backend_schema,
        api_client,
    )
    backend.assert_ready_for_use()

    if resource_name is None:
        resource_name = project_backend_config.get("default_resource")
        if resource_name is None:
            # resource not needed for local backend
            if backend_schema.type != "local":
                printing.error("No resource was specified", bold=True)
                exit(1)

    logger.info(f"Using backend {backend_name}")
    logger.info(f"Resource: {resource_name}")
    logger.info(f"Command: ({', '.join(args)})")

    workspace = project_backend_config.get("workspace", os.getcwd())
    workdir = project_backend_config.get("workdir", None)

    printing.info("Preparing docker image...")
    image = backend.prepare_image(
        project_backend_config["image"], ctx.obj["project_dir"], workspace, workdir
    )
    project_backend_config["image"] = image

    printing.info("Starting a job", bold=True)
    job = backend.run(
        args,
        num_nodes,
        resource_name,
        project_backend_config["image"],
        project_backend_config["env"],
        project_backend_config["mounts"],
        project_backend_config["workdir"],
    )

    printing.success(
        f"Created a {job.backend_name} job with ID {job.id}",
        bold=True,
    )

    if detach:
        return

    printing.info("Waiting for job to start...", bold=True)
    job_id = job.id

    while True:
        job = api_client.get_job(job_id)
        status = job.status
        if status != JobStatus.PENDING:
            break
        time.sleep(1)

    printing.success("Job started successfully")

    for line in backend.logs(job.backend_job_id, 0, True):
        if type(line) != str:
            line = line.decode("utf-8")
        printing.info(f"{line.strip()}")
