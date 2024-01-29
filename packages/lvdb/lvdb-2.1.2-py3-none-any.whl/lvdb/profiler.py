from statistics import mean

import matplotlib.pyplot as plt


class Profiler:
    """
    Performance Logging Class
    """

    def __init__(self, num_shards: int):
        super(Profiler, self).__init__()
        self.__num_shards = num_shards
        self.add_times = []
        self.access_times = []
        self.cpu_usage = []
        self.gpu_usage = []
        self.mem_usage = []
        self.cache_hit = 0
        self.cache_miss = 0
        self.shard_access_rate = {i:0 for i in range(num_shards)}

    def add_time(self, t: float, shard_id: int):
        self.add_times.append(t)
        self.shard_access_rate[shard_id] += 1

    def add_access(self, t: float, shard_id: int):
        self.access_times.append(t)
        self.shard_access_rate[shard_id] += 1

    def add_mem(self, t: float):
        self.mem_usage.append(t)

    def process_device(self, cpu_split: float, gpu_split: float):
        self.cpu_usage.append(cpu_split)
        self.gpu_usage.append(gpu_split)

    def process_cache(self, hit: bool):
        self.cache_hit += hit
        self.cache_miss += not hit

    def cache_utilization(self):
        total_access = self.cache_hit + self.cache_miss
        if total_access == 0:
            return 0
        return (self.cache_hit/total_access * 100), (self.cache_miss/total_access * 100)

    def plot_device_usage(self):
        x = [i for i in range(len(self.cpu_usage))]
        plt.plot(x, self.cpu_usage, label='cpu')
        plt.plot(x, self.gpu_usage, label='gpu')
        plt.legend()
        plt.show()

    def plot_shard_access_rate(self):
        x = self.shard_access_rate.keys()
        y = self.shard_access_rate.values()

        plt.bar(x, y, width = 0.2)
        plt.xlabel("Shard ID")
        plt.ylabel("Access Count")
        plt.title("Shard Access")
        plt.show()

    def plot_add_time(self):
        x = [i for i in range(len(self.add_times))]
        p = sorted(self.add_times)

        plt.plot(x, p, label='Add Time Distribution')
        plt.legend()
        plt.show()

    def plot_access_time(self):
        x = [i for i in range(len(self.access_times))]
        p = sorted(self.access_times)

        plt.plot(x, p, label='Access Time Distribution')
        plt.legend()
        plt.show()

    def plot_mem_usage(self):
        x = [i for i in range(len(self.mem_usage))]

        plt.plot(x, self.mem_usage, label='Memory Usage')
        plt.legend()
        plt.show()

    def average_add_time(self):
        return mean(self.add_times) if self.add_times else 0

    def average_access_time(self):
        return mean(self.access_times) if self.access_times else 0

    def clear(self):
        self.add_times = []
        self.access_times = []
        self.cpu_usage = []
        self.gpu_usage = []
        self.mem_usage = []
        self.cache_hit = 0
        self.cache_miss = 0
        self.shard_access_rate = {i:0 for i in range(self.__num_shards)}