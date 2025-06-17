import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import json
    from texttable import Texttable
    from tabulate import tabulate
    import sys
    from typing import List, Dict, Optional
    import os
    file_directory = "./"
    sys.path.append(file_directory)
    from generateDataset import generateDatasetFromResults, Dataset
    import statistics 
    return (
        Dataset,
        Dict,
        List,
        Optional,
        generateDatasetFromResults,
        json,
        mo,
        os,
        statistics,
        tabulate,
    )


@app.cell
def _(mo):
    mo.md(r"""# Functions""")
    return


@app.function
def valueInTable(value_1:str, value_2:str) -> str:
    if value_1 == "-":
        return value_1
    if value_2 == "-":
        return f"\textbf{value_1}"
    if int(value_1)> int(value_2):
        return f"\\textbf{{{value_1}}}"
    return value_1


@app.cell
def _(
    Dataset,
    Dict,
    List,
    sources: "Optional[Dict[str, Dict[str, List[str]]]]",
):
    def generateRatio(dataset: Dataset)-> Dict[str, List[float] | None]:
        ratioUsefullHttpRequest = {}
        for queryTemplate, queryResults in dataset.numberHttpRequest.items():
            ratioUsefullHttpRequest[queryTemplate] = []
            if sources is None:
                return {}
            currentSources = sources[queryTemplate]
            for i, nHttpRequest in enumerate(queryResults):
                if nHttpRequest is not None and currentSources["v{}".format(i)] is not None:
                    oracleNHttpRequest = len(currentSources["v{}".format(i)])
                    ratioUsefullHttpRequest[queryTemplate].append(oracleNHttpRequest/nHttpRequest)
                else:
                    ratioUsefullHttpRequest[queryTemplate].append(None)
        return ratioUsefullHttpRequest
    return (generateRatio,)


@app.cell
def _(mo):
    mo.md(r"""# Dataset""")
    return


@app.cell
def _(Dict, List, Optional, json):
    sourceFilePath = "./results/oracle/sources.json"
    sources: Optional[Dict[str, Dict[str, List[str]]]] = None
    with open(sourceFilePath, 'rb') as rf:
        sources = json.load(rf)
    return (sources,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shapeIndex")
    return (shapeIndexDataset,)


@app.cell
def _(generateDatasetFromResults):
    typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
    typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
    typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "typeIndexLdp")
    return (typeIndexLdpDataset,)


@app.cell
def _(mo):
    mo.md(r"""# Calculation""")
    return


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
def _(generateRatio, shapeIndexDataset, typeIndexLdpDataset):
    ratioUsefullHttpRequestShapeIndex = generateRatio(shapeIndexDataset)
    ratioUsefullHttpRequestTypeIndex = generateRatio(typeIndexLdpDataset)
    return ratioUsefullHttpRequestShapeIndex, ratioUsefullHttpRequestTypeIndex


@app.cell
def _(
    query_label_mapping,
    ratioUsefullHttpRequestShapeIndex,
    ratioUsefullHttpRequestTypeIndex,
):
    rowsShapeIndex = []
    for queryTemplate, ratiosShapeIndex in ratioUsefullHttpRequestShapeIndex.items():
        currentRation = []
        have_result = False
        ratiosTypeIndex = ratioUsefullHttpRequestTypeIndex[queryTemplate]
        if ratiosShapeIndex is None:
            continue
        for i, ratioShapeIndex in enumerate(ratiosShapeIndex):
            if ratiosTypeIndex is not None:
                ratioTypeIndex = ratiosTypeIndex[i]
            else:
                ratioTypeIndex = None
            if ratioShapeIndex is None:
                ratioShapeIndex = "-"
            else:
                ratioShapeIndex = "{:.0f}".format(ratioShapeIndex*100)

            if ratioTypeIndex is None:
                ratioTypeIndex = "-"
            else:
                ratioTypeIndex = "{:.0f}".format(ratioTypeIndex*100)

            have_result = have_result or not (ratioShapeIndex == "-" and ratioTypeIndex=="-")
   
            currentRation.append("{}/{}".format(ratioShapeIndex, ratioTypeIndex))
        currentRow = [query_label_mapping[queryTemplate]] + currentRation
        if have_result:
            rowsShapeIndex.append(currentRow)
    return (rowsShapeIndex,)


@app.cell
def _(mo):
    mo.md(r"""# Visualisation""")
    return


@app.cell
def _():
    artefactFolder = "./artefact/ratio_useful_resources"
    return (artefactFolder,)


@app.cell
def _():
    head = ["Query template", "v0", "v1", "v2", "v3", "v4"]
    return (head,)


@app.cell
def _(head, rowsShapeIndex, tabulate):
    markdownTable = tabulate(rowsShapeIndex, headers=head, tablefmt="html")
    markdownTable
    return


@app.cell
def _(artefactFolder, os, rowsShapeIndex, statistics):
    summary = {"SI": [], "T-LDP":[]}

    for row in rowsShapeIndex:
        siVal = []
        TldpVal = []
        for el in row[1:]:
            si_value, ldp_type_index_value = el.split("/")
            if si_value != "-":
                siVal.append(int(si_value))
            if ldp_type_index_value != "-":
                TldpVal.append(int(ldp_type_index_value))
        averageSiVal = int(round(statistics.mean(siVal), 0))
        maxSiVal = int(round(max(siVal), 0))
        minSiVal = int(round(min(siVal), 0))
    
        averageTlpVal = int(round(statistics.mean(TldpVal), 0))
        maxTlpVal = int(round(max(TldpVal), 0))
        minTlpVal = int(round(min(TldpVal), 0))
    
        stringSi = f"{averageSiVal}^{{{maxSiVal}}}_{{{minSiVal}}}" 
        stringTLDP = f"{averageTlpVal}^{{{maxTlpVal}}}_{{{minTlpVal}}}"
    
        if averageSiVal>averageTlpVal:
            summary["SI"].append(f"$\\boldsymbol{{{stringSi}}}$")
            summary["T-LDP"].append(f"${stringTLDP}$")
        elif averageSiVal<averageTlpVal:
            summary["SI"].append(f"${stringSi}$")
            summary["T-LDP"].append(f"$\\boldsymbol{{{stringTLDP}}}$")
        else:
            summary["SI"].append(f"${stringSi}$")
            summary["T-LDP"].append(f"${stringTLDP}$")

    with open("./templates/table_ratio_useful_resources_summary.tex", "r") as file:
        data = file.read()
        for row in summary.values():
            for value in row:
                data = data.replace("{}", f"{value}", 1)
        with open(os.path.join(artefactFolder, "table_ratio_useful_resources_summary.tex"), "w") as file:
            file.write(data)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
