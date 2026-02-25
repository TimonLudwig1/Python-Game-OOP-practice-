from buildings import * 


recruiting_options = {

    1: Peasant,
    2: Barbar,
    3: Archer,
    4: Knight
}

def store_gold(game):
    game.village.store_gold()
    print(f"\n Gold wurde gesammelt. Du hast {game.village.treasury.total_gold} Gold")

def store_meat(game):
    game.village.store_meat()
    print(f"Fleisch wurde gesammelt, du hast {game.village.barn.total_meat} Fleisch")

def invest(game):
    investment = int(input("Wie viel Gold willst du investieren\n> "))
    game.village.deposit_gold_investment(investment)

def recruiting(game):
    print("Welche Truppe möchtest du rekrutieren?\n")
    print("1. Bauer\n2. Barbar\n3. Schütze\n4. Ritter")
    troop_choice = int(input("> "))
    if troop_choice in recruiting_options:
        recruit = recruiting_options[troop_choice]
        recruit_instance = recruit()
        game.village.recruit_troop(recruit_instance) 

def attack(game):
    print("Deine Truppen ziehen in den Kampf")
    time.sleep(5)
    print("Deine Armee kämpft hart")
    time.sleep(5)
    game.village.attack_enemy()

def show_army(game):
    print("Deine Armee sieht wie folgt aus:")
    army_dict = {}
    for troop in game.village.army.troops:
        army_dict[troop.name] = army_dict.get(troop.name, 0) + 1 
    print(army_dict)
    print(f"Power: {game.village.army.total_army_damage}")
    print(f"Größe: {game.village.army.total_army_space}")

def upgrades(game):
    upgrade_choices_dict = {
        1: "Goldmine",
        2: "Farm",
        3: "Armeelager",
        4: "Rathaus"
    }

    print("Welches Gebäude willst du upgraden?")
    for key, value in upgrade_choices_dict.items():
        print(key, value)
    upgrade_choice = int(input("> "))
    if upgrade_choice == 1:
        game.village.goldmine.upgrade_goldmine()
        print(f"Goldmine wurde auf Level: {game.village.goldmine.level} verbessert")
    elif upgrade_choice == 2:
        game.village.farm.upgrade_farm()
        print(f"Farm wurde auf Level: {game.village.farm.level} verbessert")
    elif upgrade_choice == 3:
        game.village.army.armycamp.upgrade_armycamp()
        print(f"Armeelager wurde auf Level: {game.village.army.armycamp.level} verbessert")
    elif upgrade_choice == 4:
        game.village.townhall.upgrade_townhall()
        print(f"Rathaus wurde auf Level: {game.village.townhall.level} verbessert")
    else:
        print("Keine gültige Auswahl")



    