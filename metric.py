from typing import List, Optional, Dict,Set
from generateDataset import Dataset
from numbers import Number
import numpy as np

def internalResultConsistency(result_runs: List[Set[str]])->bool:
    if len(result_runs) ==0:
        return True
    first_result = result_runs[0]
    for i, repetition_result in enumerate(result_runs):
        if not first_result==repetition_result:
            return False
    return True
    
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
                if currentBaseline is not None and currentBaseline[i] is not None and val is None:
                    resp[query][i] = None
                elif val is None:
                      resp[query][i] = None
                elif currentBaseline is not None and currentBaseline[i] is not None :
                    resp[query][i] = calculatePercentageReduction(val, currentBaseline[i])
                    
    return resp
