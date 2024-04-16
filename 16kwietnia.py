# moj e-mail: pkiczko@gmail.com
#materiały ze strony
#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/11_Day_Functions/11_functions.md

# syntax
# Declaring a function
def jakas_funkcja():
    pass
# Calling a function
jakas_funkcja()     #sposób wywołania funkcji

def obliczenie(a):  #definicja funkcji z 1dnym argumentem
    return a*2      #wartość którą funkcja przekazuje
def wizytowka():    #funkcja bez argumentów
    print("Mam na imię (wpisać imię), mieszkam w (wpisać miasto)")
#powyższa funkcja jedynie wypisuje w terminalu/konsoli wskazany tekst
wizytowka()

print(obliczenie("Ewa"))
print(obliczenie(5))

def stworz_wizytowke():
    imie = input("Podaj imię: ")
    miasto = input("Podaj ulubioną miejscowość: ")
    print("{} chętnie pojechałby(-aby) do {}".format(imie, miasto))

#stworz_wizytowke()  #poprawić nazwę miasta (odpowiednia końcówka)

def stworz_lepsza_wizytowke():
    imie = input("Podaj imię: ")
    miasto = input("Podaj ulubioną miejscowość: ")
    print("{} chętnie pojechałby(-aby) do {}".format(imie, miasto))
    return imie, miasto

#dane = stworz_lepsza_wizytowke()
dane2 = stworz_wizytowke()      #ta funkcja nie ma return, więc w dane2 zapisane zostanie None

print(dane2)

kolor = 'zielony'

def pomaluj():
    kolor = 'czerwony'
    farba = "niewidzialna"      #defincje zmiennych wewnątrz funkcji działają tylko w ich obrębie!
    print(kolor)

print("Druk poza definicją pomaluj: ", kolor)
pomaluj()

for i in range(2):
        print(i)

def osoba(imie = "Anonim", nazwisko = "Gal"):
     print("Jestem {}, {} {}.".format(nazwisko, imie, nazwisko))

osoba()
osoba("Asteriks")
osoba("Pan", "Kleks")

#funkcja co przyjmuje dowolną ilość argumentów:

def sum_all_nums(*nums):
    total = 0
    for num in nums:    #pętla po wszystkich wprowadzonych liczbach
        total += num    # to samo co total = total + num 
    return total
print("Suma liczb 2 3 oraz 5 to: ", sum_all_nums(2, 3, 5)) # 10

def ogrod(drzewo, krzewy, kwiaty, *inne):
     print("W moim ogrodzie jest {} drzewo".format(drzewo))
     print("W moim ogrodzie jest {} krzew".format(krzewy))
     print("W moim ogrodzie jest {} kwiat".format(kwiaty))
     print("W moim ogrodzie sa także inne rośliny: {}".format(inne))

ogrod("owocowe", "wspianiały", "maku", ["dynie", "ogorki", "pomidory"])

ogrod("owocowe", "wspianiały", "maku", "dynie", "ogorki", "pomidory")

przypadkowa_lista = [123, 44, ["test", { "kolor": "czarny"}]]
print(przypadkowa_lista)
print(przypadkowa_lista[2])     #odwołanie do elementu z liście o indeksie 2
print(przypadkowa_lista[2][1])  #
print(przypadkowa_lista[2][1]["kolor"]) #odwołanie do klucza "kolor" do obiektu wewnątrz tej struktury
