from log_analyzer_cwj import logAnalyzer
from log_analyzer_cwj import innerRule


def start(_ruleFile, _fastMode, _multilineTime):
    print('------------start---------------')
    return logAnalyzer.log_analyze(_ruleFile, _fastMode, _multilineTime)


def json_all_to_dict(jsonString):
    return logAnalyzer.json_all_to_dict(jsonString)


def json_all_to_dict(jsonString):
    return innerRule.json_all_to_dict(jsonString)


def prepare_sequence(eventDict, startFlag):
    return innerRule.prepare_sequence(eventDict, startFlag)


def prepare_single(eventDict):
    return innerRule.prepare_single(eventDict)