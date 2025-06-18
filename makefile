ARTEFACT_DIR = ./artefact

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
OUTPUT_RATIO_USEFUL_RESOURCES = $(RATIO_USEFUL_RESOURCES_DIR)/table_ratio_useful_resources_summary.tex

SHAPE_INDEX_VARIATION_ONE_PLOT_DIR = $(ARTEFACT_DIR)/variation_shape_index_all
OUT_SHAPE_INDEX_VARIATION_ONE_PLOT = $(SHAPE_INDEX_VARIATION_ONE_PLOT_DIR)/plot.eps \
	$(SHAPE_INDEX_VARIATION_ONE_PLOT_DIR)/plot.svg

all: 
	$(MAKE) $(OUTPUTS_CONTINUOUS_PERFORMANCE_DIEF)
	$(MAKE) $(OUTPUTS_CONTINUOUS_PERFORMANCE)
	$(MAKE) $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)
	$(MAKE) $(OUTPUTS_DETAIL_SHAPE)
	$(MAKE) $(OUTPUT_QUERY_CONTAINMENT)
	$(MAKE) $(OUTPUT_RATIO_USEFUL_RESOURCES)

$(OUTPUTS_CONTINUOUS_PERFORMANCE) &: ./notebooks/continuous_performance.py ./templates/table_continuous_performance.tex
	poetry run python ./notebooks/continuous_performance.py

$(OUTPUTS_CONTINUOUS_PERFORMANCE_DIEF) &: ./notebooks/dief_continuous_performance.py ./templates/dief_table_continuous_performance.tex
	poetry run python ./notebooks/dief_continuous_performance.py

$(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION) &: ./notebooks/linearity_reduction_http_time.py
	poetry run python ./notebooks/linearity_reduction_http_time.py

$(OUTPUTS_DETAIL_SHAPE) &: ./notebooks/variation_shape_details.py
	poetry run python ./notebooks/variation_shape_details.py

$(OUTPUT_QUERY_CONTAINMENT) &: ./notebooks/query-containment-execution-time.py
	poetry run python ./notebooks/query-containment-execution-time.py

$(OUTPUT_RATIO_USEFUL_RESOURCES) : ./notebooks/ratio_useful_sources.py ./templates/table_ratio_useful_resources_summary.tex
	poetry run python ./notebooks/ratio_useful_sources.py

$(OUT_SHAPE_INDEX_VARIATION_ONE_PLOT) &: ./notebooks/shape_index_variation_one_plot.py
	poetry run python ./notebooks/shape_index_variation_one_plot.py

.PHONY: notebook

notebook:
	poetry run marimo edit
