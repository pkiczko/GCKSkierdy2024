#https://www.codecademy.com/learn/learn-the-command-line
#figma.com (projektowanie wyglądu/zachowania aplikacji, stron internetowych)


a = 0     #zamiana na int powoduje obcięcie wartości po kropce
b = 3       
c = '30'    #zmiana na int możliwa, gdyż string zawiera liczbę
#Pierwszy warunek
if int(a) >= 0:     #int(a) powoduje zmianę zawartości zmiennej a na liczbę całkowitą, jeśli to możliwe
    print('A jest dodatnie!')
else:
    print('A jest ujemne!')
#Drugi warunek
if int(a) == 3:
    print('A jest rowne 3!')
#Trzeci waruenk
if int(a) < 10:
    print('A jest mniejsze od 10!')
#Czwarty warunek
if type(a) == int: # False:     #porównuje typ zmiennej a z int (jeśli a jest int, wynik to True/Prawda)
    print('A jest calkowite')
elif type(a) == str:
    print('A jest slowem/zdaniem/string')
elif type(a) == float:
    print('A jest liczba')
else:
    print('A jest niewiadome')

#### warunek w warunku ####
if a > 0:
    print("##########")
    print("a > 0")
    print("##########")
    if a < 5:
        print("a < 5") 
else:
    print("a <= 0")

### złożone warunki ###
if a == 0 and b < 0:
    print("a = 0  oraz b > 0")
if a == 0 or b < 0:
    print("a = 0  albo b > 0")

### wprowadzanie zmiennej z konsoli ###

# bez zamiany int() zmienna będzie str (string)
#print("Podana wartość: ", zgadywanka)
#print(type(zgadywanka))
losowa_liczba = 73
for i in range(5):      #pozwala na powtórzenie 5 krotne zawartości
    zgadywanka = int(input('Zgadnij wartość liczby (0 do 100): '))
    if zgadywanka == losowa_liczba:
        print("Wygrana!")
        break
    elif zgadywanka > losowa_liczba:
        print("Szukana liczba jest mniejsza!")
    else:
        print("Szukana liczba jest większa!")
print("Koniec!")
