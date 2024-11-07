import json
from texttable import Texttable
import latextable
from tabulate import tabulate
import sys
from typing import List, Dict
import os
from generateDataset import generateDatasetFromResults 

def generateRatio(dataset: Dict[str, List[int] | None])-> Dict[str, List[float] | None]:
    ratioUsefullHttpRequest = {}
    for queryTemplate, queryResults in dataset.numberHttpRequest.items():
        ratioUsefullHttpRequest[queryTemplate] = []
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
sources = None
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
    ratiosTypeIndex = ratioUsefullHttpRequestTypeIndex[queryTemplate]
    for i, ratioShapeIndex in enumerate(ratiosShapeIndex):
        ratioTypeIndex = ratiosTypeIndex[i]
        if ratioShapeIndex is None:
            ratioShapeIndex = "-"
        else:
            ratioShapeIndex = "{:.0f}".format(ratioShapeIndex*100)

        if ratioTypeIndex is None:
            ratioTypeIndex = "-"
        else:
            ratioTypeIndex = "{:.0f}".format(ratioTypeIndex*100)

        currentRation.append("{}/{}".format(ratioShapeIndex, ratioTypeIndex))

    currentRow = [queryTemplate] + currentRation
    rowsShapeIndex.append(currentRow)

caption= "Even using the shape index (denominator) compare to the type-index with LDP (numerator) for the majority of the query their is a low ratio of useful resources aquired."
label="tab:ratioUsefulResources"

textTable = Texttable()
textTable.add_rows([head]+ rowsShapeIndex)

latexTable = latextable.draw_latex(textTable, caption=caption, label=label)
markdownTable = tabulate(rowsShapeIndex, headers=head, tablefmt="github")

with open(os.path.join(artefactFolder, "table_ratio_useful_ressources.tex"), "w") as file:
    file.write(latexTable)

with open(os.path.join(artefactFolder, "table_ratio_useful_ressources.md"), "w") as file:
    file.write(markdownTable)