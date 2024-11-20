from generateDataset import generateDatasetFromResults
from metric import calculatePercentageReductionSeries
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy.stats import pearsonr
from typing import List, Dict, Tuple, Optional
import os
import json
from matplotlib import rcParams

rcParams.update({'font.size': 12})


artefactFolder = "./artefact/http_req_exec_time_relation"


def generatePlot(x: np.array, y: np.array, x_axis_tick: int, y_axis_tick: int, savePathNoExtension: str) -> None:
    fig, ax = plt.subplots(figsize=(8,7))

    ax.grid(axis="both")

    s = 20
    ax.scatter(x, y, s=s)

    ax.xaxis.set_major_locator(MultipleLocator(x_axis_tick))
    ax.yaxis.set_major_locator(MultipleLocator(y_axis_tick))
    ax.tick_params(axis='x', rotation=20)

    ax.set_xlabel('% reduction HTTP request')
    ax.set_ylabel('% reduction execution time')

    fig.savefig("{}.svg".format(savePathNoExtension), format="svg")
    fig.savefig("{}.eps".format(savePathNoExtension), format="eps")


def aggregateReduction(reductionDataset: Dict[str, Optional[List[int | float]]], globalAggregation: List[int | float]) -> None:
    for query, versions in reductionDataset.items():
        for i, reduction in enumerate(versions):
            if reduction is not None:
                globalAggregation.append(reduction)


def dividePoints(x: np.array, y: np.array, threshold: float) -> Tuple[Tuple[np.array, np.array], Tuple[np.array, np.array]]:
    x_right = []
    y_right = []

    x_left = []
    y_left = []

    for i, val in enumerate(x):
        if val > threshold:
            x_right.append(val)
            y_right.append(y[i])
        else:
            x_left.append(val)
            y_left.append(y[i])
    return ((x_right, y_right), (x_left, y_left))


typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
typeIndexLdpDataset = generateDatasetFromResults(
    typeIndexLdpPathResult, typeIndexLdpPathSummary, "typeIndexLdp")

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(
    shapeIndexPathResult, shapeIndexPathSummary, "shapeIndex")

shapeIndex20PathResult = "./results/shape-index-20-percent/shape_index_result.json"
shapeIndex20PathSummary = "./results/shape-index-20-percent/summary_shape_index_result.json"
shapeIndex20Dataset = generateDatasetFromResults(
    shapeIndex20PathResult, shapeIndex20PathSummary, "shapeIndex20Percent")

shapeIndex50PathResult = "./results/shape-index-50-percent/shape_index_result.json"
shapeIndex50PathSummary = "./results/shape-index-50-percent/summary_shape_index_result.json"
shapeIndex50Dataset = generateDatasetFromResults(
    shapeIndex50PathResult, shapeIndex50PathSummary, "shapeIndex50Percent")

shapeIndex80PathResult = "./results/shape-index-80-percent/shape_index_result.json"
shapeIndex80PathSummary = "./results/shape-index-80-percent/summary_shape_index_result.json"
shapeIndex80Dataset = generateDatasetFromResults(
    shapeIndex80PathResult, shapeIndex80PathSummary, "shapeIndex80Percent")

shapeIndexInnerPathResult = "./results/shape-inner/shape_index_result.json"
shapeIndexInnerPathSummary = "./results/shape-inner/summary_shape_index_result.json"
shapeIndexInnerDataset = generateDatasetFromResults(
    shapeIndexInnerPathResult, shapeIndexInnerPathSummary, "shapeInner")

shapeIndexMinimalPathResult = "./results/shape-minimal/shape_index_result.json"
shapeIndexMinimalPathSummary = "./results/shape-minimal/summary_shape_index_result.json"
shapeIndexMinimalDataset = generateDatasetFromResults(
    shapeIndexMinimalPathResult, shapeIndexMinimalPathSummary, "shapeMinimal")

shapeIndex20EntryPathResult = "./results/shape-entry-20-percent/shape_index_result.json"
shapeIndex20EntryPathSummary = "./results/shape-entry-20-percent/summary_shape_index_result.json"
shapeIndex20EntryDataset = generateDatasetFromResults(shapeIndex20PathResult, shapeIndex20PathSummary, "shape index entries 20%")

shapeIndex50EntryPathResult = "./results/shape-entry-50-percent/shape_index_result.json"
shapeIndex50EntryPathSummary = "./results/shape-entry-50-percent/summary_shape_index_result.json"
shapeIndex50EntryDataset = generateDatasetFromResults(shapeIndex50PathResult, shapeIndex50PathSummary, "shape index entries 50%")

shapeIndex80EntryPathResult = "./results/shape-entry-80-percent/shape_index_result.json"
shapeIndex80EntryPathSummary = "./results/shape-entry-80-percent/summary_shape_index_result.json"
shapeIndex80EntryDataset = generateDatasetFromResults(shapeIndex80PathResult, shapeIndex80PathSummary, "shape index entries 80%")


shapeIndexDatasets = [
    shapeIndexDataset,
    shapeIndex20Dataset,
    shapeIndex50Dataset,
    shapeIndex80Dataset,
    shapeIndex20EntryDataset,
    shapeIndex50EntryDataset,
    shapeIndex80EntryDataset,
    shapeIndexInnerDataset,
    shapeIndexMinimalDataset,
]

generalReductionHttpRequest = []
generalReductionExec = []

for dataset in shapeIndexDatasets:
    currentReductionHttpRequest = calculatePercentageReductionSeries(
        dataset.numberHttpRequest, typeIndexLdpDataset.numberHttpRequest)
    currentReductionExec = calculatePercentageReductionSeries(
        dataset.meanExecutionTime, typeIndexLdpDataset.meanExecutionTime)

    aggregateReduction(currentReductionHttpRequest,
                       generalReductionHttpRequest)
    aggregateReduction(currentReductionExec, generalReductionExec)

np_x_general_reduction_http_req = np.array(generalReductionHttpRequest)
np_y_general_reduction_exec = np.array(generalReductionExec)

(
    better_dataset,
    worse_dataset
) = dividePoints(np_x_general_reduction_http_req, np_y_general_reduction_exec, -125)

PCC_worse_performance = pearsonr(
    worse_dataset[0], worse_dataset[1])
PCC_better_performance = pearsonr(
    better_dataset[0], better_dataset[1])
PCC_overall = pearsonr(np_x_general_reduction_http_req,
                       np_y_general_reduction_exec)

pearsonrAnalysis = {
    "PCC_worse_performance": {
        "PCC": PCC_worse_performance[0].item(),
        "Pvalue": PCC_worse_performance[1].item()
    },
    "PCC_better_performance": {
        "PCC": PCC_better_performance[0].item(),
        "Pvalue": PCC_better_performance[1].item()
    },
    "PCC_overall": {
        "PCC": PCC_overall[0].item(),
        "Pvalue": PCC_overall[1].item()
    }
}

with open(os.path.join(artefactFolder, "perason_analysis.json"), "w") as outfile:
    json_object = json.dumps(pearsonrAnalysis, indent=4)
    outfile.write(json_object)

generatePlot(better_dataset[0], better_dataset[1],25,20,os.path.join(artefactFolder,"http_req_exec_time_cor_better"))
generatePlot(worse_dataset[0], worse_dataset[1],100,20,os.path.join(artefactFolder,"http_req_exec_time_cor_worse"))
