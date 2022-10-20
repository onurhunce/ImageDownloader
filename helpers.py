import time
import hashlib


def measure_time(func):
    """
    A decorator to measure the time elapsed during the execution of the wrapped method.
    """

    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        func(*args, **kwargs)
        elapsed_time = time.perf_counter() - t
        print("elapsed_time:: ", elapsed_time)

    return wrapper


def hash_string(string: str) -> str:
    return hashlib.sha1((string.encode(encoding="utf-8"))).hexdigest()
