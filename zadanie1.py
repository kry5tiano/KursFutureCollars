imie_odbiorcy = input("Podaj imię odbiorcy: ")
rok_urodzenia = int(input("Podaj rok urodzenia odbiorcy: "))
wiadomosc = input("Podaj spersonalizowaną wiadomość: ")
imie_nadawcy = input("Podaj swoje imię: ")

obecny_rok = 2023
wiek = obecny_rok - rok_urodzenia

kartka_urodzinowa = f"{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek} urodzin!\n\n{wiadomosc}\n\n{imie_nadawcy}"

print("\nOto Twoja spersonalizowana kartka urodzinowa:")
print(kartka_urodzinowa)
