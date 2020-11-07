import os, sys
sys.path.append(os.path.abspath('../../../schema')) # add path nmdc schema files and modules

from lib.nmdc_etl_class import NMDC_ETL
import yaml
import json
from yaml import CLoader as Loader, CDumper as Dumper
from collections import namedtuple
from pprint import pprint
import pandas as pds
import jsonasobj
import nmdc
import lib.data_operations as dop
import align_nmdc_datatypes
import jq
from git_root import git_root

def get_json(file_path, replace_single_quote=False):
    ## load json
    with open(file_path, 'r') as in_file:
        if replace_single_quote: # json
            text = in_file.read()
            json_list = json.loads(text.replace("'", '"'))
        else:
            json_list =  json.load(in_file)
    return json_list


def save_json(json_list, file_path):
    ## save json with changed data types
    with open(file_path, 'w') as out_file:
        json.dump(json_list, out_file, indent=2)
    return json_list


def make_merged_data_source(spec_file='lib/nmdc_data_source.yaml', save_path='../data/nmdc_merged_data.tsv'):
    """Create a new data source containing the merged data sources"""

    mdf = dop.make_dataframe_from_spec_file (spec_file) # build merged data frame (mdf)
    mdf.to_csv(save_path, sep='\t', index=False) # save merged data
    print ('merged data frame length: ', len(mdf))

    return mdf


def make_json_etl(dataframe, nmdc_class, spec_class_name, spec_file='lib/nmdc_data_source.yaml', sssom_map_file=''):
    with open(spec_file, 'r') as input_file: # load data specificaiton info
        spec = yaml.load(input_file, Loader=Loader)
    
    ## specify attributes and constructor args
    attributes = spec['classes'][spec_class_name]['attributes']
    constructor = spec['classes'][spec_class_name]['constructor']

    attr_map = {}
    if len(sssom_map_file) > 0:
        ## load sssom mapping file and subset to skos:exactMatch
        mapping_df = dop.make_dataframe(sssom_map_file).query("predicate_id == 'skos:exactMatch'")
        attr_map = {subj:obj for idx, subj, obj in mapping_df[['subject_label', 'object_label']].itertuples()} # build attribute dict

    ## build json
    data_dictdf = dataframe.to_dict(orient="records") # transorm dataframe to dictionary
    data_json_list = dop.make_json_string_list \
        (data_dictdf, nmdc_class, constructor_map=constructor, attribute_fields=attributes, attribute_map=attr_map)
    
    ## return json
    return data_json_list


def make_nmdc_database():
    gold_study = get_json("output/nmdc_etl/gold_study.json")
    gold_biosample = get_json("output/nmdc_etl/gold_biosample.json")
    gold_project = get_json("output/nmdc_etl/gold_omics_processing.json")
    emsl_project = get_json("output/nmdc_etl/emsl_omics_processing.json")
    emsl_data_object = get_json("output/nmdc_etl/emsl_data_objects.json")
    jgi_data_object = get_json("output/nmdc_etl/jgi_fastq_data_objects.json")


    ## load aim 2 json files
    mg_annotation_activities = get_json('../data/aim-2-workflows/metagenome_annotation_activities.json')
    mg_annotation_data_objects = get_json('../data/aim-2-workflows/metagenome_annotation_data_objects.json')

    mg_assembly_activities = get_json('../data/aim-2-workflows/metagenome_assembly_activities.json')
    mg_assembly_data_objects = get_json('../data/aim-2-workflows/metagenome_assembly_data_objects.json')

    readQ_annotation_activities = get_json('../data/aim-2-workflows/readQC_activities.json')
    readQ_annotation_data_objects = get_json('../data/aim-2-workflows/readQC_data_objects.json')

    ## metaproteomic files
    hess_mp_analysis_activities = get_json('../data/aim-2-workflows/Hess_metaproteomic_analysis_activities.json')
    hess_mp_data_objects = get_json('../data/aim-2-workflows/Hess_emsl_analysis_data_objects.json')
    stegen_mp_analysis_activities = get_json('../data/aim-2-workflows/Stegen_metaproteomic_analysis_activities.json')
    stegen_mp_data_objects = get_json('../data/aim-2-workflows/Stegen_emsl_analysis_data_objects.json')

    database = \
    {
        "study_set": [*gold_study], 
        "omics_processing_set": [*gold_project, *emsl_project], 
        "biosample_set": [*gold_biosample], 
        "data_object_set": [*jgi_data_object, 
                            *emsl_data_object, 
                            *mg_annotation_data_objects, 
                            *mg_assembly_data_objects, 
                            *readQ_annotation_data_objects,
                            *hess_mp_data_objects,
                            *stegen_mp_data_objects],
        "activity_set": [*mg_annotation_activities, 
                         *mg_assembly_activities, 
                         *readQ_annotation_activities,
                         *hess_mp_analysis_activities,
                         *stegen_mp_analysis_activities]
    }

    save_json(database, "output/nmdc_database.json" )


def make_nmdc_example_database():
    ## load biosample json and get list of biosamples
    biosample_json = get_json('output/nmdc_etl/gold_biosample.json')
    biosample_test = json.loads(jq.compile('.[0:5]').input(biosample_json).text())
    biosample_list = jq.compile('.[0:5]| .[] | .id').input(biosample_json).text().replace('\n', ', ')

    ## load projects (omics processing)
    projects_json = get_json('output/nmdc_etl/gold_omics_processing.json')

    ## get list of associated projects from biosample
    # projects_list = jq.compile('.[] | .has_input[]').input(biosample_test).text().replace('\n', ', ')

    # projects_test = jq.compile('.[] | select(.id == (' + projects_list + '))').input(projects_json).text()
    projects_test = jq.compile('.[] | select(.has_input[]? == (' + biosample_list + '))').input(projects_json).text()
    projects_test = json.loads('[' + projects_test.replace('\n', ',') + ']') # put into correct json

    ## get list of studies
    study_list = jq.compile('.[] | .part_of[]').input(projects_test).text().replace('\n', ', ')
    study_list = ','.join(set(study_list.replace(' ', '').split(','))) # get unique list of study ids

    ## load study json
    study_json = get_json('output/nmdc_etl/gold_study.json')
    study_test = jq.compile('.[] | select(.id == (' + study_list + '))').input(study_json).text()
    study_test = json.loads('[' + study_test.replace('\n', ',') + ']') # put into correct json

    ## get outputs of projects
    data_objects_list = jq.compile('.[] | .has_output[]').input(projects_test).text().replace('\n', ', ')

    ## load data objects
    data_objects_json = get_json('output/nmdc_etl/jgi_fastq_data_objects.json')
    data_objects_test = jq.compile('.[] | select(.id == (' + data_objects_list + '))').input(data_objects_json).text().replace('\n', ', ')
    data_objects_test = json.loads('[' + data_objects_test.replace('\n', ',') + ']') # put into correct json


    ## compile into database object
    database = \
    {
      "study_set": [*study_test], 
      "omics_processing_set": [*projects_test], 
      "biosample_set": [*biosample_test], 
      "data_object_set": [*data_objects_test]
    }

    save_json(database, 'output/nmdc-03.json')

    
def main(data_file='../data/nmdc_merged_data.tsv.zip',
         etl_modules=['gold_study', 
                      'gold_omics_processing', 
                      'gold_biosample', 
                      'emsl_omics_processing',
                      'emsl_data_object', 
                      'jgi_data_object'],
         sssom_map_file=git_root('schema/mappings/gold-to-mixs.sssom.tsv'),
         spec_file='lib/nmdc_data_source.yaml'):

    
    nmdc_etl = NMDC_ETL(merged_data_file=data_file, data_source_spec_file=spec_file, sssom_file=sssom_map_file)
    
    if 'gold_study' in etl_modules:
        nmdc_etl.transform_study()
        # nmdc_etl.transform_study(test_rows=1, print_df=True, print_dict=True)
        nmdc_etl.save_study(file_path='output/nmdc_etl/gold_study.json')
    
    if 'gold_omics_processing' in etl_modules:
        nmdc_etl.transform_omics_proccessing()
        # nmdc_etl.transform_omics_proccessing(test_rows=1, print_df=True, print_dict=True)
        nmdc_etl.save_omics_proccessing(file_path='output/nmdc_etl/gold_omics_processing.json')

    if 'gold_biosample' in etl_modules:
        nmdc_etl.transform_biosample()
        # nmdc_etl.transform_biosample(test_rows=1, print_df=True, print_dict=True)
        nmdc_etl.save_biosample('output/nmdc_etl/gold_biosample.json')
        
        # align_nmdc_datatypes.align_gold_biosample() ########### currently broken

    if 'emsl_omics_processing' in etl_modules:
        emsl_json_op = make_json_etl(emsl, nmdc.OmicsProcessing, 'emsl_omics_processing')
        dop.save_json_string_list("output/nmdc_etl/emsl_omics_processing.json", emsl_json_op)
    
    if 'emsl_data_object' in etl_modules:
        emsl_json_do = make_json_etl(emsl, nmdc.DataObject, 'emsl_data_object')
        dop.save_json_string_list("output/nmdc_etl/emsl_data_objects.json", emsl_json_do)
        align_nmdc_datatypes.align_emsl_data_object()
        
    if 'jgi_data_object' in etl_modules:
        jgi_json_do = make_json_etl(fastq, nmdc.DataObject, 'jgi_data_object')
        dop.save_json_string_list("output/nmdc_etl/jgi_fastq_data_objects.json", jgi_json_do)
        align_nmdc_datatypes.align_jgi_data_object()


if __name__ == '__main__':
    # make_merged_data_source() # consolidates all nmdc data into a single tsv
    # main(etl_modules=['gold_biosample']) # test gold biosample etl
    # main(etl_modules=['gold_omics_processing']) # test gold project etl
    # main(etl_modules=['jgi_data_object']) # test jgi data object etl
    # main(etl_modules=['emsl_data_object']) # test emsl data object etl
    main() # run etl on all files
    make_nmdc_database() # combines output into database json format
    make_nmdc_example_database() # make example data
