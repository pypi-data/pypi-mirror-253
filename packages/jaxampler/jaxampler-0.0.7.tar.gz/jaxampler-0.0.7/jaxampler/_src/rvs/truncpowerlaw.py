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

import jax
from jax import jit, numpy as jnp
from jaxtyping import Array

from ..typing import Numeric
from ..utils import jxam_array_cast
from .rvs import RandomVariable


class TruncPowerLaw(RandomVariable):
    def __init__(
        self,
        alpha: Numeric | Any,
        low: Numeric | Any,
        high: Numeric | Any,
        name: Optional[str] = None,
    ) -> None:
        shape, self._alpha, self._low, self._high = jxam_array_cast(alpha, low, high)
        self.check_params()
        self._beta = 1.0 + self._alpha
        self._logZ = self.logZ()
        super().__init__(name=name, shape=shape)

    def check_params(self) -> None:
        assert jnp.all(self._low > 0.0), "low must be greater than 0"
        assert jnp.all(self._high > self._low), "high must be greater than low"

    @partial(jit, static_argnums=(0,))
    def logZ(self) -> Numeric:
        logZ_val = jnp.where(
            self._beta == 0.0,
            jnp.log(jnp.log(self._high) - jnp.log(self._low)),
            jnp.log(jnp.abs(jnp.power(self._high, self._beta) - jnp.power(self._low, self._beta)))
            - jnp.log(jnp.abs(self._beta)),
        )
        return logZ_val

    @partial(jit, static_argnums=(0,))
    def Z(self) -> Numeric:
        return jnp.exp(self._logZ)

    @partial(jit, static_argnums=(0,))
    def _logpdf_x(self, x: Numeric) -> Numeric:
        logpdf_val: Numeric = jnp.log(x) * self._alpha - self._logZ
        logpdf_val = jnp.where((x >= self._low) * (x <= self._high), logpdf_val, -jnp.inf)
        return logpdf_val

    @partial(jit, static_argnums=(0,))
    def _logcdf_x(self, x: Numeric) -> Numeric:
        conditions = [
            x < self._low,
            x > self._high,
            self._beta == 0.0,
            self._beta != 0.0,
        ]
        choices = [
            -jnp.inf,
            jnp.log(1.0),
            jnp.log(jnp.log(x) - jnp.log(self._low)) - self._logZ,
            jnp.log(jnp.abs(jnp.power(x, self._beta) - jnp.power(self._low, self._beta)))
            - jnp.log(jnp.abs(self._beta))
            - self._logZ,
        ]
        return jnp.select(conditions, choices)

    @partial(jit, static_argnums=(0,))
    def _logppf_x(self, x: Numeric) -> Numeric:
        conditions = [
            x < 0.0,
            x > 1.0,
            self._beta == 0.0,
            self._beta != 0.0,
        ]
        choices = [
            -jnp.inf,
            jnp.log(1.0),
            x * jnp.log(self._high) + (1.0 - x) * jnp.log(self._low),
            jnp.power(self._beta, -1)
            * jnp.log(x * jnp.power(self._high, self._beta) + (1.0 - x) * jnp.power(self._low, self._beta)),
        ]
        return jnp.select(conditions, choices)

    def _rvs(self, shape: tuple[int, ...], key: Array) -> Array:
        U = jax.random.uniform(key=key, shape=shape, dtype=jnp.float32)
        rvs_val = self._ppf_v(U)
        return rvs_val

    def __repr__(self) -> str:
        string = f"TruncPowerLaw(alpha={self._alpha}, low={self._low}, high={self._high}"
        if self._name is not None:
            string += f", name={self._name}"
        string += ")"
        return string
