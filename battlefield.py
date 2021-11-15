from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet
from robot import Robot
class Battlefield:
    def __init__(self,name):
        self.dino_herd = Herd()
        self.robo_fleet = Fleet()

    def display_welcome(self):
        print("Welcome to robots VS dinosaurs")

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winner()

 




    def battle(self):

        while (len(self.robo_fleet.robots_list) >0) and (len(self.dino_herd.dinosaurs_list)>0):

            selected_robo = self.show_robo_opponent_options()
            selected_dino = self.show_dino_opponent_options()
 
            while selected_dino.health >0 or selected_robo.health >0:

                self.robo_turn(selected_dino,selected_dino) 
                self.dino_turn(selected_robo,selected_dino)

            if (selected_dino.health <= 0) :
                print ("Robots wins this Round!")

            elif selected_robo.health <= 0:
                print("Dinosaur wins this round!")




    
    
    def dino_turn(self,robo, dino):

        dino.attack(robo)

        if (robo.health <= 0):
            self.robo_fleet.robots_list.remove(robo)


    def robo_turn(self,dino_obj, robot):

        robot.attack(dino_obj)
        if (dino_obj.health <= 0):
            self.dino_herd.dinosaurs_list.remove(dino_obj)



    def show_dino_opponent_options(self):
        # if len(self.dino_herd.dinosaurs_list) ==3:
        print(f"choose your dino by number {[dino.name for dino in self.dino_herd.dinosaurs_list]}")
              
        choosen_index = int(input ())
        if choosen_index == 1:
            dinoasursel = self.dino_herd.dinosaurs_list[0]
            return dinoasursel
        elif choosen_index ==2:
            dinoasursel = self.dino_herd.dinosaurs_list[1]
            return dinoasursel        
        elif choosen_index ==3:
            dinoasursel = self.dino_herd.dinosaurs_list[2]
            return dinoasursel



    def show_robo_opponent_options(self):
        print(f"choose your robot by number {[robot.name for robot in self.robo_fleet.robots_list]}")
        
        dino_index = int(input())
        if dino_index == 1:
            choosenrobo = self.robo_fleet.robots_list[0]
            return choosenrobo
        elif dino_index == 2:
            choosenrobo = self.robo_fleet.robots_list[1]
            return choosenrobo
        elif dino_index == 3:
            choosenrobo = self.robo_fleet.robots_list[2]
            return choosenrobo

    def display_winner(self):
        if len(self.dino_herd.dinosaurs_list) ==0:
            print("ROBOTS WIN")
        elif len(self.robo_fleet.robots_list) ==0:
            print("DINOSAURS WIN")