from typing import List, Optional, Dict
from generateDataset import Dataset
from numbers import Number


def calculatePercentageUsefulLinks(
    instances: Dict[str, List[int]],
    groundTruth: Dict[str, List[int]],
) -> Dict[str, List[float]]:
    resp = {}
    for query, versionInstances in instances.items():
        resp[query] = []
        for i, nHttpRequest in enumerate(versionInstances):
            usefulHttpRequest = groundTruth[query][i]
            resp[query][i] = usefulHttpRequest / nHttpRequest

    return resp


def calculatePercentageReduction(val: int|float, baseline: int|float) -> float:
    return (baseline - val) / baseline * 100

def calculatePercentageReductionSeries(
    instances: Dict[str, Optional[List[int|float]]],
    baseline: Dict[str, Optional[List[int|float]]],
) -> Dict[str, Optional[List[float]]]:
    resp = {}
    for query, versionInstances in instances.items():
        resp[query] = [None, None, None, None, None]
        if versionInstances != None:    
            for i, val in enumerate(versionInstances):
                currentBaseline= baseline[query]    
                if  currentBaseline is not None and currentBaseline[i] is not None :
                    resp[query][i] = calculatePercentageReduction(val, currentBaseline[i])
                    
    return resp
