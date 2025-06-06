import marimo

__generated_with = "0.13.15"
app = marimo.App()


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
    import numpy as np
    from matplotlib.ticker import MultipleLocator
    from scipy.optimize import curve_fit
    from scipy.stats import pearsonr
    return (
        MultipleLocator,
        calculatePercentageReductionSeries,
        generateDatasetFromResults,
        np,
        pearsonr,
        plt,
    )


@app.cell
def _(generateDatasetFromResults):
    typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
    typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
    typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "typeIndexLdp")
    return (typeIndexLdpDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shapeIndex")
    return (shapeIndexDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndex20PathResult = "./results/shape-index-20-percent/shape_index_result.json"
    shapeIndex20PathSummary = "./results/shape-index-20-percent/summary_shape_index_result.json"
    shapeIndex20Dataset = generateDatasetFromResults(shapeIndex20PathResult, shapeIndex20PathSummary, "shapeIndex20Percent")
    return (shapeIndex20Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndex50PathResult = "./results/shape-index-50-percent/shape_index_result.json"
    shapeIndex50PathSummary = "./results/shape-index-50-percent/summary_shape_index_result.json"
    shapeIndex50Dataset = generateDatasetFromResults(shapeIndex50PathResult, shapeIndex50PathSummary, "shapeIndex50Percent")
    return (shapeIndex50Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndex80PathResult = "./results/shape-index-80-percent/shape_index_result.json"
    shapeIndex80PathSummary = "./results/shape-index-80-percent/summary_shape_index_result.json"
    shapeIndex80Dataset = generateDatasetFromResults(shapeIndex80PathResult, shapeIndex80PathSummary, "shapeIndex80Percent")
    return (shapeIndex80Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexInnerPathResult = "./results/shape-inner/shape_index_result.json"
    shapeIndexInnerPathSummary = "./results/shape-inner/summary_shape_index_result.json"
    shapeIndexInnerDataset = generateDatasetFromResults(shapeIndexInnerPathResult, shapeIndexInnerPathSummary, "shapeInner")
    return (shapeIndexInnerDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexMinimalPathResult = "./results/shape-minimal/shape_index_result.json"
    shapeIndexMinimalPathSummary = "./results/shape-minimal/summary_shape_index_result.json"
    shapeIndexMinimalDataset = generateDatasetFromResults(shapeIndexMinimalPathResult, shapeIndexMinimalPathSummary, "shapeMinimal")
    return (shapeIndexMinimalDataset,)


@app.cell
def _(
    shapeIndex20Dataset,
    shapeIndex50Dataset,
    shapeIndex80Dataset,
    shapeIndexDataset,
    shapeIndexInnerDataset,
    shapeIndexMinimalDataset,
):
    evalInstances = [shapeIndexDataset, shapeIndex20Dataset, shapeIndex50Dataset, shapeIndex80Dataset, shapeIndexInnerDataset, shapeIndexMinimalDataset]
    return (evalInstances,)


@app.function
def aggregateReduction(reductionDataset, globalAggregation, aggregationByQuery):
    for query, versions in reductionDataset.items():
        if query not in aggregationByQuery:
            aggregationByQuery[query] = []
        for i, reduction in enumerate(versions):
            if reduction is not None:
                globalAggregation.append(reduction)
                aggregationByQuery[query].append(reduction)


@app.cell
def _(calculatePercentageReductionSeries, evalInstances, typeIndexLdpDataset):
    generalReductionHttpRequest = []
    generalReductionExec = []

    reductionHttpRequestByQuery = {}
    reductionExecRequestByQuery = {}

    for instance in evalInstances:
        currentReductionHttpRequest = calculatePercentageReductionSeries(instance.numberHttpRequest, typeIndexLdpDataset.numberHttpRequest)
        currentReductionExec = calculatePercentageReductionSeries(instance.meanExecutionTime, typeIndexLdpDataset.meanExecutionTime)

        aggregateReduction(currentReductionHttpRequest, generalReductionHttpRequest, reductionHttpRequestByQuery)
        aggregateReduction(currentReductionExec, generalReductionExec, reductionExecRequestByQuery)
    return (
        generalReductionExec,
        generalReductionHttpRequest,
        reductionExecRequestByQuery,
        reductionHttpRequestByQuery,
    )


@app.cell
def _(
    MultipleLocator,
    generalReductionExec,
    generalReductionHttpRequest,
    np,
    plt,
    reductionExecRequestByQuery,
    reductionHttpRequestByQuery,
):
    x = np.array(generalReductionHttpRequest)
    y = np.array(generalReductionExec)
    _indexes = np.linspace(-1500, 100, 10)
    _fig, _ax = plt.subplots(figsize=(8, 6))
    _ax.xaxis.set_major_locator(MultipleLocator(1))
    _ax.yaxis.set_major_locator(MultipleLocator(0.2))
    for template, val in reductionExecRequestByQuery.items():
        x = np.array(reductionHttpRequestByQuery[template])
        y = np.array(val)
        _ax.scatter(x, y, label=template)
    plt.legend()
    return


@app.cell
def _(
    MultipleLocator,
    generalReductionExec,
    generalReductionHttpRequest,
    np,
    plt,
):
    x_1 = np.array(generalReductionHttpRequest)
    y_1 = np.array(generalReductionExec)
    b, a = np.polyfit(x_1, y_1, deg=1)
    _indexes = np.linspace(-1500, 100, 10)
    _fig, _ax = plt.subplots(figsize=(8, 6))
    _ax.xaxis.set_major_locator(MultipleLocator(1))
    _ax.yaxis.set_major_locator(MultipleLocator(0.2))
    _ax.scatter(x_1, y_1)
    return x_1, y_1


@app.function
def dividePoints(x, y, threshold):
    x_right = []
    y_right = []

    x_left = []
    y_left = []

    for i, val in enumerate(x):
        if val>threshold:
            x_right.append(val)
            y_right.append(y[i])
        else:
            x_left.append(val)
            y_left.append(y[i])
    return ((x_right, y_right), (x_left,y_left))


@app.cell
def _(pearsonr, x_1, y_1):
    _corr, _ = pearsonr(x_1, y_1)
    print('Pearson Correlation Coefficient:', _corr)
    return


@app.cell
def _(generalReductionExec, generalReductionHttpRequest, np):
    x_2 = np.array(generalReductionHttpRequest)
    y_2 = np.array(generalReductionExec)
    (x_right, y_right), (x_left, y_left) = dividePoints(x_2, y_2, 1)
    return x_left, x_right, y_left, y_right


@app.cell
def _(MultipleLocator, plt, x_right, y_right):
    _fig, _ax = plt.subplots()
    _ax.grid(axis='both')
    _s = 20
    _ax.scatter(x_right, y_right, s=_s)
    _ax.xaxis.set_major_locator(MultipleLocator(1))
    _ax.yaxis.set_major_locator(MultipleLocator(0.5))
    _ax.tick_params(axis='x', rotation=20)
    _ax.set_xlabel('ratio HTTP request')
    _ax.set_ylabel('ratio execution time')
    plt.show()
    return


@app.cell
def _(pearsonr, x_right, y_right):
    _corr, _ = pearsonr(x_right, y_right)
    print('Pearson Correlation Coefficient:', _corr)
    return


@app.cell
def _(MultipleLocator, plt, x_left, y_left):
    _fig, _ax = plt.subplots()
    _ax.grid(axis='both')
    _s = 20
    _ax.scatter(x_left, y_left, s=_s)
    _ax.xaxis.set_major_locator(MultipleLocator(0.1))
    _ax.yaxis.set_major_locator(MultipleLocator(0.5))
    _ax.tick_params(axis='x', rotation=20)
    _ax.set_xlabel('ratio HTTP request')
    _ax.set_ylabel('ratio execution time')
    plt.show()
    return


@app.cell
def _(pearsonr, x_left, y_left):
    _corr, _ = pearsonr(x_left, y_left)
    print('Pearson Correlation Coefficient:', _corr)
    return


if __name__ == "__main__":
    app.run()
