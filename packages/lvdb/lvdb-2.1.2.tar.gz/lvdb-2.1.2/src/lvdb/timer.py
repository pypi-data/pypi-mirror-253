import os
import time
import psutil
from typing import Callable


def get_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def store_time(f: Callable):
    """
    A decorator to compute and store time taken and memory usage for database operations.
    """
    def inner(*args, **kwargs):
        if args[0].profile:
            start_time = time.time()
            shard_id = f(*args, **kwargs)
            end_time = time.time()
            if f.__name__ == "add" or f.__name__ == "batch_add":
                args[0].profiler.add_time(end_time - start_time, shard_id)
            elif f.__name__ == "query_norm_range" or f.__name__ == "query_vector_range":
                for s_id in shard_id[1]:
                    args[0].profiler.add_access(end_time - start_time, s_id)
            else:
                args[0].profiler.add_access(end_time - start_time, shard_id)
            args[0].profiler.add_mem(get_memory() / (10 ** 9))
            return shard_id
        else:
            return f(*args, **kwargs)
    return inner





