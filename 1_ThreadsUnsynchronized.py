import math
import time
import threading

step = float(0.000005)
global_start = float(1)
global_pole = float(0)


def funkcja(x):
    return 3*x**3 + math.cos(7*x) - math.log(2*x)


def calculation(step):
    global global_start
    global global_pole
    while global_start <= 40:
        global_start += step
        f = funkcja(global_start)
        global_pole = global_pole + f * global_start
        if global_start == global_start+1:
            break 
    return global_pole


st = time.time()
threads = []
for i in range(1,41):
    threads.append(threading.Thread(target=calculation, args=(step,)))

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

end = time.time()

print("Globalne pole: ", global_pole)
print("Czas wykonania: ", end - st)



