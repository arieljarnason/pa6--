import pickle

class MemberRepo:
    """Gets and updates file for info on members.

    """
    def __init__(self):
        self.default_save_file = "SportStudSave01.p"

    def save(id_map, name_map, phone_map, email_map):
        pickle.dump(id_map, open("saves/id_map.p", "wb"))
        pickle.dump(name_map, open("saves/name_map.p", "wb"))
        pickle.dump(phone_map, open("saves/phone_map.p", "wb"))
        pickle.dump(email_map, open("saves/email_map.p", "wb"))

    def load():
        try: 
            id_map = pickle.load(open("saves/id_map.p", "rb"))
            name_map = pickle.load(open("saves/name_map.p", "rb"))
            phone_map = pickle.load(open("saves/phone_map.p", "rb"))
            email_map = pickle.load(open("saves/email_map.p", "rb"))
            #nota close eða with
            return id_map, name_map, phone_map, email_map
        except FileNotFoundError or TypeError:
            print('Unfortunately we could not find your save file. No data was loaded.')

    def save_un_id(unique_id):
        pickle.dump(unique_id, open("saves/unique_id.p", "wb"))

    def load_un_id():
        try:
            unique_id = pickle.load(open("saves/unique_id.p", "rb"))
            return int(unique_id)
        except FileNotFoundError:
            print("Unfortunately we could not find your save file. Not all data was loaded.")
            return 1


class SportsRepo:
    """Gets and updates file for info on sports"""

    def save(sp_map):
        pickle.dump(sp_map, open("saves/sp_map.p", "wb"))

    def load():
        try: 
            sp_map = pickle.load(open("saves/sp_map.p", "rb"))
            return sp_map
            #nota close eða with
        except FileNotFoundError or TypeError:
            print('Unfortunately we could not find your save file. No data was loaded.')


