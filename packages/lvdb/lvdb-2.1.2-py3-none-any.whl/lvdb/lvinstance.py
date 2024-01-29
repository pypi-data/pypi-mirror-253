import sys
from bisect import bisect_left, bisect_right
from typing import Optional, Tuple

import numpy as np
import numpy.typing as npt

from .timer import store_time
from .lvshard import LVShard
from .profiler import Profiler
from .shard_math import normalize, shard_reference
from .error_handler import ErrorHandler
from .db_cache import DBCache


class LVInstance:
    """
    Vector Database Instance, supporting 1D and 2D data
    """

    def __init__(
        self,
        num_shards: int,
        reference: npt.NDArray | Tuple[int, ...],
        profile: Optional[bool] = False,
        ttl: Optional[int] = 0,
        device: Optional[str] = 'cpu'
    ):
        """
        :param num_shards: The number of shards in the database.
        :param reference: The reference vector for sharding, or the expected shape of the input data
        :param profile: Set to true to profile the usage statistics of the database.
        :param ttl: The time to live of cached requests, defined in number of function calls, default 0.
        :param device: The device that operations in the database will run on, defaults to cpu.
        """
        super(LVInstance, self).__init__()

        self.__device = device
        self.__set_device()

        self.__ttl = ttl
        self.__num_shards = num_shards
        self.__discretized_norms = np.linspace(0, 2, num_shards, endpoint = True)
        self.__shards = {i:LVShard(i, device) for i in range(len(self.__discretized_norms))}
        if type(reference) == np.ndarray:
            self.__reference_vector = normalize(reference)
        else:
            self.__reference_vector = normalize(np.random.random_sample(reference))

        self.profile = profile
        self.profiler = Profiler(num_shards)
        self.handler = ErrorHandler()
        self.cache = DBCache()

    def __set_device(self):
        if self.__device == 'gpu':
            try:
                import cupy as np
                import cupy.typing as npt
            except ImportError:
                import numpy as np
                import numpy.typing as npt
                self.__device = 'cpu'
                self.handler.device_warning()
        else:
            import numpy as np
            import numpy.typing as npt

    @property
    def shards(self):
        """
        Readonly Access to Shards
        """

        return self.__shards

    def clear(self):
        """
        Removes all generated files
        """

        for i in self.__shards:
            self.__shards[i].clear()

    @store_time
    def add(self, vector: npt.NDArray) -> int:
        """
        :param vector: The vector to be added.
        """

        v_ref = shard_reference(self.__reference_vector, normalize(vector))
        v_shard = bisect_left(self.__discretized_norms, v_ref)
        self.__shards[v_shard].insert(vector)

        return v_shard

    def batch_add(self, mat):
        """
        :param mat: The matrix of vectors to be added.
        """

        for row in mat:
            self.add(row)

    @store_time
    def delete(self, vector: npt.NDArray, first: Optional[bool] = True) -> int:
        """
        Deletes a vector, list of vectors, or a matrix of vectors from the database.
        :param vector: The vector to be deleted
        :param first: Set to false to to delete all occurrences of the provided data.
        :return: The shard_id the vector was deleted from
        """

        v_ref = shard_reference(self.__reference_vector, normalize(vector))
        s_id = bisect_left(self.__discretized_norms, v_ref)
        self.__shards[s_id].delete(vector, first)

        return s_id

    def batch_delete(self, mat, first: Optional[bool] = True):
        """
        :param mat: The matrix of vectors to be deleted
        :param first: Set to false to delete all occurrences of each row vector in mat
        """

        for row in mat:
            self.delete(row, first)

    @store_time
    def query_vector_range(self, left_bound: npt.NDArray, right_bound: npt.NDArray):
        """
        Returns all vectors that are between the two provided bound vectors
        :param left_bound: left bound for vector querying
        :param right_bound: right bound for vector querying
        :return: A list of generators for each shard of vectors within the given range and a list of shards accessed
        """

        l_norm, r_norm = normalize(left_bound), normalize(right_bound)
        l_ref = bisect_left(self.__discretized_norms, shard_reference(self.__reference_vector, l_norm))
        r_ref = bisect_right(self.__discretized_norms, shard_reference(self.__reference_vector, r_norm))

        l = min(l_ref, r_ref)
        r = max(l_ref, r_ref)

        if self.__ttl and self.cache.get((l, r)):
            if self.profile:
                self.profiler.process_cache(True)
            return self.cache.get((l, r))

        matches = [self.__shards[s_id].get_data(partial = (s_id == l or s_id == r), lo = l_norm, hi = r_norm) \
                   for s_id in range(l, r + 1)]

        if self.__ttl:
            self.cache.set((l, r), matches, self.__ttl)
            if self.profile:
                self.profiler.process_cache(False)

        return matches, [s_id for s_id in range(l, r + 1)]

    @store_time
    def query_norm_range(self, lower_norm: float, upper_norm: float):
        """
        Returns all vectors that are between the two provided norms
        :param lower_norm: Lower bound between 0 and 2
        :param upper_norm: Upper bound between 0 and 2
        :return: A list of generators for each shard of vectors within the given range and a list of shards accessed
        """

        if 0 > lower_norm or 0 > upper_norm or 2 < lower_norm or 2 < upper_norm:
            self.handler.query_error()

        l_ref = bisect_left(self.__discretized_norms, min(lower_norm, 2 - sys.float_info.epsilon))
        r_ref = bisect_right(self.__discretized_norms, min(upper_norm, 2 - sys.float_info.epsilon))

        l = min(l_ref, r_ref)
        r = max(l_ref, r_ref)

        if self.__ttl and self.cache.get((l, r)):
            if self.profile:
                self.profiler.process_cache(True)
            return self.cache.get((l, r))

        matches = [self.__shards[s_id].get_data(partial = (s_id == l or s_id == r), lo = lower_norm, hi = upper_norm) \
                   for s_id in range(l, r + 1)]

        if self.__ttl:
            self.cache.set((l, r), matches, self.__ttl)
            if self.profile:
                self.profiler.process_cache(False)

        return matches, [s_id for s_id in range(l, r + 1)]

    def get_stats(
        self,
        times: Optional[bool] = True,
        plot_times: Optional[bool] = True,
        cache_utilization: Optional[bool] = False,
        shard_access: Optional[bool] = False,
        device_usage: Optional[bool] = False,
        plot_mem: Optional[bool] = False
    ):
        """
        :param plot_mem: Plot the memory usage over time
        :param plot_times: Plot the add and access times over time
        :param times: Display the average add and access times
        :param cache_utilization: Display the cache hit/miss rate
        :param shard_access: Display a bar plot of the shard access rates
        :param device_usage: Displays a plot of the device usage rates for cpu and gpu
        """

        if not self.profile:
            self.handler.profile_warning()
            return
        if times:
            print(f"Average Insertion Time: {self.profiler.average_add_time()}")
            print(f"Average Access Time: {self.profiler.average_access_time()}")
        if plot_times:
            self.profiler.plot_add_time()
            self.profiler.plot_access_time()
        if cache_utilization:
            hit_ratio, miss_ratio = self.profiler.cache_utilization()
            print(f"Cache Hit Rate: {hit_ratio:.3f}")
            print(f"Cache Miss Rate: {miss_ratio:.3f}")
        if shard_access:
            self.profiler.plot_shard_access_rate()
        if device_usage:
            self.profiler.plot_device_usage()
        if plot_mem:
            self.profiler.plot_mem_usage()