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


import sys

import jax
import jax.numpy as jnp
import pytest
from jax.scipy.stats import binom as jax_binom


sys.path.append("../jaxampler")
from jaxampler.rvs import Binomial


class TestBinomial:
    def test_all_positive(self):
        assert jnp.allclose(
            Binomial(p=0.5, n=10, name="test_logpmf_p0.5").logpmf(5),
            jax_binom.logpmf(5, 10, 0.5),
        )

    def test_small_p(self):
        assert jnp.allclose(
            Binomial(p=0.0001, n=100, name="test_pmf_p0.0001").pmf(5),
            jax_binom.pmf(5, 100, 0.0001),
        )
        assert jnp.allclose(
            Binomial(p=0.0001, n=10, name="test_logpmf_p0.0001").logpmf(5),
            jax_binom.logpmf(5, 10, 0.0001),
        )

    def test_p_out_of_range(self):
        with pytest.raises(AssertionError):
            Binomial(p=1.1, n=10, name="test_logpmf_p1.1")

    def test_large_n(self):
        assert jnp.allclose(
            Binomial(p=0.1, n=100).logpmf(50),
            jax_binom.logpmf(50, 100, 0.1),
        )
        assert jnp.allclose(
            Binomial(p=0.5, n=1000, name="test_pmf_p0.5").pmf(5),
            jax_binom.pmf(5, 1000, 0.1),
        )
        assert jnp.allclose(
            Binomial(p=0.5, n=[10, 20], name="test_pmf_n2").pmf(5),
            jax_binom.pmf(5, jnp.asarray([10, 20]), 0.5),
        )
        assert jnp.allclose(
            Binomial(p=0.1, n=100000, name="test_pmf_p0.1n100000").pmf(50),
            jax_binom.pmf(50, 100000, 0.1),
        )

    def test_shapes(self):
        assert Binomial(p=0.5, n=[10, 20], name="test_logpmf_n2").logpmf(5).shape == (2,)
        assert Binomial(p=[0.5, 0.1], n=[10, 20], name="test_logpmf_p2n2").logpmf(5).shape == (2,)
        assert Binomial(p=[0.5, 0.1, 0.3], n=[10, 20, 30], name="test_logpmf_p3n3").logpmf(5).shape == (3,)
        assert jnp.allclose(
            Binomial(p=[0.5, 0.1], n=[10, 20], name="test_pmf_p2n2").pmf(5),
            jax_binom.pmf(5, jnp.asarray([10, 20]), jnp.asarray([0.5, 0.1])),
        )
        assert Binomial(p=[[0.5, 0.1], [0.4, 0.1]], n=[[10], [20]], name="test_pmf_p2x3n2").pmf(5).shape == (2, 2)
        assert Binomial(p=[[0.5, 0.1], [0.4, 0.1]], n=[10, 20], name="test_pmf_p2x3n2").pmf(5).shape == (2, 2)

    def test_incompatible_shapes(self):
        with pytest.raises(ValueError):
            Binomial(p=[[0.5, 0.1, 0.3], [0.4, 0.1, 0.2]], n=[10, 20], name="test_pmf_p2x3n2")

    def test_cdf(self):
        bin_cdf = Binomial(p=0.2, n=12, name="test_cdf")
        assert bin_cdf.cdf(13) == 1.0
        assert bin_cdf.cdf(-1) == 0.0
        assert bin_cdf.cdf(9) >= 0.0
        assert bin_cdf.cdf(9) <= 1.0

    def test_rvs(self):
        bin_rvs = Binomial(p=0.6, n=[5, 23], name="tets_rvs")
        shape = (3, 4)

        # with key
        key = jax.random.PRNGKey(123)
        result = bin_rvs.rvs(shape, key)
        assert result.shape, shape + bin_rvs._shape

        # without key
        result = bin_rvs.rvs(shape)
        assert result.shape, shape + bin_rvs._shape
