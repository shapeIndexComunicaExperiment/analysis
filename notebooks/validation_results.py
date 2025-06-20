import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import json
    from texttable import Texttable
    import latextable
    from tabulate import tabulate
    import sys
    file_directory = "./"
    sys.path.append(file_directory)
    from generateDataset import generateDatasetFromResults
    from metric import internalResultConsistency
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.ticker import MultipleLocator
    from scipy.optimize import curve_fit
    from scipy.stats import pearsonr
    return generateDatasetFromResults, internalResultConsistency


@app.cell
def _(generateDatasetFromResults):
    ldpPathResult = "./results/standard/ldp_result.json"
    ldpPathSummary = "./results/standard/summary_ldp_result.json"
    ldpDataset = generateDatasetFromResults(ldpPathResult, ldpPathSummary, "ldp")
    return (ldpDataset,)


@app.cell
def _(generateDatasetFromResults):
    typeIndexLdpPathResult = "./results/standard/type_index_ldp_result.json"
    typeIndexLdpPathSummary = "./results/standard/summary_type_index_ldp_result.json"
    typeIndexLdpDataset = generateDatasetFromResults(typeIndexLdpPathResult, typeIndexLdpPathSummary, "typeIndexLdp")
    return (typeIndexLdpDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexPathResult = "./results/standard/shape_index_result.json"
    shapeIndexPathSummary = "./results/standard/summary_shape_index_result.json"
    shapeIndexDataset = generateDatasetFromResults(shapeIndexPathResult, shapeIndexPathSummary, "shapeIndex")
    return (shapeIndexDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndex0PathResult = "./results/shape-index-0-percent/shape_index_result.json"
    shapeIndex0PathSummary = "./results/shape-index-0-percent/summary_shape_index_result.json"
    shapeIndex0Dataset = generateDatasetFromResults(shapeIndex0PathResult, shapeIndex0PathSummary, "shapeIndex20Percent")
    return (shapeIndex0Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndex20PathResult = "./results/shape-index-20-percent/shape_index_result.json"
    shapeIndex20PathSummary = "./results/shape-index-20-percent/summary_shape_index_result.json"
    shapeIndex20Dataset = generateDatasetFromResults(shapeIndex20PathResult, shapeIndex20PathSummary, "shapeIndex20Percent")
    return (shapeIndex20Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndex50PathResult = "./results/shape-index-50-percent/shape_index_result.json"
    shapeIndex50PathSummary = "./results/shape-index-50-percent/summary_shape_index_result.json"
    shapeIndex50Dataset = generateDatasetFromResults(shapeIndex50PathResult, shapeIndex50PathSummary, "shapeIndex50Percent")
    return (shapeIndex50Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndex80PathResult = "./results/shape-index-80-percent/shape_index_result.json"
    shapeIndex80PathSummary = "./results/shape-index-80-percent/summary_shape_index_result.json"
    shapeIndex80Dataset = generateDatasetFromResults(shapeIndex80PathResult, shapeIndex80PathSummary, "shapeIndex80Percent")
    return (shapeIndex80Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexInnerPathResult = "./results/shape-inner/shape_index_result.json"
    shapeIndexInnerPathSummary = "./results/shape-inner/summary_shape_index_result.json"
    shapeIndexInnerDataset = generateDatasetFromResults(shapeIndexInnerPathResult, shapeIndexInnerPathSummary, "shapeInner")
    return (shapeIndexInnerDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeIndexMinimalPathResult = "./results/shape-minimal/shape_index_result.json"
    shapeIndexMinimalPathSummary = "./results/shape-minimal/summary_shape_index_result.json"
    shapeIndexMinimalDataset = generateDatasetFromResults(shapeIndexMinimalPathResult, shapeIndexMinimalPathSummary, "shapeMinimal")
    return (shapeIndexMinimalDataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeEntry20PathResult = "./results/shape-entry-20-percent/shape_index_result.json"
    shapeEntry20PathSummary = "./results/shape-entry-20-percent/summary_shape_index_result.json"
    shapeEntry20Dataset = generateDatasetFromResults(shapeEntry20PathResult, shapeEntry20PathSummary, "shapeEntry20Percent")
    return (shapeEntry20Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeEntry50PathResult = "./results/shape-entry-50-percent/shape_index_result.json"
    shapeEntry50PathSummary = "./results/shape-entry-50-percent/summary_shape_index_result.json"
    shapeEntry50Dataset = generateDatasetFromResults(shapeEntry50PathResult, shapeEntry50PathSummary, "shapeEntry50Percent")
    return (shapeEntry50Dataset,)


@app.cell
def _(generateDatasetFromResults):
    shapeEntry80PathResult = "./results/shape-entry-80-percent/shape_index_result.json"
    shapeEntry80PathSummary = "./results/shape-entry-80-percent/summary_shape_index_result.json"
    shapeEntry80Dataset = generateDatasetFromResults(shapeEntry80PathResult, shapeEntry80PathSummary, "shapeEntry80Percent")
    return (shapeEntry80Dataset,)


@app.cell
def _(
    ldpDataset,
    shapeEntry20Dataset,
    shapeEntry50Dataset,
    shapeEntry80Dataset,
    shapeIndex0Dataset,
    shapeIndex20Dataset,
    shapeIndex50Dataset,
    shapeIndex80Dataset,
    shapeIndexDataset,
    shapeIndexInnerDataset,
    shapeIndexMinimalDataset,
):
    evalInstances = [
        ldpDataset,
        shapeIndexDataset,
        shapeIndex0Dataset,
        shapeIndex20Dataset,
        shapeIndex50Dataset,
        shapeIndex80Dataset,
        shapeIndexInnerDataset,
        shapeIndexMinimalDataset,
        shapeEntry20Dataset,
        shapeEntry50Dataset,
        shapeEntry80Dataset
    ]
    return (evalInstances,)


@app.cell
def _(evalInstances, typeIndexLdpDataset):
    res = {}
    n_results_by_template_type_index = typeIndexLdpDataset.numberResults
    for _instance in evalInstances:
        res[_instance.name] = {}
        n_results_by_template = _instance.numberResults
        for _query_template, n_results_by_version in n_results_by_template_type_index.items():
            res[_instance.name][_query_template] = {}
            n_results_by_version = n_results_by_template[_query_template]
            for _version, n_results_type_index in enumerate(n_results_by_version):
                if n_results_type_index is not None:
                    n_results_instance = n_results_by_version[_version]
                    res[_instance.name][_query_template][f'v{_version}'] = {'base_line_results': True, 'same_n_results': n_results_type_index == n_results_instance}
                    if not n_results_type_index == n_results_instance:
                        print(f'instance {_instance.name} on query {_query_template} version {_version} do not have the same number of results')
                else:
                    n_results_instance = n_results_by_version[_version]
                    res[_instance.name][_query_template][f'v{_version}'] = {'base_line_results': False, 'same_n_results': n_results_type_index == n_results_instance}
    return (res,)


@app.cell
def _(res):
    res
    return


@app.cell
def _(evalInstances, internalResultConsistency, typeIndexLdpDataset):
    res_1 = {}
    _to_exclude = []
    for _instance in evalInstances + [typeIndexLdpDataset]:
        res_1[_instance.name] = {}
        for _query_template, _versions in _instance.results.items():
            res_1[_instance.name][_query_template] = {}
            for _version, _repetitions in _versions.items():
                if _repetitions is None:
                    continue
                _consistent = internalResultConsistency(_repetitions)
                if _consistent == False:
                    _to_exclude.append({'instance_name': _instance.name, 'query_template': _query_template, 'version': _version})
                    print(f'instance {_instance.name} on query {_query_template} version {_version} are not consistent')
                res_1[_instance.name][_query_template][_version] = {'consistent': _consistent}
    return (res_1,)


@app.cell
def _(res_1):
    res_1
    return


@app.cell
def _(evalInstances, internalResultConsistency, typeIndexLdpDataset):
    res_2 = {}
    _to_exclude = []
    for _instance in evalInstances + [typeIndexLdpDataset]:
        res_2[_instance.name] = {}
        for _query_template, _versions in _instance.results.items():
            res_2[_instance.name][_query_template] = {}
            for _version, _repetitions in _versions.items():
                if _repetitions is None:
                    continue
                _consistent = internalResultConsistency(_repetitions)
                if _consistent == False:
                    _to_exclude.append({'instance_name': _instance.name, 'query_template': _query_template, 'version': _version})
                    print(f'instance {_instance.name} on query {_query_template} version {_version} are not consistent')
                res_2[_instance.name][_query_template][_version] = {'consistent': _consistent}
    return


if __name__ == "__main__":
    app.run()
