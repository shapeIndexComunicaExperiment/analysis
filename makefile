# Output directory
ARTEFACT_DIR = ./artefact
CONTINOUS_PERFORMANCE_DIR = $(ARTEFACT_DIR)/continuous_performance

OUTPUTS_CONTINOUS_PERFORMANCE = \
  $(CONTINOUS_PERFORMANCE_DIR)/raw_shape_index.json \
  $(CONTINOUS_PERFORMANCE_DIR)/raw_ldp.json \
  $(CONTINOUS_PERFORMANCE_DIR)/raw_type_index.json \
  $(CONTINOUS_PERFORMANCE_DIR)/summary_shape_index.json \
  $(CONTINOUS_PERFORMANCE_DIR)/summary_ldp.json \
  $(CONTINOUS_PERFORMANCE_DIR)/summary_type_index.json \
  $(CONTINOUS_PERFORMANCE_DIR)/shape_index_by_template.json \
  $(CONTINOUS_PERFORMANCE_DIR)/ldp_by_template.json \
  $(CONTINOUS_PERFORMANCE_DIR)/type_index_by_template.json \
  $(CONTINOUS_PERFORMANCE_DIR)/summary_shape_index_by_template.json \
  $(CONTINOUS_PERFORMANCE_DIR)/summary_ldp_by_template.json \
  $(CONTINOUS_PERFORMANCE_DIR)/summary_type_index_by_template.json \
  $(CONTINOUS_PERFORMANCE_DIR)/dief_1.eps \
  $(CONTINOUS_PERFORMANCE_DIR)/dief_1.svg \
  $(CONTINOUS_PERFORMANCE_DIR)/dief_10.eps \
  $(CONTINOUS_PERFORMANCE_DIR)/dief_10.svg \
  $(CONTINOUS_PERFORMANCE_DIR)/termination_time.eps \
  $(CONTINOUS_PERFORMANCE_DIR)/termination_time.svg \
  $(CONTINOUS_PERFORMANCE_DIR)/first_result.eps \
  $(CONTINOUS_PERFORMANCE_DIR)/first_result.svg \
  
HTTP_REQ_EXEC_TIME_RELATION_DIR = $(ARTEFACT_DIR)/http_req_exec_time_relation

OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION = \
  $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)/http_req_exec_time_cor_better.eps \
  $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)/http_req_exec_time_cor_better.svg \
  $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)/http_req_exec_time_cor_worse.eps \
  $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)/http_req_exec_time_cor_worse.svg \
  $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)/http_req_exec_time_cor.eps \
  $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)/http_req_exec_time_cor.svg \
  $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)/stats.json \

all: $(OUTPUTS_CONTINOUS_PERFORMANCE) $(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION)

$(OUTPUTS_CONTINOUS_PERFORMANCE): ./notebooks/continuous_performance.py
	poetry run ./notebooks/continuous_performance.py

$(OUTPUTS_HTTP_REQ_EXEC_TIME_RELATION) : ./notebooks/linearity_reduction_rhttp_time.py
  poetry run ./notebooks/linearity_reduction_rhttp_time.py

.PHONY: notebook

notebook:
	poetry run marimo edit