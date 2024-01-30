import logging
import resource
from contextlib import ContextDecorator
from time import perf_counter_ns


class logprof(ContextDecorator):
    def __init__(self, label, logger=None, level="INFO", **kwds):
        self.label = label
        self.logger = logger or logging.getLogger(__name__)
        self.level = level if isinstance(level, int) else logging._nameToLevel[level.upper()]

    def __enter__(self):
        self.logger.log(self.level, f">>> '{self.label}' started..")
        self.pcns = perf_counter_ns()
        self.ru = resource.getrusage(resource.RUSAGE_SELF)
        return self

    def __exit__(self, *exc):
        rem_ns = perf_counter_ns() - self.pcns
        dpc_m, rem_ns = divmod(rem_ns, 60 * 10**9)
        dpc_s, rem_ns = divmod(rem_ns, 10**9)
        dpc_ms, rem_ns = divmod(rem_ns, 10**6)
        dpc_us, rem_ns = divmod(rem_ns, 10**3)

        ru = resource.getrusage(resource.RUSAGE_SELF)
        rem_kb = ru.ru_maxrss - self.ru.ru_maxrss
        drss_gb, rem_kb = divmod(rem_kb, 1024**2)
        drss_mb, rem_kb = divmod(rem_kb, 1024**1)

        self.logger.log(
            self.level,
            f"<<< '{self.label}' finished. "
            f"Took {dpc_m}m {dpc_s}s {dpc_ms}ms {dpc_us}us {rem_ns}ns. "
            f"Used {drss_gb}gib {drss_mb}mib {rem_kb}kib."
        )
        return False
