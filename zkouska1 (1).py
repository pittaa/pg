# napiste funkci, ktera podle typu "+"", "-", "*", "/" provede operaci a vrati vysledek

def operace(typ, a, b):
    matematicka_operace = None
    if typ == "+":
        matematicka_operace = a + b
    elif typ == "-":
        matematicka_operace = a - b
    elif typ == "*":
        matematicka_operace = a * b
    elif typ == "/":
        matematicka_operace = a / b
    return matematicka_operace

if __name__ == "__main__":
    print(operace("+", 1, 2))  # 3
    print(operace("-", 2, 1))  # 1
    print(operace("*", 0, 5))  # 0
    print(operace("/", 4, 2))  # 2