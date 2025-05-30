from generateDataset import generateDatasetFromResults
from metric import calculatePercentageReductionSeries
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy.stats import pearsonr
from typing import List, Dict, Tuple, Optional
import os
import json
from matplotlib import rcParams
import matplotlib.patches as mpatches
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score, mean_squared_error

rcParams.update({'font.size': 25})


artefactFolder = "./artefact/http_req_exec_time_relation"

def slopeLinearRegression(x: np.array, y: np.array):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
    b = y_mean - m * x_mean
    return m

def generatePlot(x: np.array, y: np.array, x_axis_tick: int, y_axis_tick: int, savePathNoExtension: str, pcc:float,pvalue:float, slope:float, r2Lin:float, r2Expo:float) -> None:
    fig, ax = plt.subplots(figsize=(10,10))

    ax.grid(axis="both")

    s = 20
    ax.scatter(x, y, s=s)

    ax.xaxis.set_major_locator(MultipleLocator(x_axis_tick))
    ax.yaxis.set_major_locator(MultipleLocator(y_axis_tick))
    ax.tick_params(axis='x', rotation=35)
    
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    statPath = mpatches.Patch(color="None", label=f'PCC = {pcc:.2f}, p-value ={pvalue:.2E}')
    r2Path = mpatches.Patch(color="None", label=f'R2 lin = {r2Lin:.2}, R2 exp = {r2Expo:.2f}')
    ax.legend(handles=[statPath, r2Path],handlelength=0, handleheight=0)
    ax.set_xlabel('ratio of HTTP request')
    ax.set_ylabel('ratio of execution time')
    
    fig.tight_layout()

    fig.savefig("{}.svg".format(savePathNoExtension), format="svg")
    fig.savefig("{}.eps".format(savePathNoExtension), format="eps")


def aggregateReduction(reductionDataset: Dict[str, Optional[List[int | float]]], globalAggregation: List[int | float]) -> None:
    for query, versions in reductionDataset.items():
        for i, reduction in enumerate(versions):
            if reduction is not None:
                globalAggregation.append(reduction)

# Linear model
def linear_model(x, m, c):
    return m * x + c

# Exponential model
def exponential_model(x, a, b):
    return a * np.exp(b * x)

def evaluateR2LinExp(x, y):
    # Fit the linear model
    popt_linear, _ = curve_fit(linear_model,  x, y)

    # Fit the exponential model
    popt_exponential, _ = curve_fit(exponential_model, x, y)

    # Predictions
    y_pred_linear = linear_model(x, *popt_linear)
    y_pred_exponential = exponential_model(x, *popt_exponential)

    # R-squared for both models
    r2_linear = r2_score(y, y_pred_linear)
    r2_exponential = r2_score(y, y_pred_exponential)
    
    rmse_linear = np.sqrt(mean_squared_error(y, y_pred_linear))
    rmse_exponential = np.sqrt(mean_squared_error(y, y_pred_exponential))
    
    return (r2_linear, r2_exponential, rmse_linear, rmse_exponential)

def dividePoints(x: np.array, y: np.array, threshold: float) -> Tuple[Tuple[np.array, np.array], Tuple[np.array, np.array]]:
    x_right = []
    y_right = []

    x_left = []
    y_left = []

    for i, val in enumerate(x):
        if val > threshold:
            x_right.append(val)
            y_right.append(y[i])
        elif val == threshold:
            x_right.append(val)
            y_right.append(y[i])
            
            x_left.append(val)
            y_left.append(y[i])
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
    worse_dataset,
    better_dataset,
) = dividePoints(np_x_general_reduction_http_req, np_y_general_reduction_exec, 1)

PCC_worse_performance = pearsonr(
    worse_dataset[0], worse_dataset[1])
PCC_better_performance = pearsonr(
    better_dataset[0], better_dataset[1])
PCC_overall = pearsonr(np_x_general_reduction_http_req,
                       np_y_general_reduction_exec)

(r2LinWorse, r2ExpWorse, rmse_linear_worse, rmse_exponential_worse) = evaluateR2LinExp(np.array(worse_dataset[0]), np.array(worse_dataset[1]))
(r2LinBetter, r2ExpBetter, rmse_linear_better, rmse_exponential_better) = evaluateR2LinExp(np.array(better_dataset[0]), np.array(better_dataset[1]))
(r2LinOverall, r2ExpOverall, rmse_linear_overall, rmse_exponential_overall) = evaluateR2LinExp(np_x_general_reduction_http_req, np_y_general_reduction_exec)
pearsonrAnalysis = {
    "PCC_worse_performance": {
        "PCC": PCC_worse_performance[0].item(),
        "Pvalue": PCC_worse_performance[1].item(),
        "slope": slopeLinearRegression(worse_dataset[0], worse_dataset[1]),
        "r2_lin": r2LinWorse,
        "r2_exp": r2ExpWorse,
        "rmse_lin":rmse_linear_worse,
        "rmse_exp":rmse_exponential_worse,
    },
    "PCC_better_performance": {
        "PCC": PCC_better_performance[0].item(),
        "Pvalue": PCC_better_performance[1].item(),
        "slope": slopeLinearRegression(better_dataset[0], better_dataset[1]),
        "r2_lin": r2LinBetter,
        "r2_exp": r2ExpBetter,
        "rmse_lin":rmse_linear_better,
        "rmse_exp":rmse_exponential_better,
    },
    "PCC_overall": {
        "PCC": PCC_overall[0].item(),
        "Pvalue": PCC_overall[1].item(),
        "slope": slopeLinearRegression(np_x_general_reduction_http_req, np_y_general_reduction_exec),
        "r2_lin": r2LinOverall,
        "r2_exp": r2ExpOverall,
        "rmse_lin":rmse_linear_overall,
        "rmse_exp":rmse_exponential_overall,
    }
}

with open(os.path.join(artefactFolder, "stats.json"), "w") as outfile:
    json_object = json.dumps(pearsonrAnalysis, indent=4)
    outfile.write(json_object)

generatePlot(
    better_dataset[0],
    better_dataset[1],
    0.1,
    0.1,
    os.path.join(artefactFolder,"http_req_exec_time_cor_better"),
    PCC_better_performance[0].item(),
    PCC_better_performance[1].item(),
    slopeLinearRegression(better_dataset[0], better_dataset[1]),
    r2LinBetter, 
    r2ExpBetter
)
generatePlot(
    worse_dataset[0],
    worse_dataset[1],
    1.0,
    0.1,
    os.path.join(artefactFolder,"http_req_exec_time_cor_worse"),
    PCC_worse_performance[0].item(),
    PCC_worse_performance[1].item(),
    slopeLinearRegression(worse_dataset[0], worse_dataset[1]),
    r2LinWorse, 
    r2ExpWorse
    )

