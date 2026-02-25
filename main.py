from buildings import * 
from actions import * 

game = Game()

while True: 
    #game.tick()

    print("\nWas möchtetst du tun?\n")
    print("1. Gold sammeln")
    print("2. Fleisch sammeln")
    print("3. Geld anlegen")
    print("5. Truppen rekrutieren")
    print("6. Armee anschauen")
    print("7. Raid starten")

    #print(f"Deine Goldreserven betragen: {game.village.treasury.total_gold}")
    #print(f"Deine Fleischreserven betragen: {game.village.barn.total_meat}")
    #print(f"Dein investment ist mitlerweile: {game.village.bank.amount * (1 + game.village.bank.interest_rate)**game.village.bank.investment_duration} wert")

    choice = int(input("> "))
    if choice == 1:
        store_gold(game)
    if choice == 2: 
        store_meat(game)
    if choice == 3:
        invest(game)
    if choice == 4:
        recruiting(game)
    if choice == 5:
        show_army(game)
    if choice == 6:
        attack(game)




