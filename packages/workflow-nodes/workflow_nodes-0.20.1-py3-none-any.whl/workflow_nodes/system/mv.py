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
import glob
import os
import subprocess
import sys

import click
from xmlhelpy import argument
from xmlhelpy import option

from .main import system
from workflow_nodes.utils import check_binary


@system.command()
@argument("sources", description="Source(s) to be moved.", nargs=-1)
@argument("destination", description="Target destination or directory.")
@option(name="force", description="Force the move command.", is_flag=True)
def mv(sources, destination, force):
    """Wrapper node for mv."""
    check_binary("mv")

    destination = os.path.expanduser(destination)

    if os.path.isdir(destination):
        files = []

        for filename in sources:
            files.extend(glob.glob(os.path.expanduser(filename)))

        cmd = ["mv", "-t", destination, *files]
    else:
        if len(sources) > 1:
            raise ValueError(
                "Destination must be a directory when moving multiple sources."
            )

        cmd = ["mv", sources[0], destination]

    if force:
        cmd += ["-f"]

    # Do not write to stdout to keep output intact for piping.
    click.echo(" ".join(cmd), err=True)
    sys.exit(subprocess.run(cmd).returncode)
