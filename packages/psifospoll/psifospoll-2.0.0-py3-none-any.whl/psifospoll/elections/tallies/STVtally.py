from math import floor
import random
from collections import defaultdict
from psifospoll.elections.tallies.STVutils import *
from psifospoll.elections.tallies.tally import Tally
from psifospoll.elections.tallies.ballots.STVballot import STVBallot


class STVTally(Tally):
    def __init__(self, s, candidates_list, ballot_list):
        if isAValidCandidatesList(candidates_list) and isAValidBallotList(
            ballot_list, candidates_list
        ):
            self.ballot_list = [STVBallot(ballot) for ballot in ballot_list]

        n = len(ballot_list)
        self.n = n
        self.s = s
        self.m = len(candidates_list)
        self.q = floor(n / (s + 1)) + 1

        self.rounds_data = []
        self.round_resume = getRoundResume([], [], candidates_list)
        self.candidates_and_tallies = getInitialCandidatesAndTallies(candidates_list)

    def computeFirstPreferenceTallies(self):
        global candidates_and_tallies
        self.candidates_and_tallies = defaultdict(int)
        for ballot in self.ballot_list:
            preferences_list = ballot.preferences_list
            if len(preferences_list) > 0 and ballot.weight > 0:
                first_preference = preferences_list[0]
                self.candidates_and_tallies[first_preference] += ballot.weight
        self.candidates_and_tallies = dict(self.candidates_and_tallies)

    def electOrEliminateCandidates(self):
        global round_resume
        tallies_and_candidates = invertDict(self.candidates_and_tallies)
        tallies = list(tallies_and_candidates.keys())

        elected_tallies = list(filter(lambda x: x >= self.q, tallies))
        elected_candidates = [
            candidate
            for tally in elected_tallies
            for candidate in tallies_and_candidates[tally]
        ]

        rejectable_candidates = [
            candidate  # candidates with tally = 0
            for candidate in self.round_resume["hopeful"]
            if not candidate in self.candidates_and_tallies.keys()
        ]
        if len(rejectable_candidates) == 0:
            rejectable_candidates = tallies_and_candidates[min(tallies)]
        rejected_candidates = (
            [random.choice(rejectable_candidates)]
            if len(elected_candidates) == 0
            else []
        )

        resolved_candidates = elected_candidates + rejected_candidates
        hopeful_candidates = [
            candidate
            for candidate in self.round_resume["hopeful"]
            if not candidate in resolved_candidates
        ]

        self.round_resume = getRoundResume(
            elected_candidates, rejected_candidates, hopeful_candidates
        )

    def getTV(self, tally):
        return (tally - self.q) / tally

    def reweightVotes(self):
        global ballot_list
        elected = self.round_resume["elected"]
        winner_and_tv = {}
        for candidate in elected:
            winner_and_tv[candidate] = self.getTV(
                self.candidates_and_tallies[candidate]
            )
        if len(elected) > 0:
            for ballot in self.ballot_list:
                first_preference = ballot.preferences_list[0]
                if first_preference in elected:
                    ballot.weight *= winner_and_tv[first_preference]

    def eliminateCandidates(self):
        global ballot_list
        elected = self.round_resume["elected"]
        rejected = self.round_resume["rejected"]

        for ballot in self.ballot_list:
            ballot.preferences_list = [
                preference
                for preference in ballot.preferences_list
                if not preference in elected + rejected
            ]

        self.ballot_list = [
            ballot for ballot in self.ballot_list if len(ballot.preferences_list) > 0
        ]
