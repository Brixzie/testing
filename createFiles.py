#create 50 000 files in one folder and fill each file with 32 bytes of data each
import time
start = time.process_time()

for x in range(50000):
    f = open(f"file{x}.txt", "x")
    f.write("Lorem ipsum dolor sit amet,julia")
    f.close()

print(time.process_time() - start)