import os
import re

import pytest
import numpy as np

"""
Targeted tests: pytest -m <mark_name>
All tests: pytest
"""

@pytest.mark.instance
def test_shards(db_instance):
    shards = db_instance.shards
    for s in shards:
        assert len(shards[s]) is not None

@pytest.mark.instance
def test_add(db_instance):
    shard = db_instance.add(np.ones(5))
    assert shard is not None

@pytest.mark.instance
def test_batch_add(db_instance):
    db_instance.batch_add(np.ones((100, 5)))
    db_instance.batch_add(np.zeros((100, 5)))
    assert True

@pytest.mark.instance
def test_delete_one(db_instance):
    shard = db_instance.delete(np.ones(5), first = True)
    assert shard is not None

@pytest.mark.instance
def test_delete_all(db_instance):
    db_instance.delete(np.ones(5))
    assert True

@pytest.mark.instance
def test_query_vector_range(db_instance):
    matches, _ = db_instance.query_vector_range(np.zeros(5), np.ones(5))
    assert matches is not None

@pytest.mark.instance
def test_query_norm_range(db_instance):
    matches, _ = db_instance.query_norm_range(0.0,2.0)
    assert matches is not None

@pytest.mark.instance
def test_clear(db_instance):
    db_instance.clear()
    pattern = re.compile(r"lv_shrd\d+.npy")
    for filepath in os.listdir('./'):
        assert not pattern.match(filepath)