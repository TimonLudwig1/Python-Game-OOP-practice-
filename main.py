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

class Bank:
    def __init__(self):
        self.level = 1
        self.name = "Bank"
        self.interest_rate = 0.05
        self.investment_duration = 0
    
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
         


#class army_camp:
# hier brauche ich die Möglichkeit verschiedene Kämpfer zu rekrutieren, für unterschiedliche Preise, die dann dementsprechend immer mächtiger werden, um dann die Wellen an Gegner abzuwehren.

