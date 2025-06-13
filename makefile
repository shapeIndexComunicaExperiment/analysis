# Output directory
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
  $(CONTINUOUS_PERFORMANCE_DIR)/dief_1.eps \
  $(CONTINUOUS_PERFORMANCE_DIR)/dief_1.svg \
  $(CONTINUOUS_PERFORMANCE_DIR)/dief_10.eps \
  $(CONTINUOUS_PERFORMANCE_DIR)/dief_10.svg \
  $(CONTINUOUS_PERFORMANCE_DIR)/termination_time.eps \
  $(CONTINUOUS_PERFORMANCE_DIR)/termination_time.svg \
  $(CONTINUOUS_PERFORMANCE_DIR)/first_result.eps \
  $(CONTINUOUS_PERFORMANCE_DIR)/first_result.svg \
  $(CONTINUOUS_PERFORMANCE_DIR)/table_continuous_performance.tex

HTTP_REQ_EXEC_TIME_RELATION_DIR = $(ARTEFACT_DIR)/http_req_exec_time_relation

OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION = \
  $(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor_better.eps \
  $(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor_better.svg \
  $(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor_worse.eps \
  $(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor_worse.svg \
  $(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor.eps \
  $(HTTP_REQ_EXEC_TIME_RELATION_DIR)/http_req_exec_time_cor.svg \
  $(HTTP_REQ_EXEC_TIME_RELATION_DIR)/stats.json

all: 
	$(MAKE) $(OUTPUTS_CONTINUOUS_PERFORMANCE)
	$(MAKE) $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)

$(OUTPUTS_CONTINUOUS_PERFORMANCE) &: ./notebooks/continuous_performance.py ./templates/table_continuous_performance.tex
	poetry run python ./notebooks/continuous_performance.py

$(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION) &: ./notebooks/linearity_reduction_rhttp_time.py
	poetry run python ./notebooks/linearity_reduction_rhttp_time.py

.PHONY: notebook

notebook:
	poetry run marimo edit
