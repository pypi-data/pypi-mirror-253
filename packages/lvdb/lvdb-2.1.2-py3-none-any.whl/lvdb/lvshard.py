import os

import numpy as np

from .shard_math import normalize


class LVShard:
    def __init__(self, shard_id: int, device: str):
        super(LVShard, self).__init__()

        self.__id = shard_id
        self.__ref = None
        self.__device = device
        self.__vector_count = 0

    @property
    def vector_count(self):
        return self.__vector_count

    @property
    def ref(self):
        return self.__ref

    def insert(self, vector):
        if not self.__ref:
            np.save(f"lv_shrd{self.__id}", vector)
            self.__ref = f"lv_shrd{self.__id}.npy"
            self.__vector_count += 1
        else:
            with open(self.__ref, 'wb') as f:
                np.save(f, vector)
                self.__vector_count += 1

    def delete(self, vector, first: bool):
        nx = False
        keep = []

        if not self.__ref:
            return

        with open(self.__ref, 'rb') as f:
            v = np.load(f)
            while type(v) == np.ndarray:
                if nx:
                    keep.append(v)
                elif first:
                    if np.array_equal(v, vector):
                        self.__vector_count -= 1
                        nx = True
                    else:
                        keep.append(v)
                elif not first and np.array_equal(v, vector):
                    keep.append(v)
                else:
                    self.__vector_count -= 1

                try:
                    v = np.load(f)
                except EOFError:
                    return

        if keep: np.save(f"lv_shrd{self.__id}", keep[0])
        with open(self.__ref, 'wb') as f:
            for i in range(1, len(keep)):
                np.save(f, keep[i])
                self.__vector_count += 1

    def get_data(self, partial: bool, lo: float, hi: float):
        with open(self.__ref, 'rb') as f:
            v = np.load(f)
            while type(v) == np.ndarray:
                if partial:
                    if lo <= normalize(v) <= hi:
                        yield v
                else:
                    yield v

                try:
                    v = np.load(f)
                except EOFError:
                    return

    def clear(self):
        if self.__ref:
            os.remove(self.__ref)
            self.__vector_count = 0
            self.__ref = None

    def __len__(self):
        return self.__vector_count