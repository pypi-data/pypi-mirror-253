from psifospoll.elections.tallies.STVutils import *
from psifospoll.elections.election import Election
from psifospoll.elections.tallies.STVtally import STVTally


class STVElection(Election):
    def __init__(self):
        self.round_resumes = []
        self.tallies_resumes = []
        self.winners_list = []
        self.quota = None

    def getRoundResumes(self):
        return self.round_resumes

    def getTalliesResumes(self):
        return self.tallies_resumes

    def getWinnersList(self):
        return self.winners_list

    def getQuota(self):
        return self.quota

    def setQuota(self, new_value):
        global quota
        self.quota = new_value

    def runElection(self, s, candidates_list, ballot_list):
        global round_resumes, tallies_resumes, winners_list
        stv = STVTally(s, candidates_list, ballot_list)
        open_seats = s
        self.setQuota(stv.q)

        while len(stv.round_resume["hopeful"]) > open_seats and open_seats > 0:
            stv.computeFirstPreferenceTallies()
            self.tallies_resumes.append(stv.candidates_and_tallies)

            stv.electOrEliminateCandidates()
            self.round_resumes.append(stv.round_resume)
            winners = stv.round_resume["elected"]
            self.winners_list += winners
            open_seats -= len(winners)

            stv.reweightVotes()

            stv.eliminateCandidates()

        hopeful = stv.round_resume["hopeful"]
        if len(hopeful) == open_seats:
            self.winners_list += hopeful

        return self.winners_list
