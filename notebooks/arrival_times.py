import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


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
    from metric import diefficiency
    import numpy as np
    from typing import List

    # NResult, FirstResult, LastResult, ExecTime, dief@24 (20% timeout), dief@60 (50% timeout), dief@96 (80% timeout)  

    return List, diefficiency, generateDatasetFromResults, np


@app.cell
def _(List, np):
    def stats(results: List[float]):
        arr = np.array(results)

        avg = np.mean(arr)
        max = np.max(arr)
        min = np.min(arr)
        std = np.std(arr)

        return {"avg": avg, "min": min, "max":max, "std":std, "raw": results}

    return (stats,)


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
    return queries, version_dict, versions


@app.cell
def _(queries):
    resp = {}
    for query in queries:
        resp[query] = []
        for n_query in range(5):
            metrics = {
                "nResult": None,
                "firstResult": None,
                "lastResult": None,
                "execTime": None,
                "dief@20%t":None,
                "dief@50%t":None,
                "dief@80%t":None,
            }
            resp[query].append(metrics)
    return (resp,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index")
    return (shapeIndexDataset,)


@app.cell
def _():
    #shapeIndexDataset.arrivalTimes["interactive-discover-2"]["v0"]
    return


@app.cell
def _(resp, shapeIndexDataset):
    for q, nResults in shapeIndexDataset.numberResults.items():
        for i, nResult in enumerate(nResults):
            resp[q][i]["nResult"] = nResult

    return


@app.cell
def _(resp, shapeIndexDataset, stats, version_dict, versions):
    def populate_exec_times():
        for q, execTimes in shapeIndexDataset.executionTime.items():
            for v in versions:
                exec_time  = execTimes[v]
                if exec_time == None:
                    resp[q][version_dict[v]]["execTime"] = None
                    continue
                stat = stats(exec_time)
                resp[q][version_dict[v]]["execTime"] = stat
        return


    populate_exec_times()
    return


@app.cell
def _(queries, resp, shapeIndexDataset, stats, version_dict, versions):
    def populate_first_results():
        for q in queries:
            for v in versions:
                first_results = shapeIndexDataset.firstResultsTime(q, v)
                #print(first_results)
                if first_results == None:
                    resp[q][version_dict[v]]["firstResult"] = None
                    continue
                if first_results == []:
                    resp[q][version_dict[v]]["firstResult"] = None
                    continue

                stat = stats(first_results)

                resp[q][version_dict[v]]["firstResult"] = stat


        return

    populate_first_results()
    return


@app.cell
def _(queries, resp, shapeIndexDataset, stats, version_dict, versions):
    def populate_last_results():
        for q in queries:
            for v in versions:
                last_results = shapeIndexDataset.lastResultsTime(q, v)
                #print(last_results)
                if last_results == None:
                    resp[q][version_dict[v]]["lastResult"] = None
                    continue
                if last_results == []:
                    resp[q][version_dict[v]]["lastResult"] = None
                    continue

                stat = stats(last_results)

                resp[q][version_dict[v]]["lastResult"] = stat

        return

    populate_last_results()
    return


@app.cell
def _(diefficiency, resp, shapeIndexDataset, stats, version_dict):
    def populate_diefficiency():
        for q, value in shapeIndexDataset.arrivalTimes.items():
            for v, arrival_time_rep in value.items():
                exec_time = resp[q][version_dict[v]]["execTime"]
                if exec_time == None:
                    continue
                max_exec_time = exec_time["max"]
                diefficiencies_20 = []
                diefficiencies_50 = []
                diefficiencies_80 = []
                for arrival_time in arrival_time_rep:
                    diefficiency_val_20 = diefficiency(arrival_time, max_exec_time*0.20)
                    diefficiency_val_50 = diefficiency(arrival_time, max_exec_time*0.50)
                    diefficiency_val_80 = diefficiency(arrival_time, max_exec_time*0.80)

                    diefficiencies_20.append(diefficiency_val_20)
                    diefficiencies_50.append(diefficiency_val_50)
                    diefficiencies_80.append(diefficiency_val_80)

                print(diefficiencies_20)
                stat_20 = stats(diefficiencies_20)
                stat_50 = stats(diefficiencies_50)
                stat_80 = stats(diefficiencies_80)
        return

    populate_diefficiency()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
