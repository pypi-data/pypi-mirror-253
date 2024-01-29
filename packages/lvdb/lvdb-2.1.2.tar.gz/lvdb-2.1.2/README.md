# LVDB

This is a vector sharding package leveraging Python generators and built-in NumPy text loading to
conserve memory within an environment with resource constraints. It aims to reduce
memory overhead through saving and loading from shard files, in essence
trading runtime for memory.

Usage:
* The entry point for this package is the LVInstance class. This can be
imported from lvdb as LVInstance.
* An instance of this class should be initialized and data can be inserted into this instance.
* To use with GPU resources, set the device to gpu.
* To enable in-memory caching, set a time-to-live value.
* Implement an interface for either a shard or the entire store, implement the metaclass from lvdb.interfaces. This enables you to use customize external storage options like S3.
