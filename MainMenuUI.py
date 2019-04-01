import os
import time
from PrintGraphicsUI import PrintGraphicsUI
from Service import MemberList
from Service import SportList
from Service import Undo
from undo_ops import *

from Models import Sport
from Models import Member
# from Models import Group

class MainMenuUI:
    def __init__(self):
        self.MemberList = MemberList()
        self.SportList = SportList()

    def main(self):
        """Main menu"""

        action = ""
        # 
        # 
        # TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE #
        # Test subjects ################################################################################

        # self.SportList.test()
        # self.MemberList.test()
        # self.MemberList.load_all_files()
        # self.SportList.load_all_files()
        # self.SportList.group_test()

        # TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE ## TESTCASE #
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

            # self.GroupList.load_all_files()
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

            #1. Register new member
            if action == "1":
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

            #2. Register new sport
            elif action == "2":
                """Goes to service->Sport class and makes new Sport object
                checks if that Sport already exists"""
                self.SportList.new_sport()

            #3. Register new group
            elif action == "3":
                #first select sport
                print("You must first select a sport.")
                time.sleep(1.5)
                sport_list = self.print_all_sports()
                selected_sport = self.pick_a_sport(sport_list)
                self.SportList.new_group(selected_sport)

            #4. Register member into sport
            elif action == "4":
                self.print_all_members()

            #5. Find member - get data screen up
            elif action == "5":
                """Goes to service -> returns user by input name"""
                found_member = None
                search_term = input("Please write name, phone no(xxx-xxxx), email or birthyear(xxxx) of member: ")
                
                found_member = self.MemberList.search(search_term)
                if found_member != None:
                    PrintGraphicsUI.member_profile(found_member)
                    self.member_profile_selected(found_member)
                else: 
                    PrintGraphicsUI.print_not_found()

            #6. List all members - select member and see info, and all sport
            elif action == "6":
                """Prints list of all members"""
                self.print_all_members()

            #7. List all sports - select sport and see detailed info(list of users)
            elif action == "7":
                """Prints list of all sports"""
                # try:
                sport_list = self.print_all_sports()
                selected_sport = self.pick_a_sport(sport_list)
                # if selected_sport:
                self.sport_selected(selected_sport)
                # except (ValueError, TypeError, IndexError, AttributeError):
                #     PrintGraphicsUI.oops()
            
            #x. FOR UNDO
            elif action == "x":
                """Press x to undo latest actions for: [member, sport, group]"""
                self.undo_ops()
                self.save_all()

            #0. Save & Exit
            elif action == "0":
                self.save_all()

            else:
                PrintGraphicsUI.print_sel_error()

    #                                -----#### MAIN MENU ENDS #### -----------

    def undo_ops(self):
            undo = Undo.undo_stack
            if len(undo) <= 0:
                print("No more undo's available")
                return None
            op = undo.pop()
            # Conditionals for possible undo's
            # --- [ MEMBERS ] ---
            if op.op_type == OpType.ADD_MEMBER:
                print(f"Add member: {op.data}")
                self.MemberList.add_new_member(op.data)
            elif op.op_type == OpType.DELETE_MEMBER:
                print(f"Delete member: {op.data}")
                self.MemberList.member_delete(op.data)
            # # --- [ SPORTS ] ---
            if op.op_type == OpType.ADD_SPORT:
                print(f"Add sport: {op.data}")
                self.SportList.add_new_sport(op.data)
            elif op.op_type == OpType.DELETE_SPORT:
                print(f"Delete sport: {op.data}")
                self.SportList.remove_sport(op.data)
            # # --- [ GROUPS ] ---
            if op.op_type == OpType.ADD_GROUP:
                print(f"Add group: {op.data}")
                self.SportList.add_new_group(op.data, op.extra)
                self.save_all()
            elif op.op_type == OpType.DELETE_GROUP:
                print(f"Delete group: {op.data}")
                self.SportList.remove_group(op.data, op.extra)
                self.save_all()
            elif op.op_type == OpType.UPDATE_NAME:
                self.MemberList.change_member_back(op.data, op.extra)
            elif op.op_type == OpType.UPDATE_PHONE:
                self.MemberList.change_phone_back(op.data, op.extra)
            elif op.op_type == OpType.UPDATE_EMAIL:
                self.MemberList.change_email_back(op.data, op.extra)
            elif op.op_type == OpType.UPDATE_YEAR:
                self.MemberList.change_birthyear_back(op.data, op.extra)
            else:
                return None

    #                                ----#### PRINT FUNCTIONS #### ----------

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

            for idx, item in enumerate(all_members): 
                if idx in range(lower,upper):
                    print ("{:4s} {:}".format(str(idx+1).zfill(3), item))
            print()
            print("-"*106)

            action = input("\n{}\n{}\n{}\n{}\n{}\n".format(
                "1. Pick from list","2. Up list",
                "3. Down list","4. Print all members",
                "0. Exit"))
            
            if action == "1": #Choose to pick a member by nr
                self.pick_a_member(all_members)
                return

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

    def print_all_sports(self, all_sports = None):
        ##Mögulega gera bara einn prentunarfítus?
        if all_sports == None:
            all_sports = self.SportList.get_sports()
        
        # os.system('cls' if os.name == 'nt' else 'clear')
        if all_sports == []: 
            print("No sports have been registered!")
            return None
        else: 
            print("-"*106)
            print("{:>2}".format("Sports:"))
            print("-"*106)
            print()
        for idx, item in enumerate(all_sports): 
            print("{:4s} {:}".format(str(idx+1).zfill(1), item))
        print()
        print("-"*106)
        return all_sports

    def print_all_groups(self, all_groups, selected_sport):
        ##Mögulega gera bara einn prentunarfítus?
        # os.system('cls' if os.name == 'nt' else 'clear')
        if all_groups == []: 
            print("No groups available! Go into main menu and make new group.")
            return None
        else: 
            print("-"*106)
            print("{:>2}".format("Available groups:"))
            print("-"*106)
            print()
        for idx, item in enumerate(all_groups):
            group = selected_sport.sport_groups[item]
            print("{:4s} {} ({} to {})".format(str(idx+1).zfill(1), item, group.age_range[0], group.age_range[1]))
        print()
        print("-"*106)
        return all_groups

    def all_groups(self, selected_sport, selected_member = None):
        """Prints all groups within this sport available to this member (according to age)
        if no member, then return list of all group objects within this sport"""
        
        #Age check
        group_list = []
        if selected_member:
            age = selected_member.age
            for group in selected_sport.sport_groups:
                lo_age_range = selected_sport.sport_groups[group].age_range[0]
                up_age_range = selected_sport.sport_groups[group].age_range[1]
                if age >= lo_age_range and age <= up_age_range:
                    group_list.append(group)
        else:
            for group in selected_sport.sport_groups:
                group_list.append(selected_sport.sport_groups[group])
        return group_list


    #                                ----#### HELPER FUNCTIONS #### ----------


    def pick_a_member(self, member_list):
        # try:
        selection = input("Input member's number: ")
        if selection == "0":
            return
        else:
            selected_member = member_list[int(selection)-1]
            PrintGraphicsUI.member_profile(selected_member)
            self.member_profile_selected(selected_member)
        # except (ValueError, TypeError, IndexError, KeyError, AttributeError):
        #     PrintGraphicsUI.oops()

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
                # group_list = self.GroupList.get_groups()
                memb_id = found_member.unique_id

                while subaction != 0:
                    subaction = input("\n{}{}\n{}\n{}\n".format(
                        "Sport registration for ",
                        found_member.name,
                        "1. Register",
                        "2. Unregister"))
                    #Register member for sport
                    if subaction == "1":
                      
                        self.sport_registration(found_member)
                        print("Registration complete. Returning to main menu")
                        time.sleep(0.5)
                        return

                    #Unregister member from sport
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
                            
                            self.unregister_from_group(found_member, sport_to_unregister_from)
                            self.save_all()
                            return
                        except ValueError:
                            PrintGraphicsUI.print_sel_error()

            elif action == "3":
                self.group_registration(found_member)

            #9. Member DELETE
            elif action == "9":
                #member delete - unregister member from all sports and groups!
                self.unregister_from_sport(found_member)
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
    def unregister_from_group(self, selected_member, selected_sport):

        list_of_member_groups = selected_member.groups
        print("list of member's groups:", list_of_member_groups)
        list_of_all_groups_in_sport = selected_sport.sport_groups
        print("list of groups in this sport", list_of_all_groups_in_sport)

        #locates right group and removes it from user group list
        for group in list_of_member_groups:
            print(group)
            print(type(group))
            if group.name in list_of_all_groups_in_sport:
                print("Group FOUND!")
                selected_member.groups.remove(selected_sport.sport_groups[group.name])
                group.members.remove(selected_member)
                group.member_count -= 1


    def sport_registration(self, selected_member):
        """Lets user pick sport from list, select and register selected member in sport
        member -> sport -> group within sport
        member -> another group within sport
        sport -> member
        """

        sport_list = self.print_all_sports()
        selected_sport = self.pick_a_sport(sport_list)
        #must select group after sport
        print("You must select a group.")
        time.sleep(0.5)
        for sport in selected_member.sports:
            if selected_sport.name == sport.name:
                print("You are already registered for this sport!")
                print("You can register for another group from the main menu.")
                print("Returning to Main Menu")
                time.sleep(3.0)
            else:
                self.group_registration(selected_member, selected_sport)

                #apply changes to member & sport objects
                selected_member.sports.append(selected_sport)
                selected_sport.sport_members.append(selected_member)
            
                #save changes
                self.save_all()

    def group_registration(self, selected_member, selected_sport=None):
    #     """Lets user pick sport from list, select and register selected member in sport
    # todo: 
    #     !!! Finish Waiting list functionality"""
        if selected_sport == None:
            
            self.print_all_sports(selected_member.sports)
            print("Pick a sport")
            selected_sport = self.pick_a_sport(selected_member.sports)

        group_list = self.all_groups(selected_sport, selected_member)
        should_continue = self.print_all_groups(group_list, selected_sport)
        if should_continue:
            selected_group_name = self.pick_a_group(group_list)
            selected_group =  selected_sport.sport_groups[selected_group_name]

            #if group is full!
            if selected_group.size == selected_group.member_count:
                print("Group is full! You will be put on waiting list")
                print("You'll be returned to main menu.")
                selected_group.waiting_list.append(selected_member)
                time.sleep(1.0)
            else:
    #     #apply changes to member, group & sport objects
                selected_member.groups.append(selected_group)
                selected_group.members.append(selected_member)
                selected_group.member_count += 1

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
        subaction = input("{}\n{}\n{}\n".format(
            "1. Select Group",
            "2. Add new group to sport",
            "0. Exit"))
        if subaction == "1":
            group_list = self.all_groups(selected_sport)
            selected_group = self.pick_a_group(group_list)
            PrintGraphicsUI.group_info(selected_group)

            # # try:
            # sub_selection = int(input("Select group"))
            # selected_group = group_list[sub_selection]
            # bla = input("")

            # except (ValueError, TypeError, IndexError):
            # PrintGraphicsUI.oops()
            # return

        elif subaction == "2":
            self.SportList.new_group(selected_sport)
        else:
            print("Returning to Main Menu")
            time.sleep(0.5)
            return

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

    #                                ----#### SAVE FUNCTION #### ----------

    def save_all(self):
        self.MemberList.save_all_files()
        self.SportList.save_all_files()
        # self.GroupList.save_all_files()








    ################### Test case function #####################################################
    # 
    # Test case function # # Test case function # # Test case function # # Test case function
    # Connects objects made in the test functions in the service class together with object 
    # variables so they're interconnected.
    # 
    # 
    ################### Test case function #####################################################

    def test(self):
        # adding each sport to member's sport list
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

        #Adding each member to each sport's sportmembers list
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







        #Adding members to each group
        self.MemberList.id_map[1].groups.append(self.SportList.sport_map["Football"].sport_groups["Pro (Foo)"])
        self.MemberList.id_map[1].groups.append(self.SportList.sport_map["Volleyball"].sport_groups["Intermediate (Voll)"])
        self.MemberList.id_map[2].groups.append(self.SportList.sport_map["Football"].sport_groups["Pro (Foo)"])
        self.MemberList.id_map[3].groups.append(self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"])
        self.MemberList.id_map[4].groups.append(self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"])
        self.MemberList.id_map[5].groups.append(self.SportList.sport_map["Volleyball"].sport_groups["Intermediate (Voll)"])
        self.MemberList.id_map[6].groups.append(self.SportList.sport_map["Volleyball"].sport_groups["Beginners (Voll)"])
        self.MemberList.id_map[7].groups.append(self.SportList.sport_map["Football"].sport_groups["Beginners (Foo)"])
        self.MemberList.id_map[7].groups.append(self.SportList.sport_map["Volleyball"].sport_groups["Beginners (Voll)"])
        self.MemberList.id_map[7].groups.append(self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"])
        self.MemberList.id_map[8].groups.append(self.SportList.sport_map["Football"].sport_groups["Beginners (Foo)"])
        self.MemberList.id_map[9].groups.append(self.SportList.sport_map["Football"].sport_groups["Pro (Foo)"])
        self.MemberList.id_map[10].groups.append(self.SportList.sport_map["Football"].sport_groups["Intermediate (Foo)"])
        self.MemberList.id_map[10].groups.append(self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"])
        self.MemberList.id_map[11].groups.append(self.SportList.sport_map["Football"].sport_groups["Pro (Foo)"])
        self.MemberList.id_map[12].groups.append(self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"])
        self.MemberList.id_map[13].groups.append(self.SportList.sport_map["Swimming"].sport_groups["Beginners (Swi)"])




        self.SportList.sport_map["Football"].sport_groups["Pro (Foo)"].members.append(self.MemberList.id_map[1])
        self.SportList.sport_map["Volleyball"].sport_groups["Intermediate (Voll)"].members.append(self.MemberList.id_map[1])
        self.SportList.sport_map["Football"].sport_groups["Pro (Foo)"].members.append(self.MemberList.id_map[2])
        self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"].members.append(self.MemberList.id_map[3])
        self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"].members.append(self.MemberList.id_map[4])
        self.SportList.sport_map["Volleyball"].sport_groups["Intermediate (Voll)"].members.append(self.MemberList.id_map[5])
        self.SportList.sport_map["Volleyball"].sport_groups["Beginners (Voll)"].members.append(self.MemberList.id_map[6])
        self.SportList.sport_map["Football"].sport_groups["Beginners (Foo)"].members.append(self.MemberList.id_map[7])
        self.SportList.sport_map["Volleyball"].sport_groups["Beginners (Voll)"].members.append(self.MemberList.id_map[7])
        self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"].members.append(self.MemberList.id_map[7])
        self.SportList.sport_map["Football"].sport_groups["Beginners (Foo)"].members.append(self.MemberList.id_map[8])
        self.SportList.sport_map["Football"].sport_groups["Pro (Foo)"].members.append(self.MemberList.id_map[9])
        self.SportList.sport_map["Football"].sport_groups["Intermediate (Foo)"].members.append(self.MemberList.id_map[10])
        self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"].members.append(self.MemberList.id_map[10])
        self.SportList.sport_map["Football"].sport_groups["Pro (Foo)"].members.append(self.MemberList.id_map[11])
        self.SportList.sport_map["Chess"].sport_groups["Everybody (Che)"].members.append(self.MemberList.id_map[12])
        self.SportList.sport_map["Swimming"].sport_groups["Beginners (Swi)"].members.append(self.MemberList.id_map[13])

        
        # print("sdfsd")
        # print(self.MemberList.id_map[1].groups)
        # print(self.SportList.sport_map["Football"].sport_groups["Pro"].members)
        # time.sleep(1.0)
        # pass

