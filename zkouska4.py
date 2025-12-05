# Importujeme knihovnu 'requests', která umí stahovat stránky z internetu.
# Python to v základu neumí, musíme si na to půjčit tento nástroj.
import requests 

# Funkce bere dva parametry: 
# 1. 'url' = adresa stránky (např. https://google.com)
# 2. 'vystupni_soubor' = jméno souboru, kam to uložíme na disku
def stahni_a_analyzuj(url, vystupni_soubor):
    try:
        # --- KROK 1: STAHOVÁNÍ ---
        print(f"Stahuji data z: {url}")
        
        # requests.get(url) je jako když zadáš adresu do prohlížeče a zmáčkneš Enter.
        # Výsledek (co server poslal zpátky) se uloží do proměnné 'odpoved'.
        odpoved = requests.get(url)
        
        # Zkontrolujeme "semafor". Kód 200 znamená "Vše OK" (zelená).
        # Kdyby to bylo 404 (nenalezeno) nebo 500 (chyba serveru), jdeme do 'else'.
        if odpoved.status_code == 200:
            # Vytáhneme z odpovědi čistý text (HTML kód stránky)
            text_z_netu = odpoved.text
            
            # --- KROK 2: ZPRACOVÁNÍ DAT ---
            # Spočítáme, kolik má stažený text znaků (funkce len).
            # Tím plníme zadání "zpracování dat".
            pocet_znaku = len(text_z_netu)
            print(f"Staženo úspěšně. Text má {pocet_znaku} znaků.")
            
            # --- KROK 3: ZÁPIS DO SOUBORU ---
            # Otevřeme soubor v režimu "w" (Write = Zápis).
            # POZOR: Režim "w" smaže vše, co v souboru bylo, a napíše to znovu!
            with open(vystupni_soubor, "w", encoding="utf-8") as fp:
                fp.write(text_z_netu) # Fyzicky zapíšeme text na disk
                
            print(f"Data byla uložena do souboru: {vystupni_soubor}")
            
        else:
            # Pokud server vrátil chybu (třeba 404), vypíšeme ji.
            print("Chyba při stahování. Server vrátil kód:", odpoved.status_code)

    # Pokud se stane něco nečekaného (spadne internet, nemám práva k souboru...)
    except Exception as e:
        print("Nastala kritická chyba:", e)

# Hlavní spouštěcí blok
if __name__ == "__main__":
    testovaci_url = "https://www.google.com" 
    muj_soubor = "google_stazeny.html"
    
    # Spustíme naši funkci
    stahni_a_analyzuj(testovaci_url, muj_soubor)