from robot import Robot
class Fleet:
    robots_list = []
    def __init__(self):
        self.make_fleet()
    def make_fleet(self):
        robo_1 = Robot("Destructo", 10)
        robo_2 = Robot("tanko", 13)
        robo_3 = Robot("weako",7)
        self.robots_list.append(robo_1)
        self.robots_list.append(robo_2)
        self.robots_list.append(robo_3)
        
        # print(self.robots_list)
    # def display_fleet(self):

# my_fleet = Fleet()
# my_fleet.make_fleet()
# # my_fleet.display_fleet()
# gx = vars(my_fleet.robots_list)
# print(gx)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.robots.append (robot_1)




# robot_list = Fleet()------------------------main or batt---------------------------------
# robot_list.create_fleet()
# result = Fleet.robot_list[1].weapon
    # def add_to(self,instobj):-------------------------------use for attack----------------------------------
    #     self.robot_list.append(instobj) ---------------------use for attack------------------------------