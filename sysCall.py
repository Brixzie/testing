import OS
import time

start = time.perf_counter()
for x in range(1000):
    pid = OS.getpid()

finish = time.perf_counter()

final = finish - start

print(final)
