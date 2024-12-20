from generateDataset import generateDatasetFromResults
from plotsVariation import generate_stats, generatePlot
import os
import numpy as np
import statistics
from matplotlib import rcParams
import matplotlib.pyplot as plt

artefactFolder = "./artefact/variation_approach"

fontSize=25

color_map = {
    "shape index": '#1A85FF',
    "LDP": '#D41159',
    "type index and LDP": '#004D40',
}

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index")

ldpPathResult = "./results/standard/ldp_result.json"
ldpPathSummary = "./results/standard/summary_ldp_result.json"
ldpDataset = generateDatasetFromResults(ldpPathResult, ldpPathSummary, "LDP")

typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "type index and LDP")

def statisticTemplateMetric(serie):
    stat = {}
    for query_template, val in serie.items():
        clean_list = list(filter(lambda a: a != None, val))
        avg = np.nan
        std = np.nan
        min_val = np.nan
        max_val = np.nan
        if len(clean_list) !=0:
            avg = statistics.mean(clean_list)
            if len(clean_list) > 2:
                std = statistics.stdev(clean_list)
            min_val = min(clean_list)
            max_val = max(clean_list)
        stat[query_template] = {
            "avg": avg,
            "std": std,
            "min":min_val,
            "max": max_val,
            "raw": list(map(lambda x: x if x != None else np.nan, val))
        }
    return stat

result_object = {}

instances = [shapeIndexDataset, ldpDataset, typeIndexLdpDataset]
for instance in instances:
    reduction_http_req = instance.numberHttpRequest #calculatePercentageReductionSeries(instance.numberHttpRequest, typeIndexLdpDataset.numberHttpRequest)
    reduction_time = instance.meanExecutionTime#calculatePercentageReductionSeries(instance.meanExecutionTime, typeIndexLdpDataset.meanExecutionTime)
    
    stat_http_req = statisticTemplateMetric(reduction_http_req)
    stat_time = statisticTemplateMetric(reduction_time)
    
    result_object[instance.name] = {
        "http_request": stat_http_req,
        "time": stat_time
    }

result_object_means_http = {}
result_object_http = {}
result_object_means_time = {}
result_object_time = {}
result_object_raw_time = {}

for instance, results in result_object.items():
    result_object_means_http[instance] = []
    result_object_means_time[instance] = []

    result_object_http[instance] = []
    result_object_time[instance] = []
    for key, values in results.items():
        if key=="time":
            for value in values.values():
                result_object_means_time[instance].append(value['avg'])
                result_object_time[instance].append(value['raw'])
                
        if key=="http_request":
            for value in values.values():
                result_object_means_http[instance].append(value['avg'])
                result_object_http[instance].append(value['raw'])

query_map = {
        "interactive-discover-1": "D1",
        "interactive-discover-2": "D2",
        "interactive-discover-3": "D3",
        "interactive-discover-4": "D4",
        "interactive-discover-5": "D5",
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
query_to_skip = ["D8", "S2", "S3", "S6", "S7" ]
queries = list(query_map.values())
indexes_to_skip = []

def generatePlot(results, yaxisLabel, savePathNoExtension):
    
    rcParams.update({'font.size': fontSize})
    x = np.arange(len(queries))
    width = 1/len(instances) -0.1 # the width of the bars
    multiplier = 0
    
    fig, ax = plt.subplots(figsize=(10, 10))

    for dataset, measurements in results.items():
        offset = width * multiplier + width/len(results)
        data = list(range(len(queries)))
        rewind = 0
        for i, measurement in enumerate(measurements): 
            """
            all_nan = all(np.isnan(el) for el in measurement)
            if all_nan:
                rewind+=1
                continue
            """
            #print(f"len {len(data)}, i {i-rewind}")
            data[i-rewind] = list(filter(lambda x: not np.isnan(x), measurement))
        multiplier += 1
        ax.boxplot(data,
                   positions=x+offset,
                   widths=width,
                   patch_artist=True,
                   label=dataset,
                   boxprops=dict(facecolor=color_map[dataset]),
                  )
    #ax.set_yscale('log', base=2)
    #ax.axhline(1, color='gray', linestyle='--', label='No performance change')
    ax.set_ylabel(yaxisLabel)
    ax.set_xticks(x + width, queries)
    ax.grid(axis="both")
    ax.legend(fontsize="18")
    
    fig.tight_layout()
    
    fig.savefig("{}.svg".format(savePathNoExtension), format="svg")
    fig.savefig("{}.eps".format(savePathNoExtension), format="eps")

generatePlot(
    result_object_time,
    "query execution time (ms)",
    os.path.join(artefactFolder,"reduction_query_execution_time_raw")
)
