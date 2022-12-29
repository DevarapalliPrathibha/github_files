import time
start = time.perf_counter()
def calculateTime():
    print("sleep for 4 second")
    time.sleep(4)
    print("completed sleep")
calculateTime()
finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')
import threading
def calculatetime():
    print("sleep for 4 second \n")
    time.sleep(4)
    print("completed sleep \n")
t1 = threading.Thread(target = calculateTime)
t2 = threading.Thread(target = calculateTime)
t3 = threading.Thread(target = calculateTime)
t4 = threading.Thread(target = calculateTime)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')
#using loops
import threading
import time
start = time.perf_counter()
def calculateTime():
    print("sleep for 4 second \n")
    time.sleep(4)
    print("completed sleep \n")
threads = []
for _ in range(4):
    thread = threading.Thread(target = calculateTime)
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()
print(threads)
finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')

#
import threading
import time
start = time.perf_counter()
def calculateTime(dur):
    print("sleep for {seconds} second \n")
    time.sleep(dur)
    print("completed {seconds} sleep \n")
threads = []
for _ in range(4):
    thread = threading.Thread(target = calculateTime,args=[3])
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()
finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')
print("\n")
import concurrent.futures
import time
start = time.perf_counter()
def calculateTime(seconds):
    print(f"sleep for {seconds} second \n")
    time.sleep(seconds)
    print(f"completed {seconds} sleep \n")
list = [10,20,30,40,50]
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(calculateTime,k) for k in list ]
    for r in concurrent.futures.as_completed(results):
        print(r.result())
finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')


