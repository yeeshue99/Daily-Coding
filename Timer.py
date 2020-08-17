import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def Start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def Stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.10f} seconds")
        return elapsed_time

    def Average(self, lst):
        avg = sum(lst) / len(lst)
        times = [avg, avg * 1000]
        print(f"Average: {times[0]}s")
        print(f"Average: {times[1]}ms")
        return times

    def CalculateTime(self, func, *args):
        timerList = []
        for _ in range(10000):
            self.Start()
            print(func(*args))
            timerList.append(self.Stop())
        return self.Average(timerList)
