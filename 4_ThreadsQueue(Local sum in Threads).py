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
    def __init__(self, kolejka, numer):
        super().__init__()
        self.numer = numer
        self.kolejka = kolejka
        self.poleLokalne = 0
    
    def run(self):
        global a
        with zamek:    #Korzystamy z zamku aby chronić globalna zmienna "a"
            while a <= b:
                a += dx
                f = funkcja(a)
                self.poleLokalne += f*a
                if  a == a+3:
                    break
                
        #print("Pole lokalne", self.poleLokalne)
        self.kolejka.put(self.poleLokalne)

class SumaWynik(Thread):
    def __init__(self, kolejka, numer):
        super().__init__()
        self.kolejka = kolejka
        self.numer = numer
    
    def run(self):
        global poleWynik
        pole = self.kolejka.get()
        with zamek:                 #Korzystamy z zamku aby chronić globalna zmienna "poleWynik"
            poleWynik += pole

if __name__ == "__main__":
    q = Queue()
    sumaLokalnaLista = []
    for i in range(13):
        sumaLokalnaLista.append(SumaLokalna(q, i))
        sumaLokalnaLista[i].start()
    
    sumaWynikLista = []
    start = time.time()
    for i in range(13):
        sumaWynikLista.append(SumaWynik(q, i))
        sumaWynikLista[i].start()

    for i in range(13):
        sumaLokalnaLista[i].join()
        sumaWynikLista[i].join()
    
    end = time.time()
        
    
    print("Wynik: ", poleWynik )
    print("Czas wykonania: ", format(end-start))




    

            


