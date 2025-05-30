from generateDataset import generateDatasetFromResults
from plotsVariation import generate_stats, generatePlot
import os

artefactFolder = "./artefact/variation_detail_shape"

color_map = {
    "Full shape model": '#1A85FF',
    "Dataset shape model": '#D41159',
    "Minimal model": '#004D40',
}

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "Full shape model")

shapeIndexInnerPathResult = "./results/shape-inner/shape_index_result.json"
shapeIndexInnerPathSummary = "./results/shape-inner/summary_shape_index_result.json"
shapeIndexInnerDataset = generateDatasetFromResults(shapeIndexInnerPathResult, shapeIndexInnerPathSummary, "Dataset shape model")

shapeIndexMinimalPathResult = "./results/shape-minimal/shape_index_result.json"
shapeIndexMinimalPathSummary = "./results/shape-minimal/summary_shape_index_result.json"
shapeIndexMinimalDataset = generateDatasetFromResults(shapeIndexMinimalPathResult, shapeIndexMinimalPathSummary, "Minimal model")

instances = [shapeIndexInnerDataset, shapeIndexMinimalDataset]

(result_object_means_http, result_object_http, result_object_means_time, result_object_time) = generate_stats(instances, shapeIndexDataset)

query_to_skip = ["D8", "S2", "S3", "S6"]
generatePlot(
    result_object_time,
    'ratio execution time',
    len(instances),
    color_map=color_map,
    query_to_skip=query_to_skip,
    savePathNoExtension=os.path.join(artefactFolder,"reduction_query_execution_time")
    )

generatePlot(
    result_object_http,
    'ratio HTTP request',
    len(instances),
    color_map=color_map,
    query_to_skip=query_to_skip,
    ylim=None,
    savePathNoExtension=os.path.join(artefactFolder,"reduction_number_HTTP_requests")
    )