# Copyright 2023 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import platform
import subprocess

import click
from xmlhelpy import argument

from .main import wsl
from workflow_nodes.utils import check_binary


def detect_virtualization_technique():
    """For detecting if virtualization technique is WSL"""
    try:
        output = subprocess.run(
            ["systemd-detect-virt"],
            capture_output=True,
            text=True,
        )
        return output.stdout.strip().lower()
    except FileNotFoundError as fe:
        if "wsl" in platform.uname().release.lower():
            return "wsl"

        return f"FileNotFoundError: {fe}"
    except Exception as e:
        return f"Error: {e}"


def convert_to_win_path_format(path, flag):
    """Wrapper for wslpath utility"""
    check_binary("wslpath")
    result = subprocess.run(
        ["wslpath", flag, path], stdout=subprocess.PIPE, text=True, check=True
    )
    return result.stdout.strip()


@wsl.command()
@argument("path", description="File path to be converted", required=True)
def convert_path(path):
    """For converting WSL file paths into Windows file paths"""
    virtualization_info = detect_virtualization_technique()

    if virtualization_info != "wsl":
        # If not WSL
        click.echo(virtualization_info, err=True)
        click.echo(path)
    else:
        # Path is in WSL format, so convert it to Windows format
        click.echo(convert_to_win_path_format(path, "-m"))
