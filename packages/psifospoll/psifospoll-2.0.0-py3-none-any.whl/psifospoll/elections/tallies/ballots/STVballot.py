from psifospoll.elections.tallies.ballots.ballot import Ballot


class STVBallot(Ballot):
    def __init__(self, preferences_list):
        self.preferences_list = preferences_list
        self.weight = 1
