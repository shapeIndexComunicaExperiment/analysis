from generateDataset import generateDatasetFromResults
from plotsVariation import generate_stats, generatePlot
import os

artefactFolder = "./artefact/variation_approach"

color_map = {
    "shape index": '#1A85FF',
    "ldp": '#D41159',
    "type index and ldp": '#004D40',
}

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shape index")

ldpPathResult = "./results/standard/ldp_result.json"
ldpPathSummary = "./results/standard/summary_ldp_result.json"
ldpDataset = generateDatasetFromResults(ldpPathResult, ldpPathSummary, "ldp")

typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "type index and LDP")

instances = [shapeIndexDataset, ldpDataset]

(result_object_means_http, result_object_http, result_object_means_time, result_object_time) = generate_stats(instances, typeIndexLdpDataset)

generatePlot(
    result_object_time,
    'ratio execution time',
    len(instances),
    color_map=color_map,
    deactivate_y_axis=False,
    savePathNoExtension=os.path.join(artefactFolder,"reduction_query_execution_time")
    )

generatePlot(
    result_object_http,
    'ratio HTTP request',
    len(instances),
    color_map=color_map,
    deactivate_y_axis=False,
    savePathNoExtension=os.path.join(artefactFolder,"reduction_number_HTTP_requests")
    )