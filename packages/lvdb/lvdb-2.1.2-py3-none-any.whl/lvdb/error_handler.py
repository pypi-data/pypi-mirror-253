import warnings


class ErrorHandler:
    def __new__(cls, *args, **kwargs):
        """ Override __new__ to enforce singularity """
        if not hasattr(cls, 'instance'):
            cls.instance = super(ErrorHandler, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(ErrorHandler, self).__init__()

    @staticmethod
    def device_warning():
        warnings.warn("Failed to import CuPy, verify that CuPy is installed and your device has a GPU.", Warning)

    @staticmethod
    def profile_warning():
        warnings.warn("You have not enabled profiling.", Warning)

    @staticmethod
    def query_error():
        raise ValueError("The input range is out of bounds.")

    @staticmethod
    def shape_error():
        raise ValueError("The input vector is not compatible.")
