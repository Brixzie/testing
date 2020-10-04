import threading
import time

start = time.perf_counter()

def do_something():
    print('sleep 1 sec')
    time.sleep(1)
    print('Done sleeping')

threads = []

for x in range(100):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()



finish = time.perf_counter()

final = finish - start

print('Total time:', final)
print('Thread overhead time:', final - 1, 'seconds')