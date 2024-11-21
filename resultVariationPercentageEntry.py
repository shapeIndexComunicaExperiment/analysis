from generateDataset import generateDatasetFromResults
from plotsVariation import generate_stats, generatePlot
import os

artefactFolder = "./artefact/variation_percentage_entry_shape_index"

color_map = {
    "shape index entries 100%": '#1A85FF',
    "shape index entries 0%": '#D41159',
    "shape index entries 20%": '#004D40',
    "shape index entries 50%": '#FFC107',
    "shape index entries 80%": '#994F00'
}

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index entries 100%")

shapeIndex20PathResult = "./results/shape-entry-20-percent/shape_index_result.json"
shapeIndex20PathSummary = "./results/shape-entry-20-percent/summary_shape_index_result.json"
shapeIndex20Dataset = generateDatasetFromResults(shapeIndex20PathResult, shapeIndex20PathSummary, "shape index entries 20%")

shapeIndex50PathResult = "./results/shape-entry-50-percent/shape_index_result.json"
shapeIndex50PathSummary = "./results/shape-entry-50-percent/summary_shape_index_result.json"
shapeIndex50Dataset = generateDatasetFromResults(shapeIndex50PathResult, shapeIndex50PathSummary, "shape index entries 50%")

shapeIndex80PathResult = "./results/shape-entry-80-percent/shape_index_result.json"
shapeIndex80PathSummary = "./results/shape-entry-80-percent/summary_shape_index_result.json"
shapeIndex80Dataset = generateDatasetFromResults(shapeIndex80PathResult, shapeIndex80PathSummary, "shape index entries 80%")

instances = [ shapeIndex20Dataset, shapeIndex50Dataset, shapeIndex80Dataset]

(result_object_means_http, result_object_http, result_object_means_time, result_object_time) = generate_stats(instances, shapeIndexDataset)

generatePlot(
    result_object_time,
    'ratio execution time',
    len(instances),
    color_map=color_map,
    deactivate_x_axis_title=False,
    savePathNoExtension=os.path.join(artefactFolder,"reduction_query_execution_time")
    )

generatePlot(
    result_object_http,
    'ratio HTTP request',
    len(instances),
    color_map=color_map,
    deactivate_x_axis_title=False,
    savePathNoExtension=os.path.join(artefactFolder,"reduction_number_HTTP_requests")
    )