import json
from dataclasses import dataclass
import typing


@dataclass
class Dataset:
    name: str
    meanExecutionTime: typing.Dict[str, typing.List[float] | None]
    numberHttpRequest: typing.Dict[str, typing.List[int] | None]
    stdExecutionTime: typing.Dict[str, typing.List[float] | None]
    executionTime: typing.Dict[str,
                               typing.Dict[str, typing.List[float] | None]]
    results: typing.Dict[str, typing.Dict[str, typing.List[dict] | None]]
    arrivalTimes: typing.Dict[str, typing.Dict[str, typing.List[float] | None]]


filepathFullResuls = "/home/bryanelliott/Documents/PhD/coding/shapeIndexExperiment/best-case/results/shape_index_result.json"
filepathSummaryResuls = "/home/bryanelliott/Documents/PhD/coding/shapeIndexExperiment/best-case/results/summary_shape_index_result.json"


def divideResultsIntoArrivalTime(results: typing.List[dict]) -> typing.Tuple[typing.List[dict], typing.List[float]]:
    resultsCurrated = []
    arrivalTimes = []

    for result in results:
        arrivalTimes.append(result.pop('_arrival_time'))
        resultsCurrated.append(result)
    return [resultsCurrated, arrivalTimes]


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
                if field == "n_http_requests":
                    numberHttpRequest[queryName].append(value)
                if field == "execution_time":
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


eg = generateDatasetFromResults(
    filepathFullResuls, filepathSummaryResuls, "shape_index_result")
print(eg.arrivalTimes)
