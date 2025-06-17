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
    from plotsVariation import generatePlot, generate_stats
    from pathlib import Path
    return (
        Line2D,
        Path,
        generateDatasetFromResults,
        generatePlot,
        generate_stats,
        mo,
        np,
        plt,
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
    mo.md(r"""# Reduction by query templates figure""")
    return


@app.cell
def _(
    generate_stats,
    shapeIndexDataset,
    shapeIndexInnerDataset,
    shapeIndexMinimalDataset,
):
    instances = [shapeIndexInnerDataset, shapeIndexMinimalDataset]

    (result_object_means_http, result_object_http, result_object_means_time, result_object_time) = generate_stats(instances, shapeIndexDataset)
    return instances, result_object_http, result_object_time


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
    query_to_skip = ["D8", "S2", "S3", "S6"]
    return (query_to_skip,)


@app.cell
def _(Path):
    artefact_path = Path("artefact") / "variation_detail_shape"
    return (artefact_path,)


@app.cell
def _(color_map, generatePlot, instances, query_to_skip, result_object_time):
    time_figure = generatePlot(
        result_object_time,
        'ratio execution time',
        len(instances),
        color_map=color_map,
        query_to_skip=query_to_skip,
    )

    time_figure
    return (time_figure,)


@app.cell
def _(artefact_path, time_figure):
    time_figure.savefig(artefact_path / "reduction_query_execution_time.svg", format="svg")
    time_figure.savefig(artefact_path / "reduction_query_execution_time.eps", format="eps")
    return


@app.cell
def _(color_map, generatePlot, instances, query_to_skip, result_object_http):
    http_req_fig = generatePlot(
        result_object_http,
        'ratio HTTP request',
        len(instances),
        color_map=color_map,
        query_to_skip=query_to_skip,
        ylim=16
    )
    http_req_fig
    return (http_req_fig,)


@app.cell
def _(artefact_path, http_req_fig):
    http_req_fig.savefig(artefact_path / "reduction_number_HTTP_requests.svg", format="svg")
    http_req_fig.savefig(artefact_path / "reduction_number_HTTP_requests.eps", format="eps")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
