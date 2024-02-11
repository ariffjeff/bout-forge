from enum import Enum

import pandas as pd


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

    def __init__(self, name_first, name_last=None, weapons=None):
        self.id = Fencer._id_counter  # Assign unique ID
        Fencer._id_counter += 1  # Increment ID counter

        self.name_first = name_first
        self.name_last = name_last
        self.weapons = {weapon_type: False for weapon_type in WeaponType}

    def add_weapons(self, weapons):
        '''
        Add the weapons this fencer is capable of using.
        This does not refer to the weapons a fencer will actually be using at any given event.
        '''

        if not isinstance(weapons, list):
            weapons = [weapons]

        for weapon_type in weapons:
            if weapon_type in self.weapons:
                self.weapons[weapon_type] = True

    def remove_weapon(self, weapon):
        if weapon in self.weapons:
            self.weapons.remove(weapon)
        else:
            print(f"{self.name_first, self.name_last} does not have {weapon}.")


class Team:
    def __init__(self, name):
        self.name = name
        # self.id =

        self.fencers = pd.DataFrame(columns=["Name", "Weapons"])

    def add_coach(self, name):
        pass

    def remove_coach(self, name):
        pass

    def add_fencer(self, fencer):
        new_row = {
            "name_first": fencer.name_first,
            "name_last": fencer.name_last,
            "Weapons": fencer.weapons,
        }
        self.fencers = pd.concat(
            [self.fencers, pd.DataFrame([new_row])], ignore_index=True
        )

    def remove_fencer(self, fencer_id):
        self.fencers = [f for f in self.fencers if f.id != fencer_id]


# class TeamOptimizer:
#     def __init__(self) -> None:
#         pass

#     # optimize teams arrangement
