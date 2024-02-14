from bout_forge.team_manager import Team, Fencer, WeaponType, TeamManager
from bout_forge.event_manager import Event


def main():

    from datetime import datetime
    from bout_forge.bout_forge import Team
    from pathlib import Path

    # example: load json and create objects
    team_manager = TeamManager(Path("bout_forge/config/teams.json"))

    # example: create data manually
    event = Event("Winter Classic", datetime.now(), "East Lyme High School")
    teams = [
        Team("East Lyme"),
        Team("Waterford")
    ]

    event.add_teams(teams)


    fencer1 = Fencer("Alice", "Aorta", "female")
    fencer1.add_weapons([WeaponType.FOIL, WeaponType.SABRE])
    teams[0].add_fencer(fencer1)

    fencer2 = Fencer("Bob", "Barns", WeaponType.EPEE)
    teams[0].add_fencer(fencer2)

    # Try adding a fencer with the same name
    fencer3 = Fencer("Alice", "Aorta", [WeaponType.FOIL, WeaponType.EPEE])
    teams[1].add_fencer(fencer3)

    print("Team Fencers:")
    for fencer in teams[1].fencers:
        print(
            f"ID: {fencer.id}, Name: {fencer.name_first} {fencer.name_last}, Weapons: {fencer.weapons}"
        )

    # Remove a fencer
    teams[1].remove_fencer(fencer2.id)

    print("\nTeam Fencers after removal:")
    for fencer in teams[1].fencers:
        print(
            f"ID: {fencer.id}, Name: {fencer.name_first} {fencer.name_last}, Weapons: {fencer.weapons}"
        )
