import pytest


@pytest.mark.profile
def test_add_time(profiler_instance):
    profiler_instance.add_time(0.01, 0)
    assert profiler_instance.add_times[-1] == 0.01
    assert profiler_instance.shard_access_rate[0] == 1

@pytest.mark.profile
def test_add_access(profiler_instance):
    profiler_instance.add_access(0.02, 1)
    assert profiler_instance.access_times[-1] == 0.02
    assert profiler_instance.shard_access_rate[1] == 1

@pytest.mark.profile
def test_add_mem(profiler_instance):
    profiler_instance.add_mem(0.03)
    assert profiler_instance.mem_usage[-1] == 0.03

@pytest.mark.profile
def test_process_device(profiler_instance):
    profiler_instance.process_device(0.5, 0.5)
    assert profiler_instance.cpu_usage[-1] == 0.5
    assert profiler_instance.gpu_usage[-1] == 0.5

@pytest.mark.profile
def test_process_cache_hit(profiler_instance):
    profiler_instance.process_cache(True)
    assert profiler_instance.cache_hit == 1

def test_process_cache_miss(profiler_instance):
    profiler_instance.process_cache(False)
    assert profiler_instance.cache_miss == 1

@pytest.mark.profile
def test_cache_utilization(profiler_instance):
    profiler_instance.process_cache(True)
    profiler_instance.process_cache(False)
    assert profiler_instance.cache_utilization() == (50.0, 50.0)

@pytest.mark.profile
def test_average_add(profiler_instance):
    profiler_instance.add_time(0.01, 0)
    assert profiler_instance.average_add_time() == 0.01

@pytest.mark.profile
def test_average_access(profiler_instance):
    profiler_instance.add_access(0.02, 1)
    assert profiler_instance.average_access_time() == 0.02
