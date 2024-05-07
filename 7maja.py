# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md

#metody dla stringów

lista_imion = ['Adam Piotr', 'eWa', 'RoberT', 'ElIza', 'ANIA']
for imiona in lista_imion:        #Bierze każde pojedyncze imię i wykonuje operacje
    for imie in imiona.split():   #podzielić stringi z wieloma słowami
        print(imie.capitalize())


language = 'Python'
pto = language[::-1] #
print(pto) # Pto

print("Czy Python kończy się na 'on'?", language.endswith('on'))
print("Czy Python zaczyna się na 'Pt'?", language.startswith('Pt'))

print("TEST \t TEST TEST".expandtabs(15))   #powiększa odstęp tabulatorów

challenge = 'thirty\\days\tof\'python\"'
print(challenge)    #różne znaki uzyskane za pomocą \

# zobacz https://realpython.com/python-string-contains-substring/
# dt. znajdywania wszystkich podstringów w danym stringu

import re

file_content = """hi there and welcome.
... this is a special hidden file with a secret secret.
... i don't want to tell you the secret,
... but i do want to secretly tell you that i have one."""

# formuły regex - zobacz np.
# https://regexr.com/3e48o

wynik = re.search(r"secret\w+", file_content)

wynik_wszystko = re.findall(r"secret[ .,]", file_content)
wynik_dwa = re.findall("secret", file_content)
print(wynik_wszystko)
print(wynik_dwa)

# metoda do sprawdzania czy liczba

num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False



