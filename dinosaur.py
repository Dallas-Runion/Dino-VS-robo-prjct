from robot import Robot
class Dinosaur:

    def __init__(self,name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        
    def attack(self, Robot):
        Robot.health -= self.attack_power
# dino_1 = Dinosaur("deathosaurs",10, 95)
# dino_2 = Dinosaur("rockosaur",5,130)
# dino_3= Dinosaur("megasours",15,75)
# print(dino_1.name)
# print(dino_1.health)
# print(dino_2.name)