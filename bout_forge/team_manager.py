import json
from enum import Enum
from pathlib import Path
from typing import List, Union

import pandas as pd


class WeaponType(Enum):
    FOIL = "foil"
    EPEE = "epee"
    SABRE = "sabre"


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

    def __init__(self, name_first=None, name_last=None, gender=None, weapons:WeaponType | list=None):
        self.id = Fencer._id_counter  # Assign unique ID
        Fencer._id_counter += 1  # Increment ID counter

        self.name_first = name_first
        self.name_last = name_last
        self.gender = gender

        for weapon_type in WeaponType:
            setattr(self, weapon_type.value, False)

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

    def add_weapons(self, weapons: Union[WeaponType, List[WeaponType]]):
        '''
        Add the weapons this fencer is capable of using.
        This does not refer to the weapons a fencer will actually be using at any given event.
        '''
        if not isinstance(weapons, list):
            weapons = [weapons]
        for weapon_type in weapons:
            if weapon_type in WeaponType:
                setattr(self, weapon_type.value, True)

    # def remove_weapon(self, weapon):
    #     if weapon in self.weapons:
    #         self.weapons.remove(weapon)
    #     else:
    #         print(f"{self.name_first, self.name_last} does not have {weapon}.")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name_first": self.name_first,
            "name_last": self.name_last,
            "gender": self.gender,
            "foil": self.foil,
            "epee": self.epee,
            "sabre": self.sabre,
        }
    
    def intake_dict(self, d: dict) -> None:
        self.name_first = d["name_first"]
        self.name_last = d["name_last"]
        self.gender = d["gender"]
        self.foil = d["foil"]
        self.epee = d["epee"]
        self.sabre = d["sabre"]


class Team:
    _id_counter = 0  # Class variable to generate unique IDs

    def __init__(self, name):
        self.id = Team._id_counter
        Team._id_counter += 1

        self.name = name
        self.fencers = pd.DataFrame()

    def add_coach(self, name):
        pass

    def remove_coach(self, name):
        pass

    def add_fencer(self, fencer: Fencer):
        row = fencer.to_dict()
        self.fencers = pd.concat([self.fencers, pd.DataFrame([row])], ignore_index=True)

    def remove_fencer(self, fencer_id):
        self.fencers = [f for f in self.fencers if f.id != fencer_id]


class TeamManager:
    def __init__(self, json_file: Path=None) -> None:
        self.teams = []
        self.json_file = json_file
        if json_file:
            self.load_json_and_build()

    def load_json_and_build(self) -> None:
        with open(self.json_file) as file:
            data = json.load(file)
            for team in data['teams']:
                team_name = team['team_name']
                fencers = team['fencers']
                team = Team(team_name)
                for fencer_data in fencers:
                    fencer = Fencer()
                    fencer.intake_dict(fencer_data)
                    team.add_fencer(fencer)
                self.teams.append(team)

    def write_json_config(self) -> None:
        pass

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
