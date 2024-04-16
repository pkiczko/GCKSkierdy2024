from random import randint

ilosc_zgadywan = 7

losowa_liczba = randint(0,100)

for i in range(ilosc_zgadywan):      #pozwala na powtórzenie ilosc_zgadywan krotne zawartości
    zgadywanka = input('Zgadnij wartość liczby (0 do 100): ')
    
    if zgadywanka.isdigit():    #sprawdzamy czy podana wartość to liczba całkowita
        pass                    #jeśli tak, kontynuuje wykonywanie kodu
    else:
        print("Nieprawidłowy znak!")
        break                   #jeśli nie przerywa kod

    if int(zgadywanka) == losowa_liczba:
        print("Wygrana!")
        break
    elif int(zgadywanka) > losowa_liczba:
        print("Szukana liczba jest mniejsza!")
    else:
        print("Szukana liczba jest większa!")

print("Koniec!")    #poza pętlą for