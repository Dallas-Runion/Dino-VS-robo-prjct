# from dinosaur import Dinosaur
from weapon import Weapon
class Robot:


    # print(weapon.name)
    def __init__(self, name_bot,health):
        self.name = name_bot
        self.weapon = Weapon("deathgun12", 10)
        self.health = health
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        
    # def chang_wep(self, wep): ----------------------change wep 
    #     self.weapon =

# robo_1 = Robot("Destructo", 100)
# robo_2 = Robot("tanko", 130)
# robo_3 = Robot("weako",7)
# print(robo_1.name)
# print(robo_2.weapon.name)
# print(robo_3)