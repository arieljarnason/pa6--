import time
import datetime
import os
from Repo import MemberRepo
from Repo import SportsRepo
from Repo import GroupRepo
from Models import Sport
from Models import Group
from Models import Member
from PrintGraphicsUI import PrintGraphicsUI
from sortedcontainers import SortedDict

# 
# 
#-----------------------SPORTLIST-----------------
#
#   



class SportList:
    def __init__(self):
        self.sport_map = SortedDict()

    def new_sport(self):
        sport_name = input("Input sport Name (Football): ")
        new_sport = Sport(sport_name)
        self.add_new_sport(new_sport)

    def add_new_sport(self, new_sport):
        #Makes sport map that has key: [name] = value: sport_object
        self.sport_map[new_sport.sport_name] = new_sport
        print("{} added to system. You will be redirected to main menu.".format(new_sport.sport_name))
        SportsRepo.save(self.sport_map)


    def save_all_files(self):
        SportsRepo.save(self.sport_map)

    def load_all_files(self):
        try:
            self.sport_map = SportsRepo.load()
            print(self.sport_map)
        except TypeError:
            print("TypeError")
        
    def get_sports(self):
        ordered_list = []
        for sport_object in self.sport_map:
            ordered_list.append(self.sport_map[sport_object])
        return ordered_list
        # print(self.sport_map)
        # return self.sport_map

    def test(self):
        self.add_new_sport(Sport("Football", [5, 7, 12, 13]))
        self.add_new_sport(Sport("Volleyball", [2, 4, 5, 12]))
        self.add_new_sport(Sport("Chess", [1, 3, 10, 11]))