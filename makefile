RUN = poetry run python
MARIMO = poetry run marimo
ARTEFACT_DIR = ./artefact

NOTEBOOK_HTML = html_notebook

CONTINUOUS_PERFORMANCE_DIR = $(ARTEFACT_DIR)/continuous_performance

OUTPUTS_CONTINUOUS_PERFORMANCE = \
	$(CONTINUOUS_PERFORMANCE_DIR)/raw_shape_index.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/raw_ldp.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/raw_type_index.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/summary_shape_index.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/summary_ldp.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/summary_type_index.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/shape_index_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/ldp_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/type_index_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/summary_shape_index_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/summary_ldp_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/summary_type_index_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/termination_time.eps \
	$(CONTINUOUS_PERFORMANCE_DIR)/termination_time.svg \
	$(CONTINUOUS_PERFORMANCE_DIR)/first_result.eps \
	$(CONTINUOUS_PERFORMANCE_DIR)/first_result.svg \
	$(CONTINUOUS_PERFORMANCE_DIR)/table_continuous_performance.tex 

OUTPUTS_CONTINUOUS_PERFORMANCE_DIEF = \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_raw_shape_index.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_raw_ldp.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_raw_type_index.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_summary_shape_index.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_summary_ldp.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_summary_type_index.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_shape_index_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_ldp_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_type_index_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_summary_shape_index_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_summary_ldp_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_summary_type_index_by_template.json \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_1.eps \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_1.svg \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_10.eps \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_10.svg \
	$(CONTINUOUS_PERFORMANCE_DIR)/dief_table_continuous_performance.tex 

HTTP_REQ_EXEC_TIME_RELATION_DIR = $(ARTEFACT_DIR)/http_req_exec_time_relation

OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION = \
	$(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor_better.eps \
	$(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor_better.svg \
	$(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor_worse.eps \
	$(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor_worse.svg \
	$(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor.eps \
	$(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor.svg \
	$(HTTP_REQ_EXEC_TIME_RELATION_DIR)/stats.json 

DETAIL_SHAPE_DIR = $(ARTEFACT_DIR)/variation_detail_shape

OUTPUTS_DETAIL_SHAPE = \
	$(DETAIL_SHAPE_DIR)/reduction_number_HTTP_requests.eps \
	$(DETAIL_SHAPE_DIR)/reduction_number_HTTP_requests.svg \
	$(DETAIL_SHAPE_DIR)/reduction_query_execution_time.eps \
	$(DETAIL_SHAPE_DIR)/reduction_query_execution_time.svg 

QUERY_CONTAINMENT_DIR = $(ARTEFACT_DIR)/query_containment_execution_time
OUTPUT_QUERY_CONTAINMENT = \
	$(QUERY_CONTAINMENT_DIR)/fully_bounded/table_query_shape_containment_exec.md \
	$(QUERY_CONTAINMENT_DIR)/fully_bounded/table_query_shape_containment_exec.tex \
	$(QUERY_CONTAINMENT_DIR)/inner_dataset/table_query_shape_containment_exec.md \
	$(QUERY_CONTAINMENT_DIR)/inner_dataset/table_query_shape_containment_exec.tex \
	$(QUERY_CONTAINMENT_DIR)/minimal/table_query_shape_containment_exec.md \
	$(QUERY_CONTAINMENT_DIR)/minimal/table_query_shape_containment_exec.tex
	

RATIO_USEFUL_RESOURCES_DIR = $(ARTEFACT_DIR)/ratio_useful_resources
OUTPUT_RATIO_USEFUL_RESOURCES = \
	$(RATIO_USEFUL_RESOURCES_DIR)/table_ratio_useful_resources_summary.tex

SHAPE_INDEX_VARIATION_ONE_PLOT_DIR = $(ARTEFACT_DIR)/variation_shape_index_all
OUTPUT_SHAPE_INDEX_VARIATION_ONE_PLOT = $(SHAPE_INDEX_VARIATION_ONE_PLOT_DIR)/plot.eps \
	$(SHAPE_INDEX_VARIATION_ONE_PLOT_DIR)/plot.svg \
	$(NOTEBOOK_HTML)/variation_one_plot.html

STATISTICAL_SIGNIFICANCE_DIR = $(ARTEFACT_DIR)/statistical_significance
OUTPUT_STATISTICAL_SIGNIFICANCE = \
	$(STATISTICAL_SIGNIFICANCE_DIR)/comparaisonStateOfTheArt.tex 

VARIATION_APPROACH_DIR = $(ARTEFACT_DIR)/variation_approach
OUTPUT_VARIATION_APPROACH = $(VARIATION_APPROACH_DIR)/reduction_number_HTTP_requests.eps \
	$(VARIATION_APPROACH_DIR)/reduction_number_HTTP_requests.svg \
	$(VARIATION_APPROACH_DIR)/reduction_query_execution_time.svg \
	$(VARIATION_APPROACH_DIR)/reduction_query_execution_time.eps

OUTPUT_VARIATION_APPROACH_NET = $(VARIATION_APPROACH_DIR)/reduction_number_HTTP_requests_raw.eps \
	$(VARIATION_APPROACH_DIR)/reduction_number_HTTP_requests_raw.svg \
	$(VARIATION_APPROACH_DIR)/reduction_query_execution_time_raw.svg \
	$(VARIATION_APPROACH_DIR)/reduction_query_execution_time_raw.eps

VARIATION_PERCENTAGE_SI_ENTRY_DIR = $(ARTEFACT_DIR)/variation_percentage_entry_shape_index
OUTPUT_VARIATION_PERCENTAGE_ENTRY_SI = $(VARIATION_PERCENTAGE_SI_ENTRY_DIR)/reduction_number_HTTP_requests.eps \
	$(VARIATION_PERCENTAGE_SI_ENTRY_DIR)/reduction_number_HTTP_requests.svg \
	$(VARIATION_PERCENTAGE_SI_ENTRY_DIR)/reduction_query_execution_time.svg \
	$(VARIATION_PERCENTAGE_SI_ENTRY_DIR)/reduction_query_execution_time.eps

VARIATION_PERCENTAGE_SI_DIR = $(ARTEFACT_DIR)/variation_percentage_shape_index
OUTPUT_VARIATION_PERCENTAGE_SI = $(VARIATION_PERCENTAGE_SI_DIR)/reduction_number_HTTP_requests.eps \
	$(VARIATION_PERCENTAGE_SI_DIR)/reduction_number_HTTP_requests.svg \
	$(VARIATION_PERCENTAGE_SI_DIR)/reduction_query_execution_time.svg \
	$(VARIATION_PERCENTAGE_SI_DIR)/reduction_query_execution_time.eps

TARGETS = \
	$(OUTPUTS_CONTINUOUS_PERFORMANCE_DIEF) \
	$(OUTPUTS_CONTINUOUS_PERFORMANCE) \
	$(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION) \
	$(OUTPUTS_DETAIL_SHAPE) \
	$(OUTPUT_QUERY_CONTAINMENT) \
	$(OUTPUT_RATIO_USEFUL_RESOURCES) \
	$(OUTPUT_SHAPE_INDEX_VARIATION_ONE_PLOT) \
	$(OUTPUT_STATISTICAL_SIGNIFICANCE) \
	$(OUTPUT_VARIATION_APPROACH) \
	$(OUTPUT_VARIATION_APPROACH_NET) \
	$(OUTPUT_VARIATION_PERCENTAGE_ENTRY_SI) \
	$(OUTPUT_VARIATION_PERCENTAGE_SI) \
	$(NOTEBOOK_HTML)/continuous_performance.html \
	$(NOTEBOOK_HTML)/dief_continuous_performance.html \
	$(NOTEBOOK_HTML)/relation_number_http_req_exec_time.html \
	$(NOTEBOOK_HTML)/variation_shape_detail.html \
	$(NOTEBOOK_HTML)/query_shape_subsumption_execution_time.html \
	$(NOTEBOOK_HTML)/ratio_useful_sources.html \
	$(NOTEBOOK_HTML)/statistical_significance.html \
	$(NOTEBOOK_HTML)/variation_approaches.html \
	$(NOTEBOOK_HTML)/variation_approaches_net.html \
	$(NOTEBOOK_HTML)/variation_percentage_shape_index_entry.html \
	$(NOTEBOOK_HTML)/variation_percentage_shape_index.html

all: $(TARGETS)
	
$(OUTPUTS_CONTINUOUS_PERFORMANCE) &: ./notebooks/continuous_performance.py ./templates/table_continuous_performance.tex
	$(RUN) ./notebooks/continuous_performance.py

$(NOTEBOOK_HTML)/continuous_performance.html: ./notebooks/continuous_performance.py
	$(MARIMO) export html ./notebooks/continuous_performance.py -o $(NOTEBOOK_HTML)/continuous_performance.html

$(OUTPUTS_CONTINUOUS_PERFORMANCE_DIEF) &: ./notebooks/dief_continuous_performance.py ./templates/dief_table_continuous_performance.tex
	$(RUN) ./notebooks/dief_continuous_performance.py

$(NOTEBOOK_HTML)/dief_continuous_performance.html: ./notebooks/dief_continuous_performance.py
	$(MARIMO) export html ./notebooks/dief_continuous_performance.py -o $(NOTEBOOK_HTML)/dief_continuous_performance.html

$(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION) &: ./notebooks/linearity_reduction_http_time.py
	$(RUN) ./notebooks/linearity_reduction_http_time.py

$(NOTEBOOK_HTML)/relation_number_http_req_exec_time.html: ./notebooks/linearity_reduction_http_time.py
	$(MARIMO) export html ./notebooks/linearity_reduction_http_time.py -o $(NOTEBOOK_HTML)/relation_number_http_req_exec_time.html

$(OUTPUTS_DETAIL_SHAPE) &: ./notebooks/variation_shape_details.py
	$(RUN) ./notebooks/variation_shape_details.py

$(NOTEBOOK_HTML)/variation_shape_detail.html: ./notebooks/variation_shape_details.py
	$(MARIMO) export html ./notebooks/variation_shape_details.py -o $(NOTEBOOK_HTML)/variation_shape_detail.html

$(OUTPUT_QUERY_CONTAINMENT) &: ./notebooks/query_containment_execution_time.py
	$(RUN) ./notebooks/query_containment_execution_time.py

$(NOTEBOOK_HTML)/query_shape_subsumption_execution_time.html: ./notebooks/query_containment_execution_time.py
	$(MARIMO) export html ./notebooks/query_containment_execution_time.py -o $(NOTEBOOK_HTML)/query_shape_subsumption_execution_time.html

$(OUTPUT_RATIO_USEFUL_RESOURCES) : ./notebooks/ratio_useful_sources.py ./templates/table_ratio_useful_resources_summary.tex
	$(RUN) ./notebooks/ratio_useful_sources.py

$(NOTEBOOK_HTML)/ratio_useful_sources.html: ./notebooks/ratio_useful_sources.py
	$(MARIMO) export html ./notebooks/ratio_useful_sources.py -o $(NOTEBOOK_HTML)/ratio_useful_sources.html

$(OUTPUT_SHAPE_INDEX_VARIATION_ONE_PLOT) &: ./notebooks/shape_index_variation_one_plot.py
	$(RUN) ./notebooks/shape_index_variation_one_plot.py

$(NOTEBOOK_HTML)/variation_one_plot.html: ./notebooks/shape_index_variation_one_plot.py
	$(MARIMO) export html ./notebooks/shape_index_variation_one_plot.py -o $(NOTEBOOK_HTML)/variation_one_plot.html

$(OUTPUT_STATISTICAL_SIGNIFICANCE): ./notebooks/statistical_significance.py
	$(RUN) ./notebooks/statistical_significance.py

$(NOTEBOOK_HTML)/statistical_significance.html: ./notebooks/statistical_significance.py
	$(MARIMO) export html ./notebooks/statistical_significance.py -o $(NOTEBOOK_HTML)/statistical_significance.html

$(OUTPUT_VARIATION_APPROACH) &: ./notebooks/variation_approach.py
	$(RUN) ./notebooks/variation_approach.py

$(NOTEBOOK_HTML)/variation_approaches.html: ./notebooks/variation_approach.py
	$(MARIMO) export html ./notebooks/variation_approach.py -o $(NOTEBOOK_HTML)/variation_approaches.html

$(OUTPUT_VARIATION_APPROACH_NET) &: ./notebooks/variation_net_approach.py
	$(RUN) ./notebooks/variation_net_approach.py

$(NOTEBOOK_HTML)/variation_approaches_net.html: ./notebooks/variation_net_approach.py
	$(MARIMO) export html ./notebooks/variation_net_approach.py -o $(NOTEBOOK_HTML)/variation_approaches_net.html

$(OUTPUT_VARIATION_PERCENTAGE_ENTRY_SI) &: ./notebooks/variation_percentage_shape_entries.py
	$(RUN) ./notebooks/variation_percentage_shape_entries.py

$(NOTEBOOK_HTML)/variation_percentage_shape_index_entry.html: ./notebooks/variation_percentage_shape_entries.py
	$(MARIMO) export html ./notebooks/variation_percentage_shape_entries.py -o $(NOTEBOOK_HTML)/variation_percentage_shape_index_entry.html

$(OUTPUT_VARIATION_PERCENTAGE_SI) &: ./notebooks/variation_percentage_shape_index.py
	$(RUN) ./notebooks/variation_percentage_shape_index.py

$(NOTEBOOK_HTML)/variation_percentage_shape_index.html: ./notebooks/variation_percentage_shape_index.py
	$(MARIMO) export html ./notebooks/variation_percentage_shape_index.py -o $(NOTEBOOK_HTML)/variation_percentage_shape_index.html

.PHONY: notebook clean

clean:
	rm -f $(TARGETS)

notebook:
	$(MARIMO) edit
