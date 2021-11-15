from dinosaur import Dinosaur
class Herd:
    dinosaurs_list = []
    def __init__(self):
        self.create_herd()

        
    def create_herd(self):
        dino_1 = Dinosaur("deathosaurs",10, 5)
        dino_2 = Dinosaur("rockosaur",5,13)
        dino_3= Dinosaur("megasours",15,7)
        self.dinosaurs_list.append(dino_1)
        self.dinosaurs_list.append(dino_2)
        self.dinosaurs_list.append(dino_3)

# this_herd = Herd()
# this_herd.create_herd()
# print(this_herd.dinosaurs_list)