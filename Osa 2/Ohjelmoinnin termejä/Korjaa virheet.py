luku = int(input("Anna luku: "))

if luku > 100:
    print("Luku oli suurempi kuin sata")
    print("Nyt luvun arvo on pienentynyt sadalla")
    print(f"Arvo on nyt {luku - 100}")
    print(f"{luku - 100} taitaa olla onnenlukuni!")

elif luku < 100:
    print(f"{luku} taitaa olla onnenlukuni!")

print("Hyvää päivänjatkoa!")