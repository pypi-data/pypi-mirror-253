import pytest

import numpy as np

from lvdb.lvinstance import LVInstance
from lvdb.lvshard import LVShard
from lvdb.db_cache import DBCache
from lvdb.profiler import Profiler

@pytest.fixture(autouse=True)
def db_instance():
    e_db = LVInstance(3, reference=np.random.rand(5))

    # yield fixture for teardown
    yield e_db

    e_db.clear()

@pytest.fixture
def db_shard():
    s1 = LVShard(100, 'cpu')

    yield s1

    s1.clear()

@pytest.fixture
def profiler_instance():
    return Profiler(3)

@pytest.fixture
def cache_instance():
    return DBCache()