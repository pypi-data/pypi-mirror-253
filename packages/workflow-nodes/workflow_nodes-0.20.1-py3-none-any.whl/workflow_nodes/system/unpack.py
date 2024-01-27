# Copyright 2021 Karlsruhe Institute of Technology
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
import os
import shutil

import click
from xmlhelpy import option
from xmlhelpy import Path

from .main import system


@system.command()
@option(
    "unpacktarget",
    char="c",
    description="Archive to be unpacked.",
    required=True,
    param_type=Path(path_type="file", exists=True),
)
@option(
    "outputpath",
    char="p",
    description="Target directory path. Defaults to a folder in the current working"
    " directory using the base name of the archive.",
    param_type=Path(path_type="directory", exists=True),
)
@option("force_overwrite", char="o", is_flag=True)
@option("delete_compressed_folder", char="d", is_flag=True)
def unpack(unpacktarget, outputpath, force_overwrite, delete_compressed_folder):
    """Wrapper node for unpacking archives."""
    unpacked = False
    unpacktarget = os.path.expanduser(unpacktarget)
    compresseditem = os.path.basename(unpacktarget)

    if outputpath:
        outputpath = os.path.expanduser(outputpath)
    else:
        outputpath = os.path.splitext(compresseditem)[0]

    if force_overwrite or not os.path.isdir(outputpath):
        shutil.unpack_archive(unpacktarget, outputpath)
        click.echo(
            f"Unpacked compressed folder '{compresseditem}' into the folder"
            f" '{outputpath}'.",
            err=True,
        )
        unpacked = True
    elif os.path.isdir(outputpath):
        click.echo(
            "Target already exists and won't be overwritten! If you want to overwrite"
            " it, please use the flag 'force_overwrite'.",
            err=True,
        )

    if delete_compressed_folder and unpacked:
        os.remove(unpacktarget)
