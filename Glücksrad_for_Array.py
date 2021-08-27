import random
import time

print('Gebe die Anzahl der Leute an')
x = int(input())
print('Heute sind ' + str(x) + " Leute mit dabei")
time.sleep(2.5)

Packs = []
counter = 1

for i in range(0,x):
    
   
    print("Bitte geben den Namen für die " + str(counter) + "te Person ein")
    counter += 1
    UserInput = input()
    Packs.append(UserInput)

    
time.sleep(2.5)   

for j in range(0,len(Packs)):
    randomvar = random.choice(Packs)
    print(str(randomvar) + " ist an der Reihe ")
    index = Packs.index(randomvar)
    Packs.pop(index)
    print("Warte auf Eingabe")
    input()
    
print("Danke für den Stream! <3")



