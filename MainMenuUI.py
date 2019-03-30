import os
import time
from PrintGraphicsUI import PrintGraphicsUI
from Service import MemberList
from Service import SportList
from Service import GroupList
# from Registration import Registration

from Models import Sport
from Models import Member
from Models import Group

class MainMenuUI:
    def __init__(self):
        self.MemberList = MemberList()
        self.SportList = SportList()
        self.GroupList = GroupList()
        # self.Registration = Registration()

    def main(self):
        """Main menu"""

        action = ""
        #
        # 
        # 
        # 
        # TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE #
        # Test subjects ################################################################################

        # self.SportList.test()
        # self.MemberList.test()
        # self.GroupList.test()
        # TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE #
        #
        #
        #
        #
        #
    #                                -----#### MAIN MENU STARTS #### -----------

        while action != "0":
            # os.system('cls' if os.name == 'nt' else 'clear')

            print("Loading savefiles....")
            #Use Pickle to load saved data. If No savefile found -> print error. 
            self.MemberList.load_all_files()
            self.SportList.load_all_files()
            self.GroupList.load_all_files()
            time.sleep(0.5)
            #
            #  
            # 
            # TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE #
            # Register tests for test subjects #############################################################
            # self.test()
            # Register tests for test subjects #############################################################
            # TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE #
            #
            #
            #
            PrintGraphicsUI.print_intro()
            action = input("What would you like to do?\n")
            #1. Register new sport
            if action == "1":
                """Goes to service->Sport class and makes new Sport object
                checks if that Sport already exists"""
                self.SportList.new_sport()

            #2. Register new member
            elif action == "2":
                """Goes to service->Member class, makes new Member object
                Gives each member a unique ID no for easy listing
                Goes to Registraion and registers member in sport + group"""
                new_member = self.MemberList.new_member()

                subaction = input("Would you like to register for a sport now?\n1. Yes 2. No, later ")
                print()
                if subaction == "1":
                    self.sport_registration(new_member)
                else:
                    pass

            #3. Register new group
            elif action == "3":
                self.GroupList.create_new_group()
            
            #4. Register member into sport
            elif action == "4":
                """Register member in sport
                1. First pick a member from list
                2. send selected member to sport registration
                """
                self.sport_registration()
            
            #5. Register member into group
            elif action == "5":
                self.group_registration()

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

            #8. List all sports - select sport and see detailed info(list of users)
            elif action == "8":
                """Prints list of all sports"""
                try:
                    sport_list = self.print_all_sports()
                    selected_sport = self.pick_a_sport(sport_list)
                    # if selected_sport:
                    self.sport_selected(selected_sport)
                except (ValueError, TypeError, IndexError, AttributeError):
                    PrintGraphicsUI.oops()

            #9. List all groups
            elif action == "9":
                """Lists all groups"""
                group_list = self.print_all_groups()
                selected_group = self.pick_a_group(group_list)
                self.group_selected(selected_group)

            #0. Save & Exit
            elif action == "0":
                self.save_all()

            else:
                PrintGraphicsUI.print_sel_error()
    

    #                                -----#### MAIN MENU ENDS #### -----------
    


    #                                ----#### MEMBER FUNCTIONS #### ----------

    def print_all_members(self):
        
        all_members = self.MemberList.get_members_ordered_by_name()
        lower = 0; upper = 8; action = ""; highest = len(all_members); action = ""
        
        while action != 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            if all_members == []: print("No members have been registered!")
            else: 
                print("-"*106)
                print("{:>2}".format("Members:"))
                print("-"*106)
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
                return
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
            action = input("\n1. Edit member\n2. Sport registration\n3. Group registration\n9. Remove member from system\n0. Exit\n")
            
            #1. Member Edit
            if action == "1":
                print("{}\n{}\n{}\n{}\n{}\n".format(
                "1. Name",
                "2. Phone no",
                "3. Email",
                "4. Birthyear",
                "0. Exit"))
                print("What would you like to edit?")

                new_info = self.MemberList.member_edit(found_member)
                if new_info != None:
                    print("Info has been changed to {}".format(new_info))
                print("Returning to main menu")
                self.MemberList.save_all_files()
                time.sleep(1)
                return
            
            #2. Member registration: Sport
            elif action == "2": 
                subaction = ""
                sport_list = self.SportList.get_sports()
                group_list = self.GroupList.get_groups()
                memb_id = found_member.unique_id

                while subaction != 0:
                    subaction = input("\n{}\n{}\n".format(
                        "1.Register",
                        "2.Unregister"))
                    if subaction == "1":
                        # for idx, item in enumerate(sport_list):
                        #     print(idx+1, item.name)
                        # sport_selected = int(input("Which sport would you like to register for? "))
                        # sport_to_register_for = sport_list[sport_selected-1]

                        # self.MemberList.id_map[memb_id].sports.append(self.SportList.sport_map[sport_selected.name])
                        # self.SportList.sport_map[sport_selected.name].sport_members.append(self.MemberList.id_map[memb_id])
                        # #must register for group also
                        # self.group_registration()
                        self.sport_registration(found_member)
                        print("Registration complete. Returning to main menu")
                        time.sleep(0.5)
                        return

                    elif subaction == "2":
                        print("Registered sports:\n")
                        for idx, item in enumerate(found_member.sports):
                            print(idx+1, item.name)
                        try:
                            sport_selected = int(input("Which sport would you like to unregister? "))
                            sport_to_unregister_from = found_member.sports[sport_selected-1]
                            self.unregister_from_sport(found_member, sport_to_unregister_from)
                            print("Member has been unregistered. Returning to Main menu.")
                            found_member.sports.remove(sport_to_unregister_from)
                            self.save_all()
                            return

                        except ValueError:
                            PrintGraphicsUI.print_sel_error()

            #2. Member registration: Group
            elif action == "3":
                subaction = ""
                while subaction != 0:
                    subaction = input("\n{}\n{}\n".format(
                        "1.Register",
                        "2.Unregister"))
                    if subaction == "1":
                        self.group_registration(found_member)

                    elif subaction == "2":
                        print("Registered groups:\n")
                        for idx, item in enumerate(found_member.groups):
                            print(idx+1, item.name)
                        try:
                            group_selected = int(input("Which group would you like to unregister? "))
                            group_to_unregister_from = found_member.groups[group_selected-1]
                            self.unregister_from_group(found_member, group_to_unregister_from)
                            found_member.groups.remove(group_to_unregister_from)

                            print("Member has been unregistered. Returning to Main menu.")
                            self.save_all()
                            return

                        except ValueError:
                            PrintGraphicsUI.print_sel_error()

            #9. Member DELETE
            elif action == "9":
                #member delete - unregister member from all sports and groups!
                self.unregister_from_sport(found_member)
                self.unregister_from_group(found_member)

                #delete member from savefiles
                self.MemberList.member_delete(found_member)

                print("Member has been deleted. Returning to Main menu.")         
                self.save_all()
                time.sleep(1)
                return
            
            elif action == "0":
                return
            else:
                PrintGraphicsUI.print_sel_error()
                PrintGraphicsUI.member_profile(found_member)

    # ---  Registration functions --- 

    def sport_registration(self, selected_member):
        """Lets user pick sport from list, select and register selected member in sport
        group -> sport
        member -> sport
        sport -> group
        member -> group
        group -> member
        sport -> member"""

        sport_list = self.print_all_sports()
        selected_sport = self.pick_a_sport(sport_list)
        #must select group after sport
        print("You must select a group.")
        self.group_registration(selected_member, selected_sport)

        #apply changes to member & sport objects
        selected_member.sports.append(selected_sport)
        selected_sport.sport_members.append(selected_member)
        
        #save changes
        self.save_all()

    def group_registration(self, selected_member, selected_sport):
        """Lets user pick sport from list, select and register selected member in sport
        !!! Age Check 
        !!! Full group check
        !!! Waiting list functionality?"""

        group_list = self.print_all_groups()
        selected_group = self.pick_a_group(group_list)

        #apply changes to member, group & sport objects
        selected_member.groups.append(selected_group)
        selected_sport.sport_groups.append(selected_group)
        selected_group.group_members.append(selected_member)
        #save changes
        self.save_all()

    def unregister_from_sport(self, found_member, selected_sport = None):
        #First we find the lists of groups and sports this member is a part of
        
        #Then we need to go to each member list of each sport this member was a part of
        #find the corresponding member object in each list
        #and delete the member from every one

        #MAYBE  problem - list of sport.sport_members does not include 
        #object references to the member object found above - 
        #possibly keeping member objects in two places
        #not sure if its ok - or its because each sport object
        #has its own copy of members object in list of members
        #thus multiplying all objects extravagantly.
        #Check later!
        member_sports = found_member.sports
        if selected_sport == None:
            for sport in member_sports:
                sport_member_list = self.SportList.sport_map[sport.name].sport_members
                for item in sport_member_list:
                    if item.name == found_member.name:
                        sport_member_list.remove(item)
        else:
            sport_member_list = self.SportList.sport_map[selected_sport.name].sport_members
            for item in sport_member_list:
                if item.name == found_member.name:
                    sport_member_list.remove(item)


        #oldcode##
        # sport_member_list = self.SportList.sport_map[sport.name].sport_members
        # self.SportList.sport_map[sport.name].sport_members.remove(found_member)
        # for group in member_groups:
        # group.group_members.remove(found_member)
        #oldcode##

    def unregister_from_group(self, found_member):
        #same as above
        member_groups = found_member.groups
        for group in member_groups:
            group_member_list = self.GroupList.group_map[group.name].group_members
            for item in group_member_list:
                if item.name == found_member.name:
                    group_member_list.remove(item)



    # ---  SPORT functions --- 


    def print_all_sports(self):
        ##Mögulega gera bara einn prentunarfítus?
        all_sports = self.SportList.get_sports()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        if all_sports == []: 
            print("No sports have been registered!")
            return None
        else: 
            print("-"*106)
            print("{:>2}".format("Sports:"))
            print("-"*106)
            print()
        for index, item in enumerate(all_sports): 
            print("{:4s} {:}".format(str(index+1).zfill(1), item))
        print()
        print("-"*106)
        return all_sports
            
    def pick_a_sport(self, sport_list):
        """Lets you select a sport from the list above. Returns: selected sport object"""
        try:
            selection = input("Input sport number: ")
            if selection == "0":
                pass
            else:
                selected_sport = sport_list[int(selection)-1]
                return selected_sport

        except (ValueError, TypeError, IndexError):
            PrintGraphicsUI.print_sel_error()
    
    def sport_selected(self, selected_sport):
        PrintGraphicsUI.sport_information(selected_sport)
        print(selected_sport.sport_members)
        print(selected_sport.sport_groups)
        getout = input("Press any key to return to Main menu")


    # ---  GROUP functions --- 


    def print_all_groups(self):
        ##Mögulega gera bara einn prentunarfítus?
        
        all_groups = self.GroupList.get_groups()
        action = ""

        while action != 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            if all_groups == []: print("No groups have been registered!")
            else: 
                print("-"*106)
                print("{:>2}".format("Sports:"))
                print("-"*106)
                print()
                print("{:>10} {:>25s} {:>20s}{:>12s}".format("Name:", "Size:", "Age range:", "Sport:"))

                print("-"*106)
                print()
            for index, item in enumerate(all_groups): 
                print("{:4s} {:}".format(str(index+1).zfill(2), item))
            print()
            print("-"*106)

            action = input("\n{}\n{}\n".format(
                "1. Pick from list",
                "0. Exit"))
            
            if action == "1": #Choose to pick a sport by nr
                return all_groups

            elif action == "0": #Exit
                return
            else: 
                PrintGraphicsUI.print_sel_error()

    def pick_a_group(self, group_list):
        """Lets you select a group from the list above. Returns: selected group object"""
        try:
            selection = input("Input group number: ")
            if selection == "0":
                return
            else:
                selected_group = group_list[int(selection)-1]
                return selected_group
        except (ValueError, TypeError, IndexError):
            PrintGraphicsUI.print_sel_error()

        
    def group_selected(self, selected_group):
        PrintGraphicsUI.group_info(selected_group)
        print(selected_group.group_members)
        getout = input("Press any key to return to Main menu")



    #Save function

    def save_all(self):
        self.MemberList.save_all_files()
        self.SportList.save_all_files()
        self.GroupList.save_all_files()








    ################### Test case function #####################################################
    # 
    # Test case function # # Test case function # # Test case function # # Test case function
    # Connects objects made in the test functions in the service class together with object 
    # variables so they're interconnected.
    # 
    # 
    ################### Test case function #####################################################

    def test(self):
        self.MemberList.id_map[1].sports.append(self.SportList.sport_map["Football"])
        self.MemberList.id_map[1].sports.append(self.SportList.sport_map["Volleyball"])
        self.MemberList.id_map[2].sports.append(self.SportList.sport_map["Football"])
        self.MemberList.id_map[3].sports.append(self.SportList.sport_map["Chess"])
        self.MemberList.id_map[4].sports.append(self.SportList.sport_map["Chess"])
        self.MemberList.id_map[5].sports.append(self.SportList.sport_map["Volleyball"])
        self.MemberList.id_map[6].sports.append(self.SportList.sport_map["Volleyball"])
        self.MemberList.id_map[7].sports.append(self.SportList.sport_map["Volleyball"])
        self.MemberList.id_map[7].sports.append(self.SportList.sport_map["Football"])
        self.MemberList.id_map[7].sports.append(self.SportList.sport_map["Chess"])
        self.MemberList.id_map[8].sports.append(self.SportList.sport_map["Football"])
        self.MemberList.id_map[9].sports.append(self.SportList.sport_map["Football"])
        self.MemberList.id_map[10].sports.append(self.SportList.sport_map["Football"])
        self.MemberList.id_map[10].sports.append(self.SportList.sport_map["Chess"])
        self.MemberList.id_map[11].sports.append(self.SportList.sport_map["Football"])
        self.MemberList.id_map[12].sports.append(self.SportList.sport_map["Chess"])
        self.MemberList.id_map[13].sports.append(self.SportList.sport_map["Volleyball"])

        self.GroupList.group_map["Fjölnir"].group_sport = self.SportList.sport_map["Football"]
        self.GroupList.group_map["Ármann"].group_sport = self.SportList.sport_map["Chess"]
        self.GroupList.group_map["Breiðablik"].group_sport = self.SportList.sport_map["Volleyball"]
        self.GroupList.group_map["Fylkir"].group_sport = self.SportList.sport_map["Volleyball"]
        self.GroupList.group_map["Fylkir"].group_sport = self.SportList.sport_map["Chess"]
        self.GroupList.group_map["Fylkir"].group_sport = self.SportList.sport_map["Football"]

        self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[1])
        self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[2])
        self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[7])
        self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[8])
        self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[9])
        self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[10])
        self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[11])
        self.SportList.sport_map["Football"].sport_members.append(self.MemberList.id_map[11])
        self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[3])
        self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[4])
        self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[7])
        self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[10])
        self.SportList.sport_map["Chess"].sport_members.append(self.MemberList.id_map[12])
        self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[2])
        self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[5])
        self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[6])
        self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[7])
        self.SportList.sport_map["Volleyball"].sport_members.append(self.MemberList.id_map[13])
        self.SportList.sport_map["Swimming"].sport_members.append(self.MemberList.id_map[10])
        self.SportList.sport_map["Swimming"].sport_members.append(self.MemberList.id_map[6])


        self.SportList.sport_map["Football"].sport_groups.append(self.GroupList.group_map["Fjölnir"])
        self.SportList.sport_map["Chess"].sport_groups.append(self.GroupList.group_map["Ármann"])
        self.SportList.sport_map["Volleyball"].sport_groups.append(self.GroupList.group_map["Breiðablik"])
        self.SportList.sport_map["Volleyball"].sport_groups.append(self.GroupList.group_map["Fylkir"])
        self.SportList.sport_map["Chess"].sport_groups.append(self.GroupList.group_map["Fylkir"])
        self.SportList.sport_map["Football"].sport_groups.append(self.GroupList.group_map["Fylkir"])
        self.SportList.sport_map["Swimming"].sport_groups.append(self.GroupList.group_map["Fylkir"])

        self.MemberList.id_map[1].groups.append(self.GroupList.group_map["Fjölnir"])
        self.MemberList.id_map[1].groups.append(self.GroupList.group_map["Breiðablik"])
        self.MemberList.id_map[2].groups.append(self.GroupList.group_map["Fjölnir"])
        self.MemberList.id_map[3].groups.append(self.GroupList.group_map["Ármann"])
        self.MemberList.id_map[4].groups.append(self.GroupList.group_map["Ármann"])
        self.MemberList.id_map[5].groups.append(self.GroupList.group_map["Breiðablik"])
        self.MemberList.id_map[6].groups.append(self.GroupList.group_map["Fylkir"])
        self.MemberList.id_map[7].groups.append(self.GroupList.group_map["Breiðablik"])
        self.MemberList.id_map[7].groups.append(self.GroupList.group_map["Fjölnir"])
        self.MemberList.id_map[7].groups.append(self.GroupList.group_map["Ármann"])
        self.MemberList.id_map[8].groups.append(self.GroupList.group_map["Fjölnir"])
        self.MemberList.id_map[9].groups.append(self.GroupList.group_map["Fjölnir"])
        self.MemberList.id_map[10].groups.append(self.GroupList.group_map["Fylkir"])
        self.MemberList.id_map[10].groups.append(self.GroupList.group_map["Ármann"])
        self.MemberList.id_map[11].groups.append(self.GroupList.group_map["Fjölnir"])
        self.MemberList.id_map[12].groups.append(self.GroupList.group_map["Ármann"])
        self.MemberList.id_map[13].groups.append(self.GroupList.group_map["Breiðablik"])

        self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[1])
        self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[3])
        self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[7])
        self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[8])
        self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[9])
        self.GroupList.group_map["Fylkir"].group_members.append(self.MemberList.id_map[10])
        self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[11])
        self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[2])
        self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[5])
        self.GroupList.group_map["Fylkir"].group_members.append(self.MemberList.id_map[6])
        self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[7])
        self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[13])
        self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[3])
        self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[4])
        self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[7])
        self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[10])
        self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[12])
        # pass

