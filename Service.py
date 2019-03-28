import time
import datetime
import os
from Repo import MemberRepo
from Repo import SportsRepo
from PrintGraphicsUI import PrintGraphicsUI
from sortedcontainers import SortedDict

class Member:
    """Makes the member object"""
    def __init__(
        self, 
        name, 
        phone, 
        email, 
        birthyear, 
        sports = None,
        groups = None,
        unique_id = None 
        ):

        self.name = name
        self.phone = phone
        self.email = email
        self.birthyear = birthyear
        self.sports = sports
        self.groups = groups
        self.unique_id = unique_id
    
    def __str__(self):
        try:
            sport_string = PrintGraphicsUI.make_string(self.sports)
        except TypeError:
            sport_string = ""
            
        age = (datetime.date.today().year) - self.birthyear
        
        return "{:<26s} Age: {} Ph. No: {:12s} Email: {:<12s} Sports: {:>4}".format(
            self.name,
            age,
            self.phone,
            self.email,
            sport_string)

class MemberList:

    def __init__(self):
        self.id_map = SortedDict()
        self.name_map = SortedDict()
        self.phone_map = dict()
        self.email_map = SortedDict()

        self.unique_id = int(MemberRepo.load_un_id())

    def test(self):
        self.add_new_member(Member("Karl Bernharðsson", "898-8787", "1@sport.is", 1989, ["Football", "Volleyball"]))
        self.add_new_member(Member("Sigurður Sigurðsson", "844-8484", "2@sport.is", 1994, ["Football"]))
        self.add_new_member(Member("Magnús Friðriksson", "898-4111", "3@sport.is", 1993, ["Football"]))
        self.add_new_member(Member("Elísabet Skaargard", "778-1155", "4@sport.is", 1992, ["Volleyball"]))
        self.add_new_member(Member("Knútur Olsen", "877-1588", "5@sport.is", 1993))
        self.add_new_member(Member("Sigrún Tinnudóttir", "677-8877", "6@sport.is", 1992, ["Football", "Volleyball"]))
        self.add_new_member(Member("Jón Karlsson", "661-8488", "7@sport.is", 1993, ["Volleyball"]))
        self.add_new_member(Member("Geir Sigurður Magnússon", "771-2121", "8@sport.is", 1995, ["Chess"]))
        self.add_new_member(Member("Bertrand Filibusarson", "771-2121", "8@sport.is", 1995, ["Chess"]))
        self.add_new_member(Member("Not0", "771-2121", "8@sport.is", 1998))
        self.add_new_member(Member("Not1", "771-2121", "8@sport.is", 1994))
        self.add_new_member(Member("Not2", "771-2121", "8@sport.is", 1992, ["Chess"]))
        self.add_new_member(Member("Not3", "771-2121", "8@sport.is", 1997, ["Chess"]))


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

        new_member = Member(member_name, member_phone, member_email, member_birthyear,None, None, self.unique_id)
        self.add_new_member(new_member)


    def add_new_member(self, new_member):
        self.id_map[self.unique_id] = new_member
        self.name_map[new_member.name] = self.unique_id
        self.phone_map[new_member.phone] = self.unique_id
        self.email_map[new_member.email] = self.unique_id


        print("{} added to system. You will be redirected to main menu.".format(new_member.name))
        self.unique_id += 1
        MemberRepo.save(self.id_map, self.name_map, self.phone_map, self.email_map)
        MemberRepo.save_un_id(self.unique_id)
        time.sleep(0.1)


    

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

    
    def member_delete(self, selected_member):
        id = self.name_map[selected_member.name]
        del self.name_map[selected_member.name]
        del self.phone_map[selected_member.phone]
        del self.email_map[selected_member.email]
        del self.id_map[id]

        self.save_all_files()


    def save_all_files(self):
        #Temporary save solution - find way to put all in one dict? 
        MemberRepo.save(self.id_map, self.name_map, self.phone_map, self.email_map)

    def load_all_files(self):
        try:
            self.id_map, self.name_map, self.phone_map, self.email_map = MemberRepo.load()
            print(self.id_map)
            print(self.name_map)

        except TypeError:
            print("TypeError")
    
    def get_members_ordered_by_name(self):
        ordered_list = []
        for name in self.name_map:
            ordered_list.append(self.id_map[self.name_map[name]])
        return ordered_list

    


class Sport:
    """Makes the Sport object"""
    def __init__(
        self, 
        sport_name, 
        sport_members = None
        ):

        self.sport_name = sport_name
        self.sport_members = sport_members
    

    def __str__(self):
        return "{} ({})".format(self.sport_name, len(self.sport_members))


class SportList:
    def __init__(self):
        self.sport_map = SortedDict()

    def new_sport(self):
        sport_name = input("Input sport Name (Football): ")
        new_sport = Sport(sport_name)
        self.add_new_sport(new_sport)

    def add_new_sport(self, new_sport):
        self.sport_map[new_sport.sport_name] = new_sport.sport_members
        print("{} added to system. You will be redirected to main menu.".format(new_sport.sport_name))
        SportsRepo.save(self.sport_map)

    def test(self):
        self.add_new_sport(Sport("Football"))
        self.add_new_sport(Sport("Volleyball"))
        self.add_new_sport(Sport("Chess"))

    def save_all_files(self):
        #Temporary save solution - find way to put all in one dict? 
        SportsRepo.save(self.sport_map)

    def load_all_files(self):
        try:
            self.sport_map = SportsRepo.load()
            # print(self.sport_map)
           
        except TypeError:
            print("TypeError")




