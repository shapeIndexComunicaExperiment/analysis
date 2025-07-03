import marimo

__generated_with = "0.13.15"
app = marimo.App(width="full")


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
    from pathlib import Path
    return Path, generateDatasetFromResults, mo, np, plt, statistics


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index")
    return (shapeIndexDataset,)


@app.cell
def _(generateDatasetFromResults):
    ldpPathResult = "./results/standard/ldp_result.json"
    ldpPathSummary = "./results/standard/summary_ldp_result.json"
    ldpDataset = generateDatasetFromResults(ldpPathResult, ldpPathSummary, "ldp")
    return (ldpDataset,)


@app.cell
def _(generateDatasetFromResults):
    typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
    typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
    typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "type index and ldp")
    return (typeIndexLdpDataset,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Reduction by query templates""")
    return


@app.cell
def _(Path):
    artefactFolder = Path("./artefact/variation_approach")
    return (artefactFolder,)


@app.cell
def _():
    color_map = {'shape index': '#1A85FF', 'ldp': '#D41159', 'type index and ldp': '#004D40'}
    return (color_map,)


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
                "raw": list(map(lambda x: x if x != None else np.nan, val))
            }
        return stat
    return (statisticTemplateMetric,)


@app.cell
def _():
    result_object = {}
    return (result_object,)


@app.cell
def _(
    ldpDataset,
    result_object,
    shapeIndexDataset,
    statisticTemplateMetric,
    typeIndexLdpDataset,
):
    instances = [shapeIndexDataset, ldpDataset, typeIndexLdpDataset]
    for _instance in instances:
        reduction_http_req = _instance.numberHttpRequest
        reduction_time = _instance.meanExecutionTime
        stat_http_req = statisticTemplateMetric(reduction_http_req)
        stat_time = statisticTemplateMetric(reduction_time)
        result_object[_instance.name] = {'http_request': stat_http_req, 'time': stat_time}
    return (instances,)


@app.cell
def _(result_object):
    result_object
    return


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
    result_object_raw_time = {}
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
    query_to_skip = ["D8", "S2", "S3", "S6", "S7" ]
    queries = list(query_map.values())
    indexes_to_skip = []
    return (queries,)


@app.cell
def _(result_object_time):
    result_object_time
    return


@app.cell
def _(color_map, instances, np, plt, queries):
    def generatePlot(results, yaxisLabel):
        fontSize=20
        x = np.arange(len(queries))
        width = 1/len(instances) -0.1 # the width of the bars
        multiplier = 0
    
        fig, ax = plt.subplots(figsize=(10, 10))

    
        for text in fig.findobj(match=plt.Text):
            text.set_fontsize(fontSize)
        
        for dataset, measurements in results.items():
            offset = width * multiplier + width/len(results)
            data = list(range(len(queries)))
            rewind = 0
            for i, measurement in enumerate(measurements): 
                """
                all_nan = all(np.isnan(el) for el in measurement)
                if all_nan:
                    rewind+=1
                    continue
                """
                #print(f"len {len(data)}, i {i-rewind}")
                data[i-rewind] = list(filter(lambda x: not np.isnan(x), measurement))
            multiplier += 1
            ax.boxplot(data,
                       positions=x+offset,
                       widths=width,
                       patch_artist=True,
                       label=dataset,
                       boxprops=dict(facecolor=color_map[dataset]),
                      )
        #ax.set_yscale('log', base=2)
        #ax.axhline(1, color='gray', linestyle='--', label='No performance change')
        ax.set_ylabel(yaxisLabel)
        ax.set_xticks(x + width, queries)
        ax.grid(axis="both")
        ax.set_xlabel("query template")
        ax.legend()
        return fig
    return (generatePlot,)


@app.cell
def _(generatePlot, result_object_time):
    exec_time_plot = generatePlot(result_object_time,'query execution time (ms)')
    exec_time_plot
    return (exec_time_plot,)


@app.cell
def _(artefactFolder, exec_time_plot):
    exec_time_plot.savefig(artefactFolder/ "reduction_query_execution_time_raw.svg", format="svg")

    exec_time_plot.savefig(artefactFolder/ "reduction_query_execution_time_raw.eps", format="eps")

    return


@app.cell
def _(generatePlot, result_object_http):
    http_req_plot = generatePlot(result_object_http,'Number HTTP request')
    http_req_plot
    return (http_req_plot,)


@app.cell
def _(artefactFolder, http_req_plot):
    http_req_plot.savefig(artefactFolder/ "reduction_number_HTTP_requests_raw.svg", format="svg")

    http_req_plot.savefig(artefactFolder/ "reduction_number_HTTP_requests_raw.eps", format="eps")
    return


if __name__ == "__main__":
    app.run()
