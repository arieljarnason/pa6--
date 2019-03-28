import datetime
import time 
import os
from PrintGraphicsUI import PrintGraphicsUI

class Member:
    """Makes the Member object"""
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
        
        return "{:<26s} {:12s} {:12s}{:<12s}{:6s}{:>4}".format(
            self.name,
            str(age),
            self.phone,
            self.email,
            str(self.unique_id),
            sport_string)

    def __repr__(self):
        return self.name

class Sport:
    """Makes the Sport object"""
    def __init__(
        self, 
        sport_name, 
        sport_members = None,
        sport_groups = None
        ):

        self.sport_name = sport_name
        self.sport_members = sport_members
        self.sport_groups = sport_groups
    

    def __str__(self):
        # return "{} ({}) -- Groups: {}".format(self.sport_name, len(self.sport_members), self.sport_groups)
        return self.sport_name

    # def __repr__(self):
    #     return self.sport_name

class Group:
    """Makes Group objects"""
    def __init__(
        self,
        group_name,
        group_size,
        group_age_range,
        group_sport = None,
        group_members = None,
        group_waiting_list = None):

            self.group_name = group_name
            self.group_size = group_size
            self.group_age_range = group_age_range
            self.group_sport = group_sport
            self.group_members = group_members
            self.group_waiting_list = group_waiting_list

    def __str__(self):
        # return "{}........................{}..........{}...........{}".format(
        #     self.group_name,
        #     self.group_size,
        #     self.group_age_range,
        #     self.group_sport)
        return self.group_name
        
    def __repr__(self):
        return self.group_name
