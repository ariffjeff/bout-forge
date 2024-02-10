from enum import Enum


class WeaponType(Enum):
    FOIL = "Foil"
    EPEE = "Epee"
    SABRE = "Sabre"


class Weapon:
    def __init__(self, weapon_type):
        if not isinstance(weapon_type, WeaponType):
            raise ValueError("Invalid weapon type.")
        
        self.weapon_type = weapon_type


class Foil(Weapon):
    def __init__(self):
        super().__init__(WeaponType.FOIL)


class Epee(Weapon):
    def __init__(self):
        super().__init__(WeaponType.EPEE)


class Sabre(Weapon):
    def __init__(self):
        super().__init__(WeaponType.SABRE)


class Fencer:
    _id_counter = 0  # Class variable to generate unique IDs

    def __init__(self, first_name, last_name=None, weapons=None):
        self.id = Fencer._id_counter  # Assign unique ID
        Fencer._id_counter += 1  # Increment ID counter

        self.first_name = first_name
        self.last_name = last_name

        self.weapons = {
            WeaponType.FOIL: False,
            WeaponType.EPEE: False,
            WeaponType.SABRE: False
        }

        # if not isinstance(weapons, list):
        #     weapons = [weapons]
        # self.weapons = weapons

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def remove_weapon(self, weapon):
        if weapon in self.weapons:
            self.weapons.remove(weapon)
        else:
            print(f"{self.first_name, self.last_name} does not have {weapon}.")


class Team:
    def __init__(self):
        self.fencers = []

    def add_fencer(self, fencer):
        self.fencers.append(fencer)

    def remove_fencer(self, fencer_id):
        self.fencers = [f for f in self.fencers if f.id != fencer_id]
