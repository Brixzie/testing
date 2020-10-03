import threading
import time


start = time.perf_counter()




def emptyMethod():
    return True

for x in range(100):
    x = threading.Thread(target=emptyMethod)
    x.start()
    x.join()

finish =time.perf_counter()
final = finish - start

print("Microseconds: ", final*1000) #Milli seconds

