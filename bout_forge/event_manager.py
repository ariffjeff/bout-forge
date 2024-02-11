class Event:
    def __init__(self, name, date, location) -> None:
        self.name = name
        self.date = date
        self.location = location

        # self.id = id # unique id calculated from name and date

    def add_team(self, team):
        '''
        Assign a team to this event.
        '''
        

    def remove_team(self, team):
        '''
        Remove a team from this event.
        '''

    def get_absent_fencers(self, teams=None):
        '''
        Return all the absent fencers for the event. If teams is specified, only return the absent fencers for the given teams.
        '''
        pass

    def create_pools():
        # ignore fencers that have no valid weapons, assign them as spectators? maybe specialize them as squires for specific fencers
        pass



from datetime import datetime
from bout_forge.bout_forge import Team

event1 = Event("Winter Classic", datetime.now(), "East Lyme High School")
team1 = Team()

event1.add_team(team1)
