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
    from metric import statisticalSignificanceByTemplate
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.ticker import MultipleLocator
    from scipy.optimize import curve_fit
    from scipy.stats import pearsonr
    from matplotlib.ticker import FormatStrFormatter
    from matplotlib.lines import Line2D
    import statistics
    from pathlib import Path
    from plotsVariation import calculatePercentageReductionSeries, statisticTemplateMetric
    return (
        Path,
        Texttable,
        calculatePercentageReductionSeries,
        generateDatasetFromResults,
        latextable,
        np,
        statisticTemplateMetric,
        statisticalSignificanceByTemplate,
        tabulate,
    )


@app.cell
def _(Path):
    artefactFolder = Path("./artefact/statistical_significance")
    return (artefactFolder,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Datasets""")
    return


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index")
    return (shapeIndexDataset,)


@app.cell
def _(generateDatasetFromResults):
    typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
    typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
    typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "type index and ldp")
    return (typeIndexLdpDataset,)


@app.cell
def _(generateDatasetFromResults):
    _shapeIndex20PathResult = './results/shape-entry-20-percent/shape_index_result.json'
    _shapeIndex20PathSummary = './results/shape-entry-20-percent/summary_shape_index_result.json'
    shapeIndex20Dataset = generateDatasetFromResults(_shapeIndex20PathResult, _shapeIndex20PathSummary, 'shape index entries 20%')
    return (shapeIndex20Dataset,)


@app.cell
def _(generateDatasetFromResults):
    _shapeIndex50PathResult = './results/shape-entry-50-percent/shape_index_result.json'
    _shapeIndex50PathSummary = './results/shape-entry-50-percent/summary_shape_index_result.json'
    shapeIndex50Dataset = generateDatasetFromResults(_shapeIndex50PathResult, _shapeIndex50PathSummary, 'shape index entries 50%')
    return (shapeIndex50Dataset,)


@app.cell
def _(generateDatasetFromResults):
    _shapeIndex80PathResult = './results/shape-entry-80-percent/shape_index_result.json'
    _shapeIndex80PathSummary = './results/shape-entry-80-percent/summary_shape_index_result.json'
    shapeIndex80Dataset = generateDatasetFromResults(_shapeIndex80PathResult, _shapeIndex80PathSummary, 'shape index entries 80%')
    return (shapeIndex80Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndex0PathResult = "./results/shape-index-0-percent/shape_index_result.json"
    shapeIndex0PathSummary = "./results/shape-index-0-percent/summary_shape_index_result.json"
    shapeIndex0NetworkDataset = generateDatasetFromResults(shapeIndex0PathResult, shapeIndex0PathSummary, "shape index network 0%")
    return (shapeIndex0NetworkDataset,)


@app.cell
def _(generateDatasetFromResults):
    _shapeIndex20PathResult = './results/shape-index-20-percent/shape_index_result.json'
    _shapeIndex20PathSummary = './results/shape-index-20-percent/summary_shape_index_result.json'
    shapeIndex20NetworkDataset = generateDatasetFromResults(_shapeIndex20PathResult, _shapeIndex20PathSummary, 'shape index network 20%')
    return (shapeIndex20NetworkDataset,)


@app.cell
def _(generateDatasetFromResults):
    _shapeIndex50PathResult = './results/shape-index-50-percent/shape_index_result.json'
    _shapeIndex50PathSummary = './results/shape-index-50-percent/summary_shape_index_result.json'
    shapeIndex50NetworkDataset = generateDatasetFromResults(_shapeIndex50PathResult, _shapeIndex50PathSummary, 'shape index network 50%')
    return (shapeIndex50NetworkDataset,)


@app.cell
def _(generateDatasetFromResults):
    _shapeIndex80PathResult = './results/shape-index-80-percent/shape_index_result.json'
    _shapeIndex80PathSummary = './results/shape-index-80-percent/summary_shape_index_result.json'
    shapeIndex80NetworkDataset = generateDatasetFromResults(_shapeIndex80PathResult, _shapeIndex80PathSummary, 'shape index network 80%')
    return (shapeIndex80NetworkDataset,)


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Statistical significance""")
    return


@app.cell
def _():
    head = ["query template", "relation execution time", "p-value", "average ratio HTTP request"]
    return (head,)


@app.cell
def _():
    query_label_mapping = {
        "interactive-discover-1":"D1",
        "interactive-discover-2": "D2",
        "interactive-discover-3": "D3",
        "interactive-discover-4": "D4",
        "interactive-discover-5": "D5" ,
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

    return (query_label_mapping,)


@app.cell
def _(np, query_label_mapping):
    def generateTableInfo(results, stat_http_req):  
        rows = []
        p_value_significant = 0.05
        for query_template, value in results.items():
            relation  = "-"
            p_value= "-"
            ratio_Http_Req = "-"
            if value["greater"] is not None:
                if value["different"] > p_value_significant:
                    relation = "similar"
                    p_value = f"{value["greater"]:.2E} (RH)"
                elif value["greater"] < p_value_significant:
                    relation = "greater"
                    p_value = f"{value["greater"]:.2E}"
                elif value["lesser"] < p_value_significant:
                    relation = "lesser"
                    p_value = f"{value["lesser"]:.2E}"
            if relation == "-":
                continue
            avg_http_req = stat_http_req[query_template]['avg']
            if not np.isnan(avg_http_req):
                ratio_Http_Req = f"{float(avg_http_req):.2f}"
            row = [
                query_label_mapping[query_template],
                relation,
                p_value,
                ratio_Http_Req
                  ]
            rows.append(row)
        return rows
    return (generateTableInfo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Shape index vs the state of the art""")
    return


@app.cell
def _():
    results = {}
    return (results,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results,
    shapeIndexDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
    typeIndexLdpDataset,
):
    for _template, _execution_times in shapeIndexDataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, typeIndexLdpDataset.executionTime[_template])
        results[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndexDataset.numberHttpRequest, typeIndexLdpDataset.numberHttpRequest)
    stat_http_req = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req,)


@app.cell
def _(generateTableInfo, results, stat_http_req):
    rows = generateTableInfo(results, stat_http_req)
    return (rows,)


@app.cell
def _(head, rows, tabulate):
    print(tabulate(rows, headers=head, tablefmt="github"))
    return


@app.cell
def _(Texttable, head, latextable, rows):
    textTable = Texttable()
    textTable.set_cols_dtype(['t', 't', 't', 't'])
    textTable.add_rows([head]+ rows)
    label = "tab:statSignificanceStateOfTheArt"
    caption = "Table comparing the shape index approach to the state-of-the-art. RH, indicate that the p-value is associated to the rejected hypothesis. Every query performs better or similarly to the state-of-the-art with the shape index approach except for interactive-short-4."

    latex_table_state_of_the_art = latextable.draw_latex(textTable, caption=caption, label=label)

    return (latex_table_state_of_the_art,)


@app.cell
def _(artefactFolder, latex_table_state_of_the_art):
    with open(artefactFolder / "comparaisonStateOfTheArt.tex", "w") as outfile:
        outfile.write(latex_table_state_of_the_art)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## shape index 20 percent entries vs shape index""")
    return


@app.cell
def _():
    results_1 = {}
    return (results_1,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results_1,
    shapeIndex20Dataset,
    shapeIndexDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
):
    for _template, _execution_times in shapeIndex20Dataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, shapeIndexDataset.executionTime[_template])
        results_1[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndex20Dataset.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req_1 = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req_1,)


@app.cell
def _(generateTableInfo, results_1, stat_http_req_1):
    rows_1 = generateTableInfo(results_1, stat_http_req_1)
    return (rows_1,)


@app.cell
def _(head, rows_1, tabulate):
    print(tabulate(rows_1, headers=head, tablefmt='github'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## shape index 50 percent entries vs shape index""")
    return


@app.cell
def _():
    results_2 = {}
    return (results_2,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results_2,
    shapeIndex50Dataset,
    shapeIndexDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
):
    for _template, _execution_times in shapeIndex50Dataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, shapeIndexDataset.executionTime[_template])
        results_2[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndex50Dataset.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req_2 = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req_2,)


@app.cell
def _(generateTableInfo, results_2, stat_http_req_2):
    rows_2 = generateTableInfo(results_2, stat_http_req_2)
    return (rows_2,)


@app.cell
def _(head, rows_2, tabulate):
    print(tabulate(rows_2, headers=head, tablefmt='github'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## shape index 80 percent entries vs shape index""")
    return


@app.cell
def _():
    results_3 = {}
    return (results_3,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results_3,
    shapeIndex80Dataset,
    shapeIndexDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
):
    for _template, _execution_times in shapeIndex80Dataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, shapeIndexDataset.executionTime[_template])
        results_3[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndex80Dataset.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req_3 = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req_3,)


@app.cell
def _(generateTableInfo, results_3, stat_http_req_3):
    rows_3 = generateTableInfo(results_3, stat_http_req_3)
    return (rows_3,)


@app.cell
def _(head, rows_3, tabulate):
    print(tabulate(rows_3, headers=head, tablefmt='github'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## shape index 0 percent network vs shape index""")
    return


@app.cell
def _():
    results_4 = {}
    return (results_4,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results_4,
    shapeIndex0NetworkDataset,
    shapeIndexDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
):
    for _template, _execution_times in shapeIndex0NetworkDataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, shapeIndexDataset.executionTime[_template])
        results_4[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndex0NetworkDataset.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req_4 = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req_4,)


@app.cell
def _(generateTableInfo, results_4, stat_http_req_4):
    rows_4 = generateTableInfo(results_4, stat_http_req_4)
    return (rows_4,)


@app.cell
def _(head, rows_4, tabulate):
    print(tabulate(rows_4, headers=head, tablefmt='github'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## shape index 20 percent network vs shape index""")
    return


@app.cell
def _():
    results_5 = {}
    return (results_5,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results_5,
    shapeIndex20NetworkDataset,
    shapeIndexDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
):
    for _template, _execution_times in shapeIndex20NetworkDataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, shapeIndexDataset.executionTime[_template])
        results_5[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndex20NetworkDataset.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req_5 = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req_5,)


@app.cell
def _(generateTableInfo, results_5, stat_http_req_5):
    rows_5 = generateTableInfo(results_5, stat_http_req_5)
    return (rows_5,)


@app.cell
def _(head, rows_5, tabulate):
    print(tabulate(rows_5, headers=head, tablefmt='github'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## shape index 50 percent network vs shape index""")
    return


@app.cell
def _():
    results_6 = {}
    return (results_6,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results_6,
    shapeIndex50NetworkDataset,
    shapeIndexDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
):
    for _template, _execution_times in shapeIndex50NetworkDataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, shapeIndexDataset.executionTime[_template])
        results_6[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndex50NetworkDataset.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req_6 = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req_6,)


@app.cell
def _(generateTableInfo, results_6, stat_http_req_6):
    rows_6 = generateTableInfo(results_6, stat_http_req_6)
    return (rows_6,)


@app.cell
def _(head, rows_6, tabulate):
    print(tabulate(rows_6, headers=head, tablefmt='github'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## shape index 80 percent network vs shape index""")
    return


@app.cell
def _():
    results_7 = {}
    return (results_7,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results_7,
    shapeIndex80NetworkDataset,
    shapeIndexDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
):
    for _template, _execution_times in shapeIndex80NetworkDataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, shapeIndexDataset.executionTime[_template])
        results_7[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndex80NetworkDataset.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req_7 = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req_7,)


@app.cell
def _(generateTableInfo, results_7, stat_http_req_7):
    rows_7 = generateTableInfo(results_7, stat_http_req_7)
    return (rows_7,)


@app.cell
def _(head, rows_7, tabulate):
    print(tabulate(rows_7, headers=head, tablefmt='github'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## shape index inner shapes vs shape index""")
    return


@app.cell
def _():
    results_8 = {}
    return (results_8,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results_8,
    shapeIndexDataset,
    shapeIndexInnerDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
):
    for _template, _execution_times in shapeIndexInnerDataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, shapeIndexDataset.executionTime[_template])
        results_8[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndexInnerDataset.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req_8 = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req_8,)


@app.cell
def _(generateTableInfo, results_8, stat_http_req_8):
    rows_8 = generateTableInfo(results_8, stat_http_req_8)
    return (rows_8,)


@app.cell
def _(head, rows_8, tabulate):
    print(tabulate(rows_8, headers=head, tablefmt='github'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## shape index minimal shapes vs shape index""")
    return


@app.cell
def _():
    results_9 = {}
    return (results_9,)


@app.cell
def _(
    calculatePercentageReductionSeries,
    results_9,
    shapeIndexDataset,
    shapeIndexMinimalDataset,
    statisticTemplateMetric,
    statisticalSignificanceByTemplate,
):
    for _template, _execution_times in shapeIndexMinimalDataset.executionTime.items():
        _p_value_greater, _p_value_different, _p_value_lesser = statisticalSignificanceByTemplate(_execution_times, shapeIndexDataset.executionTime[_template])
        results_9[_template] = {'greater': _p_value_greater, 'lesser': _p_value_lesser, 'different': _p_value_different}
    _reduction_http_req = calculatePercentageReductionSeries(shapeIndexMinimalDataset.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req_9 = statisticTemplateMetric(_reduction_http_req)
    return (stat_http_req_9,)


@app.cell
def _(generateTableInfo, results_9, stat_http_req_9):
    rows_9 = generateTableInfo(results_9, stat_http_req_9)
    return (rows_9,)


@app.cell
def _(head, rows_9, tabulate):
    print(tabulate(rows_9, headers=head, tablefmt='github'))
    return


if __name__ == "__main__":
    app.run()
