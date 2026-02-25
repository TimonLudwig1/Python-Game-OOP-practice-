import time 
import threading

class Building:
    def __init__(self, upgrade_cost, name, level = 1):
        self.level = level
        self.upgrade_cost = upgrade_cost
        self.name = name


class Townhall(Building):
    def __init__(self):
        super().__init__(upgrade_cost=5000, name="Townhall")                    
        self.boost = 1                                                        
        self.counter = 0 
    
    def upgrade_townhall(self):
        self.level +=1 
        self.upgrade_cost += 5000
        self.boost +=0.25
        return self.level, self.upgrade_cost, self.boost


class Farm(Building):
    def __init__(self):
        super().__init__(upgrade_cost=5000, name="Farm")
        self.meat_production_rate = 800
        self.meat_storage = 0
    
    def farming(self):
        self.meat_storage += self.meat_production_rate
        return self.meat_storage
    
    def upgrade_farm(self):
        self.level +=1
        self.meat_production_rate += 1000
        self.upgrade_cost += 1200 
        return self.level, self.upgrade_cost, self.meat_production_rate
    
    def collect_meat(self):
        meat_payout = self.meat_storage
        self.meat_storage = 0
        return meat_payout 


class Goldmine(Building):
    def __init__(self):
        super().__init__(upgrade_cost=5000, name="Goldmine")
        self.gold_production_rate = 800
        self.gold_storage = 0

    def mining(self):
        self.gold_storage += self.gold_production_rate
        return self.gold_storage
    
    def upgrade_goldmine(self):
        self.level +=1 
        self.gold_production_rate += 1000
        self.upgrade_cost += 1200
        return self.level, self.upgrade_cost, self.gold_production_rate
    
    def collect_gold(self):
        gold_payout = self.gold_storage
        self.gold_storage = 0
        return gold_payout 


class Bank:
    def __init__(self):
        self.level = 1
        self.name = "Bank"
        self.interest_rate = 0.05
        self.investment_duration = 0
        self.amount = 0
    
    def deposit(self, amount):
        self.amount = amount
        return amount
    
    def intrest_tick(self):
        self.investment_duration += 1 
    
    def withdraw(self):
        payout = self.amount * (1 + self.interest_rate)**self.investment_duration
        self.amount = 0
        self.investment_duration = 0
        return payout


class Treasury(Building):
    def __init__(self):
        super().__init__(upgrade_cost=4500, name="Goldlager")
        self.total_gold: float = 0
        self.max_gold_storage = 15000
        
    def upgrade_treasury(self):
        self.level +=1 
        self.upgrade_cost +=1500
        self.max_gold_storage +=20000


class Barn(Building):
    def __init__(self):
        super().__init__(upgrade_cost=4500, name="Scheune")
        self.total_meat = 0
        self.max_meat_storage = 15000

    def upgrade_barn(self):
        self.level +=1
        self.upgrade_cost +=1500
        self.max_meat_storage +=20000


class Troop:
    def __init__(self, name, damage, recruiting_cost, health, weight):
        self.name = name 
        self.damage = damage
        self.recruiting_cost = recruiting_cost
        self.health = health
        self.weight = weight


class Peasant(Troop):
    def __init__(self):
        super().__init__(name="Bauer", damage=2, recruiting_cost=300, health=20, weight=5)


class Barbar(Troop):
    def __init__(self):
        super().__init__(name="Barbar", damage=25, recruiting_cost=3000, health=200, weight=45)


class Archer(Troop):
    def __init__(self):
        super().__init__(name="Schütze", damage=35, recruiting_cost=3000, health=100, weight=40)


class Knight(Troop):
    def __init__(self):
        super().__init__(name="Ritter", damage=30, recruiting_cost=3200, health=450, weight=60)


class Army():
    def __init__(self):
        self.troops = []
        self.armycamp = ArmyCamp()
        self.total_army_damage = 0
        self.total_army_space = 0

    def update_army_damage(self):
        self.total_army_damage = sum(troop.damage for troop in self.troops)
    
    def update_army_space(self):
        self.total_army_space = sum(troop.weight for troop in self.troops)
        

class ArmyCamp:
    def __init__(self):
        self.level = 1
        self.space = 100
        self.upgrade_cost = 3000
    
    def upgrade_armycamp(self):
        self.level += 1
        self.upgrade_cost += 1000
        self.space += 200


class Enemy:
    def __init__(self):
        self.power = 150
        self.level = 1
        self.name = "Feind"

    def update_level(self):
        self.level +=1
        self.power = self.power**1.25


class Village():
    def __init__(self):
        self.goldmine = Goldmine()
        self.treasury = Treasury()
        self.farm = Farm()
        self.barn = Barn()
        self.bank = Bank()
        self.townhall = Townhall()
        self.enemy = Enemy()
        self.army = Army()

    def store_gold(self):
        gold = self.goldmine.collect_gold()
        self.treasury.total_gold += gold 
    
    def store_meat(self):
        meat = self.farm.collect_meat()
        self.barn.total_meat += meat 

    def store_withdrawl(self):
        money = self.bank.withdraw()
        self.treasury.total_gold += money
    
    def attack_enemy(self):
        if self.enemy.power <= self.army.total_army_damage:
            print("Glückwunsch, du hast den Gegner besigt!")
            self.enemy.update_level()
        else:
            print("Du warst nicht stark genung, errichte eine stärkere Armee!")
        
        self.army.troops.clear()
        self.army.update_army_damage()
    
    def recruit_troop(self, troop):
        if self.army.total_army_space + troop.weight > self.army.armycamp.space:
            print("Nicht genug Platz. Die Truppe wird nicht hinzugefügt!")
            return
        if self.treasury.total_gold < troop.recruiting_cost:
            print("Nicht genug Gold!") 
            return
        
        self.army.troops.append(troop)
        self.army.update_army_damage()
        self.army.update_army_space()
        self.treasury.total_gold -= troop.recruiting_cost
    
    def deposit_gold_investment(self, amount):
        if self.treasury.total_gold >= amount:
            self.bank.deposit(amount)
            self.treasury.total_gold -= amount
        else:
            print("Du hast nicht genug Gold")
        

class Game():
    def __init__(self):
        self.village = Village()
        self.start_ticking()
    
    def tick(self):
        while True:
            time.sleep(10)
            self.village.farm.farming()
            self.village.goldmine.mining()
    
    def start_ticking(self):
        thread = threading.Thread(target=self.tick, daemon=True)
        thread.start()
