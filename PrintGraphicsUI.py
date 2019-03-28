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
        group_string = PrintGraphicsUI.make_string(found_member.groups)
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
            "\tGroups:     -------------------------   ", group_string,

            ))

    def print_not_found():
        print("Unfortunately we could not find anyone by that search term.")
        time.sleep(1.5)

    def sport_information(selected_sport):
        print(selected_sport)
    
    def group_info(selected_group):
        print(selected_group)