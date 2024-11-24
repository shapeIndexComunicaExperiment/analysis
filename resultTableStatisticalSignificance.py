import json
from texttable import Texttable
import latextable
from tabulate import tabulate
import sys
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
from plotsVariation import calculatePercentageReductionSeries, statisticTemplateMetric
import os

artefactFolder = "./artefact/statistical_significance"
head = ["query template", "relation execution time", "p-value", "avg ratio HTTP request"]

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
            query_template,
            relation,
            p_value,
            ratio_Http_Req
              ]
        rows.append(row)
    return rows

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index")

typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "type index and ldp")

shapeIndex20PathResult = "./results/shape-entry-20-percent/shape_index_result.json"
shapeIndex20PathSummary = "./results/shape-entry-20-percent/summary_shape_index_result.json"
shapeIndex20Dataset = generateDatasetFromResults(shapeIndex20PathResult, shapeIndex20PathSummary, "shape index with 20% entries incomplete")

shapeIndex50PathResult = "./results/shape-entry-50-percent/shape_index_result.json"
shapeIndex50PathSummary = "./results/shape-entry-50-percent/summary_shape_index_result.json"
shapeIndex50Dataset = generateDatasetFromResults(shapeIndex50PathResult, shapeIndex50PathSummary, "shape index with 50% entries incomplete")

shapeIndex80PathResult = "./results/shape-entry-80-percent/shape_index_result.json"
shapeIndex80PathSummary = "./results/shape-entry-80-percent/summary_shape_index_result.json"
shapeIndex80Dataset = generateDatasetFromResults(shapeIndex80PathResult, shapeIndex80PathSummary, "shape index with 80% entries incomplete")

shapeIndex0PathResult = "./results/shape-index-0-percent/shape_index_result.json"
shapeIndex0PathSummary = "./results/shape-index-0-percent/summary_shape_index_result.json"
shapeIndex0NetworkDataset = generateDatasetFromResults(shapeIndex0PathResult, shapeIndex0PathSummary, "shape index absent from the network")

shapeIndex20PathResult = "./results/shape-index-20-percent/shape_index_result.json"
shapeIndex20PathSummary = "./results/shape-index-20-percent/summary_shape_index_result.json"
shapeIndex20NetworkDataset = generateDatasetFromResults(shapeIndex20PathResult, shapeIndex20PathSummary, "shape index absent in 20% of the network")

shapeIndex50PathResult = "./results/shape-index-50-percent/shape_index_result.json"
shapeIndex50PathSummary = "./results/shape-index-50-percent/summary_shape_index_result.json"
shapeIndex50NetworkDataset = generateDatasetFromResults(shapeIndex50PathResult, shapeIndex50PathSummary, "shape index absent in 50% of the network")

shapeIndex80PathResult = "./results/shape-index-80-percent/shape_index_result.json"
shapeIndex80PathSummary = "./results/shape-index-80-percent/summary_shape_index_result.json"
shapeIndex80NetworkDataset = generateDatasetFromResults(shapeIndex80PathResult, shapeIndex80PathSummary, "shape index absent in 80% of the network")

shapeIndexInnerPathResult = "./results/shape-inner/shape_index_result.json"
shapeIndexInnerPathSummary = "./results/shape-inner/summary_shape_index_result.json"
shapeIndexInnerDataset = generateDatasetFromResults(shapeIndexInnerPathResult, shapeIndexInnerPathSummary, "shape index with shapes with only information about the dataset model")

shapeIndexMinimalPathResult = "./results/shape-minimal/shape_index_result.json"
shapeIndexMinimalPathSummary = "./results/shape-minimal/summary_shape_index_result.json"
shapeIndexMinimalDataset = generateDatasetFromResults(shapeIndexMinimalPathResult, shapeIndexMinimalPathSummary, "shape index with shapes with minimal information")

instances_shape_index = [
    (shapeIndex20Dataset, "shapeIndex20CompleteDataset"),
    (shapeIndex50Dataset, "shapeIndex50CompleteDataset"),
    (shapeIndex80Dataset, "shapeIndex80CompleteDataset"),
    (shapeIndex0NetworkDataset, "shapeIndex0NetworkDataset"),
    (shapeIndex20NetworkDataset, "shapeIndex20NetworkDataset"),
    (shapeIndex50NetworkDataset, "shapeIndex50NetworkDataset"),
    (shapeIndex80NetworkDataset, "shapeIndex80NetworkDataset"),
    (shapeIndexInnerDataset, "shapeIndexInnerDataset"),
    (shapeIndexMinimalDataset, "shapeIndexMinimalDataset")
]

results = {}

for template, execution_times in shapeIndexDataset.executionTime.items():
    
    (p_value_greater, p_value_different, p_value_lesser) = statisticalSignificanceByTemplate(
        execution_times,
        typeIndexLdpDataset.executionTime[template]
    )

    results[template] = {
        "greater": p_value_greater,
        "lesser": p_value_lesser,
        "different":p_value_different,
    }
    
reduction_http_req = calculatePercentageReductionSeries(shapeIndexDataset.numberHttpRequest, typeIndexLdpDataset.numberHttpRequest)
stat_http_req = statisticTemplateMetric(reduction_http_req)

rows = generateTableInfo(results, stat_http_req)

table_state_of_the_art = tabulate(rows, headers=head, tablefmt="github")

textTable = Texttable()
textTable.set_cols_dtype(['t', 't', 't', 't'])
textTable.add_rows([head]+ rows)
label = "tab:statSignificanceStateOfTheArt"
caption = "Table comparing the shape index approach to the state-of-the-art. RH, indicate that the p-value is associated to the rejected hypothesis. Every query performs better or similarly to the state-of-the-art with the shape index approach except for interactive-short-4, which performs worse but is already a fast-running query."

latex_table_state_of_the_art = latextable.draw_latex(textTable, caption=caption, label=label)

table_to_save = f"""
# Comparaison execution time shape index approach against the type index

{table_state_of_the_art}
"""

with open(os.path.join(artefactFolder, "comparaisonStateOfTheArt.md"), "w") as outfile:
    outfile.write(table_to_save)

with open(os.path.join(artefactFolder, "comparaisonStateOfTheArt.tex"), "w") as outfile:
    outfile.write(latex_table_state_of_the_art)
    
for (instance, file_name) in instances_shape_index:
    results = {}

    for template, execution_times in instance.executionTime.items():
        
        (p_value_greater, p_value_different, p_value_lesser) = statisticalSignificanceByTemplate(
            execution_times,
            shapeIndexDataset.executionTime[template]
        )

        results[template] = {
            "greater": p_value_greater,
            "lesser": p_value_lesser,
            "different":p_value_different,
        }
        
    reduction_http_req = calculatePercentageReductionSeries(instance.numberHttpRequest, shapeIndexDataset.numberHttpRequest)
    stat_http_req = statisticTemplateMetric(reduction_http_req)

    rows = generateTableInfo(results, stat_http_req)

    table_state_of_the_art = tabulate(rows, headers=head, tablefmt="github")

    table_to_save = f"""
    # Comparaison {instance.name} against an ideal shape index
    
    {table_state_of_the_art}
    """

    with open(os.path.join(artefactFolder, f"{file_name}.md"), "w") as outfile:
        outfile.write(table_to_save)