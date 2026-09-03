from __future__ import annotations

import os
import shutil
from doctest import Example
from pathlib import Path
from typing import List

import nox

nox.options.default_venv_backend = "uv"


repo_root = Path(__file__).parent
build_root = repo_root / "build"
dist_root = repo_root / "dist"
build_root.mkdir(parents=True, exist_ok=True)


@nox.session(reuse_venv=True)
def format_latex(session):
    session.run_install("uv", "sync", "--all-packages")
    session.run("uv", "run", "badness", "format", ".")


@nox.session(reuse_venv=True)
def build_latex(session):
    _run_latex(session, repo_root.joinpath("exercices/constellations.tex"))


def _run_latex(
    session: nox.Session,
    src_file: Path,
    name: str | None = None,
    extra_def: dict[str, str] | None = None,
    extra_texinputs: list[Path] | None = None,
    latexmk_args: list[str] | None = None,
) -> Path:
    name = name or src_file.stem
    extra_def = extra_def or {}
    extra_texinputs = extra_texinputs or []
    latexmk_args = latexmk_args or []

    build_directory = build_root.joinpath(f"latexmk/{name}")
    working_directory = src_file.parent
    built_file = working_directory.joinpath(f"{src_file.stem}.pdf")

    working_directory.mkdir(parents=True, exist_ok=True)

    proc_env = os.environ.copy()

    proc_env["TEXINPUTS"] = ":".join(
        *proc_env.get("TEXINPUTS", "").split(":"), *extra_texinputs
    )

    latex_def = " ".join(rf"\def\{key}{{{value}}}" for key, value in extra_def.items())

    pdflatex_cmd = (
        rf"-pdflatex=pdflatex -interaction=nonstopmode %O '{latex_def}\input{{%S}}'"
    )

    # latexmk_args.extend(("-use-make", pdflatex_cmd))

    with session.chdir(working_directory):
        session.run(
            *[
                "latexmk",
                "-pdf",
                "-dvi-",
                "-ps-",
                "-f",
                f"-output-directory={build_directory}",
                *latexmk_args,
                "-xelatex",
                src_file.resolve(),
            ],
            env=proc_env,
        )

    return built_file
