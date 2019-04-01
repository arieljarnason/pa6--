import time

class PrintGraphicsUI:
    """Often used print messages can be used from here"""

    def print_intro():
        with open("texts/intro.txt", encoding = "utf-8") as logo:
            print(logo.read()); logo.seek(0)

    def print_sel_error():
        print("Error, please select from list")
        print()
        time.sleep(1.5)

    def make_string(list_of_things):
        mystring = ""
        try:
            for item in list_of_things:
                mystring += "{} ".format(item)
            return mystring
        except TypeError:
            return mystring

    def member_profile(found_member):
        sport_string = PrintGraphicsUI.make_string(found_member.sports)
        print( """
{}{}
{}{}
{}{}
{}{} ({})
{}{}
{}{}
""".format(
            "\tName:       -------------------------   ", found_member.name, 
            "\tPhone No:   -------------------------   ", found_member.phone,
            "\tEmail:      -------------------------   ", found_member.email,
            "\tBirthyear:  -------------------------   ", found_member.birthyear, 2019-found_member.birthyear,
            "\tSports:     -------------------------   ", sport_string,
            "\tGroups:     -------------------------   ", found_member.groups,

            ))

    def print_not_found():
        print("Unfortunately we could not find anyone by that search term.")
        time.sleep(1.5)

    def sport_information(selected_sport):
        # member_string = PrintGraphicsUI.make_string(selected_sport.sport_members)
        # group_string = PrintGraphicsUI.make_string(selected_sport.sport_groups)
        group_list = []
        for group in selected_sport.sport_groups:
            group_list.append(selected_sport.sport_groups[group])

        print("Sport: {}".format(selected_sport.name))
        print("\nGroups:")
        for idx, i in enumerate(group_list):
            print("{}. {}".format(idx+1, i))
        print("\nAll Sport Members:\n")
        # for idx, member in enumerate(selected_sport.sport_members):
        #     print(idx, member.name)
        print(selected_sport.sport_members)
        print()

    def group_info(selected_group):
        print()
        for idx, member in enumerate(selected_group.members):
            print(idx+1, member.name)
        
        get_out = input("\nEnter any key to exit")
        
            

# {}{}
# {}
# {}{}
# {}
# {}{}
# """.format(
#             "\tSport:       -------------------------   ", selected_sport.name, 
#             "\tGroups:",
#             "\t",group_list,
#             "\tMembers:",
#             "\t", selected_sport.sport_members

#             ))
    
    def oops():
        print("Oops! Something went wrong. Please try again.")
        time.sleep(1.5)