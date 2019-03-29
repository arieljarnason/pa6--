import os
import time
from PrintGraphicsUI import PrintGraphicsUI
from MainMenuUI import MemberList
from Service import SportList
from Service import GroupList
from Models import Sport
from Models import Member
from Models import Group


class Registration:
    """
    This class registers members into groups & sports, sports in groups, groups in sports
    group -> sport
    member -> sport
    sport -> group
    member -> group
    group -> member
    sport -> member"""

    def __init__(self):
        pass
    
    def register_member_in_sport(self, chosen_member, chosen_sport):
        """When members are registered in a --sport-- they must choose a --group--
        1. List of available sports
        2. pick sport
        3. list of available groups (age& sport requirements)
        4. finalize registration
        """
        # id = chosen_member.unique_id
        # MemberList.id_map[id].sports.append(self.SportList.sport_map["Football"])
        # chosen_member.sports.append(chosen_sport)
        # MemberList.id_map[chosen_member.unique_id] = chosen_member
        print("Worked!")
        time.sleep(1.0)
        
    
    def register_member_in_group(self, chosen_member, chosen_group):
        """Members must be in 1> --group-- when registered in --sport--.
        Can be registered in many --groups--"""
        pass
    




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
        # self.GroupList.group_map["Fylkir"].group_sport = self.SportList.sport_map["Volleyball"]
        # self.GroupList.group_map["Fylkir"].group_sport = self.SportList.sport_map["Chess"]
        # self.GroupList.group_map["Fylkir"].group_sport = self.SportList.sport_map["Football"]

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
        # self.SportList.sport_map["Swimming"].sport_members.append(self.MemberList.id_map[10])
        # self.SportList.sport_map["Swimming"].sport_members.append(self.MemberList.id_map[6])


        # self.SportList.sport_map["Football"].sport_groups.append(self.GroupList.group_map["Fjölnir"])
        # self.SportList.sport_map["Chess"].sport_groups.append(self.GroupList.group_map["Ármann"])
        # self.SportList.sport_map["Volleyball"].sport_groups.append(self.GroupList.group_map["Breiðablik"])
        # self.SportList.sport_map["Volleyball"].sport_groups.append(self.GroupList.group_map["Fylkir"])
        # self.SportList.sport_map["Chess"].sport_groups.append(self.GroupList.group_map["Fylkir"])
        # self.SportList.sport_map["Football"].sport_groups.append(self.GroupList.group_map["Fylkir"])
        # self.SportList.sport_map["Swimming"].sport_groups.append(self.GroupList.group_map["Fylkir"])



        # self.MemberList.id_map[1].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[1].groups.append(self.GroupList.group_map["Breiðablik"])
        # self.MemberList.id_map[2].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[3].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[4].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[5].groups.append(self.GroupList.group_map["Breiðablik"])
        # self.MemberList.id_map[6].groups.append(self.GroupList.group_map["Fylkir"])
        # self.MemberList.id_map[7].groups.append(self.GroupList.group_map["Breiðablik"])
        # self.MemberList.id_map[7].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[7].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[8].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[9].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[10].groups.append(self.GroupList.group_map["Fylkir"])
        # self.MemberList.id_map[10].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[11].groups.append(self.GroupList.group_map["Fjölnir"])
        # self.MemberList.id_map[12].groups.append(self.GroupList.group_map["Ármann"])
        # self.MemberList.id_map[13].groups.append(self.GroupList.group_map["Breiðablik"])

        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[1])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[3])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[7])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[8])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[9])
        # self.GroupList.group_map["Fylkir"].group_members.append(self.MemberList.id_map[10])
        # self.GroupList.group_map["Fjölnir"].group_members.append(self.MemberList.id_map[11])
        # self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[2])
        # self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[5])
        # self.GroupList.group_map["Fylkir"].group_members.append(self.MemberList.id_map[6])
        # self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[7])
        # self.GroupList.group_map["Breiðablik"].group_members.append(self.MemberList.id_map[13])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[3])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[4])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[7])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[10])
        # self.GroupList.group_map["Ármann"].group_members.append(self.MemberList.id_map[12])