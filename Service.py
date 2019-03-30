import time
import datetime
import os
from Repo import MemberRepo
from Repo import SportsRepo
# from Repo import GroupRepo
from Models import Member
from Models import Sport
from Models import Group

from PrintGraphicsUI import PrintGraphicsUI
from sortedcontainers import SortedDict

# 
# 
#-----------------------MEMBERLIST-----------------
#
#   


class MemberList:

    def __init__(self):
        self.id_map = SortedDict()
        self.name_map = SortedDict()
        self.phone_map = dict()
        self.email_map = SortedDict()
        self.unique_id = int(MemberRepo.load_un_id())


    def new_member(self):
        member_name = input("Input member Name (Jón Jónsson): ")
        member_phone = input("Input member Phone (898-8989): ")
        member_email = input("Input member Email (email@email.com): ")
        
        continues = True
        while continues:
            try:
                member_birthyear = int(input("Input member Birthyear (1999): "))
                continues = False
            except ValueError:
                print("Error! Only write a number!")

        new_member = Member(member_name, member_phone, member_email, member_birthyear,[], [], self.unique_id)
        self.add_new_member(new_member)
        return new_member

    def add_new_member(self, new_member):
        self.id_map[self.unique_id] = new_member
        self.name_map[new_member.name] = self.unique_id
        self.phone_map[new_member.phone] = self.unique_id
        self.email_map[new_member.email] = self.unique_id

        print("{} added to system.".format(new_member.name))
        self.unique_id += 1
        self.save_all_files()
        MemberRepo.save_un_id(self.unique_id)
        time.sleep(0.1)

        """
        -Kalla á fall sem skráir meðlim í sport 
        -kallar á annað föll sem að:
        group -> sport
        member -> sport
        sport -> group
        member -> group
        group -> member
        sport -> member
        
        """

    def search(self, search_term):
        if search_term in self.name_map:
            id = self.name_map[search_term]
        elif search_term in self.phone_map:
            id = self.phone_map[search_term]
        elif search_term in self.email_map:
            id = self.email_map[search_term]
        #SEARCH BY BIRTHDATES - DIFFERENT FUNCTION?
        else:
            return
        return self.id_map[id]

    
    def member_edit(self, selected_member):
        action = ""
        while action != "0":
            action = input()
            #If 1 - change name
            if action == "1":
                new_name = input("Please write new name: ")
                self.name_map[new_name] = self.name_map.pop(selected_member.name)
                selected_member.name = new_name
                return new_name
            
            #If 2 - change Phone No.
            elif action == "2":
                new_phone = input("Please write new phone (xxx-xxxx): ")
                self.phone_map[new_phone] = self.phone_map.pop(selected_member.phone)
                selected_member.phone = new_phone
                return new_phone
            
            #If 3 - change Email
            elif action == "3":
                new_email = input("Please write new email: ")
                self.email_map[new_email] = self.email_map.pop(selected_member.email)
                selected_member.email = new_email
                return new_email
            #If 4 - change Birthyear
            elif action == "4":
                try:
                    new_birthyear = int(input("Please write new birthyear (xxxx): "))
                    selected_member.birthyear = new_birthyear
                    return new_birthyear
                except ValueError:
                    print("Error! Only write a number!")
                    print("1. Name 2. Phone no 3. Email 4. Birthyear 5. Sport registration 0. Exit")
                    print("What would you like to edit?")

            #If 5 - change sports
            elif action == "5":
                pass

            #If 6 - change groups
            elif action == "6":
                pass
    
    def member_delete(self, selected_member):
        id = selected_member.unique_id
        del self.name_map[selected_member.name]
        del self.phone_map[selected_member.phone]
        del self.email_map[selected_member.email]
        del self.id_map[id]


        self.save_all_files()


    def save_all_files(self):
        #Temporary save solution - find way to put all in one dict? 
        MemberRepo.save(self.id_map, self.name_map, self.phone_map, self.email_map)

    def load_all_files(self):
        # load_success = True
        try:
            self.id_map, self.name_map, self.phone_map, self.email_map = MemberRepo.load()
            # return load_success
        except TypeError:
            print("TypeError")
    
    def get_members_ordered_by_name(self):
        ordered_list = []
        for name in self.name_map:
            ordered_list.append(self.id_map[self.name_map[name]])
        return ordered_list

    def test(self):
        self.add_new_member(Member("Karl Bernharðsson", "898-8787", "1@sport.is", 1989, [], [], 1))
        self.add_new_member(Member("Sigurður Sigurðsson", "844-8484", "2@sport.is", 2000, [], [], 2))
        self.add_new_member(Member("Magnús Friðriksson", "898-4111", "3@sport.is", 2001, [], [], 3))
        self.add_new_member(Member("Elísabet Skaargard", "778-1155", "4@sport.is", 2002, [], [], 4))
        self.add_new_member(Member("Knútur Olsen", "877-1588", "5@sport.is", 2000, [], [], 5))
        self.add_new_member(Member("Sigrún Tinnudóttir", "677-8877", "6@sport.is", 2010, [], [], 6))
        self.add_new_member(Member("Jón Karlsson", "661-8488", "7@sport.is", 2011, [], [], 7))
        self.add_new_member(Member("Geir Sigurður Magnússon", "771-2126", "8@sport.is", 2010, [], [], 8))
        self.add_new_member(Member("Bertrand Filibusarson", "771-2125", "9@sport.is", 2000, [], [], 9))
        self.add_new_member(Member("Notandi0", "771-2121", "10@sport.is", 2005, [], [], 10))
        self.add_new_member(Member("Notandi01", "771-2122", "11@sport.is", 1994, [], [], 11))
        self.add_new_member(Member("Notandi02", "771-2123", "12@sport.is", 1992, [], [], 12))
        self.add_new_member(Member("Notandi03", "771-2124", "13@sport.is", 1997, [], [], 13))
        
# # 
# # 
# #-----------------------SPORTLIST-----------------
# #
# #   


class SportList:
    def __init__(self):
        self.sport_map = SortedDict()

    def new_sport(self):
        name = input("Input sport Name (Football): ")
        new_sport = Sport(name)
        self.add_new_sport(new_sport)

    def add_new_sport(self, new_sport):
        #Makes sport map that has key: [name] = value: sport_object
        self.sport_map[new_sport.name] = new_sport
        print("{} added to system. You will be redirected to main menu.".format(new_sport.name))
        SportsRepo.save(self.sport_map)
    
    def new_group(self, sport_of_group):
        name = input("Write name of new group: ")
        try:
            group_size = input("Decide how big the group shall be: (number) ")
            #tuple of two integers, ages from (12,14)
            group_age_range_l = int(input("Ages ranging from: (number) "))
            group_age_range_h = int(input("to: (number) "))

            group_age_range = (group_age_range_l, group_age_range_h)

        except (ValueError, TypeError, IndexError):
            PrintGraphicsUI.oops()
        
        new_group = Group(name, group_size, group_age_range, 0, [], [])
        self.add_new_group(new_group, sport_of_group)


        return new_group #for when member makes new group to add to member?


    def add_new_group(self, new_group, sport_of_group):
        sport_of_group.sport_groups[new_group.name] = new_group
        self.save_all_files()
        print("Group was added. Returning to Main Menu.")
        time.sleep(0.4)



    def save_all_files(self):
        SportsRepo.save(self.sport_map)

    def load_all_files(self):
        try:
            self.sport_map = SportsRepo.load()
            # print(self.sport_map)
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
        self.add_new_sport(Sport("Football", [], {}))
        self.add_new_sport(Sport("Volleyball", [], {}))
        self.add_new_sport(Sport("Chess", [], {}))
        self.add_new_sport(Sport("Swimming", [], {}))

        # self.add_new_group
    def group_test(self):
        self.add_new_group(Group("Beginners (Foo)", 16, (6,12), 2, [], []), self.sport_map["Football"])
        self.add_new_group(Group("Intermediate (Foo)", 10, (12,16), 1, [], []), self.sport_map["Football"])
        self.add_new_group(Group("Pro (Foo)", 6, (16,35), 4, [], []), self.sport_map["Football"])

        self.add_new_group(Group("Beginners (Voll)", 16, (6,12), 2, [], []), self.sport_map["Volleyball"])
        self.add_new_group(Group("Intermediate (Voll)", 10, (10,33), 2, [], []), self.sport_map["Volleyball"])

        self.add_new_group(Group("Everybody (Che)", 30, (6,99), 5, [], []), self.sport_map["Chess"])

        self.add_new_group(Group("Beginners (Swi)", 16, (6,12), 1, [], []), self.sport_map["Swimming"])
        self.add_new_group(Group("Intermediate (Swi)", 10, (10,20), 0, [], []), self.sport_map["Swimming"])
        print("test success")
        time.sleep(1.0)


# class GroupList:
#     """Makes a list of the Groups and functions to work with groups"""

#     def __init__(self):
#         self.group_map = SortedDict()

#     

#     def add_new_group(self, new_group):
#         self.group_map[new_group.name] = new_group
#         GroupRepo.save(self.group_map)
#         print("Group was added. Returning to Main Menu.")
#         time.sleep(0.4)

    def get_groups(self):
        ordered_list = []
        for group_object in self.group_map:
            ordered_list.append(self.group_map[group_object])
        return ordered_list

#     def save_all_files(self):
#         GroupRepo.save(self.group_map)

#     def load_all_files(self):
#         try:
#             self.group_map = GroupRepo.load()
#             # print(self.group_map)
#         except TypeError:
#             print("TypeError")


    # def test(self):
        # self.add_new_group(Group("Fjölnir", 10, (10,12), None, [], []))
        # self.add_new_group(Group("Ármann", 12, (12,14), None, [], []))
        # self.add_new_group(Group("Breiðablik", 6, (20,26), None, [], []))
        # self.add_new_group(Group("Fylkir", 80, (5,99), None, [], []))

