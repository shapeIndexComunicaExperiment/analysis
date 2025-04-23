from generateDataset import generateDatasetFromResults
from plotsVariation import generate_stats, generatePlot
import os

artefactFolder = "./artefact/variation_approach"

ldpLabel = "LDP"
shapeIndexLabel = "shape index"
typeIndexLdpLabel = "type index"

color_map = {
    shapeIndexLabel: '#1A85FF',
    ldpLabel: '#D41159',
    typeIndexLdpLabel: '#004D40',
}

shapeIndexPathResult = "./results/standard/shape_index_result.json"
shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, shapeIndexLabel)

ldpPathResult = "./results/standard/ldp_result.json"
ldpPathSummary = "./results/standard/summary_ldp_result.json"
ldpDataset = generateDatasetFromResults(ldpPathResult, ldpPathSummary, ldpLabel)

typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, typeIndexLdpLabel)

instances = [shapeIndexDataset, ldpDataset]

(result_object_means_http, result_object_http, result_object_means_time, result_object_time) = generate_stats(instances, typeIndexLdpDataset)

query_to_skip = ["D8", "S2", "S3", "S6", "S7" ]

generatePlot(
    result_object_time,
    'ratio execution time',
    len(instances),
    color_map=color_map,
    ylim=None,
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
    savePathNoExtension=os.path.join(artefactFolder,"reduction_number_HTTP_requests"),
    formatYAxis = '{:.2f}'
    )