#  Copyright 2023 The Jaxampler Authors
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import annotations

from functools import partial
from typing import Any, Optional

from jax import jit, numpy as jnp
from jax.scipy.special import erf

from ..typing import Numeric
from ..utils import jxam_array_cast
from .rvs import RandomVariable


class Boltzmann(RandomVariable):
    def __init__(self, a: Numeric | Any, name: Optional[str] = None) -> None:
        shape, self._a = jxam_array_cast(a)
        self.check_params()
        super().__init__(name=name, shape=shape)

    def check_params(self) -> None:
        assert jnp.all(self._a > 0.0), "a must be positive"

    @partial(jit, static_argnums=(0,))
    def _logpdf_x(self, x: Numeric) -> Numeric:
        logpdf_val = 2 * jnp.log(x) - 0.5 * jnp.power(x / self._a, 2)
        logpdf_val -= 0.5 * jnp.log(jnp.pi * 0.5) + 3 * jnp.log(self._a)
        logpdf_val = jnp.where(x > 0.0, logpdf_val, -jnp.inf)
        return logpdf_val

    @partial(jit, static_argnums=(0,))
    def _logcdf_x(self, x: Numeric) -> Numeric:
        return jnp.log(self._cdf_x(x))

    @partial(jit, static_argnums=(0,))
    def _cdf_x(self, x: Numeric) -> Numeric:
        cdf_val = jnp.log(x) - 0.5 * jnp.power(x / self._a, 2)
        cdf_val -= 0.5 * jnp.log(jnp.pi * 0.5) + jnp.log(self._a)
        cdf_val = jnp.exp(cdf_val)
        cdf_val = erf(x / (jnp.sqrt(2) * self._a)) - cdf_val
        return cdf_val

    def __repr__(self) -> str:
        string = f"Boltzmann(a={self._a}"
        if self._name is not None:
            string += f", name={self._name}"
        string += ")"
        return string
