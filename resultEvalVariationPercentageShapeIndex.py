import json
import sys
from generateDataset import generateDatasetFromResults
from metric import internalResultConsistency, calculatePercentageReductionSeries
import statistics

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index network 100%")

shapeIndex0PathResult = "./results/shape-index-0-percent/shape_index_result.json"
shapeIndex0PathSummary = "./results/shape-index-0-percent/summary_shape_index_result.json"
shapeIndex0Dataset = generateDatasetFromResults(shapeIndex0PathResult, shapeIndex0PathSummary, "shape index network 0%")

shapeIndex20PathResult = "./results/shape-index-20-percent/shape_index_result.json"
shapeIndex20PathSummary = "./results/shape-index-20-percent/summary_shape_index_result.json"
shapeIndex20Dataset = generateDatasetFromResults(shapeIndex20PathResult, shapeIndex20PathSummary, "shape index network 20%")

shapeIndex50PathResult = "./results/shape-index-50-percent/shape_index_result.json"
shapeIndex50PathSummary = "./results/shape-index-50-percent/summary_shape_index_result.json"
shapeIndex50Dataset = generateDatasetFromResults(shapeIndex50PathResult, shapeIndex50PathSummary, "shape index network 50%")

shapeIndex80PathResult = "./results/shape-index-80-percent/shape_index_result.json"
shapeIndex80PathSummary = "./results/shape-index-80-percent/summary_shape_index_result.json"
shapeIndex80Dataset = generateDatasetFromResults(shapeIndex80PathResult, shapeIndex80PathSummary, "shape index network 80%")