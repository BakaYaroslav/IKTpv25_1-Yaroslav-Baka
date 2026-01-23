import math

# Arvutuste ajalugu
history = []


def get_number(prompt):
    """Turvaline numbri sisestamine"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Viga: palun sisesta arv!")


def add(a, b):
    # Liitmine
    return a + b


def subtract(a, b):
    # Lahutamine
    return a - b


def multiply(a, b):
    # Korrutamine
    return a * b


def divide(a, b):
    # Jagamine (kontrollime nulliga jagamist)
    if b == 0:
        raise ZeroDivisionError
    return a / b


def power(a, b):
    # Astendamine
    return a ** b


def square_root(a):
    # Ruudujuur (negatiivne arv ei ole lubatud)
    if a < 0:
        raise ValueError
    return math.sqrt(a)


def factorial(a):
    # Faktoriaal (ainult mittenegatiivne täisarv)
    if a < 0 or not a.is_integer():
        raise ValueError
    return math.factorial(int(a))


def percent(a, b):
    # Protsendi arvutamine
    return (a * b) / 100


def show_history():
    # Kuvab arvutuste ajaloo
    if not history:
        print(" Ajalugu on tühi")
    else:
        print("\n Arvutuste ajalugu:")
        for item in history:
            print("*", item)


def menu():
    # Peamenüü
    print("""
 KALKULAATOR
1  ➜ Liitmine (+)
2  ➜ Lahutamine (-)
3  ➜ Korrutamine (*)
4  ➜ Jagamine (/)
5  ➜ Astendamine (a^b)
6  import math

# Arvutuste ajalugu
history = []


def get_number(prompt):
    """Turvaline numbri sisestamine"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Viga: palun sisesta arv!")


def add(a, b):
    # Liitmine
    return a + b


def subtract(a, b):
    # Lahutamine
    return a - b


def multiply(a, b):
    # Korrutamine
    return a * b


def divide(a, b):
    # Jagamine (kontrollime nulliga jagamist)
    if b == 0:
        raise ZeroDivisionError
    return a / b


def power(a, b):
    # Astendamine
    return a ** b


def square_root(a):
    # Ruudujuur (negatiivne arv ei ole lubatud)
    if a < 0:
        raise ValueError
    return math.sqrt(a)


def factorial(a):
    # Faktoriaal (ainult mittenegatiivne täisarv)
    if a < 0 or not a.is_integer():
        raise ValueError
    return math.factorial(int(a))


def percent(a, b):
    # Protsendi arvutamine
    return (a * b) / 100


def show_history():
    # Kuvab arvutuste ajaloo
    if not history:
        print("📭 Ajalugu on tühi")
    else:
        print("\n📜 Arvutuste ajalugu:")
        for item in history:
            print("•", item)


def menu():
    # Peamenüü
    print("""
🧮 KALKULAATOR
--------------------
1  ➜ Liitmine (+)
2  ➜ Lahutamine (-)
3  ➜ Korrutamine (*)
4  ➜ Jagamine (/)
5  ➜ Astendamine (a^b)
6  ➜ Ruudujuur (√)
7  ➜ Protsent
8  ➜ Faktoriaal
9  ➜ Ajalugu
0  ➜ Välju
""")


# Põhitsükkel
while True:
    menu()
    choice = input("👉 Vali tegevus: ")

    try:
        if choice == "1":
            a = get_number("a = ")
            b = get_number("b = ")
            result = add(a, b)
            history.append(f"{a} + {b} = {result}")

        elif choice == "2":
            a = get_number("a = ")
            b = get_number("b = ")
            result = subtract(a, b)
            history.append(f"{a} - {b} = {result}")

        elif choice == "3":
            a = get_number("a = ")
            b = get_number("b = ")
            result = multiply(a, b)
            history.append(f"{a} * {b} = {result}")

        elif choice == "4":
            a = get_number("a = ")
            b = get_number("b = ")
            result = divide(a, b)
            history.append(f"{a} / {b} = {result}")

        elif choice == "5":
            a = get_number("Alus = ")
            b = get_number("Aste = ")
            result = power(a, b)
            history.append(f"{a}^{b} = {result}")

        elif choice == "6":
            a = get_number("Arv = ")
            result = square_root(a)
            history.append(f"√{a} = {result}")

        elif choice == "7":
            a = get_number("Arv = ")
            b = get_number("Protsent = ")
            result = percent(a, b)
            history.append(f"{b}% arvust {a} = {result}")

        elif choice == "8":
            a = get_number("Arv = ")
            result = factorial(a)
            history.append(f"{int(a)}! = {result}")

        elif choice == "9":
            show_history()
            continue

        elif choice == "0":
            print("👋 Programm lõpetatud")
            break

        else:
            print("❌ Vale valik")
            continue

        print(f"✅ Tulemus: {result}\n")

    except ZeroDivisionError:
        print("❌ Viga: nulliga jagamine!\n")

    except ValueError:
        print("❌ Viga: sobimatu arv!\n")Ruudujuur (√)
7  Protsent
8  Faktoriaal
9  Ajalugu
0  Välju
""")


# Põhitsükkel
while True:
    menu()
    choice = input(" Vali tegevus: ")

    try:
        if choice == "1":
            a = get_number("a = ")
            b = get_number("b = ")
            result = add(a, b)
            history.append(f"{a} + {b} = {result}")

        elif choice == "2":
            a = get_number("a = ")
            b = get_number("b = ")
            result = subtract(a, b)
            history.append(f"{a} - {b} = {result}")

        elif choice == "3":
            a = get_number("a = ")
            b = get_number("b = ")
            result = multiply(a, b)
            history.append(f"{a} * {b} = {result}")

        elif choice == "4":
            a = get_number("a = ")
            b = get_number("b = ")
            result = divide(a, b)
            history.append(f"{a} / {b} = {result}")

        elif choice == "5":
            a = get_number("Alus = ")
            b = get_number("Aste = ")
            result = power(a, b)
            history.append(f"{a}^{b} = {result}")

        elif choice == "6":
            a = get_number("Arv = ")
            result = square_root(a)
            history.append(f"√{a} = {result}")

        elif choice == "7":
            a = get_number("Arv = ")
            b = get_number("Protsent = ")
            result = percent(a, b)
            history.append(f"{b}% arvust {a} = {result}")

        elif choice == "8":
            a = get_number("Arv = ")
            result = factorial(a)
            history.append(f"{int(a)}! = {result}")

        elif choice == "9":
            show_history()
            continue

        elif choice == "0":
            print("Programm lõpetatud")
            break

        else:
            print("Vale valik")
            continue

        print(f" Tulemus: {result}\n")

    except ZeroDivisionError:
        print(" Viga: nulliga jagamine!\n")

    except ValueError:
        print(" Viga: sobimatu arv!\n")
