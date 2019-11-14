from threading import Thread
import threading
import math
import time

pole = 0
start = 1
dx = 0.0000005
zamek = threading.Lock()

def funkcja(x):
    return 3*x**3 + math.cos(7*x) - math.log(2*x)

class Watek(Thread):
  def __init__(self, numer):
    self.numer = numer
    super().__init__()

  def run(self):
    global pole
    global start
    with zamek:
      while start <= 40:
        start+=dx
        f = funkcja(start)
        pole += f*start
        if start == start+1:
          break

st = time.time()          
watki = []
for i in range(41):
  watki.append(Watek(i))
  watki[i].start()

for watek in watki:
  watek.join()
end = time.time()

print("Wynik: ", pole)
print("Czas wykonania: ", end - st)