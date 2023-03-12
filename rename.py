import io
import random
f = io.open("C:/Users/remi9/OneDrive/Documents/Projets_code/RemBot/noms.txt",
            mode="r", encoding="utf-8").read()
names = f.split("\n")
while True:
    print(names[random.randint(0, len(names))])
    input()
