## author: Bill Duncan
## summary: Contians class with methods and properties for transforming data in NMDC ETL pipeline.

## add ./lib directory to sys.path so that local modules can be found
from git_root import git_root
import os, sys
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./lib"))
sys.path.append(os.path.abspath(git_root('schema'))) # add path nmdc schema files and modules
# print(sys.path)

import transform_nmdc_data as tx
import extract_nmdc_data as ex
import load_nmdc_data as lx
import nmdc_dataframes as nmdc_dfs
import nmdc

## system level modules
import pandas as pds
import jq
import jsonasobj
import json
import zipfile
import yaml
from yaml import CLoader as Loader, CDumper as Dumper
from dotted_dict import DottedDict
from collections import namedtuple

class NMDC_ETL():
    ## merged datafame that holds all the data
    merged_dataframe = None
    
    ## tables from merged dataset
    study_table = None
    contact_table = None
    proposals_table = None
    project_table = None
    jgi_emsl_table = None
    emsl_table = None
    emsl_biosample_table = None
    fastq_table = None
    project_biosample_table = None
    biosample_table = None
    
    ## dataframes built from tables
    study = None # gold studies
    emsl = None # emsl projects / data objects
    # data_objects = None # jgi data objects
    fastq = None 
    biosample = None # gold biosamples
    project = None # gold projects
    
    ## dicts that result from transformation methods
    study_dict = None
    omics_processing_dict = None
    biosample_dict = None
    emsl_omics_processing_dict = None
    emsl_data_object_dict = None
    jgi_data_object_dict = None
    
    # dict to hold the datasource spec
    data_source_spec = None
    
    # dict to hold sssom mappings
    sssom_map = None
    
    def __init__(self, merged_data_file, data_source_spec_file, sssom_file):
        ## create merged dataframe
        self.merged_dataframe = pds.read_csv(merged_data_file, sep='\t', dtype=str)
        
        ## build data source specfication
        with open(data_source_spec_file, 'r') as input_file:
            self.data_source_spec = yaml.load(input_file, Loader=Loader)
            
        ## build sssom mapping
        self.sssom_map = tx.make_attribute_map(sssom_file)  
        
        ## Extract tables from merged dataset
        self.study_table = ex.extract_table(self.merged_dataframe, 'study_table')
        self.contact_table = ex.extract_table(self.merged_dataframe, 'contact_table')
        self.proposals_table = ex.extract_table(self.merged_dataframe, 'proposals_table')
        self.project_table = ex.extract_table(self.merged_dataframe, 'project_table')
        self.jgi_emsl_table = ex.extract_table(self.merged_dataframe, 'ficus_jgi_emsl')
        self.emsl_table = ex.extract_table(self.merged_dataframe, 'ficus_emsl')
        self.emsl_biosample_table = ex.extract_table(self.merged_dataframe, 'ficus_emsl_biosample')
        self.fastq_table = ex.extract_table(self.merged_dataframe, 'ficus_fastq_table')
        self.project_biosample_table = ex.extract_table(self.merged_dataframe, 'project_biosample_table')
        self.biosample_table = ex.extract_table(self.merged_dataframe, 'biosample_table')
        
        ## build dataframes from tables
        self.study = \
            nmdc_dfs.make_study_dataframe(self.study_table, self.contact_table, self.proposals_table) # gold studies
        self.emsl = \
            nmdc_dfs.make_emsl_dataframe(self.emsl_table, self.jgi_emsl_table, self.study_table, self.emsl_biosample_table) # emsl projects / data objects
        # self.data_objects = nmdc_dfs.make_data_objects_dataframe(self.faa_table, self.fna_table, self.fastq_table, self.project_table) # jgi data objects
        self.fastq = \
            nmdc_dfs.make_jgi_fastq_dataframe(self.fastq_table, self.project_table)
        self.biosample = \
            nmdc_dfs.make_biosample_dataframe(self.biosample_table, self.project_biosample_table, self.project_table) # gold biosamples
        self.project = \
            nmdc_dfs.make_project_dataframe(self.project_table, self.study_table, self.contact_table, self.fastq, self.project_biosample_table, self.biosample) # gold projects
        
    @staticmethod
    def transform_dataframe(nmdc_df:pds.DataFrame,
                            nmdc_class,
                            constructor_map={}, 
                            attribute_fields=[], 
                            attribute_map={},
                            test_rows=0, 
                            print_df=False, 
                            print_dict=False,
                            remove_key_attributes=True,
                            add_attribute=True):
        
        ## used for testing
        if test_rows != 0: 
            nmdc_df = nmdc_df.head(test_rows)
        if print_df:
            print(nmdc_df)
        
        ## create nmdc dict of data from dataframe   
        nmdc_dict = \
            tx.dataframe_to_dict(nmdc_df, 
                                 nmdc_class, 
                                 constructor_map=constructor_map, 
                                 attribute_fields=attribute_fields, 
                                 attribute_map=attribute_map,
                                 remove_key_attributes=remove_key_attributes,
                                 add_attribute=add_attribute)
        
        ## used for testing
        if print_dict:
            print(nmdc_dict)
            
        return nmdc_dict
    
    
    def transform_study(self, data_source_class='gold_study', test_rows=0, print_df=False, print_dict=False):
        ## specify constructor args adn attributes
        constructor = self.data_source_spec['classes'][data_source_class]['constructor']
        attributes = self.data_source_spec['classes'][data_source_class]['attributes']
        
        self.study_dict = \
            NMDC_ETL.transform_dataframe(nmdc_df=self.study, 
                                         nmdc_class=nmdc.Study,
                                         constructor_map=constructor,
                                         attribute_fields=attributes,
                                         test_rows=test_rows,
                                         print_df=print_df,
                                         print_dict=print_dict)
        return self.study_dict
        
    
    def save_study(self, file_path='output/nmdc_etl/gold_study.json', data_format='json'):
        return lx.save_nmdc_dict(self.study_dict, file_path, data_format)

    
    def transform_omics_proccessing(self, data_source_class='gold_omics_processing', test_rows=0, print_df=False, print_dict=False):
        ## specify constructor args adn attributes
        constructor = self.data_source_spec['classes'][data_source_class]['constructor']
        attributes = self.data_source_spec['classes'][data_source_class]['attributes']
        
        self.omics_processing_dict = \
            NMDC_ETL.transform_dataframe(nmdc_df=self.project, 
                                         nmdc_class=nmdc.OmicsProcessing,
                                         constructor_map=constructor,
                                         attribute_fields=attributes,
                                         test_rows=test_rows,
                                         print_df=print_df,
                                         print_dict=print_dict)
        return self.omics_processing_dict

    
    def save_omics_proccessing(self, file_path='output/nmdc_etl/gold_omics_processing.json', data_format='json'):
        return lx.save_nmdc_dict(self.omics_processing_dict, file_path, data_format)

    
    def transform_biosample(self, data_source_class='gold_biosample', test_rows=0, print_df=False, print_dict=False):
        ## specify constructor args adn attributes
        constructor = self.data_source_spec['classes'][data_source_class]['constructor']
        attributes = self.data_source_spec['classes'][data_source_class]['attributes']
        
        self.biosample_dict = \
            NMDC_ETL.transform_dataframe(nmdc_df=self.biosample, 
                                         nmdc_class=nmdc.Biosample,
                                         constructor_map=constructor,
                                         attribute_fields=attributes,
                                         test_rows=test_rows,
                                         print_df=print_df,
                                         print_dict=print_dict)
        return self.biosample_dict

    
    def save_biosample(self, file_path='output/nmdc_etl/gold_biosample.json', data_format='json'):
        return lx.save_nmdc_dict(self.biosample_dict, file_path, data_format)
    
    
    def transform_emsl_omics_processing(self, data_source_class='emsl_omics_processing', test_rows=0, print_df=False, print_dict=False):
        ## specify constructor args adn attributes
        constructor = self.data_source_spec['classes'][data_source_class]['constructor']
        attributes = self.data_source_spec['classes'][data_source_class]['attributes']
        
        self.emsl_omics_processing_dict = \
            NMDC_ETL.transform_dataframe(nmdc_df=self.emsl, 
                                         nmdc_class=nmdc.OmicsProcessing,
                                         constructor_map=constructor,
                                         attribute_fields=attributes,
                                         test_rows=test_rows,
                                         print_df=print_df,
                                         print_dict=print_dict)
        
        return self.emsl_omics_processing_dict
        
    
    def save_emsl_omics_processing(self, file_path='output/nmdc_etl/emsl_omics_processing.json', data_format='json'):
        return lx.save_nmdc_dict(self.emsl_omics_processing_dict, file_path, data_format)
    
    
    def transform_emsl_data_object(self, data_source_class='emsl_data_object', test_rows=0, print_df=False, print_dict=False):
        ## specify constructor args adn attributes
        constructor = self.data_source_spec['classes'][data_source_class]['constructor']
        attributes = self.data_source_spec['classes'][data_source_class]['attributes']
        
        self.emsl_data_object_dict = \
            NMDC_ETL.transform_dataframe(nmdc_df=self.emsl, 
                                         nmdc_class=nmdc.DataObject,
                                         constructor_map=constructor,
                                         attribute_fields=attributes,
                                         test_rows=test_rows,
                                         print_df=print_df,
                                         print_dict=print_dict)
        
        return self.emsl_data_object_dict
        
    
    def save_emsl_data_object(self, file_path='output/nmdc_etl/emsl_data_objects.json', data_format='json'):
        return lx.save_nmdc_dict(self.emsl_data_object_dict, file_path, data_format)
    
    
    def transform_jgi_data_object(self, data_source_class='jgi_data_object', test_rows=0, print_df=False, print_dict=False):
        ## specify constructor args adn attributes
        constructor = self.data_source_spec['classes'][data_source_class]['constructor']
        attributes = self.data_source_spec['classes'][data_source_class]['attributes']
        
        self.jgi_data_object_dict = \
            NMDC_ETL.transform_dataframe(nmdc_df=self.fastq, 
                                         nmdc_class=nmdc.DataObject,
                                         constructor_map=constructor,
                                         attribute_fields=attributes,
                                         test_rows=test_rows,
                                         print_df=print_df,
                                         print_dict=print_dict)
        
        return self.jgi_data_object_dict
        
    
    def save_jgi_data_object(self, file_path='output/nmdc_etl/jgi_fastq_data_objects.json', data_format='json'):
        return lx.save_nmdc_dict(self.jgi_data_object_dict, file_path, data_format)