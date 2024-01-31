import json
import pandas as pd
from collections import defaultdict
from typing import List
from ..models.pipeline_models import (IndexPairPipelineBean, CountResultOutputPipelineBean, SampleAnnotationPipelineBean, SampleResultModel)

def read_pipeline_output_json(pipeline_output_json_fn):
    with open(pipeline_output_json_fn) as fn:
        pipeline_output_json_dict = json.load(fn)
        
    # TODO: Could process into beans here, or just convert into DefaultDict. I prefer a fully processed structure
    return pipeline_output_json_dict

#
# Recursive function for pre-processing pipeline elements into canonical Python types
#
def process_pipeline_element(pipeline_element):
    if type(pipeline_element) is dict:
        if ('left' in pipeline_element.keys()) and ('right' in pipeline_element.keys()): # THIS IS A PAIR
            return (process_pipeline_element(pipeline_element["left"]), process_pipeline_element(pipeline_element["right"])) # RETURN AS TUPLE
        else: # THIS IS A MAP
            new_dict_wrapper = defaultdict()
            for key in pipeline_element.keys():
                pipeline_subelement = pipeline_element[key]
                new_dict_wrapper[key] = process_pipeline_element(pipeline_subelement)
            return new_dict_wrapper # RETURN AS DEFAULTDICT
    elif type(pipeline_element) is list: # THIS IS AN ARRAY
        new_list_wrapper = list()
        for pipeline_subelement in pipeline_element:
            new_list_wrapper.append(process_pipeline_element(pipeline_subelement))
        return new_list_wrapper # RETURN AS ARRAY
    else:
        return pipeline_element
        

"""
    IMPORTANT TODO:
    - Handle optional arguments (i.e. surrogate, barcode, read2 arguments). Maybe convert dict to default dict with None as default value
    - Need to ensure that the corresponding sample is the same between different indices of the output types: output_screen_countResults_map, output_screen_editingEfficiencies_map, output_screen_supplementaryFiles_map
        - Can do some assertions, or better yet, build a helper function that converts Maps/Pairs into Dict/
"""
def retrieve_sample_result_model_list(input_i5ToBarcodeToSampleInfoVarsMap,input_sampleInfoVarnames, output_screen_countResults_map, output_screen_editingEfficiencies_map, output_screen_supplementaryFiles_map, screen_id) -> List[SampleResultModel]:
    input_i5ToBarcodeToSampleInfoVarsMap_processed = process_pipeline_element(input_i5ToBarcodeToSampleInfoVarsMap)
    input_sampleInfoVarnames_processed = process_pipeline_element(input_sampleInfoVarnames)
    output_screen_countResults_map_processed = process_pipeline_element(output_screen_countResults_map)
    output_screen_editingEfficiencies_map_processed = process_pipeline_element(output_screen_editingEfficiencies_map)
    output_screen_supplementaryFiles_map_processed = process_pipeline_element(output_screen_supplementaryFiles_map)
    
    total_count_result: int = len(output_screen_countResults_map_processed[screen_id])
    
    sample_result_model_list: List[SampleResultModel] = []
    for index in range(0, total_count_result):
        index_pair_pipeline_bean = IndexPairPipelineBean(
                barcode_index =  output_screen_countResults_map_processed[screen_id][index][0][0]["barcodeIndex"],
                i5_index =  output_screen_countResults_map_processed[screen_id][index][0][0]["i5Index"],
                read1_fn =  output_screen_countResults_map_processed[screen_id][index][0][0]["read1"],
                read2_fn =  output_screen_countResults_map_processed[screen_id][index][0][0]["read2"]
            )
        
        sample_annotation_pipeline_bean = SampleAnnotationPipelineBean(
            sample_annotations_series = pd.Series(input_i5ToBarcodeToSampleInfoVarsMap_processed[index_pair_pipeline_bean.i5_index][index_pair_pipeline_bean.barcode_index], index=input_sampleInfoVarnames_processed)
        )
        
        count_result_output_pipeline_bean = None
        if (output_screen_countResults_map is not None) and (output_screen_editingEfficiencies_map is not None) and (output_screen_supplementaryFiles_map is not None):
            count_result_output_pipeline_bean = CountResultOutputPipelineBean(
                count_result_fn =  output_screen_countResults_map_processed[screen_id][index][1],
                screen_id = output_screen_countResults_map_processed[screen_id][index][0][0]["screenId"],

                protospacer_editing_efficiency = output_screen_editingEfficiencies_map_processed[screen_id][index][1]["protospacer_editing_efficiency"],
                surrogate_editing_efficiency = output_screen_editingEfficiencies_map_processed[screen_id][index][1]["surrogate_editing_efficiency"],
                barcode_editing_efficiency = output_screen_editingEfficiencies_map_processed[screen_id][index][1]["barcode_editing_efficiency"],

                match_set_whitelist_reporter_observed_sequence_counter_series_results_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["match_set_whitelist_reporter_observed_sequence_counter_series_results"],
                mutations_results_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["mutations_results"],
                linked_mutation_counters_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["linked_mutation_counters"],
                protospacer_total_mutation_histogram_pdf_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["protospacer_total_mutation_histogram_pdf"],
                surrogate_total_mutation_histogram_pdf_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["surrogate_total_mutation_histogram_pdf"],
                barcode_total_mutation_histogram_pdf_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["barcode_total_mutation_histogram_pdf"],
                surrogate_trinucleotide_mutational_signature_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["surrogate_trinucleotide_mutational_signature"],
                surrogate_trinucleotide_positional_signature_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["surrogate_trinucleotide_positional_signature"],
                whitelist_guide_reporter_df_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["whitelist_guide_reporter_df"],
                count_series_result_fn = output_screen_supplementaryFiles_map_processed[screen_id][index][1]["count_series_result"],
            )
        
        sample_result_model = SampleResultModel(
            index_pair_pipeline_bean = index_pair_pipeline_bean,
            count_result_output_pipeline_bean = count_result_output_pipeline_bean,
            sample_annotation_pipeline_bean = sample_annotation_pipeline_bean
        )
        
        sample_result_model_list.append(sample_result_model)
        
    return sample_result_model_list


"""
    IMPORTANT TODO:
    - Handle optional arguments (i.e. surrogate, barcode, read2 arguments). Maybe convert dict to default dict with None as default value
    - Need to ensure that the corresponding sample is the same between different indices of the output types: output_screen_countResults_map, output_screen_editingEfficiencies_map, output_screen_supplementaryFiles_map
        - Can do some assertions, or better yet, build a helper function that converts Maps/Pairs into Dict/
"""
def retrieve_demultiplex_sample_result_model_list(input_i5ToBarcodeToSampleInfoVarsMap,input_sampleInfoVarnames, output_screenIdToSampleMap, screen_id) -> List[SampleResultModel]:
    
    input_i5ToBarcodeToSampleInfoVarsMap_processed = process_pipeline_element(input_i5ToBarcodeToSampleInfoVarsMap)
    input_sampleInfoVarnames_processed = process_pipeline_element(input_sampleInfoVarnames)
    output_screenIdToSampleMap_processed = process_pipeline_element(output_screenIdToSampleMap)
    
    total_count_result: int = len(output_screenIdToSampleMap_processed[screen_id])
    
    sample_result_model_list: List[SampleResultModel] = []
    for index in range(0, total_count_result):
        index_pair_pipeline_bean = IndexPairPipelineBean(
                barcode_index =  output_screenIdToSampleMap_processed[screen_id][index][0]["barcodeIndex"],
                i5_index =  output_screenIdToSampleMap_processed[screen_id][index][0]["i5Index"],
                read1_fn =  output_screenIdToSampleMap_processed[screen_id][index][0]["read1"],
                read2_fn =  output_screenIdToSampleMap_processed[screen_id][index][0]["read2"]
            )
        
        sample_annotation_pipeline_bean = SampleAnnotationPipelineBean(
            sample_annotations_series = pd.Series(input_i5ToBarcodeToSampleInfoVarsMap_processed[index_pair_pipeline_bean.i5_index][index_pair_pipeline_bean.barcode_index], index=input_sampleInfoVarnames_processed)
        )
        
        sample_result_model = SampleResultModel(
            index_pair_pipeline_bean = index_pair_pipeline_bean,
            sample_annotation_pipeline_bean = sample_annotation_pipeline_bean
        )
        
        sample_result_model_list.append(sample_result_model)
        
    return sample_result_model_list    
    

def sample_result_model_to_series(sample_result_model: SampleResultModel) -> pd.Series:
    indices = []
    values = [] 
    
    indices.extend(sample_result_model.index_pair_pipeline_bean.__dict__.keys())
    values.extend(sample_result_model.index_pair_pipeline_bean.__dict__.values())
    
    if sample_result_model.count_result_output_pipeline_bean is not None:
        indices.extend(sample_result_model.count_result_output_pipeline_bean.__dict__.keys())
        values.extend(sample_result_model.count_result_output_pipeline_bean.__dict__.values())
    
    indices.extend(sample_result_model.sample_annotation_pipeline_bean.sample_annotations_series.index.values)
    values.extend(sample_result_model.sample_annotation_pipeline_bean.sample_annotations_series.values)
    
    return pd.Series(values, index=indices)
    
    
