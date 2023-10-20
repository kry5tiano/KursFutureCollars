def main():
    paczki = []
    puste_kilogramy = []

    while True:
        element = float(input("Podaj wagę elementu (0 aby zakończyć): "))

        if element == 0:
            break
        elif element < 1 or element > 10:
            print("Błąd: Waga elementu musi być między 1 a 10 kg.")
            continue

        dodano_element = False
        for paczka in paczki:
            if sum(paczka) + element <= 20:
                paczka.append(element)
                dodano_element = True
                break

        if not dodano_element:
            paczka_nowa = [element]
            paczki.append(paczka_nowa)

    for paczka in paczki:
        puste_kilogramy.append(20 - sum(paczka))

    ilosc_paczek = len(paczki)
    ilosc_kilogramow = sum(map(sum, paczki))
    suma_pustych_kilogramow = ilosc_paczek * 20
    indeks_najwiekszej_pustej_paczki = puste_kilogramy.index(max(puste_kilogramy))

    print("\nPodsumowanie:")
    print(f"Liczba paczek wysłanych: {ilosc_paczek}")
    print(f"Liczba kilogramów wysłanych: {ilosc_kilogramow}")
    print(f"Suma 'pustych' kilogramów: {suma_pustych_kilogramow}")
    print(f"Największa liczba 'pustych' kilogramów była w paczce o indeksie: {indeks_najwiekszej_pustej_paczki}")
    print(f"Wartość pustych kilogramów: {max(puste_kilogramy)}")

if __name__ == "__main__":
    main()
