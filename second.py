def cislo_text(cislo):
    """
    Funkce převede číslo (0–100) na jeho českou textovou podobu.
    """
    cislo = int(cislo)  # převedeme vstup na číslo
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    special = {11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 15: "patnáct",
               16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct", 10: "deset", 100: "sto"}

    if cislo in special:
        return special[cislo]
    elif cislo < 10:
        return jednotky[cislo]
    else:
        d = cislo // 10
        j = cislo % 10
        if j == 0:
            return desitky[d]
        else:
            return f"{desitky[d]} {jednotky[j]}"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)