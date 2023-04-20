from random import *
joueur1 = 50
joueur2 = 50
potion = 3
skipturn = False





while True:
    if skipturn:
        print("Vous passez le tour")
        skipturn = False
    else: 
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("attaquez l'ennemi  (1)   ou     utiliser une potion   (2)")
        if user_choice == "1":
            attaque1 = randint(5, 10)
            joueur2 -= attaque1
            print(f"vous avez fait {attaque1} dégats")
        elif user_choice == "2":
            if potion > 0:
                soigné = randint(15, 50)
                joueur1 += soigné
                potion -= 1
                skipturn = True
                print(f"vous avez gagné {soigné} pv     et il vous reste {potion} potion")
            else:
                print("Il ne vous reste plus de potion")
                continue
    if joueur2 <= 0:
        print("Vous avez gagné")
        break
    attaque2 = randint(5, 15)
    joueur1 -= attaque2
    print(f"il vous à fait {attaque2} dégats")
    print(f"il te reste {joueur1} pv ")
    print(f"il lui reste {joueur2} pv ")
    print("-" * 70)
    if joueur1 <= 0:
        print("vous avez perdu")
        break

