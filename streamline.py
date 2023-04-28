#!/usr/bin/env python

import click
import pathlib
from pathlib import Path
import time
import subprocess
import sys

def error(message):
    click.secho("error: ", fg="red", bold=True, nl=False)
    click.secho(message)

def success(message):
    click.secho("success: ", fg="green", bold=True, nl=False)
    click.secho(message)

def info(message):
    click.secho("info: ", fg="blue", bold=True, nl=False)
    click.secho(message)

@click.group()
def cli():
    pass

@cli.command()
@click.option("--name", default=Path.cwd().name, help="The name of the project.")
@click.option("--edition", default="17", help="The version of C++ to use. Options include: 98, 11, 14, 17, 20, 23, and 26. Compiler availability has an impact.")
def init(name, edition):
    # Check that the project name is valid
    valid_characters = [c for c in name if c.islower() or c.isdigit() or c=='-' or c=='_']

    if len(valid_characters) != len(name):
        error("project names can only contain alphanumeric characters, hyphens, and underscores")
        return
    
    # Check that the C++ edition is valid
    if edition not in ["98", "11", "14", "17", "20", "23", "26"]:
        error("edition must be 98, 11, 14, 17, 20, 23, or 26")
        return

    # Check if the current directory is empty
    current_directory = Path(".")

    if any(current_directory.glob("*")):
        error(f"destination `{current_directory.resolve()}` is not empty")
        return

    # Populate via the Pitchfork Layout
    src_directory = Path(current_directory, "src")
    tools_directory = Path(current_directory, "tools")

    Path(current_directory, "build").mkdir() # Build output, has debug and release folders
    src_directory.mkdir() # Source code / header files
    Path(current_directory, "tests").mkdir() # Hold test files
    Path(current_directory, "external").mkdir() # Hold third-party libraries
    Path(current_directory, "data").mkdir() # Hold non-code files
    tools_directory.mkdir() # Hold scripts for project management (e.g. build, test, docs)
    Path(current_directory, "docs").mkdir() # Holds generated documents

    # Create `main.cpp`
    with (src_directory / "main.cpp").open("w", encoding="utf-8") as f:
        f.writelines("""#include <iostream>

int
main() {
    std::cout << "Hello, world!\\n";
    std::cout << "Goodbye, cruel world!\\n";
    
    return 0;
}
""")

    # Create `CMakeLists.txt`
    with (src_directory / "CMakeLists.txt").open("w", encoding="utf-8") as f:
        f.writelines(f"""cmake_minimum_required(VERSION 3.1)

project({name} VERSION 1.0
             LANGUAGES CXX)

add_executable(out main.cpp)

set_target_properties(out PROPERTIES
    CXX_STANDARD {edition}
    CXX_STANDARD_REQUIRED YES
    CXX_EXTENSIONS NO
)""")
    
    # Create `build_debug.py`
    with (tools_directory / "build_debug.py").open("w", encoding="utf-8") as f:
        f.writelines("""import pathlib
from pathlib import Path
import subprocess

directory_of_script = Path(__file__).parent.resolve()

subprocess.call(["cmake", "-S", "../src", "-B", "../build/debug"], cwd=directory_of_script)
subprocess.call(["cmake", "--build", "../build/debug"], cwd=directory_of_script)
""")

    # Create `build_release.py`
    with (tools_directory / "build_release.py").open("w", encoding="utf-8") as f:
        f.writelines("""import pathlib
from pathlib import Path
import subprocess

directory_of_script = Path(__file__).parent.resolve()

subprocess.call(["cmake", "-DCMAKE_BUILD_TYPE=Release", "-S", "../src", "-B", "../build/release"], cwd=directory_of_script)
subprocess.call(["cmake", "--build", "../build/release"], cwd=directory_of_script)
""")

    # Create `run.py`
    with (tools_directory / "run.py").open("w", encoding="utf-8") as f:
        f.writelines("""import pathlib
from pathlib import Path
import subprocess
import sys

directory_of_script = Path(__file__).parent.resolve()

subprocess.call(["../build/debug/out"], cwd=directory_of_script)
""")

    # Create `.gitignore`
    with (current_directory / ".gitignore").open("w", encoding="utf-8") as f:
        f.writelines(""".streamline
build""")

    success("created new project")

    # Add Google Test

    # Add Doxygen

@cli.command()
@click.option("--release", is_flag=True)
def build(release):
    if release:
        run_build_release_py()
    else:
        run_build_debug_py()

def run_build_debug_py():
    # Check that `build_debug.py` exists
    build_debug_py = Path(".") / "tools/build_debug.py"

    if not build_debug_py.exists():
        error("could not find `build.py` in `./tools/build_debug.py`")
        return False
    
    # Run `build_debug.py`
    subprocess.call([sys.executable, build_debug_py])

    success("finished debug build")

    return True

def run_build_release_py():
    # Check that `build_release.py` exists
    build_release_py = Path(".") / "tools/build_release.py"

    if not build_release_py.exists():
        error("could not find `build.py` in `./tools/build_release.py`")
        return False
    
    # Run `build_release.py`
    subprocess.call([sys.executable, build_release_py])

    success("finished release build")

    return True

def run_run_py():
    # Check that `run.py` exists
    run_py = Path(".") / "tools/run.py"

    if not run_py.exists():
        error("could not find `run.py` in `./tools/run.py`")
        return
    
    # Run `run.py`
    subprocess.call([sys.executable, run_py])

@cli.command()
def run():
    was_found = run_build_debug_py()

    if not was_found:
        return

    # Add a space to separate the build and run outputs
    click.echo()

    run_run_py()

if __name__ == "__main__":
    cli()