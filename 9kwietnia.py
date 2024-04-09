import math  #po imporcie bibliotek dobrze jest zostawić przestrzeń - oddzielić od reszty kodu
from random import random, randint  #zaimportowaliśmy jednie 2 metody!
#https://www.w3schools.com/python/module_random.asp
import statistics as stat

a = 1       #podobnie z deklaracją zmiennych, funkcjami etc
b = 2
n = 7
random()

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(stat.mean(ages))


print(int(math.pi))         
print(math.floor(math.pi))  #wynik obydwu metod jest taki sam!

print(type(math.floor(math.pi)))
print(type(int(math.pi)))

print(math.ceil(math.pi))
print(type(math.ceil(math.pi)))

print(123, 432, 542.2324, "jd", "\n")   #"\n" komenda oznaczająca następną linię

tekst = "Dzięcioł \t Gołąb \t Bocian"
dane = [3, 18, 2]

print(tekst)
print('   ', dane[0], '\t\t  ', dane[1], '\t   ', dane[2])   #\t tabulator - odstęp w tekscie
print(dane)

for liczby in dane:     #pętla po wszystkich elementach listy dane
    print(liczby)

print("Przybliżona wartość stałej PI to", math.pi, '\n', '"jakiś cytat (...)"', "' ' ' ' ' '")

print("test {} {} test2".format(math.pi, math.sin(0)))  #injekcja zmiennych w string
print("test", math.pi, math.sin(0), "test2")            #

print(random())
print(random())     #losowa liczba między 0.0 a 1.0

print(random()*10)  #losowa liczba między 0.0 a 10.0
print(math.ceil(random()*10))   #losowa liczba między 1 a 10
print(math.floor(random()*10))  #losowa liczba między 0 a 9

print(randint(0,10))