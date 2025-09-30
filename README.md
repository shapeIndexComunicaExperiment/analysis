# Analysis of the results of the paper Traveling with a Map: Optimizing the Search Space of Link Traversal Queries Using RDF Data Shapes

Python script and Marimo notebooks for analyzing the experiment results for the paper Traveling with a Map: Optimizing the Search Space of Link Traversal Queries Using RDF Data Shapes.
The figures and the table from the paper are generated from this repository in `./artefact`.
The `./results` folder contains the raw data of the experiment.
The notebook that generate the artefact are located in `./notebooks.`

## Online notebooks
The analysis notebooks are available as HTML pages in the `./docs` directory.

**View online:** https://shapeindexcomunicaexperiment.github.io/analysis/

## Description of the artifact

### `./artefact/http_req_exec_time_relation`
`./artefact/http_req_exec_time_relation` contains plots of the relation between HTTP request and the query execution time compared to the state-of-the-art approach, type index with LDP.
The file `./stats.json` presents some statistics about the curve of the plot.

### `./artefact/continuous_performance`
`./artefact/continuous_performance` contains plot of the continuous performance of the results.
We measure the `dief@t` at various time, the time of to get the first results, the termination time,
and the waiting time between results.

### `./artefact/query_containment_execution_time`
`./artefact/query_containment_execution_time` contains tables of the execution time of the query-shape containment algorithm in relation to different sets of shapes.

### `./artefact/ratio_useful_resources`
`./artefact/ratio_useful_resources` contains a table of the ratio of useful sources of the shape index approach and the state-of-the-art.

### `./statistical_significance`
`./statistical_significance` contains tables of the statistical significance of the difference in query execution time of different experiments.

### `./variation_approach`
`./variation_approach` contains plots of the reduction of the number of HTTP and query execution times of the shape index and LDP approach in relation to the state-of-the-art type index with LDP.

### `./variation_detail_shape`
`./variation_detail_shape` contains plots of the reduction of the number of HTTP and query execution time of the shape index with different levels of detail of shapes.

### `./variation_percentage_shape_index`
`./variation_percentage_shape_index` contains plots of the reduction of the number of HTTP and query execution times of the shape index in networks with different percentages of datasets having a shape index.

### `./artefact/variation_percentage_entry_shape_index`
`./variation_percentage_entry_shape_index` contains plots of the reduction of the number of HTTP and query execution time of the shape index in networks with different percentages of shape index entries having closed shapes as keys.

### `./variation_shape_index_all`
`./variation_percentage_entry_shape_index` contains a combined plot of the three previous plots.

## Dependencies
- [python 3](https://www.python.org/)

## Installation

```sh
poetry install
```

## Usage

## Marimo notebook

To launch the 

```sh
make notebook
```

The notebooks are located in `./notebooks`

## Generate the artifact
To generate all the artifacts run

```sh
make all -j
```
