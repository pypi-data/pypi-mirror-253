import os

import pytest
import numpy as np


@pytest.mark.shard
def test_insert(db_shard):
    db_shard.insert(np.ones(5))
    assert db_shard.ref
    assert db_shard.vector_count == 1
    assert os.path.isfile(db_shard.ref)

@pytest.mark.shard
def test_len(db_shard):
    db_shard.insert(np.ones(5))
    assert len(db_shard) == 1

@pytest.mark.shard
def test_get(db_shard):
    db_shard.insert(np.ones(5))
    gen = db_shard.get_data(False, 0, 0)
    assert np.array_equal(next(gen), np.ones(5))

@pytest.mark.shard
def test_delete(db_shard):
    db_shard.insert(np.ones(5))
    db_shard.delete(np.ones(5), first = True)
    assert len(db_shard) == 0