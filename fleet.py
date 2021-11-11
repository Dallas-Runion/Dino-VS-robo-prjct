from robot import Robot
class Fleet:
    def __init__(self):
        self.robots_list = []
    def make_fleet(self):
        robo_1 = Robot("Destructo", 100)
        robo_2 = Robot("tanko", 130)
        robo_3 = Robot("weako",7)
        self.robots_list.append(robo_1)
        self.robots_list.append(robo_2)
        self.robots_list.append(robo_3)
        print(self.robots_list)


my_fleet = Fleet()
my_fleet.make_fleet()
print(my_fleet.robots_list)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.robots.append (robot_1)




# robot_list = Fleet()------------------------main or batt---------------------------------
# robot_list.create_fleet()
# result = Fleet.robot_list[1].weapon
    # def add_to(self,instobj):-------------------------------use for attack----------------------------------
    #     self.robot_list.append(instobj) ---------------------use for attack------------------------------