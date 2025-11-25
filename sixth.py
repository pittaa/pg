import sys
import requests
import re  # Nutné pro vyhledávání vzorů v textu (regex)


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    # 1. Stažení obsahu stránky
    response = requests.get(url)

    # 2. Kontrola návratového kódu
    if response.status_code != 200:
        # Pokud stránka neexistuje nebo je chyba serveru, vyhodíme výjimku
        raise Exception(f"Chyba při stahování stránky. Status code: {response.status_code}")

    # 3. Získání textu stránky
    # response.content jsou surová data (bytes), response.text je dekódovaný text (str)
    # Pro hledání textu je lepší použít .text
    html_content = response.text

    # 4. Vyhledání všech odkazů pomocí regulárního výrazu
    # Hledáme vzor: href="neco_uvnitr"
    # Vysvětlení regexu r'href="([^"]*)"':
    #  href="  -> hledá přesně tento text
    #  (...)   -> to co je v závorce se uloží do výsledku
    #  [^"]* -> jakýkoliv znak, který NENÍ uvozovka, opakující se
    hrefs = re.findall(r'href="([^"]*)"', html_content)

    return hrefs


if __name__ == "__main__":
    try:
        # Ověření, zda byl zadán argument
        if len(sys.argv) < 2:
            raise Exception("Nebylo zadáno URL. Použití: python sixth.py <url>")
            
        url = sys.argv[1]
        
        # Zavolání funkce a uložení výsledku
        found_links = download_url_and_get_all_hrefs(url)
        
        # Výpis výsledků (každý odkaz na nový řádek)
        print(f"Na stránce {url} nalezeno {len(found_links)} odkazů:")
        for link in found_links:
            print(link)

    # Ošetření chyb
    except requests.exceptions.RequestException as e:
        print(f"Chyba při komunikaci se serverem (requests): {e}")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")