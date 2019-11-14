from threading import Thread
from queue import Queue
import threading
import math
import time

#Korzystamy z kolejki
#Robimy 13 watkow

a = 1
dx = 0.0000005
b = 40

zamek = threading.Lock()
poleWynik = 0
#poleLokalne = 0

def funkcja(x):
    return 3*x**3 + math.cos(7*x) - math.log(2*x)

class SumaLokalna(Thread):
    def __init__(self,numer):
        super().__init__()
        self.numer = numer
        self.poleLokalne = 0
    
    def run(self):
        global a, poleWynik
        with zamek:                 #Korzystamy z zamku aby chronić globalna zmienna "a", "poleWynik"
            while a <= b:
                a += dx
                f = funkcja(a)
                self.poleLokalne += f*a
                if  a == a+3:
                    break
            poleWynik += self.poleLokalne



if __name__ == "__main__":
    Threads = []
    
    start = time.time()
    for i in range(13):
        Threads.append(SumaLokalna(i))
        Threads[i].start()   

    for i in range(13):
        Threads[i].join()

    end = time.time()
        
    
    print("Wynik: ", poleWynik )
    print("Czas wykonania: ", format(end-start))