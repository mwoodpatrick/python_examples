import datetime as dt
from pathlib import Path

import click
import rich
import toml

from dcsbt.manifest import DcSimManifest
from dcsbt.update import update_gpu_driver, update_gpu_fmodel


def collect(src_dcsim_git_tree: Path, manifest_file: Path, dst_repo: Path):
    """Collect a repository package base on the given manifest file"""
    raw: dict = toml.load(manifest_file)
    manifest = DcSimManifest.parse(raw)

    now: str = dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    manifest.collect(
        src_dcsim_git_tree=src_dcsim_git_tree,
        target_repo=dst_repo,
        extra_info={
            "last_collect_time": now,
        },
    )


def build(working_dcsim_git_tree: Path, repo_path: Path, dst: Path):
    """Create a DCSim result package base on repo given"""
    breakpoint()
    manifest = DcSimManifest.restore(target_repo=repo_path)
    rich.print(manifest)
    manifest.build(
        working_dcsim_git_tree=working_dcsim_git_tree, repo_path=repo_path, dst=dst
    )


@click.group()
def app():
    """DCSim CLI - A command line interface for managing DCSim operations."""


@app.command()
def dev() -> None:
    manifest_file: Path = Path("manifest.toml")
    repo: Path = Path("repo")
    git_root: Path = Path("../../..")
    fianl_build_loc: Path = Path("artifacts")

    collect(src_dcsim_git_tree=git_root, manifest_file=manifest_file, dst_repo=repo)
    build(working_dcsim_git_tree=git_root, repo_path=repo, dst=fianl_build_loc)


ARG_PATH_NEED_EXIST = click.Path(
    exists=True,
    resolve_path=True,
    path_type=Path,
)

ARG_PATH_NOT_NEED_EXIST = click.Path(
    exists=False,
    resolve_path=True,
    path_type=Path,
)


@app.command(name="collect")
@click.option(
    "--dcsim-git-tree",
    required=True,
    type=ARG_PATH_NEED_EXIST,
    help="Path to DCSim git tree",
)
@click.option(
    "--manifest-file",
    required=True,
    type=ARG_PATH_NEED_EXIST,
    help="Path to DCSim Manifest file",
)
@click.option(
    "--dst-repo",
    required=True,
    type=ARG_PATH_NOT_NEED_EXIST,
    help="Path to your output satellite-source repo",
)
def cmd_collect(dcsim_git_tree: Path, manifest_file: Path, dst_repo: Path):
    """Collect a repository package base on the given manifest file.

    This is the first stage of DCSim build
    """
    collect(
        src_dcsim_git_tree=dcsim_git_tree,
        manifest_file=manifest_file,
        dst_repo=dst_repo,
    )


@app.command(name="build")
@click.option(
    "--dcsim-git-tree",
    required=True,
    type=ARG_PATH_NEED_EXIST,
    help="Path to DCSim git tree",
)
@click.option(
    "--src-repo",
    required=True,
    type=ARG_PATH_NEED_EXIST,
    help="Path to satellite-source repo",
)
@click.option(
    "--dst-pkg", required=True, type=ARG_PATH_NEED_EXIST, help="Path to your output pkg"
)
def cmd_build(dcsim_git_tree: Path, src_repo: Path, dst_pkg: Path):
    """Create a DCSim result package base on a repo containing all dependecies.

    This is the second stage of DCSim build
    """
    build(working_dcsim_git_tree=dcsim_git_tree, repo_path=src_repo, dst=dst_pkg)
