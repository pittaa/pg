def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    pozice = figurka["pozice"]
    r, s = pozice
    cr, cs = cilova_pozice

    # 1️⃣ kontrola – mimo šachovnici
    if not (1 <= cr <= 8 and 1 <= cs <= 8):
        return False

    # 2️⃣ kontrola – cílové pole obsazeno
    if cilova_pozice in obsazene_pozice:
        return False

    # Pomocná funkce pro ověření volné cesty (u věže, střelce, dámy)
    def cesta_volna(dr, ds):
        krok_r = (dr > 0) - (dr < 0)
        krok_s = (ds > 0) - (ds < 0)
        r_temp, s_temp = r + krok_r, s + krok_s
        while (r_temp, s_temp) != (cr, cs):
            if (r_temp, s_temp) in obsazene_pozice:
                return False
            r_temp += krok_r
            s_temp += krok_s
        return True

    dr = cr - r
    ds = cs - s

    # 3️⃣ logika podle typu figurky
    if typ == "pěšec":
        # Pěšec jde jen dopředu (z pohledu bílého – řádky rostou)
        if s != cs:
            return False
        # jeden krok vpřed
        if dr == 1 and (cr, cs) not in obsazene_pozice:
            return True
        # dva kroky vpřed z výchozí pozice (řádek 2)
        if r == 2 and dr == 2 and (r+1, s) not in obsazene_pozice and (cr, cs) not in obsazene_pozice:
            return True
        return False

    elif typ == "jezdec":
        return (abs(dr), abs(ds)) in [(2, 1), (1, 2)]

    elif typ == "věž":
        if dr == 0 or ds == 0:
            return cesta_volna(dr, ds)
        return False

    elif typ == "střelec":
        if abs(dr) == abs(ds):
            return cesta_volna(dr, ds)
        return False

    elif typ == "dáma":
        if dr == 0 or ds == 0 or abs(dr) == abs(ds):
            return cesta_volna(dr, ds)
        return False

    elif typ == "král":
        return abs(dr) <= 1 and abs(ds) <= 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
