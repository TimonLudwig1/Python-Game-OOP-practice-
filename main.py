from buildings import * 

game = Game()
print("Choose your first building:\n")
inp_first_building = int(input("1: Goldmine\n2: Farm\n"))
if inp_first_building == 1:
    goldmine = Goldmine()
elif inp_first_building == 2:
    farm = Farm()
else:
    print("You did not press 1 or 2")