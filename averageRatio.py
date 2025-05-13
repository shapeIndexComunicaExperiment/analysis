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
from plotsVariation import generate_stats
from plotsVariation import calculatePercentageReductionSeries, statisticTemplateMetric
import os

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index")

typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "type index and ldp")

instances = [shapeIndexDataset]

(result_object_means_http, result_object_http, result_object_means_time, result_object_time) = generate_stats(instances, typeIndexLdpDataset)

res = result_object_time["shape index"]
res_flaten = [item for row in res for item in row]
clean_mean_time = [x**-1 for x in res_flaten if str(x) != 'nan']
summary = {
    "avg": statistics.mean(clean_mean_time),
    "std": statistics.stdev(clean_mean_time),
    "min": min(clean_mean_time),
    "max": max(clean_mean_time)
}

print(summary)