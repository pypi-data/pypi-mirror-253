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
import operator as op

import click
from xmlhelpy import Choice
from xmlhelpy import option

from .main import misc


OPS = {"<": op.lt, "<=": op.le, "==": op.eq, "!=": op.ne, ">=": op.ge, ">": op.gt}


@misc.command()
@option(
    "leftside", char="l", description="The left side of the comparison.", required=True
)
@option(
    "operator",
    char="o",
    description="The operator of the comparison.",
    required=True,
    param_type=Choice(list(OPS)),
)
@option(
    "rightside",
    char="r",
    description="The right side of the comparison.",
    required=True,
)
@option(
    "cast_to_int",
    char="i",
    description="Cast the numbers to integers instead of floats.",
    is_flag=True,
)
def compare_number(leftside, operator, rightside, cast_to_int):
    """Compare two numbers and print the resulting boolean."""
    leftside = float(leftside)
    rightside = float(rightside)

    if cast_to_int:
        leftside = int(leftside)
        rightside = int(rightside)

    click.echo(OPS[operator](leftside, rightside))
