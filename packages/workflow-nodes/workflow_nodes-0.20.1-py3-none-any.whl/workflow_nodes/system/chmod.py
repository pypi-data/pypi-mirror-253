# Copyright 2022 Karlsruhe Institute of Technology
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
import subprocess
import sys

import click
from xmlhelpy import argument
from xmlhelpy import Choice
from xmlhelpy import option

from .main import system
from workflow_nodes.utils import check_binary


@system.command()
@argument("filepath", description="Path to the file.")
@option(
    "usertype",
    char="u",
    description="The usertype the permission applies to.",
    param_type=Choice(["u", "g", "o"]),
)
@option(
    "operator",
    char="o",
    description="The operator to determine whether to remove, add or set the"
    " permission.",
    required=True,
    param_type=Choice(["-", "+", "="]),
)
@option(
    "type",
    char="t",
    description="The type of permission.",
    required=True,
    param_type=Choice(["r", "w", "x"]),
    var_name="permission_type",
)
def chmod(filepath, usertype, operator, permission_type):
    """Wrapper node for basic chmod operations."""
    check_binary("chmod")

    cmd = ["chmod"]
    permission = f"{operator}{permission_type}"

    if usertype:
        permission = f"{usertype}{permission}"

    cmd += [permission, filepath]

    click.echo(" ".join(cmd), err=True)
    sys.exit(subprocess.run(cmd).returncode)
