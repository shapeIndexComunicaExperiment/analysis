from typing import List, Optional, Dict,Set
import scipy.stats as stats
import numpy as np
from scipy.stats import ks_2samp

def statisticalSignificanceByTemplate(instance: Dict[str, Optional[List[float]]], baseline: Dict[str, Optional[List[float]]]):
    baseline_template_results = []
    instance_template_results = []
    for key, results in baseline.items():
        if results is not None and instance[key] is not None:
            baseline_template_results += results
            instance_template_results += instance[key]
    
    if len(baseline_template_results) == 0:
        return (None, None, None)
    pValueGreater = stats.mannwhitneyu(x=np.array(instance_template_results),
                           y=np.array(baseline_template_results),
                           method="auto",
                           alternative = 'greater').pvalue
    
    pValueLess = stats.mannwhitneyu(x=np.array(instance_template_results),
                           y=np.array(baseline_template_results),
                           method="auto",
                           alternative = 'less').pvalue
        
    pValueEqual = stats.mannwhitneyu(x=instance_template_results,
                           y=baseline_template_results,
                           method="auto",
                           alternative = 'two-sided').pvalue
    

    return (pValueGreater.item(), pValueEqual.item(), pValueLess.item())
    
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
    return (val/baseline)
    #return (baseline - val) / baseline * 100

def calculatePercentageReductionSeries(
    instances: Dict[str, Optional[List[int|float|None]]],
    baseline: Dict[str, Optional[List[int|float|None]]],
) -> Dict[str, List[Optional[float]]]:
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
