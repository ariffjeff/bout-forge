from bout_forge.team_manager import Team

class Event:
    def __init__(self, name, date, location) -> None:
        self.name = name
        self.date = date
        self.location = location
        self.teams = {}

        # self.id = id # unique id calculated from name and date

    def add_teams(self, teams: Team | list):
        '''
        Assign teams to this event.
        '''
        if not isinstance(teams, list):
            teams = [teams]

        for team in teams:
            self.teams[team.id] = team

    def remove_teams(self, teams):
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


class Session:
    '''
    A complete set of fencing activity such as a full round of pool bouts, relay bouts, or a direct elimination bout.
    '''
    def __init__(self) -> None:
        self.fencers = []


class Pool(Session):
    def __init__(self) -> None:
        super().__init__()

class Relay(Session):
    def __init__(self) -> None:
        super().__init__()
    
class DirectElimination(Session):
    def __init__(self) -> None:
        super().__init__()

