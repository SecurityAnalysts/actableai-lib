import numpy as np
import pytest
import ray

from actableai.utils.testing import init_ray as _init_ray
from actableai.utils import is_gpu_available as _is_gpu_available


@pytest.fixture(scope="function")
def np_rng(random_state=0):
    yield np.random.default_rng(random_state)


@pytest.fixture(scope="function")
def init_ray():
    if not ray.is_initialized():
        _init_ray()

        yield None

        ray.shutdown()
    else:
        yield None


@pytest.fixture(scope="session")
def is_gpu_available():
    return _is_gpu_available()
