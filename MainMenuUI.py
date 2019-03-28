import os
import time
import pickle
from PrintGraphicsUI import PrintGraphicsUI
from Service import Member
from Service import MemberList
from Service import Sport
from Service import SportList


class MainMenuUI:
    def __init__(self):
        # self.default_save_file = "SportStudSave01.p"
        self.MemberList = MemberList()
        self.SportList = SportList()

    def main(self):
        """Main menu"""

        action = ""
        #
        # 
        # 
        # 
        # TESTCASE:
        self.MemberList.test()
        self.SportList.test()
        #TESTCASE:
        #
        #
        #
        #
        #



        while action != "0":
            os.system('cls' if os.name == 'nt' else 'clear')

            print("Loading savefiles....")

            self.MemberList.load_all_files()
            self.SportList.load_all_files()

            PrintGraphicsUI.print_intro()
            #Use Pickle to load saved data. If No savefile has been made -> error. 

            action = input("What would you like to do?\n")
            #Register new sport
            if action == "1":
                """Goes to service->Sport class and makes new Sport object
                checks if that Sport already exists"""
                self.SportList.new_sport()

            #Register new member
            elif action == "2":
                """Goes to service->Member class, makes new Member object
                Gives each member a unique ID no for easy listing"""
                self.MemberList.new_member()

            #Register new group
            elif action == "3":
                pass

            #Find member - get data screen up
            elif action == "4":
                """Goes to service -> returns user by input name"""
                found_member = None
                search_term = input("Please write name, phone no(xxx-xxxx), email or birthyear(xxxx) of member: ")
                
                found_member = self.MemberList.search(search_term)
                if found_member != None:
                    PrintGraphicsUI.member_profile(found_member)
                    self.member_profile_selected(found_member)
                else: 
                    PrintGraphicsUI.print_not_found()

            #List all members - select member and see info, and all sport
            elif action == "5":
                """Prints list of all members"""
                self.print_all_members()

            #List all sports - select sport and see detailed info(list of users)
            elif action == "6":
                """Prints list of all sports"""
                pass
            
            #Save & Exit
            elif action == "0":
                self.MemberList.save_all_files()
                # pass

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
                print("-"*106)
                print()
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
            PrintGraphicsUI.print_sel_error(self)


    def member_profile_selected(self, found_member):
        action = ""

        while action != 0:
            action = input("\n1. Edit member 2. Remove member 0. Exit\n")
            if action == "1":
                print("1. Name 2. Phone no 3. Email 4. Birthyear 5. Sport registration 0. Exit")
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

# m = MainMenuUI
# m.main()