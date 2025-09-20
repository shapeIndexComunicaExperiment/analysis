import marimo

__generated_with = "0.14.11"
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
    from plotsVariation import generate_stats, generatePlot
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
    import matplotlib.patches as patches
    import matplotlib
    import matplotlib.patches as mpatches
    return (
        Line2D,
        Path,
        generateDatasetFromResults,
        generatePlot,
        generate_stats,
        mo,
        mpatches,
        np,
        plt,
    )


@app.cell
def _():
    #plt.rcParams['hatch.linewidth'] = 1
    return


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


@app.cell
def _(ldpDataset, shapeIndexDataset, typeIndexLdpDataset):
    evalInstances = [shapeIndexDataset, ldpDataset, typeIndexLdpDataset]
    return (evalInstances,)


@app.cell
def _():
    color_map = {'shape index': '#1A85FF', 'ldp': '#D41159', 'type index and ldp': '#004D40'}
    pattern_map = {'shape index': '++', 'ldp': '//', 'type index and ldp': '..'}
    return color_map, pattern_map


@app.cell
def _(Path):
    artefactFolder = Path("./artefact/variation_approach")
    return (artefactFolder,)


@app.cell
def _(Line2D, evalInstances, mpatches, np, plt):
    def colorViolon(part, color, pattern=None):
        for pc in part['bodies']:
            pc.set_color(color)
            pc.set_edgecolor(color)
            pc.set_alpha(0.75)
            if pattern:
                pc.set_hatch(pattern)
                pc.set_edgecolor((0, 0, 0, 1))
        part['cmeans'].set_color('black')
        part['cmins'].set_color('black')
        part['cmaxes'].set_color('black')
        part['cbars'].set_color('black')
        part['cmedians'].set_color('black')

    def plotOneQueryExecutionTime(instances, queryName, color_map, pattern_map):
        query_map = {'interactive-discover-1': 'D1', 'interactive-discover-2': 'D2', 'interactive-discover-3': 'D3', 'interactive-discover-4': 'D4', 'interactive-discover-5': 'D5', 'interactive-discover-6': 'D6', 'interactive-discover-7': 'D7', 'interactive-discover-8': 'D8', 'interactive-short-1': 'S1', 'interactive-short-2': 'S2', 'interactive-short-3': 'S3', 'interactive-short-4': 'S4', 'interactive-short-5': 'S5', 'interactive-short-6': 'S6', 'interactive-short-7': 'S7'}

        # Define patterns mapped to color_map keys (using global color_map)

        indexes = np.linspace(0, 0.25, 5)
        width = 0.05
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xticks(indexes)
        ax.set_xticklabels(['{}V{}'.format(query_map[queryName], i+1) for i, v in enumerate(indexes)])
        violon_plots = {}

        for idx, _instance in enumerate(evalInstances):
            # Filter out None data and keep track of positions
            plot_data = []
            plot_positions = []
            timeout_positions = []

            for i, (label, data) in enumerate(_instance.executionTime[queryName].items()):
                if data is not None:
                    plot_data.append(data)
                    plot_positions.append(indexes[i])
                else:
                    timeout_positions.append(indexes[i])

            # Only create violin plot if we have data
            if plot_data:
                current_plot = ax.violinplot(plot_data, plot_positions, widths=width, showmeans=True, showmedians=True)
                violon_plots[_instance.name] = current_plot

            # Add timeout markers at y=0
            for pos in timeout_positions:
                ax.scatter(pos, 0, color=color_map[_instance.name], marker='X', s=150, alpha=0.8, edgecolors='black', linewidths=2)

        ax.set_xlabel('Query')
        ax.set_ylabel('Execution time (ms)')
        ax.grid(axis='y')
        legend_elements = []
        for label, plot in violon_plots.items():
            color = color_map[label]
            pattern = pattern_map[label]  # Use pattern_map based on instance name
            colorViolon(plot, color, pattern)

            # Create legend patch with pattern
            legend_patch = mpatches.Patch(facecolor=color, hatch=pattern, alpha=1, 
                                            edgecolor='black', linewidth=2, label=label)
            legend_elements.append(legend_patch)

        # Add timeout legend
        legend_elements.append(Line2D([0], [0], marker='X', color='black', linestyle='None', markersize=10, label='Timeout'))

        for text in fig.findobj(match=plt.Text):
            text.set_fontsize(25)

        ax.legend(handles=legend_elements, fontsize="18")
        return fig
    return (plotOneQueryExecutionTime,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Single plots""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Discover""")
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    d1_Plot = plotOneQueryExecutionTime(evalInstances,"interactive-discover-1", color_map, pattern_map)

    d1_Plot.savefig(artefactFolder/ "d1_violon_plots.svg", format="svg")
    d1_Plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    d2_Plot = plotOneQueryExecutionTime(evalInstances,"interactive-discover-2", color_map, pattern_map)

    d2_Plot.savefig(artefactFolder/ "d2_violon_plots.svg", format="svg")
    d2_Plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    d3_Plot = plotOneQueryExecutionTime(evalInstances,"interactive-discover-3", color_map, pattern_map)

    d3_Plot.savefig(artefactFolder/ "d3_violon_plots.svg", format="svg")
    d3_Plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    d4_Plot = plotOneQueryExecutionTime(evalInstances,"interactive-discover-4", color_map, pattern_map)

    d4_Plot.savefig(artefactFolder/ "d4_violon_plots.svg", format="svg")
    d4_Plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    d5_Plot = plotOneQueryExecutionTime(evalInstances,"interactive-discover-5", color_map, pattern_map)

    d5_Plot.savefig(artefactFolder/ "d5_violon_plots.svg", format="svg")
    d5_Plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    d6_Plot = plotOneQueryExecutionTime(evalInstances,"interactive-discover-6", color_map, pattern_map)

    d6_Plot.savefig(artefactFolder/ "d6_violon_plots.svg", format="svg")
    d6_Plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    d7_Plot = plotOneQueryExecutionTime(evalInstances,"interactive-discover-7", color_map, pattern_map)

    d7_Plot.savefig(artefactFolder/ "d7_violon_plots.svg", format="svg")
    d7_Plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    d8_Plot = plotOneQueryExecutionTime(evalInstances,"interactive-discover-8", color_map, pattern_map)

    d8_Plot.savefig(artefactFolder/ "d8_violon_plots.svg", format="svg")
    d8_Plot
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Short""")
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    s1_plot = plotOneQueryExecutionTime(evalInstances,"interactive-short-1", color_map, pattern_map)

    s1_plot.savefig(artefactFolder/ "s1_violon_plots.svg", format="svg")
    s1_plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    s2_plot = plotOneQueryExecutionTime(evalInstances,"interactive-short-2", color_map, pattern_map)

    s2_plot.savefig(artefactFolder/ "s2_violon_plots.svg", format="svg")
    s2_plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    s3_plot = plotOneQueryExecutionTime(evalInstances,"interactive-short-3", color_map, pattern_map)

    s3_plot.savefig(artefactFolder/ "s3_violon_plots.svg", format="svg")
    s3_plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    s4_plot = plotOneQueryExecutionTime(evalInstances,"interactive-short-4", color_map, pattern_map)

    s4_plot.savefig(artefactFolder/ "s4_violon_plots.svg", format="svg")
    s4_plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    s5_plot = plotOneQueryExecutionTime(evalInstances,"interactive-short-5", color_map, pattern_map)

    s5_plot.savefig(artefactFolder/ "s5_violon_plots.svg", format="svg")
    s5_plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    s6_plot = plotOneQueryExecutionTime(evalInstances,"interactive-short-6", color_map, pattern_map)

    s6_plot.savefig(artefactFolder/ "s6_violon_plots.svg", format="svg")
    s6_plot
    return


@app.cell
def _(
    artefactFolder,
    color_map,
    evalInstances,
    pattern_map,
    plotOneQueryExecutionTime,
):
    s7_plot = plotOneQueryExecutionTime(evalInstances,"interactive-short-7", color_map, pattern_map)

    s7_plot.savefig(artefactFolder/ "s7_violon_plots.svg", format="svg")
    s7_plot
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Reduction by query templates""")
    return


@app.cell
def _(ldpDataset, shapeIndexDataset):
    instances = [shapeIndexDataset, ldpDataset]
    return (instances,)


@app.cell
def _(generate_stats, instances, typeIndexLdpDataset):
    (result_object_means_http, result_object_http, result_object_means_time, result_object_time) = generate_stats(instances, typeIndexLdpDataset)
    return result_object_http, result_object_time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Reduction by query templates figure""")
    return


@app.cell
def _():
    query_to_skip = ["D8", "S2", "S3", "S6", "S7" ]
    return (query_to_skip,)


@app.cell
def _(color_map, generatePlot, instances, query_to_skip, result_object_time):
    exec_time_plot = generatePlot(
        result_object_time,
        'ratio execution time',
        len(instances),
        color_map=color_map,
        ylim=None,
        query_to_skip=query_to_skip,

    )
    exec_time_plot
    return (exec_time_plot,)


@app.cell
def _(artefactFolder, exec_time_plot):
    exec_time_plot.savefig(artefactFolder/ "reduction_query_execution_time.svg", format="svg")

    exec_time_plot.savefig(artefactFolder/ "reduction_query_execution_time.eps", format="eps")
    return


@app.cell
def _(color_map, generatePlot, instances, query_to_skip, result_object_http):
    http_req_plot = generatePlot(
        result_object_http,
        'ratio HTTP request',
        len(instances),
        color_map=color_map,
        query_to_skip=query_to_skip,
        ylim=None,
        formatYAxis = '{:.2f}'
    )
    http_req_plot
    return (http_req_plot,)


@app.cell
def _(artefactFolder, http_req_plot):
    http_req_plot.savefig(artefactFolder/ "reduction_number_HTTP_requests.svg", format="svg")

    http_req_plot.savefig(artefactFolder/ "reduction_number_HTTP_requests.eps", format="eps")
    return


if __name__ == "__main__":
    app.run()
