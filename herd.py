from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs_list = []
        
    def create_herd(self):
        dino_1 = Dinosaur("deathosaurs",10, 95)
        dino_2 = Dinosaur("rockosaur",5,130)
        dino_3= Dinosaur("megasours",15,75)
        self.dinosaurs_list.append(dino_1.name)
        self.dinosaurs_list.append(dino_2.name)
        self.dinosaurs_list.append(dino_3.name)

this_herd = Herd()
this_herd.create_herd()
print(this_herd.dinosaurs_list)