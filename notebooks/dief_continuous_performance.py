import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import json
    from texttable import Texttable
    import latextable
    from tabulate import tabulate
    import sys
    sys.path.append("./")
    from generateDataset import generateDatasetFromResults
    from metric import diefficiency
    import numpy as np
    from typing import List, Optional
    from pathlib import Path
    import numpy as np
    import diefpy
    return Path, diefpy, generateDatasetFromResults, json, mo, np, sys


@app.cell
def _():
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FormatStrFormatter
    from matplotlib.lines import Line2D
    return


@app.cell
def _(sys):
    sys.path.append("./notebooks/")
    from continuous_performance import create_resp_by_template, plot, stats, resp_no_raw, resp_no_raw_by_template
    return (
        create_resp_by_template,
        plot,
        resp_no_raw,
        resp_no_raw_by_template,
        stats,
    )


@app.cell
def _():
    from continuous_performance import is_zero, displayed_stat
    return displayed_stat, is_zero


@app.cell
def _(mo):
    mo.md(r"""# Function definition""")
    return


@app.cell
def _():
    queries = [
        "interactive-discover-1",
        "interactive-discover-2",
        "interactive-discover-3",
        "interactive-discover-4",
        "interactive-discover-5",
        "interactive-discover-6",
        "interactive-discover-7",
        "interactive-discover-8",
        "interactive-short-1",
        "interactive-short-2",
        "interactive-short-3",
        "interactive-short-4",
        "interactive-short-5",
        "interactive-short-6",
        "interactive-short-7"
    ]

    versions = [f"v{i}" for i in range(5)]
    version_dict = {v: i for i, v in enumerate(versions)}
    return queries, version_dict


@app.cell
def _(queries):
    def produce_initial_resp():
        resp = {}
        for query in queries:
            resp[query] = []
            for n_query in range(5):
                metrics = {
                    "dief@0.1s":None,
                    "dief@1s":None,
                    "dief@10s":None,
                }
                resp[query].append(metrics)
        return resp

    return (produce_initial_resp,)


@app.cell
def _(diefpy, np, stats, version_dict):
    def populate_diefficiency(resp, dataset):
        for q, value in dataset.arrivalTimes.items():
            for v, arrival_time_rep in value.items():

                if arrival_time_rep == None and dataset.executionTime[q][v] != None:
                    resp[q][version_dict[v]]["dief@0.1s"] = {"avg": 0, "min": 0, "max": 0, "std": 0, "raw": [0]}
                    resp[q][version_dict[v]]["dief@1s"] = {"avg": 0, "min": 0, "max": 0, "std": 0, "raw": [0]}
                    resp[q][version_dict[v]]["dief@10s"] = {"avg": 0, "min": 0, "max": 0, "std": 0, "raw": [0]}
                    continue

                elif arrival_time_rep == None:
                    resp[q][version_dict[v]]["dief@0.1s"] = None
                    resp[q][version_dict[v]]["dief@1s"] = None
                    resp[q][version_dict[v]]["dief@10s"] = None
                    continue


                diefficiencies_0_1s = []
                diefficiencies_1s = []
                diefficiencies_10s = []

                dtype  = [('test', 'U100'), ('approach', 'U100'), ('answer', 'i8'), ('time', 'f8')]

                for arrival_time in arrival_time_rep:

                    if len(arrival_time) == 0:
                        diefficiencies_0_1s.append(0)
                        diefficiencies_1s.append(0)
                        diefficiencies_10s.append(0)
                        continue

                    data = []
                    for i, t in enumerate(arrival_time):
                        current = (q, dataset.name, i+1, t)
                        data.append(current)

                    arr = np.array(data, dtype=dtype)

                    diefficiency_val_0_1s = diefpy.dieft(arr, q, 0.1*1_000)
                    diefficiency_val_1s = diefpy.dieft(arr, q, 1_000)
                    diefficiency_val_10s = diefpy.dieft(arr, q, 10*1_000)

                    diefficiencies_0_1s.append(diefficiency_val_0_1s[0][2])
                    diefficiencies_1s.append(diefficiency_val_1s[0][2])
                    diefficiencies_10s.append(diefficiency_val_10s[0][2])


                stat_0_1s = stats(diefficiencies_0_1s)
                stat_1s = stats(diefficiencies_1s)
                stat_10s = stats(diefficiencies_10s)

                resp[q][version_dict[v]]["dief@0.1s"] = stat_0_1s
                resp[q][version_dict[v]]["dief@1s"] = stat_1s
                resp[q][version_dict[v]]["dief@10s"] = stat_10s
        return
    return (populate_diefficiency,)


@app.cell
def _(diefpy, np):
    def plot_distribution(dataset):
        plts = []
        for q, value in dataset.arrivalTimes.items():
            for v, arrival_time_rep in value.items():

                if arrival_time_rep == None and dataset.executionTime[q][v] != None:
                    continue

                elif arrival_time_rep == None:
                    continue

                dtype  = [('test', 'U100'), ('approach', 'U100'), ('answer', 'i4'), ('time', 'f8')]
                for arrival_time in arrival_time_rep:

                    if len(arrival_time) == 0:
                        continue

                    data = []
                    for i, t in enumerate(arrival_time):
                        current = (q, dataset.name, i+1, t)
                        data.append(current)

                    arr = np.array(data, dtype=dtype)

                    plt = diefpy.plot_answer_trace(arr, q)
                    plt.show(warn=False)
                    plts.append(plt)
                    break

        return plts

    return


@app.cell
def _(create_resp_by_template, populate_diefficiency, produce_initial_resp):
    def generate_continuous_performances(dataset):
        resp = produce_initial_resp()
        populate_diefficiency(resp, dataset)
        resp_by_template = create_resp_by_template(resp)

        return (resp, resp_by_template)
    return (generate_continuous_performances,)


@app.cell
def _(mo):
    mo.md(r"""# Dataset""")
    return


@app.cell
def _(Path):
    artefact_path = Path("artefact") / "continuous_performance"
    return (artefact_path,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index")

    ldpPathResult = "./results/standard/ldp_result.json"
    ldpPathSummary = "./results/standard/summary_ldp_result.json"
    ldpDataset = generateDatasetFromResults(ldpPathResult, ldpPathSummary, "LDP")

    typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
    typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
    typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "type index")
    return ldpDataset, shapeIndexDataset, typeIndexLdpDataset


@app.cell
def _(mo):
    mo.md(r"""# Calculation""")
    return


@app.cell
def _(
    generate_continuous_performances,
    ldpDataset,
    shapeIndexDataset,
    typeIndexLdpDataset,
):
    (resp_si, resp_by_template_si) = generate_continuous_performances(shapeIndexDataset)
    (resp_ldp, resp_by_template_ldp) = generate_continuous_performances(ldpDataset)
    (resp_ti, resp_by_template_ti) = generate_continuous_performances(typeIndexLdpDataset)
    return (
        resp_by_template_ldp,
        resp_by_template_si,
        resp_by_template_ti,
        resp_ldp,
        resp_si,
        resp_ti,
    )


@app.cell
def _(
    artefact_path,
    json,
    resp_by_template_ldp,
    resp_by_template_si,
    resp_by_template_ti,
    resp_ldp,
    resp_no_raw,
    resp_no_raw_by_template,
    resp_si,
    resp_ti,
):
    with open(artefact_path / "dief_raw_shape_index.json", 'w') as f:
        json.dump(resp_si, f)

    with open(artefact_path / "dief_raw_ldp.json", 'w') as f:
        json.dump(resp_ldp, f)

    with open(artefact_path / "dief_raw_type_index.json", 'w') as f:
        json.dump(resp_ti, f)


    with open(artefact_path / "dief_summary_shape_index.json", 'w') as f:
        json.dump(resp_no_raw(resp_si), f)

    with open(artefact_path / "dief_summary_ldp.json", 'w') as f:
        json.dump(resp_no_raw(resp_ldp), f)

    with open(artefact_path / "dief_summary_type_index.json", 'w') as f:
        json.dump(resp_no_raw(resp_ti), f)


    with open(artefact_path / "dief_shape_index_by_template.json", 'w') as f:
        json.dump(resp_by_template_si, f)

    with open(artefact_path / "dief_ldp_by_template.json", 'w') as f:
        json.dump(resp_by_template_ldp, f)

    with open(artefact_path / "dief_type_index_by_template.json", 'w') as f:
        json.dump(resp_by_template_ti, f)


    with open(artefact_path / "dief_summary_shape_index_by_template.json", 'w') as f:
        json.dump(resp_no_raw_by_template(resp_by_template_si), f)

    with open(artefact_path / "dief_summary_ldp_by_template.json", 'w') as f:
        json.dump(resp_no_raw_by_template(resp_by_template_ldp), f)

    with open(artefact_path / "dief_summary_type_indexby_template.json", 'w') as f:
        json.dump(resp_no_raw_by_template(resp_by_template_ti), f)

    return


@app.cell
def _():
    reported_templates = [
        "interactive-discover-1",
        "interactive-discover-2",
        "interactive-discover-3",
        "interactive-discover-4",
        "interactive-discover-5",
        "interactive-discover-6",
        "interactive-discover-7",
        "interactive-short-1",
        "interactive-short-4",
        "interactive-short-5",
        "interactive-short-7",
    ]

    return (reported_templates,)


@app.cell
def _(mo):
    mo.md(r"""## Visualization""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Table""")
    return


@app.function
def best_result(value, field, best_value):
    if value[field] == None:
        return False
    if best_value == None:
        return True
    if best_value[field]["avg"] < value[field]["avg"]:
        return True
    return False


@app.cell
def _(
    displayed_stat,
    is_zero,
    reported_templates,
    resp_by_template_ldp,
    resp_by_template_si,
    resp_by_template_ti,
):
    template  = ""
    with open("./templates/dief_table_continuous_performance.tex", "r") as template_file:
        template = template_file.read()

    for q in reported_templates:
        summaries = [resp_by_template_si[q], resp_by_template_ti[q], resp_by_template_ldp[q]]
        best_d_0_1 = None
        best_d_1 = None
        best_d_10 = None

        all_zero_d_0_1 = True
        all_zero_d_1 = True
        all_zero_d_10 = True

        for summary in summaries:
            all_zero_d_0_1 = all_zero_d_0_1 and is_zero(summary["dief@0.1s"])
            all_zero_d_1 = all_zero_d_1 and is_zero(summary["dief@1s"])
            all_zero_d_10 = all_zero_d_10 and is_zero(summary["dief@10s"])

            if best_result(summary, "dief@0.1s", best_d_0_1):
                best_d_0_1 = summary

            if best_result(summary, "dief@1s", best_d_1):
                best_d_1 = summary 

            if best_result(summary,"dief@10s", best_d_10):
                best_d_10 = summary

        for summary in summaries:
            ft = None
            tt = None 
            wt = None 

            if best_d_0_1 == summary and not all_zero_d_0_1:
                ft = displayed_stat(summary["dief@0.1s"], True)
            else:
                ft = displayed_stat(summary["dief@0.1s"], False)

            if best_d_1 == summary and not all_zero_d_1:
                tt = displayed_stat(summary["dief@1s"], True)
            else:
                tt = displayed_stat(summary["dief@1s"], False)

            if best_d_10 == summary and not all_zero_d_10:    
                wt = displayed_stat(summary["dief@10s"], True)
            else:
                wt = displayed_stat(summary["dief@10s"], False)

            template = template.replace("{}", ft, 1)
            template = template.replace("{}", tt, 1)
            template = template.replace("{}", wt, 1)
    return (template,)


@app.cell
def _(artefact_path, template):
    with open(artefact_path / "dief_table_continuous_performance.tex", "w") as table_file:
        table_file.write(template)
    return


@app.cell
def _(mo):
    mo.md(r"""### Plot""")
    return


@app.cell
def _():
    y_label = "result-time (n x s)"
    return (y_label,)


@app.cell
def _(
    artefact_path,
    plot,
    reported_templates,
    resp_by_template_si,
    resp_by_template_ti,
    shapeIndexDataset,
    typeIndexLdpDataset,
    y_label,
):
    fig_dief_01 = plot("dief@0.1s", resp_by_template_si, resp_by_template_ti, shapeIndexDataset, typeIndexLdpDataset, reported_templates, y_label=y_label)

    fig_dief_01.savefig(artefact_path / "dief_01.svg", format="svg")
    fig_dief_01.savefig(artefact_path / "dief_01.eps", format="eps")

    fig_dief_01
    return


@app.cell
def _(
    artefact_path,
    plot,
    reported_templates,
    resp_by_template_si,
    resp_by_template_ti,
    shapeIndexDataset,
    typeIndexLdpDataset,
    y_label,
):
    fig_dief_1 = plot("dief@1s", resp_by_template_si, resp_by_template_ti, shapeIndexDataset, typeIndexLdpDataset, reported_templates, y_label=y_label)

    fig_dief_1.savefig(artefact_path / "dief_1.svg", format="svg")
    fig_dief_1.savefig(artefact_path / "dief_1.eps", format="eps")

    fig_dief_1
    return


@app.cell
def _(
    artefact_path,
    plot,
    reported_templates,
    resp_by_template_si,
    resp_by_template_ti,
    shapeIndexDataset,
    typeIndexLdpDataset,
    y_label,
):
    fig_dief_10 = plot("dief@10s", resp_by_template_si, resp_by_template_ti, shapeIndexDataset, typeIndexLdpDataset, reported_templates, y_label=y_label)

    fig_dief_10.savefig(artefact_path / "dief_10.svg", format="svg")
    fig_dief_10.savefig(artefact_path / "dief_10.eps", format="eps")

    fig_dief_10
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
