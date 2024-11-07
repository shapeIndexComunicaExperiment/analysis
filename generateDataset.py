import json
from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Dataset:
    name: str
    meanExecutionTime: Dict[str, List[float] | None]
    numberHttpRequest: Dict[str, List[int] | None]
    stdExecutionTime: Dict[str, List[float] | None]
    executionTime: Dict[str,
                               Dict[str, List[float] | None]]
    results: Dict[str, Dict[str, List[dict] | None]]
    arrivalTimes: Dict[str, Dict[str, List[float] | None]]

def divideResultsIntoArrivalTime(results: List[dict]) -> Tuple[List[dict], List[float]]:
    resultsCurrated = []
    arrivalTimes = []

    for result in results:
        arrivalTimes.append(result.pop('_arrival_time'))
        resultsCurrated.append(result)
    return (resultsCurrated, arrivalTimes)

def generateDatasetFromResults(filepathFullResuls: str, filepathSummaryResuls: str, name: str) -> Dataset:
    fullResuls = None
    summaryResults = None

    executionTime = {}
    results = {}
    arrivalTimes = {}
    meanExecutionTime = {}
    numberHttpRequest = {}
    stdExecutionTime = {}

    with open(filepathFullResuls, 'rb') as rf:
        fullResuls = json.load(rf)

    with open(filepathSummaryResuls, 'rb') as rf:
        summaryResults = json.load(rf)

    for queryName, versionData in summaryResults.items():
        meanExecutionTime[queryName] = []
        numberHttpRequest[queryName] = []
        stdExecutionTime[queryName] = []
        for version, data in versionData.items():
            for field, value in data.items():
                if field == "timeout":
                    meanExecutionTime[queryName].append(None)
                    numberHttpRequest[queryName].append(None)
                    stdExecutionTime[queryName].append(None)
                elif field == "n_http_requests":
                    numberHttpRequest[queryName].append(value)
                elif field == "execution_time":
                    meanExecutionTime[queryName].append(value["average"])
                    stdExecutionTime[queryName].append(value["std"])
                

    for queryName, versionData in fullResuls["data"].items():
        executionTime[queryName] = {}
        results[queryName] = {}
        arrivalTimes[queryName] = {}
        for version, repetitionData in versionData.items():
            executionTime[queryName][version] = []
            results[queryName][version] = []
            arrivalTimes[queryName][version] = []
            for i, repetition in enumerate(repetitionData):
                if (type(repetition) != str):
                    res = divideResultsIntoArrivalTime(
                        repetition['results'])

                    results[queryName][version].append(res[0])
                    executionTime[queryName][version].append(
                        repetition['execution_time'])
                    arrivalTimes[queryName][version].append(res[1])
                else:
                    executionTime[queryName][version] = None
                    results[queryName][version] = None
                    arrivalTimes[queryName][version] = None
    return Dataset(
        name=name,
        arrivalTimes=arrivalTimes,
        results=results,
        executionTime=executionTime,
        meanExecutionTime=meanExecutionTime,
        numberHttpRequest=numberHttpRequest,
        stdExecutionTime=stdExecutionTime)

def generateGroundTruthResults(filepath)-> List[dict]:
    data = None
    with open(filepath, 'rb') as rf:
        data = json.load(rf)
    bindings = data["results"]["bindings"]
    resp = []
    for binding in bindings:
        transformedBinding = {}
        for key, value in binding.items():
            currentValue = '"{}"'.format(value['value'])
            if "datatype" in value:
                currentValue+= '^^{}'.format(value["datatype"])
            transformedBinding[key] = currentValue
        resp.append(transformedBinding)
    return resp
