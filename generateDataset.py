import json
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional, Set


@dataclass
class Dataset:
    name: str
    
    meanExecutionTime: Dict[str, List[Optional[float]]]
    numberHttpRequest: Dict[str, List[Optional[int]]]
    stdExecutionTime: Dict[str, List[Optional[float]]]
    numberResults: Dict[str, List[Optional[int]]]
    
    executionTime: Dict[str,
                        Dict[str, Optional[List[float]]]]
    results: Dict[str, Dict[str, List[Set[str]]]]
    arrivalTimes: Dict[str, Dict[str, List[List[float]]]]
    
    def _resultsArrivalNth(self, query_name:str, version:str, nth:int)->List[float]:
        arrival_times = self.arrivalTimes[query_name][version]
        first_results = []
        for times in arrival_times:
            first_results.append(times[nth])
        return first_results
    
    def firstResultsTime(self, query_name:str, version:str)->List[float]:
        return self._resultsArrivalNth(query_name, version,1)
    
    def lastResultsTime(self, query_name:str, version:str)->List[float]:
        return self._resultsArrivalNth(query_name, version,-1)
        

def divideResultsIntoArrivalTime(results: List[dict]) -> Tuple[Set[str], List[float]]:
    resultsCurrated = set()
    arrivalTimes = []

    for result in results:
        arrivalTimes.append(result.pop('_arrival_time'))
        resultsCurrated.add(json.dumps(dict(sorted(result.items()))))
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
    numberResults = {}

    with open(filepathFullResuls, 'rb') as rf:
        fullResuls = json.load(rf)

    with open(filepathSummaryResuls, 'rb') as rf:
        summaryResults = json.load(rf)

    for queryName, versionData in summaryResults.items():
        meanExecutionTime[queryName] = []
        numberHttpRequest[queryName] = []
        stdExecutionTime[queryName] = []
        numberResults[queryName] = []
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
                elif "n_results":
                    numberResults[queryName].append(value)

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
        stdExecutionTime=stdExecutionTime,
        numberResults=numberResults
        )


def generateGroundTruthResults(filepath) -> List[dict]:
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
                currentValue += '^^{}'.format(value["datatype"])
            transformedBinding[key] = currentValue
        resp.append(transformedBinding)
    return resp
