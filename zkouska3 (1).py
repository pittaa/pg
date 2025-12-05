# Třída Osoba je "Rodič". Je to základní šablona.
class Osoba:
    # __init__ je "Konstruktor". Spustí se automaticky, když vyrábíme novou Osobu.
    # self znamená "já" (ten konkrétní objekt, který právě vzniká).
    def __init__(self, jmeno, vek) -> None:
        self.jmeno = jmeno  # Uložím si jméno do paměti objektu
        self.vek = vek      # Uložím si věk do paměti objektu

    # __str__ říká, co se má vypsat, když na objekt zavoláme print().
    # Kdybychom to tu neměli, vypsalo by to jen divný kód (adresu v paměti).
    def __str__(self) -> str:
        return f"Osoba(jmeno={self.jmeno}, vek={self.vek})"


# Třída Student "dědí" z Osoby (vidíš to v závorce).
# Student umí všechno, co Osoba, plus něco navíc.
class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik) -> None:
        # super() znamená "zavolej Rodiče (Osobu)".
        # Říkáme: "Mami, nastav jméno a věk, ty to umíš." (nemusíme to psát znovu)
        super().__init__(jmeno, vek)
        # Tohle je ta věc navíc, kterou má jen student.
        self.rocnik = rocnik
    
    # Přepisujeme funkci print(). Student se chce vypisovat jinak než obyčejná Osoba.
    def __str__(self) -> str:
        return f"Student {self.jmeno} studuje {self.rocnik} rocnik"


# Třída Ucitel také dědí z Osoby.
class Ucitel(Osoba):
    def __init__(self, jmeno, vek, obor) -> None:
        # Zase voláme Rodiče, ať zařídí jméno a věk.
        super().__init__(jmeno, vek)
        # Učitel má navíc "obor".
        self.obor = obor
    
    # Učitel se taky vypisuje po svém.
    def __str__(self) -> str:
        return f"Ucitel {self.jmeno} uci obor {self.obor}"


# Hlavní část programu - testování
if __name__ == "__main__":
    # Vyrobíme Studenta (zavolá se __init__ u Studenta a pak u Osoby)
    student1 = Student("Adam", 20, 2)
    student2 = Student("Eva", 19, 1)
    
    # Vyrobíme Učitele
    ucitel = Ucitel("Tomas", 40, "IT")

    # Vypíšeme je (zavolá se __str__)
    print(student1)
    print(student2)
    print(ucitel)