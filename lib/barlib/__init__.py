import psutil

__all__ = [
    "num_cpus",
]


def num_cpus():
    return psutil.cpu_count()
