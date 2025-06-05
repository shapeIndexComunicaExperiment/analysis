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
    file_directory = "./"
    sys.path.append(file_directory)
    from generateDataset import generateDatasetFromResults
    from metric import diefficiency
    import numpy as np
    from typing import List, Optional
    return List, Optional, diefficiency, generateDatasetFromResults, mo, np


@app.cell
def _(mo):
    mo.md(
        r"""
    On this notebook we are calculating the continuous performances of the approaches.
    For the diefficiency metric we consider [state of the art response time limits derived from neuropsycology](https://www.uxtigers.com/post/ai-response-time) also [detailed in this book.](https://www.amazon.com/dp/0125184069?tag=useitcomusablein)

    We are considering: 

    - The number of results
    - The arrival time of the first result *
    - The arrival time of the last result *
    - The execution time
    - The difference between the execution time and the last result (Termination time)*
    - The waiting time (we consider that a user wait after 1 second without results) *
    - The diefficiency at 0.1s (instant response illusion) *
    - The diefficiency at 1s (seamless flow of thought) *
    - The diefficiency at 10s (attention drifts) *
    """
    )
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
    return queries, version_dict, versions


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index")
    return (shapeIndexDataset,)


@app.cell
def _(queries):
    def produce_initial_resp():
        resp = {}
        for query in queries:
            resp[query] = []
            for n_query in range(5):
                metrics = {
                    "nResult": None,
                    "firstResult": None,
                    "lastResult": None,
                    "execTime": None,
                    "terminationTime":None,
                    "waitingTime":None,
                    "dief@0.1s":None,
                    "dief@1s":None,
                    "dief@10s":None,
                }
                resp[query].append(metrics)
        return resp
    return (produce_initial_resp,)


@app.function
def print_resp(resp):
    clean_resp = {}

    for query, metrics_list in resp.items():
        clean_resp[query] = []
        for metrics in metrics_list:
            clean_metrics = {}
            for key, value in metrics.items():
                if isinstance(value, dict) and "raw" in value:
                    clean_metrics[key] = {k: v for k, v in value.items() if k != "raw"}
                else:
                    clean_metrics[key] = value
            clean_resp[query].append(clean_metrics)
    return clean_resp


@app.cell
def _(List, Optional, np):
    def stats(results: Optional[List[float]]):
        if results == None:
            return None
        arr = np.array(results)

        avg = np.mean(arr)
        max = np.max(arr)
        min = np.min(arr)
        std = np.std(arr)

        return {"avg": avg, "min": min, "max":max, "std":std, "raw": results}

    return (stats,)


@app.function
def populate_number_of_results(resp, dataset):
    for q, nResults in dataset.numberResults.items():
        for i, nResult in enumerate(nResults):
            resp[q][i]["nResult"] = nResult


@app.cell
def _(stats, version_dict, versions):
    def populate_exec_times(resp, dataset):
        for q, execTimes in dataset.executionTime.items():
            for v in versions:
                exec_time  = execTimes[v]
                if exec_time == None:
                    resp[q][version_dict[v]]["execTime"] = None
                    continue
                stat = stats(exec_time)
                resp[q][version_dict[v]]["execTime"] = stat
        return
    return (populate_exec_times,)


@app.cell
def _(queries, stats, version_dict, versions):
    def populate_first_results(resp, dataset):
        for q in queries:
            for v in versions:
                first_results = dataset.firstResultsTime(q, v)
                if first_results == None:
                    resp[q][version_dict[v]]["firstResult"] = None
                    continue
                if first_results == []:
                    resp[q][version_dict[v]]["firstResult"] = None
                    continue

                stat = stats(first_results)

                resp[q][version_dict[v]]["firstResult"] = stat

        return
    return (populate_first_results,)


@app.cell
def _(queries, stats, version_dict, versions):
    def populate_last_results(resp, dataset):
        for q in queries:
            for v in versions:
                last_results = dataset.lastResultsTime(q, v)
                if last_results == None:
                    resp[q][version_dict[v]]["lastResult"] = None
                    continue
                if last_results == []:
                    resp[q][version_dict[v]]["lastResult"] = None
                    continue

                stat = stats(last_results)

                resp[q][version_dict[v]]["lastResult"] = stat
        return
    return (populate_last_results,)


@app.cell
def _(np, stats):
    def populate_termination_time(resp):
        for q, value in resp.items():
            for metrics in value:
                last_result = metrics["lastResult"]
                exec_time = metrics["execTime"]
                if last_result != None and exec_time != None:
                    termination_time = np.array(exec_time["raw"]) - np.array(last_result["raw"]) 
                    metrics["terminationTime"] = stats(termination_time.tolist())
        return

    return (populate_termination_time,)


@app.cell
def _(queries, stats, version_dict, versions):
    def populate_waiting_time(resp, dataset):
        for q in queries:
            for v in versions:
                arrival_times_rep = dataset.arrivalTimes[q][v]
                waiting_times = []
                if arrival_times_rep == None:
                    resp[q][version_dict[v]]["waitingTime"] = None
                    continue
                for arrival_times in arrival_times_rep:
                    waiting_time = 0
                    for i in range(len(arrival_times)-1):
                        in_between = arrival_times[i+1] - arrival_times[i]
                        if in_between > 1*1_000:
                            waiting_time += in_between - 1*1_000
                    waiting_times.append(waiting_time)

                stat = stats(waiting_times)

                resp[q][version_dict[v]]["waitingTime"] = stat
        return
    return (populate_waiting_time,)


@app.cell
def _(diefficiency, stats, version_dict):
    def populate_diefficiency(resp, dataset):
        for q, value in dataset.arrivalTimes.items():
            for v, arrival_time_rep in value.items():
                exec_time = resp[q][version_dict[v]]["execTime"]
                if exec_time == None:
                    resp[q][version_dict[v]]["dief@0.1s"] = None
                    resp[q][version_dict[v]]["dief@1s"] = None
                    resp[q][version_dict[v]]["dief@10s"] = None
                    continue

                n_results = resp[q][version_dict[v]]["nResult"]

                if n_results <=1:
                    resp[q][version_dict[v]]["dief@0.1s"] = stats([0])
                    resp[q][version_dict[v]]["dief@1s"] = stats([0])
                    resp[q][version_dict[v]]["dief@10s"] = stats([0])
                    continue

                diefficiencies_0_1s = []
                diefficiencies_1s = []
                diefficiencies_10s = []

                for arrival_time in arrival_time_rep:
                    diefficiency_val_0_1s = diefficiency(arrival_time, 0.1*1_000)
                    diefficiency_val_1s = diefficiency(arrival_time, 1_000)
                    diefficiency_val_10s = diefficiency(arrival_time, 10*1_000)

                    diefficiencies_0_1s.append(diefficiency_val_0_1s)
                    diefficiencies_1s.append(diefficiency_val_1s)
                    diefficiencies_10s.append(diefficiency_val_10s)

                stat_0_1s = stats(diefficiencies_0_1s)
                stat_1s = stats(diefficiencies_1s)
                stat_10s = stats(diefficiencies_10s)

                resp[q][version_dict[v]]["dief@0.1s"] = stat_0_1s
                resp[q][version_dict[v]]["dief@1s"] = stat_1s
                resp[q][version_dict[v]]["dief@10s"] = stat_10s
        return
    return (populate_diefficiency,)


@app.cell
def _(stats):

    def create_resp_by_template(resp):
        resp_by_template = {}
    
        for q, values in resp.items():
            resp_by_template[q] = {

                "nResult": [],
                "firstResult": [],
                "lastResult": [],
                "execTime": [],
                "terminationTime":[],
                "waitingTime":[],
                "dief@0.1s":[],
                "dief@1s":[],
                "dief@10s":[],
            }
            for instantiation in values:
                for name, metric in instantiation.items():
                    if type(metric) == int:
                        resp_by_template[q][name].append(metric)
                    elif metric != None:
                        resp_by_template[q][name].extend(metric["raw"])
            for name, metric in resp_by_template[q].items():
                if len(metric) > 0:
                    resp_by_template[q][name] = stats(metric)
                else:
                    resp_by_template[q][name] = None
        return resp_by_template
    return (create_resp_by_template,)


@app.function
def print_resp_by_template(resp_by_template):
    clean_resp = {}

    for query, metrics in resp_by_template.items():
        clean_resp[query] = []
        clean_metrics = {}
        for key, value in metrics.items():
            if isinstance(value, dict) and "raw" in value:
                clean_metrics[key] = {k: v for k, v in value.items() if k != "raw"}
            else:
                clean_metrics[key] = value
        clean_resp[query].append(clean_metrics)
    return clean_resp


@app.cell
def _(
    create_resp_by_template,
    populate_diefficiency,
    populate_exec_times,
    populate_first_results,
    populate_last_results,
    populate_termination_time,
    populate_waiting_time,
    produce_initial_resp,
):
    def generate_continuous_performances(dataset):
        resp = produce_initial_resp()
        populate_number_of_results(resp, dataset)
        populate_exec_times(resp, dataset)
        populate_first_results(resp, dataset)
        populate_last_results(resp, dataset)
        populate_termination_time(resp)
        populate_waiting_time(resp, dataset)
        populate_diefficiency(resp, dataset)
        resp_by_template = create_resp_by_template(resp)
    
        return (resp, resp_by_template)
    return (generate_continuous_performances,)


@app.cell
def _(generate_continuous_performances, shapeIndexDataset):
    (resp, resp_by_template) = generate_continuous_performances(shapeIndexDataset)
    return resp, resp_by_template


@app.cell
def _(resp_by_template):
    print_resp_by_template(resp_by_template)
    return


@app.cell
def _(resp):
    print_resp(resp)
    return


if __name__ == "__main__":
    app.run()
