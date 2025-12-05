
# vas program nacte ze souboru, ktery dostane jako argument z prikazove radky, text a vypise ho pozpatku

# vytvorte funkce pozpatku(), ktera jako parametr bere text a vraci ho pozpatku tzn "ahoj" -> "joha"

# osetrete chybove stavy pomoci try - except

import sys  # Importuje "balíček nářadí" sys, abychom mohli číst z příkazové řádky

# Definice funkce, která přijme text a vrátí ho otočený
def pozpatku(text):
    text_pozpatku = ""  # Vytvoříme prázdnou proměnnou, kam budeme skládat písmena
    
    # Zjistíme startovní pozici. Musíme začít od posledního písmene.
    # len(text) je délka, ale indexujeme od 0, takže poslední index je délka mínus 1.
    i = len(text) - 1  
    
    # Cyklus běží, dokud index 'i' není menší než 0.
    # Jdeme od konce (třeba 3) až k nule (začátek slova).
    while i >= 0:
        pismeno = text[i]        # Vezmeme písmeno na aktuální pozici indexu 'i'
        text_pozpatku += pismeno # Přilepíme (přičteme) toto písmeno k výsledku
        i -= 1                   # Snížíme index o 1 (posuneme se v textu doleva/couváme)
        
    return text_pozpatku # Funkce končí a vrátí hotový otočený text

# Podmínka, která zajistí, že se testy spustí jen když pouštíme přímo tento soubor
if __name__ == "__main__":
    try:
        # Zkoušíme provést rizikový kód (práce se soubory může selhat)
        
        # sys.argv[0] je název programu, sys.argv[1] je název souboru, který jsme zadali
        soubor = sys.argv[1] 
        
        # Otevřeme soubor v režimu čtení ("r" = read).
        # Příkaz 'with' zajistí, že se soubor po přečtení sám bezpečně zavře.
        with open(soubor, "r") as fp:
            obsah = fp.read()          # Přečteme celý text ze souboru najednou
            obracene = pozpatku(obsah) # Zavoláme naši funkci nahoře a výsledek uložíme
            print(obracene)            # Vypíšeme výsledek na obrazovku
            
    # Pokud uživatel zapomněl napsat název souboru (seznam argv je moc krátký)
    except IndexError:
        print("Zadej nazev souboru")
        
    # Pokud uživatel zadal název, ale takový soubor na disku není
    except FileNotFoundError:
        print("Soubor neexistuje")