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
  
  

all: $(OUTPUTS_CONTINOUS_PERFORMANCE)

$(OUTPUTS_CONTINOUS_PERFORMANCE): ./notebooks/continuous_performance.py
	python ./notebooks/continuous_performance.py
