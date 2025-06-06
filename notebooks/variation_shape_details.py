import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import json
    from texttable import Texttable
    import latextable
    from tabulate import tabulate
    import sys
    file_directory = "./"
    sys.path.append(file_directory)
    from generateDataset import generateDatasetFromResults
    from metric import internalResultConsistency, calculatePercentageReductionSeries
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.ticker import MultipleLocator
    from scipy.optimize import curve_fit
    from scipy.stats import pearsonr
    from matplotlib.ticker import FormatStrFormatter
    from matplotlib.lines import Line2D
    import statistics
    return (
        Line2D,
        MultipleLocator,
        calculatePercentageReductionSeries,
        generateDatasetFromResults,
        mo,
        np,
        plt,
        statistics,
    )


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "Full shape model")
    return (shapeIndexDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexInnerPathResult = "./results/shape-inner/shape_index_result.json"
    shapeIndexInnerPathSummary = "./results/shape-inner/summary_shape_index_result.json"
    shapeIndexInnerDataset = generateDatasetFromResults(shapeIndexInnerPathResult, shapeIndexInnerPathSummary, "Dataset shape model")
    return (shapeIndexInnerDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexMinimalPathResult = "./results/shape-minimal/shape_index_result.json"
    shapeIndexMinimalPathSummary = "./results/shape-minimal/summary_shape_index_result.json"
    shapeIndexMinimalDataset = generateDatasetFromResults(shapeIndexMinimalPathResult, shapeIndexMinimalPathSummary, "Minimal model")
    return (shapeIndexMinimalDataset,)


@app.cell
def _(shapeIndexDataset, shapeIndexInnerDataset, shapeIndexMinimalDataset):
    evalInstances = [shapeIndexDataset, shapeIndexInnerDataset, shapeIndexMinimalDataset]
    return (evalInstances,)


@app.cell
def _(Line2D, evalInstances, mo, np, plt):
    def colorViolon(part, color):
        for pc in part['bodies']:
            pc.set_color(color)
            pc.set_edgecolor(color)
            pc.set_edgecolor(color)
            pc.set_alpha(0.75)
        part['cmeans'].set_color('black')
        part['cmins'].set_color('black')
        part['cmaxes'].set_color('black')
        part['cbars'].set_color('black')
        part['cmedians'].set_color('black')
    color_map = {'Full shape model': '#1A85FF', 'Dataset shape model': '#D41159', 'Minimal model': '#004D40'}

    def plotOneQueryExecutionTime(instances, queryName, color_map):
        query_map = {'interactive-discover-1': 'D1', 'interactive-discover-2': 'D2', 'interactive-discover-3': 'D3', 'interactive-discover-4': 'D4', 'interactive-discover-5': 'D5', 'interactive-discover-6': 'D6', 'interactive-discover-7': 'D7', 'interactive-discover-8': 'D8', 'interactive-short-1': 'S1', 'interactive-short-2': 'S2', 'interactive-short-3': 'S3', 'interactive-short-4': 'S4', 'interactive-short-5': 'S5', 'interactive-short-6': 'S6', 'interactive-short-7': 'S7'}
        indexes = np.linspace(0, 0.25, 5)
        width = 0.05
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xticks(indexes)
        ax.set_xticklabels(['{}V{}'.format(query_map[queryName], i) for i, v in enumerate(indexes)])
        violon_plots = {}
        for _instance in evalInstances:
            all_data = [data if data is not None else [0, 0, 0, 0, 0] for label, data in _instance.executionTime[queryName].items()]
            current_plot = ax.violinplot(all_data, indexes, widths=width, showmeans=True, showmedians=True)
            violon_plots[_instance.name] = current_plot
        ax.set_xlabel('Query')
        ax.set_ylabel('Execution time (ms)')
        ax.grid(axis='both')
        legend_elements = []
        for label, plot in violon_plots.items():
            color = color_map[label]
            colorViolon(plot, color)
            legend_elements.append(Line2D([0], [0], color=color, label=label))
        ax.legend(handles=legend_elements)

        mo.mpl.interactive(ax)
        return fig
    return color_map, plotOneQueryExecutionTime


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Single plots""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Discover""")
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-discover-1", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-discover-2", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-discover-3", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-discover-4", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-discover-5", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-discover-6", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-discover-7", color_map)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Short""")
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-short-1", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-short-2", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-short-3", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-short-4", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-short-5", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-short-6", color_map)
    return


@app.cell
def _(color_map, evalInstances, plotOneQueryExecutionTime):
    plotOneQueryExecutionTime(evalInstances,"interactive-short-7", color_map)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Reduction by query templates""")
    return


@app.cell
def _(np, statistics):
    def statisticTemplateMetric(serie):
        stat = {}
        for query_template, val in serie.items():
            clean_list = list(filter(lambda a: a != None, val))
            avg = np.nan
            std = np.nan
            min_val = np.nan
            max_val = np.nan
            if len(clean_list) !=0:
                avg = statistics.mean(clean_list)
                if len(clean_list) > 2:
                    std = statistics.stdev(clean_list)
                min_val = min(clean_list)
                max_val = max(clean_list)
            stat[query_template] = {
                "avg": avg,
                "std": std,
                "min":min_val,
                "max": max_val,
                "raw": list(map(lambda x: x if x != None else 0, val))
            }
        return stat
    return (statisticTemplateMetric,)


@app.cell
def _():
    result_object = {}
    return (result_object,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    result_object,
    shapeIndexDataset,
    shapeIndexInnerDataset,
    shapeIndexMinimalDataset,
    statisticTemplateMetric,
):
    instances = [shapeIndexInnerDataset, shapeIndexMinimalDataset]
    for _instance in instances:
        reduction_http_req = calculatePercentageReductionSeries(_instance.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
        reduction_time = calculatePercentageReductionSeries(_instance.meanExecutionTime, shapeIndexDataset.meanExecutionTime)
        stat_http_req = statisticTemplateMetric(reduction_http_req)
        stat_time = statisticTemplateMetric(reduction_time)
        result_object[_instance.name] = {'http_request': stat_http_req, 'time': stat_time}
    return (instances,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Reduction by query templates figure""")
    return


@app.cell
def _(result_object):
    result_object_means_http = {}
    result_object_http = {}
    result_object_means_time = {}
    result_object_time = {}
    for _instance, results in result_object.items():
        result_object_means_http[_instance] = []
        result_object_means_time[_instance] = []
        result_object_http[_instance] = []
        result_object_time[_instance] = []
        for key, values in results.items():
            if key == 'time':
                for value in values.values():
                    result_object_means_time[_instance].append(value['avg'])
                    result_object_time[_instance].append(value['raw'])
            if key == 'http_request':
                for value in values.values():
                    result_object_means_http[_instance].append(value['avg'])
                    result_object_http[_instance].append(value['raw'])
    return result_object_http, result_object_time


@app.cell
def _():
    query_map = {
            "interactive-discover-1": "D1",
            "interactive-discover-2": "D2",
            "interactive-discover-3": "D3",
            "interactive-discover-4": "D4",
            "interactive-discover-5": "D5",
            "interactive-discover-6": "D6",
            "interactive-discover-7": "D7",
            "interactive-discover-8": "D8",
            "interactive-short-1": "S1",
            "interactive-short-2": "S2",
            "interactive-short-3": "S3",
            "interactive-short-4": "S4",
            "interactive-short-5": "S5",
            "interactive-short-6": "S6",
            "interactive-short-7": "S7"
        }

    queries = query_map.values()
    return (queries,)


@app.cell
def _(MultipleLocator, color_map, instances, mo, np, plt, queries):
    def generatePlot(results, yaxisLabel):

        x = np.arange(len(queries))
        width = 1/len(instances) -0.1 # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(figsize=(10, 8))

        for dataset, measurements in results.items():
            offset = width * multiplier + width/len(results)
            data = list(range(len(queries)))
            for i, measurement in enumerate(measurements):
                data[i] = measurement
            multiplier += 1
            ax.boxplot(data,
                       positions=x+offset,
                       widths=width,
                       patch_artist=True,
                       label=dataset,
                       boxprops=dict(facecolor=color_map[dataset]),
                      )
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.set_ylabel(yaxisLabel)
        ax.set_xticks(x + width, queries)
        ax.grid(axis="both")
        #ax.legend(fontsize="x-large")
        mo.mpl.interactive(ax)
    
        return fig
    return (generatePlot,)


@app.cell
def _(generatePlot, result_object_time):
    generatePlot(result_object_time,'ratio execution time')
    return


@app.cell
def _(generatePlot, result_object_http):
    generatePlot(result_object_http,'ratio HTTP request')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
