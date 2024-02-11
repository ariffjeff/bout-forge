from bout_forge.team_manager import Team, Fencer, WeaponType


def main():
    team = Team("East Lyme")

    fencer1 = Fencer("Alice", "Aorta")
    fencer1.add_weapons([WeaponType.FOIL, WeaponType.SABRE])
    team.add_fencer(fencer1)

    fencer2 = Fencer("Bob", "Barns", WeaponType.EPEE)
    team.add_fencer(fencer2)

    # Try adding a fencer with the same name
    fencer3 = Fencer("Alice", "Aorta", [WeaponType.FOIL, WeaponType.EPEE])
    team.add_fencer(fencer3)

    print("Team Fencers:")
    for fencer in team.fencers:
        print(
            f"ID: {fencer.id}, Name: {fencer.name_first} {fencer.name_last}, Weapons: {fencer.weapons}"
        )

    # Remove a fencer
    team.remove_fencer(fencer2.id)

    print("\nTeam Fencers after removal:")
    for fencer in team.fencers:
        print(
            f"ID: {fencer.id}, Name: {fencer.name_first} {fencer.name_last}, Weapons: {fencer.weapons}"
        )
