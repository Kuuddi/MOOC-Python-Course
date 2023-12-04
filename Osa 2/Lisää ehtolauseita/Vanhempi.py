person1 = input("Nimi: ")
age1 = int(input("Ikä: "))

person2 = input("Nimi: ")
age2 = int(input("Ikä: "))

if age1 == age2:
    print(f"{person1} ja {person2} ovat yhtä vanhoja")

elif age2 > age1:
    print(f"Vanhempi on {person2}")

elif age1 > age2:
    print(f"Vanhempi on {person1}")
