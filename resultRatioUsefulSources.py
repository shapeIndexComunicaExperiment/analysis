import json
from texttable import Texttable
from tabulate import tabulate
import sys
from typing import List, Dict, Optional
import os
from generateDataset import generateDatasetFromResults, Dataset


def valueInTable(value_1:str, value_2:str) -> str:
    if value_1 == "-":
        return value_1
    if value_2 == "-":
        return f"\textbf{value_1}"
    if int(value_1)> int(value_2):
        return f"\\textbf{{{value_1}}}"
    return value_1
    
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

artefactFolder = "./artefact/ratio_useful_resources"

head = ["Query template", "v0", "v1", "v2", "v3", "v4"]

sourceFilePath = "./results/oracle/sources.json"
sources: Optional[Dict[str, Dict[str, List[str]]]] = None
with open(sourceFilePath, 'rb') as rf:
    sources = json.load(rf)

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shapeIndex")

typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "typeIndexLdp")

ratioUsefullHttpRequestShapeIndex = generateRatio(shapeIndexDataset)
ratioUsefullHttpRequestTypeIndex = generateRatio(typeIndexLdpDataset)


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
    currentRow = [queryTemplate] + currentRation
    if have_result:
        rowsShapeIndex.append(currentRow)

markdownTable = tabulate(rowsShapeIndex, headers=head, tablefmt="github")

with open("./template_table_ratio_useful_resources.tex", "r") as file:
    data = file.read()
    for row in rowsShapeIndex:
        for el in row[1:]:
            si_value, ldp_type_index_value = el.split("/")
            data = data.replace("{}", valueInTable(si_value, ldp_type_index_value) , 1)
            data = data.replace("{}", valueInTable(ldp_type_index_value, si_value), 1)
    with open(os.path.join(artefactFolder, "table_ratio_useful_ressources.tex"), "w") as file:
        file.write(data)

with open(os.path.join(artefactFolder, "table_ratio_useful_ressources.md"), "w") as file:
    file.write(markdownTable)
