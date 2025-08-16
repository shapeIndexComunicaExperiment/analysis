import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import json
    from texttable import Texttable
    import latextable
    from tabulate import tabulate
    import sys
    file_directory = "./"
    sys.path.append(file_directory)
    from generateDataset import generateDatasetFromResults
    from metric import calculatePercentageReductionSeries 
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    import matplotlib.patches as mpatches
    import numpy as np
    from matplotlib.ticker import MultipleLocator
    from scipy.optimize import curve_fit
    from scipy.stats import pearsonr
    from typing import List, Dict, Tuple, Optional
    from sklearn.metrics import r2_score, mean_squared_error
    from pathlib import Path
    return (
        Dict,
        FormatStrFormatter,
        List,
        MultipleLocator,
        Optional,
        Path,
        Tuple,
        calculatePercentageReductionSeries,
        curve_fit,
        generateDatasetFromResults,
        json,
        mean_squared_error,
        mpatches,
        np,
        pearsonr,
        plt,
        r2_score,
    )


@app.cell
def _(Path):
    artefact_path = Path("artefact") / "http_req_exec_time_relation"
    return (artefact_path,)


@app.cell
def _(mo):
    mo.md(r"""# Function definition""")
    return


@app.cell
def _(np):
    def slopeLinearRegression(x: np.array, y: np.array):
        n = len(x)
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
        b = y_mean - m * x_mean
        return m

    return (slopeLinearRegression,)


@app.cell
def _(FormatStrFormatter, MultipleLocator, mpatches, np, plt):
    def generatePlot(x: np.array,
                     y: np.array,
                     x_axis_tick: int,
                     y_axis_tick: int,
                     pcc:float,
                     pvalue:float,
                     slope:float,
                     r2Lin:float,
                     r2Expo:float) -> None:
        fontSize = 22
        fig, ax = plt.subplots(figsize=(10,10))

    
        for text in fig.findobj(match=plt.Text):
                text.set_fontsize(fontSize)

        ax.grid(axis="both")

        s = 20
        ax.scatter(x, y, s=s)

        ax.xaxis.set_major_locator(MultipleLocator(x_axis_tick))
        ax.yaxis.set_major_locator(MultipleLocator(y_axis_tick))
        ax.tick_params(axis='x', rotation=35)

        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        statPath = mpatches.Patch(color="None", label=f'PCC = {pcc:.2f}, p-value ={pvalue:.2E}')
        r2Path = mpatches.Patch(color="None", label=f'R2 lin = {r2Lin:.2}, R2 exp = {r2Expo:.2f}')
        ax.legend(handles=[statPath, r2Path],handlelength=0, handleheight=0, 
    prop={'size': 20}
    )
        ax.set_xlabel('ratio of HTTP request')
        ax.set_ylabel('ratio of execution time')

        fig.tight_layout()

        return fig

    return (generatePlot,)


@app.cell
def _(Dict, List, Optional):
    def aggregateReduction(reductionDataset: Dict[str, Optional[List[int | float]]], globalAggregation: List[int | float]) -> None:
        for query, versions in reductionDataset.items():
            for i, reduction in enumerate(versions):
                if reduction is not None:
                    globalAggregation.append(reduction)

    return (aggregateReduction,)


@app.function
# Linear model
def linear_model(x, m, c):
    return m * x + c


@app.cell
def _(np):
    # Exponential model
    def exponential_model(x, a, b):
        return a * np.exp(b * x)

    return (exponential_model,)


@app.cell
def _(curve_fit, exponential_model, mean_squared_error, np, r2_score):
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
    return (evaluateR2LinExp,)


@app.cell
def _(Tuple, np):
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

    return (dividePoints,)


@app.cell
def _(mo):
    mo.md(r"""# Dataset""")
    return


@app.cell
def _(generateDatasetFromResults):
    typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
    typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
    typeIndexLdpDataset = generateDatasetFromResults(
        typeIndexLdpPathResult, typeIndexLdpPathSummary, "typeIndexLdp")
    return (typeIndexLdpDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(
        shapeIndexPathResult, shapeIndexPathSummary, "shapeIndex")
    return (shapeIndexDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndex20PathResult = "./results/shape-index-20-percent/shape_index_result.json"
    shapeIndex20PathSummary = "./results/shape-index-20-percent/summary_shape_index_result.json"
    shapeIndex20Dataset = generateDatasetFromResults(
        shapeIndex20PathResult, shapeIndex20PathSummary, "shapeIndex20Percent")
    return shapeIndex20Dataset, shapeIndex20PathResult, shapeIndex20PathSummary


@app.cell
def _(generateDatasetFromResults):
    shapeIndex50PathResult = "./results/shape-index-50-percent/shape_index_result.json"
    shapeIndex50PathSummary = "./results/shape-index-50-percent/summary_shape_index_result.json"
    shapeIndex50Dataset = generateDatasetFromResults(
        shapeIndex50PathResult, shapeIndex50PathSummary, "shapeIndex50Percent")
    return shapeIndex50Dataset, shapeIndex50PathResult, shapeIndex50PathSummary


@app.cell
def _(generateDatasetFromResults):
    shapeIndex80PathResult = "./results/shape-index-80-percent/shape_index_result.json"
    shapeIndex80PathSummary = "./results/shape-index-80-percent/summary_shape_index_result.json"
    shapeIndex80Dataset = generateDatasetFromResults(
        shapeIndex80PathResult, shapeIndex80PathSummary, "shapeIndex80Percent")
    return shapeIndex80Dataset, shapeIndex80PathResult, shapeIndex80PathSummary


@app.cell
def _(generateDatasetFromResults):
    shapeIndexInnerPathResult = "./results/shape-inner/shape_index_result.json"
    shapeIndexInnerPathSummary = "./results/shape-inner/summary_shape_index_result.json"
    shapeIndexInnerDataset = generateDatasetFromResults(
        shapeIndexInnerPathResult, shapeIndexInnerPathSummary, "shapeInner")
    return (shapeIndexInnerDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexMinimalPathResult = "./results/shape-minimal/shape_index_result.json"
    shapeIndexMinimalPathSummary = "./results/shape-minimal/summary_shape_index_result.json"
    shapeIndexMinimalDataset = generateDatasetFromResults(
        shapeIndexMinimalPathResult, shapeIndexMinimalPathSummary, "shapeMinimal")
    return (shapeIndexMinimalDataset,)


@app.cell
def _(
    generateDatasetFromResults,
    shapeIndex20PathResult,
    shapeIndex20PathSummary,
):
    shapeIndex20EntryPathResult = "./results/shape-entry-20-percent/shape_index_result.json"
    shapeIndex20EntryPathSummary = "./results/shape-entry-20-percent/summary_shape_index_result.json"
    shapeIndex20EntryDataset = generateDatasetFromResults(shapeIndex20PathResult, shapeIndex20PathSummary, "shape index entries 20%")

    return (shapeIndex20EntryDataset,)


@app.cell
def _(
    generateDatasetFromResults,
    shapeIndex50PathResult,
    shapeIndex50PathSummary,
):
    shapeIndex50EntryPathResult = "./results/shape-entry-50-percent/shape_index_result.json"
    shapeIndex50EntryPathSummary = "./results/shape-entry-50-percent/summary_shape_index_result.json"
    shapeIndex50EntryDataset = generateDatasetFromResults(shapeIndex50PathResult, shapeIndex50PathSummary, "shape index entries 50%")

    return (shapeIndex50EntryDataset,)


@app.cell
def _(
    generateDatasetFromResults,
    shapeIndex80PathResult,
    shapeIndex80PathSummary,
):
    shapeIndex80EntryPathResult = "./results/shape-entry-80-percent/shape_index_result.json"
    shapeIndex80EntryPathSummary = "./results/shape-entry-80-percent/summary_shape_index_result.json"
    shapeIndex80EntryDataset = generateDatasetFromResults(shapeIndex80PathResult, shapeIndex80PathSummary, "shape index entries 80%")

    return (shapeIndex80EntryDataset,)


@app.cell
def _(
    shapeIndex20Dataset,
    shapeIndex20EntryDataset,
    shapeIndex50Dataset,
    shapeIndex50EntryDataset,
    shapeIndex80Dataset,
    shapeIndex80EntryDataset,
    shapeIndexDataset,
    shapeIndexInnerDataset,
    shapeIndexMinimalDataset,
):
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
    return (shapeIndexDatasets,)


@app.cell
def _(mo):
    mo.md(r"""# Calculation""")
    return


@app.cell
def _():
    generalReductionHttpRequest = []
    generalReductionExec = []
    return generalReductionExec, generalReductionHttpRequest


@app.cell
def _(
    aggregateReduction,
    calculatePercentageReductionSeries,
    generalReductionExec,
    generalReductionHttpRequest,
    np,
    shapeIndexDatasets,
    typeIndexLdpDataset,
):
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
    return np_x_general_reduction_http_req, np_y_general_reduction_exec


@app.cell
def _(
    dividePoints,
    np_x_general_reduction_http_req,
    np_y_general_reduction_exec,
):
    (
        worse_dataset,
        better_dataset,
    ) = dividePoints(np_x_general_reduction_http_req, np_y_general_reduction_exec, 1)
    return better_dataset, worse_dataset


@app.cell
def _(
    better_dataset,
    np_x_general_reduction_http_req,
    np_y_general_reduction_exec,
    pearsonr,
    worse_dataset,
):
    PCC_worse_performance = pearsonr(
        worse_dataset[0], worse_dataset[1])
    PCC_better_performance = pearsonr(
        better_dataset[0], better_dataset[1])
    PCC_overall = pearsonr(np_x_general_reduction_http_req,
                           np_y_general_reduction_exec)
    return PCC_better_performance, PCC_overall, PCC_worse_performance


@app.cell
def _(
    better_dataset,
    evaluateR2LinExp,
    np,
    np_x_general_reduction_http_req,
    np_y_general_reduction_exec,
    worse_dataset,
):
    (r2LinWorse, r2ExpWorse, rmse_linear_worse, rmse_exponential_worse) = evaluateR2LinExp(np.array(worse_dataset[0]), np.array(worse_dataset[1]))
    (r2LinBetter, r2ExpBetter, rmse_linear_better, rmse_exponential_better) = evaluateR2LinExp(np.array(better_dataset[0]), np.array(better_dataset[1]))
    (r2LinOverall, r2ExpOverall, rmse_linear_overall, rmse_exponential_overall) = evaluateR2LinExp(np_x_general_reduction_http_req, np_y_general_reduction_exec)
    return (
        r2ExpBetter,
        r2ExpOverall,
        r2ExpWorse,
        r2LinBetter,
        r2LinOverall,
        r2LinWorse,
        rmse_exponential_better,
        rmse_exponential_overall,
        rmse_exponential_worse,
        rmse_linear_better,
        rmse_linear_overall,
        rmse_linear_worse,
    )


@app.cell
def _(
    PCC_better_performance,
    PCC_overall,
    PCC_worse_performance,
    better_dataset,
    np_x_general_reduction_http_req,
    np_y_general_reduction_exec,
    r2ExpBetter,
    r2ExpOverall,
    r2ExpWorse,
    r2LinBetter,
    r2LinOverall,
    r2LinWorse,
    rmse_exponential_better,
    rmse_exponential_overall,
    rmse_exponential_worse,
    rmse_linear_better,
    rmse_linear_overall,
    rmse_linear_worse,
    slopeLinearRegression,
    worse_dataset,
):
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

    pearsonrAnalysis
    return (pearsonrAnalysis,)


@app.cell
def _(mo):
    mo.md(r"""# Plot""")
    return


@app.cell
def _(
    PCC_better_performance,
    better_dataset,
    generatePlot,
    r2ExpBetter,
    r2LinBetter,
    slopeLinearRegression,
):
    improvement_plot = generatePlot(
        better_dataset[0],
        better_dataset[1],
        0.1,
        0.1,
        PCC_better_performance[0].item(),
        PCC_better_performance[1].item(),
        slopeLinearRegression(better_dataset[0], better_dataset[1]),
        r2LinBetter, 
        r2ExpBetter
    )
    improvement_plot
    return (improvement_plot,)


@app.cell
def _(
    PCC_worse_performance,
    generatePlot,
    r2ExpWorse,
    r2LinWorse,
    slopeLinearRegression,
    worse_dataset,
):
    deteriotation_plot= generatePlot(
        worse_dataset[0],
        worse_dataset[1],
        1,
        0.1,
        PCC_worse_performance[0].item(),
        PCC_worse_performance[1].item(),
        slopeLinearRegression(worse_dataset[0], worse_dataset[1]),
        r2LinWorse, 
        r2ExpWorse
    )
    deteriotation_plot
    return (deteriotation_plot,)


@app.cell
def _(
    PCC_overall,
    generatePlot,
    np_x_general_reduction_http_req,
    np_y_general_reduction_exec,
    r2ExpOverall,
    r2LinOverall,
    slopeLinearRegression,
):
    general_tendency_plot = generatePlot(
        np_x_general_reduction_http_req,
        np_y_general_reduction_exec,
        1,
        0.1,
        PCC_overall[0].item(),
        PCC_overall[1].item(),
        slopeLinearRegression(np_x_general_reduction_http_req, np_y_general_reduction_exec),
        r2LinOverall, 
        r2ExpOverall
    )
    general_tendency_plot
    return (general_tendency_plot,)


@app.cell
def _(mo):
    mo.md(r"""# Artefact""")
    return


@app.cell
def _(artefact_path, json, pearsonrAnalysis):
    with open(artefact_path/ "stats.json", "w") as outfile:
        json_object = json.dumps(pearsonrAnalysis, indent=4)
        outfile.write(json_object)
    return


@app.cell
def _(artefact_path, improvement_plot):
    improvement_plot.savefig(artefact_path / "http_req_exec_time_cor_better.svg", format="svg")
    improvement_plot.savefig(artefact_path / "http_req_exec_time_cor_better.eps", format="eps")
    return


@app.cell
def _(artefact_path, deteriotation_plot):
    deteriotation_plot.savefig(artefact_path / "http_req_exec_time_cor_worse.svg", format="svg")
    deteriotation_plot.savefig(artefact_path / "http_req_exec_time_cor_worse.eps", format="eps")
    return


@app.cell
def _(artefact_path, general_tendency_plot):
    general_tendency_plot.savefig(artefact_path / "http_req_exec_time_cor.svg", format="svg")
    general_tendency_plot.savefig(artefact_path / "http_req_exec_time_cor.eps", format="eps")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
