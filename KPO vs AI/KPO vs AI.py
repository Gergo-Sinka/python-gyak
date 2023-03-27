import random # külcső csomagok importálása

# függvények
def gép_válasza(e):
    return random.choice(e[0:3])

def döntés(a, b):
    if a == b:
        print("Döntetlen!")
    elif a == "flex":
        print("Oké, oké... nyertél!")
    elif a == "Na":
                print("Na")
    elif a == "hajrá":
        print("Fain vagy")
    elif(a== "kő" and b == "papír") or \
            (a == "papír" and b == "olló") or \
            (a == "olló" and b == "kő"):
        print("Vesztettél")
    else:
        print("Nyertél!")


def játék(e):
    j = "" # A játékos válasza
    while j  not in e:
        j = input(f"Mit választasz? {e[0:3]}")
    g = gép_válasza(e)
    print(f"A gép válasza: {g}")
    döntés(j, g)

eszközök = ["kő", "papír", "olló", "flex", "hajrá",]
while True:
    játék(eszközök)

