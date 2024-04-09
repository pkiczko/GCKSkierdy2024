from random import randint

limit = 10

print("Powitanie")

ilosc_scian = input("Podaj ilo-ścienną kością chcesz rzucać?")
ilosc = input("Podaj ile razy chcesz rzucić kością (limit 10): ")


if ilosc.isdigit():
    if int(ilosc) > 0 and int(ilosc) <= limit:
        print("wynik")
        for i in range(int(ilosc)):     #pętla, powtarza się "ilosc" razy
            print(randint(1,6))         #za każdym razem drukuje losową liczbę między 1 a 6
    else:
        print("Podano zbyt wileką liczbę!")
else:
    print("Błąd wprowadzonych danych")