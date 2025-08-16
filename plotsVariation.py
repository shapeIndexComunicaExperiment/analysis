import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import statistics
from typing import List, Optional, Dict, Tuple
from generateDataset import Dataset
from metric import calculatePercentageReductionSeries
from matplotlib.ticker import MultipleLocator
from matplotlib import rcParams, ticker
import copy

QUERY_MAP = {
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

QUERIES = list(QUERY_MAP.values())

def statisticTemplateMetric(serie:Dict[str, List[Optional[float|int]]])->Dict[str, float|List[float]]:
    stat = {}
    for query_template, val in serie.items():
        clean_list:List[float|int] = list(filter(lambda a: a != None, val))
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


def generatePlot(results,
                 yaxisLabel,
                 len_instance,
                 color_map,
                 deactivate_y_axis=False,
                 deactivate_x_axis_title=False,
                 fontSize=25,
                 ylim=11,
                 query_to_skip=[],
                 formatYAxis = '{:.1f}'
                 ):
    #rcParams.update({'font.size': fontSize})

    indexes_to_skip = []
    queries = copy.deepcopy(QUERIES)
    for query in query_to_skip:
        index = queries.index(query)
        indexes_to_skip.append(index)
    
    for query in query_to_skip:
        index = queries.index(query)
        del queries[index]
    
    x = np.arange(len(queries))
    width = 1/len_instance - 0.1
    multiplier = 0
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    for text in fig.findobj(match=plt.Text):
        text.set_fontsize(fontSize)
        
    for dataset, measurements in results.items():
        offset = width * multiplier + width/len(results)
        data = list(range(len(queries)))
        rewind = 0
        for i, measurement in enumerate(measurements):
            all_nan = all(np.isnan(el) for el in measurement)
            if all_nan:
                rewind+=1
                continue
            data[i-rewind] = [1 if np.isnan(x) else x for x in measurement]
        multiplier += 1
        ax.boxplot(data,
                   positions=x+offset,
                   widths=width,
                   patch_artist=True,
                   medianprops={"linewidth": 3},
                   label=dataset,
                   boxprops=dict(facecolor=color_map[dataset]),
                  )
        
    if ylim is not None:
        ax.set_ylim(0.25, ylim)
    if deactivate_y_axis:
        #ax.set_yticks([])
        ax.set_yticklabels([])
    else:
        ax.set_ylabel(yaxisLabel)
    if not deactivate_x_axis_title:
        ax.set_xlabel("query template")
        
    ax.set_yscale('log', base=2)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda val, pos: formatYAxis.format(val)))
    #ax.axhline(1, color='gray', linestyle='--', label='No performance change')
    ax.set_xticks(x + width, queries)
    ax.grid(axis="both")
    ax.legend(loc='upper left',  fontsize="18")
    
    fig.tight_layout()
    
    return fig
    
    

def generate_stats(instances:List[Dataset], comparatorInstance:Dataset)->Tuple[dict,dict,dict,dict]:
    result_object = {}
    for instance in instances:
        reduction_http_req = calculatePercentageReductionSeries(instance.numberHttpRequest, comparatorInstance.numberHttpRequest)
        reduction_time = calculatePercentageReductionSeries(instance.meanExecutionTime, comparatorInstance.meanExecutionTime)
        
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
    return (result_object_means_http, result_object_http, result_object_means_time, result_object_time)