from enum import Enum

import pandas as pd
import json
from pathlib import Path

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

    def __init__(self, name_first, name_last=None, weapons:WeaponType | list=None):
        self.id = Fencer._id_counter  # Assign unique ID
        Fencer._id_counter += 1  # Increment ID counter

        self.name_first = name_first
        self.name_last = name_last

        self.weapons = {weapon_type: False for weapon_type in WeaponType}
        
        if weapons:
            if not isinstance(weapons, list):
                weapons = [weapons]
            if not isinstance(weapons[0], WeaponType) and not isinstance(weapons[0], str):
                raise TypeError('Weapons must be objects of WeaponType or str')
            # convert strings to WeaponType enums
            if isinstance(weapons[0], str):
                for i, weapon_type in enumerate(weapons):
                    weapons[i] = WeaponType[weapon_type.upper()]
            self.add_weapons(weapons)

    def add_weapons(self, weapons: WeaponType | list):
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
    _id_counter = 0  # Class variable to generate unique IDs

    def __init__(self, name):
        self.id = Team._id_counter
        Team._id_counter += 1

        self.name = name
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


class TeamManager:
    def __init__(self, json_file: Path) -> None:
        self.json_file = json_file
        self.teams = []
        self.load_and_build_data()

    def load_and_build_data(self):
        with open(self.json_file) as file:
            data = json.load(file)
            for team in data['teams']:
                team_name = team['team_name']
                fencers = team['fencers']
                team = Team(team_name)
                for fencer_data in fencers:
                    fencer = Fencer(fencer_data['name_first'], fencer_data['name_last'], fencer_data['weapons'])
                    team.add_fencer(fencer)
                self.teams.append(team)

    def print_teams(self):
        for team in self.teams:
            print("Team:", team.name)
            print("Fencers:")
            for fencer in team.fencers:
                print("Name:", fencer.name)
                print("Weapons:", ', '.join(fencer.weapons))
            print()


# class TeamOptimizer:
#     def __init__(self) -> None:
#         pass

#     # optimize teams arrangement
