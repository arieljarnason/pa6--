import os
import time
import pickle
from PrintGraphicsUI import PrintGraphicsUI
from Service import MemberList
from Service import SportList
from Service import GroupList

from Models import Sport
from Models import Member
from Models import Group

class MainMenuUI:
    def __init__(self):
        self.MemberList = MemberList()
        self.SportList = SportList()
        self.GroupList = GroupList()

    def main(self):
        """Main menu"""

        action = ""
        #
        # 
        # 
        # 
        # TESTCASE:
        # self.SportList.test()
        # self.MemberList.test()
        # self.GroupList.test()
        #TESTCASE:
        #
        #
        #
        #
        #



        while action != "0":
            # os.system('cls' if os.name == 'nt' else 'clear')

            print("Loading savefiles....")

            self.MemberList.load_all_files()
            self.SportList.load_all_files()
            self.GroupList.load_all_files()



            PrintGraphicsUI.print_intro()
            #Use Pickle to load saved data. If No savefile has been made -> error. 


            # 
            # 
            # TESTCASE:
            # print("TESTSEST")
            # self.test()
            #TESTCASE:
            #
            #


            action = input("What would you like to do?\n")


                





            #1. Register new sport
            if action == "1":
                """Goes to service->Sport class and makes new Sport object
                checks if that Sport already exists"""
                self.SportList.new_sport()

            #2. Register new member
            elif action == "2":
                """Goes to service->Member class, makes new Member object
                Gives each member a unique ID no for easy listing"""
                self.MemberList.new_member()

            #3. Register new group
            elif action == "3":
                self.GroupList.create_new_group()
                
            
            #4. Register member into sport
            elif action == "4":
                pass
            
            #5. Register member into group
            elif action == "5":
                """Register member in sport"""
                pass

            #6. Find member - get data screen up
            elif action == "6":
                """Goes to service -> returns user by input name"""
                found_member = None
                search_term = input("Please write name, phone no(xxx-xxxx), email or birthyear(xxxx) of member: ")
                
                found_member = self.MemberList.search(search_term)
                if found_member != None:
                    PrintGraphicsUI.member_profile(found_member)
                    self.member_profile_selected(found_member)
                else: 
                    PrintGraphicsUI.print_not_found()

            #7. List all members - select member and see info, and all sport
            elif action == "7":
                """Prints list of all members"""
                self.print_all_members()

            #List all sports - select sport and see detailed info(list of users)
            elif action == "8":
                """Prints list of all sports"""
                self.print_all_sports()

            # 9. List all groups
            elif action == "9":
                """Lists all groups"""
                self.print_all_groups()

            #0. Save & Exit
            elif action == "0":
                self.MemberList.save_all_files()
                self.SportList.save_all_files()
                self.GroupList.save_all_files()

            else:
                PrintGraphicsUI.print_sel_error()

    def print_all_members(self):
        
        all_members = self.MemberList.get_members_ordered_by_name()
        lower = 0; upper = 8; action = ""; loop = True; highest = len(all_members)

        while loop:
            os.system('cls' if os.name == 'nt' else 'clear')
            if all_members == []: print("No members have been registered!")
            else: 
                print("\Members:")
                print()
                print("{:>10} {:>25s} {:>20s}{:<12s}{}{:>4}".format("Name:", "Age:", "Phone No:", "Email:", "Unique ID:", "Sports"))
                print("-"*106)

            for index, item in enumerate(all_members): 
                if index in range(lower,upper):
                    print ("{:4s} {:}".format(str(index+1).zfill(3), item))
            print()
            print("-"*106)

            action = input("\n{}\n{}\n{}\n{}\n{}\n".format(
                "1. Pick from list","2. Up list",
                "3. Down list","4. Print all members",
                "0. Exit"))
            
            if action == "1": #Choose to pick a member by nr
                loop = False
                self.pick_a_member(all_members)


            elif action == "2": #Go up
                if lower > 0: lower -= 8
                if upper > 8: upper -= 8
            elif action == "3": #Go down
                if upper >= highest:
                    print("There are no more members!")
                    time.sleep(1.0)
                else:
                    lower += 8; upper += 8
            elif action == "4": #Show all
                lower = 0; upper = highest
            elif action == "0": #Exit
                loop = False
            else: 
                PrintGraphicsUI.print_sel_error()

    def pick_a_member(self, member_list):
        try:
            selection = input("Input member's number: ")
            if selection == "0":
                return
            else:
                selected_member = member_list[int(selection)-1]
                PrintGraphicsUI.member_profile(selected_member)
                self.member_profile_selected(selected_member)
        except (ValueError, TypeError, IndexError):
            PrintGraphicsUI.print_sel_error()


    def member_profile_selected(self, found_member):
        action = ""

        while action != 0:
            action = input("\n1. Edit member 2. Remove member 0. Exit\n")
            if action == "1":
                print("1. Name 2. Phone no 3. Email 4. Birthyear 5. Sport registration 6. Groups 0. Exit")
                print("What would you like to edit?")

                new_info = self.MemberList.member_edit(found_member)
                if new_info != None:
                    print("Info has been changed to {}".format(new_info))
                print("Returning to main menu")
                self.MemberList.save_all_files()
                time.sleep(1)
                return

            elif action == "2":
                self.MemberList.member_delete(found_member)
                print("Member has been deleted. Returning to Main menu.")
                time.sleep(1)
                return
            
            elif action == "0":
                return
            else:
                PrintGraphicsUI.print_sel_error()
                PrintGraphicsUI.member_profile(found_member)

    def print_all_sports(self):
        ##Mögulega gera bara einn prentunarfítus?

        all_sports = self.SportList.get_sports()
        # print(all_sports)
        loop = True

        while loop:
            os.system('cls' if os.name == 'nt' else 'clear')
            if all_sports == []: print("No sports have been registered!")
            else: 
                print("\Sports:")
                print("-"*106)
                print()
            for index, item in enumerate(all_sports): 
                print("{:4s} {:}".format(str(index+1).zfill(2), item))
            print()
            print("-"*106)

            action = input("\n{}\n{}\n".format("1. Pick from list",
                "0. Exit"))
            
            if action == "1": #Choose to pick a sport by nr
                loop = False
                self.pick_a_sport(all_sports)

            elif action == "0": #Exit
                loop = False

            else: 
                PrintGraphicsUI.print_sel_error()
            
    def pick_a_sport(self, sport_list):
        try:
            selection = input("Input sport number: ")
            if selection == "0":
                return
            else:
                selected_sport = sport_list[int(selection)-1]
                self.sport_selected(selected_sport)
        except (ValueError, TypeError, IndexError):
            PrintGraphicsUI.print_sel_error()
    
    def sport_selected(self, selected_sport):
        PrintGraphicsUI.sport_information(selected_sport)
        print(selected_sport.sport_members)
        print(selected_sport.sport_groups)
        getout = input("Press any key to return to Main menu")



    def print_all_groups(self):
        ##Mögulega gera bara einn prentunarfítus?
        
        all_groups = self.GroupList.get_groups()
        # print(all_sports)
        loop = True

        while loop:
            os.system('cls' if os.name == 'nt' else 'clear')
            if all_groups == []: print("No groups have been registered!")
            else: 
                print("\Groups:")
                print("{:>10} {:>25s} {:>20s}{:>12s}".format("Name:", "Size:", "Age range:", "Sport:"))

                print("-"*106)
                print()
            for index, item in enumerate(all_groups): 
                print("{:4s} {:}".format(str(index+1).zfill(2), item))
            print()
            print("-"*106)

            action = input("\n{}\n{}\n".format("1. Pick from list",
                "0. Exit"))
            
            if action == "1": #Choose to pick a sport by nr
                loop = False
                self.pick_a_group(all_groups)

            elif action == "0": #Exit
                loop = False

            else: 
                PrintGraphicsUI.print_sel_error()

    def pick_a_group(self, group_list):
        try:
            selection = input("Input group number: ")
            if selection == "0":
                return
            else:
                selected_group = group_list[int(selection)-1]
                self.group_selected(selected_group)
        except (ValueError, TypeError, IndexError):
            PrintGraphicsUI.print_sel_error()
        
    def group_selected(self, selected_group):
        PrintGraphicsUI.group_info(selected_group)
        print(selected_group.group_members)
        getout = input("Press any key to return to Main menu")







    def test(self):
        # self.MemberList.id_map[1].sports.append(self.SportList.sport_map["Football"])
        # self.MemberList.id_map[1].sports.append(self.SportList.sport_map["Volleyball"])
        # self.MemberList.id_map[2].sports.append(self.SportList.sport_map["Football"])
        # self.MemberList.id_map[3].sports.append(self.SportList.sport_map["Chess"])
        # self.MemberList.id_map[4].sports.append(self.SportList.sport_map["Chess"])
        # self.MemberList.id_map[5].sports.append(self.SportList.sport_map["Volleyball"])
        # self.MemberList.id_map[6].sports.append(self.SportList.sport_map["Volleyball"])
        # self.MemberList.id_map[7].sports.append(self.SportList.sport_map["Volleyball"])
        # self.MemberList.id_map[7].sports.append(self.SportList.sport_map["Football"])
        # self.MemberList.id_map[7].sports.append(self.SportList.sport_map["Chess"])
        # self.MemberList.id_map[8].sports.append(self.SportList.sport_map["Football"])
        # self.MemberList.id_map[9].sports.append(self.SportList.sport_map["Football"])
        # self.MemberList.id_map[10].sports.append(self.SportList.sport_map["Football"])
        # self.MemberList.id_map[10].sports.append(self.SportList.sport_map["Chess"])
        # self.MemberList.id_map[11].sports.append(self.SportList.sport_map["Football"])
        # self.MemberList.id_map[12].sports.append(self.SportList.sport_map["Chess"])
        # self.MemberList.id_map[13].sports.append(self.SportList.sport_map["Volleyball"])

        # self.GroupList.group_map["Fjölnir"].group_sport = self.SportList.sport_map["Football"]
        # self.GroupList.group_map["Ármann"].group_sport = self.SportList.sport_map["Chess"]
        # self.GroupList.group_map["Breiðablik"].group_sport = self.SportList.sport_map["Volleyball"]

        # self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[1])
        # self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[2])
        # self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[7])
        # self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[8])
        # self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[9])
        # self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[10])
        # self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[11])
        # self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[11])
        # self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[3])
        # self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[4])
        # self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[7])
        # self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[10])
        # self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[12])
        # self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[2])
        # self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[5])
        # self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[6])
        # self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[7])
        # self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[13])


        # self.SportList.sport_map["Football"].sport_groups.append(self.GroupList.group_map["Fjölnir"])
        # self.SportList.sport_map["Chess"].sport_groups.append(self.GroupList.group_map["Ármann"])
        # self.SportList.sport_map["Volleyball"].sport_groups.append(self.GroupList.group_map["Breiðablik"])

        # self.MemberList.id_map[1].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[1].groups.append(self.GroupList.group_map["Breiðablik"])
        # self.MemberList.id_map[2].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[3].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[4].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[5].groups.append(self.GroupList.group_map["Breiðablik"])
        # self.MemberList.id_map[6].groups.append(self.GroupList.group_map["Breiðablik"])
        # self.MemberList.id_map[7].groups.append(self.GroupList.group_map["Breiðablik"])
        # self.MemberList.id_map[7].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[7].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[8].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[9].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[10].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[10].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[11].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[12].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[13].groups.append(self.GroupList.group_map["Breiðablik"])

        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[1])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[3])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[7])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[8])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[9])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[10])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[11])
        # self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[2])
        # self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[5])
        # self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[6])
        # self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[7])
        # self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[13])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[3])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[4])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[7])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[10])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[12])
        pass

