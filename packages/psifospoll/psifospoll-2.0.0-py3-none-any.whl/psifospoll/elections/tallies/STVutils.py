def isAValidBallot(preferences_list, candidates_list):
    if set(preferences_list).issubset(set(candidates_list)):
        if len(set(preferences_list)) == len(preferences_list):
            return True
    return False


def isAValidBallotList(ballot_list, candidates_list):
    if len(ballot_list) > 0 and all(
        isAValidBallot(ballot, candidates_list) for ballot in ballot_list
    ):
        return True
    raise Exception("Invalid ballot list")


def isAValidCandidatesList(candidates_list):
    if len(candidates_list) > 0 and len(set(candidates_list)) == len(candidates_list):
        return True
    raise Exception("Invalid candidates list")


def getRoundResume(elected, rejected, hopeful):
    return {
        "elected": elected,
        "rejected": rejected,
        "hopeful": hopeful,
    }


def invertDict(original_dict):
    result_dict = {}
    for key, value in original_dict.items():
        result_dict.setdefault(value, []).append(key)
    return result_dict


def getInitialCandidatesAndTallies(candidates_list):
    candidates_and_tallies = {}
    for candidate in candidates_list:
        candidates_and_tallies[candidate] = 0
