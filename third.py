import math

def je_prvocislo(cislo):
    """
    Funkce vrátí True, pokud je cislo prvočíslo, jinak False.
    """
    cislo = int(cislo)
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False
    # Kontrolujeme jen lichá čísla až do odmocniny z cisla
    for delitel in range(3, int(math.isqrt(cislo)) + 1, 2):
        if cislo % delitel == 0:
            return False
    return True


def vrat_prvocisla(maximum):
    """
    Funkce vrátí seznam všech prvočísel od 2 do zadaného maxima (včetně).
    """
    maximum = int(maximum)
    results = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            results.append(i)
    return results


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    print("Je prvočíslo?", je_prvocislo(cislo))
    prvocisla = vrat_prvocisla(cislo)
    print("Prvočísla:", prvocisla)