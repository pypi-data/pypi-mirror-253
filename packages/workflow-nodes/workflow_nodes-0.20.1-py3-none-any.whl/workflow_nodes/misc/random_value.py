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
import random

import click
from xmlhelpy import Float
from xmlhelpy import Integer
from xmlhelpy import option

from .main import misc


@misc.command()
@option(
    "min_value", description="Minimum value possible.", required=True, param_type=Float
)
@option(
    "max_value", description="Maximum value possible.", required=True, param_type=Float
)
@option(
    "step_size",
    description="Step size between the possible random values.",
    required=True,
    param_type=Float,
)
@option(
    "seed",
    description="Seed value for deterministic random values.",
    param_type=Integer,
    default=0,
)
def random_value(min_value, max_value, step_size, seed):
    """Generate a pseudo-random number within a specified range and step.

    Note that the generated numbers are pseudo-random and should not be used for
    security-related purposes.
    """
    if seed:
        random.seed(seed)

    value = random.random()

    scaled_value = value * (max_value - min_value)
    scaled_value = scaled_value // step_size * step_size
    value = min_value + scaled_value

    click.echo(value)
