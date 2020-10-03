import threading
import time

def emptyMethod():
    return True

start = time.perf_counter()

for x in range(100):
    x = threading.Thread(target=emptyMethod)
    x.start()
    x.join()

finish =time.perf_counter()
final = finish - start

print("Microseconds: ", final*1000) #Milli seconds

