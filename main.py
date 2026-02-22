class townhall:
    def __init__(self, level, boost, upgrade_cost, name, counter):
        self.name = "Townhall"
        self.level = 1
        self.boost = 1                                                        #[0, 10, 25, 35, 45, 60, 80, 100, 150, 200]
        self.upgrade_cost = 5000                                                #[5000, 7500, 11000, 13000, 16000, 20000, 30000, 41000, 60000, 100000]
        self.counter = 0 
    
    def upgrade_townhall(self):
        self.level +=1 
        self.upgrade_cost += 5000
        self.boost +=0.25
        return self.level, self.upgrade_cost, self.boost


class goldmine:
    def __init__(self, level, name, upgrade_cost, production_rate, storage):
        self.name = "Goldmine"
        self.level = 1
        self.upgrade_cost = 3500
        self.production_rate = 800
        self.storage = 0

    def mining(self):
        self.storage =+ self.production_rate
        return self.storage
    
    def upgrade_goldmine(self):
        self.level +=1 
        self.production_rate += 1000
        self.upgrade_cost =+ 1200
        return self.level, self.upgrade_cost, self.production_rate

        
    

#class bank:

#class army_camp:
