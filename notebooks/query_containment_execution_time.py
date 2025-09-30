import marimo

__generated_with = "0.14.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import json
    from texttable import Texttable 
    import latextable
    from tabulate import tabulate
    from typing import Optional, Dict
    import os
    from pathlib import Path
    return Dict, Optional, Path, Texttable, json, latextable, os, tabulate


@app.cell
def _(Path):
    artefactFolder = Path("./artefact/query_containment_execution_time")
    return (artefactFolder,)


@app.cell
def _(Dict):
    datasets: Dict[str, str] = {
        "fully_bounded": "./results/shape-containment/fully_bounded/time_eval_summary_with_warm_up.json",
        "inner_dataset": "./results/shape-containment/inner_dataset/time_eval_summary_with_warm_up.json",
        "minimal": "./results/shape-containment/minimal/time_eval_summary_with_warm_up.json"
    }
    ignoreQueries = ["interactive-short-1-nocity", "interactive-short-3-unidir", "interactive-short-4-creator"]
    return datasets, ignoreQueries


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
def _(
    Dict,
    Optional,
    Texttable,
    artefactFolder,
    datasets: "Dict[str, str]",
    ignoreQueries,
    json,
    latextable,
    os,
    query_label_mapping,
    tabulate,
):
    tables = {}
    for key, filePath in datasets.items():
        os.makedirs(os.path.join(artefactFolder, key), exist_ok=True)

        results: Optional[Dict[str,float]] = None

        with open(filePath, 'rb') as rf:
            results = json.load(rf)

        head = ["Query Template", "avg (ms)", "std (ms)", "max (ms)"]
        rows = []

        for query, value in results.items():
            if query not in ignoreQueries:
                row = [query_label_mapping[query], value["average"],value["std"],value["max"] ]
                rows.append(row)

        caption= "Query-Shape containment computation time (100 samples) is negligeable with the most restrictive shapes of our experiments."
        label="tab:queryShapeContainmentEval"

        textTable = Texttable()
        textTable.add_rows([head]+ rows)

        latexTable = latextable.draw_latex(textTable, caption=caption, label=label)
        markdownTable = tabulate(rows, headers=head, tablefmt="github")

        tables[key] =  tabulate(rows, headers=head, tablefmt="html")
        with open(os.path.join(artefactFolder,key, "table_query_shape_containment_exec.tex"), "w") as file:
            file.write(latexTable)

        with open(os.path.join(artefactFolder,key, "table_query_shape_containment_exec.md"), "w") as file:
            file.write(markdownTable)

    return (tables,)


@app.cell
def _(tables):
    tables["fully_bounded"]
    return


@app.cell
def _(tables):
    tables["inner_dataset"]
    return


@app.cell
def _(tables):
    tables["minimal"]
    return


if __name__ == "__main__":
    app.run()
