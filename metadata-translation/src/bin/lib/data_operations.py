## add ./lib directory to sys.path so that local modules can be found
import os, sys; sys.path.append(os.path.abspath("."))
# print(sys.path)


## system level modules
import pandas as pds
import jsonasobj
import json
import zipfile
import importlib

## add all classes for local nmdc.py
## this is the file of python classes generated by biolinkml
import nmdc



def make_dataframe(file_name, subset_cols=[], exclude_cols=[], nrows=None, lowercase_col_names=True,
                   replace_spaces=True, file_type="tsv", delimiter="\t", sheet_name=0, file_archive_name=""):
    """
    Builds a pandas dataframe from the designated file.
    
    Args:
        file_name: The name of the file containing the data for the dataframe. If the file is not in the same directory, then specify the path as part of the file name.
        subset_cols: Specifies a specific of subset of columns to be included in the dataframe.
        exclude_cols: Specifies a specific of subset of columns to be excluded from the dataframe.
        nrows: Specifies the number of rows to be returned in the dataframe (useful for testing).
        lowercase_col_names: If true, the column names are converted to lower case.
        replace_spaces: If true, spaces in column names are replaced with spaces.
        file_type: Speicfies the type of file. Current acceptable file types are tsv, csv, and excel. Note that when using excel, you may need to specify a sheet name.
        delimiter: Specifies the delimiter character used between fields.
        sheet_name: If the files is an Excel spreadsheet, this parameter specifies a particular sheet.
        archive_name: If the file_name is contained in an zip or file, this is the name of archive file.
    Returns:
        Pandas dataframe
    """
    ## normalize paramaters for use with pandas
    if len(subset_cols) < 1: subset_cols = None
    if len(exclude_cols) < 1: exclude_cols = None

    ## check if file is contained in an archive
    file_archive = None
    if len(file_archive_name) > 1:
        file_archive = zipfile.ZipFile(file_archive_name, "r")

    ## load data from file
    if "tsv" == file_type.lower() or "csv" == file_type.lower():
        if None != file_archive:
            df = pds.read_csv(file_archive.open(file_name), sep=delimiter, nrows=nrows)
        else:
            df = pds.read_csv(file_name, sep=delimiter, nrows=nrows)
    elif "excel" == file_type.lower():
        if None != file_archive:
            df = pds.read_excel(file_archive.open(file_name), sheet_name=sheet_name, nrows=nrows)
        else:
            df = pds.read_excel(file_name, sheet_name=sheet_name, nrows=nrows)

    ## clean column names
    df = clean_dataframe_column_names(df, lowercase_col_names, replace_spaces)

    ## create subset of columns
    ## note: since column names are case sensitive, this needs to happen after cleaning column names
    if subset_cols:
        df = df[subset_cols]

    ## return dataframe
    return df


def clean_dataframe_column_names(df, lowercase_col_names=True, replace_spaces=True):
    """
    Changes the column names of a dataframe into a standard format. The default settings change the column names to:
      - lower case
      - replaces spaces with underscores
    Args:
        df: The dataframe whose columns will be cleaned.
        lowercase_col_names: If true, the column names are converted to lower case.
        replace_spaces: If true, spaces in column names are replaced with spaces.
    Returns:
      Pandas dataframe
    """

        ## clean column names
    if lowercase_col_names:
        df.columns = [c.strip().lower() for c in df.columns]

    if replace_spaces:
        df.columns = [c.replace(" ", "_") for c in df.columns]

    return df



def make_dataframe_dictionary(file_name, subset_cols=[], exclude_cols=[], nrows=None, lowercase_col_names=True,
                              replace_spaces=True, file_type="tsv", delimiter="\t", sheet_name=0, file_archive_name=""):
    """
    Builds a dictionary based on the structure of the pandas dataframe generated from the designated file.
    The dictionary is oriented for records.
    E.g.:
      [
        {
          'col1': 1, 
          'col2': 0.5
        }, 
        {
          'col1': 2, 
          'col2': 0.75
        }
      ]

    Essentially, this function is a shortcut for calling make_dataframe() and then transforming the result into a dictionary. 
    E.g.:
      df = make_dataframe(file_name)
      dictdf = dictdf = df.to_dict(orient="records")
    
    
    Args:
        file_name: The name of the file containing the data for the dataframe. If the file is not in the same directory, then specify the path as part of the file name.
        subset_cols: Specifies a specific of subset of columns to be included in the dataframe.
        exclude_cols: Specifies a specific of subset of columns to be excluded from the dataframe.
        nrows: Specifies the number of rows to be returned in the dataframe (useful for testing).
        lowercase_col_names: If true, the column names are converted to lower case.
        replace_spaces: If true, spaces in column names are replaced with spaces.
        file_type: Speicfies the type of file. Current acceptable file types are tsv, csv, and excel. Note that when using excel, you may need to specify a sheet name.
        delimiter: Specifies the delimiter character used between fields.
        sheet_name: If the files is an Excel spreadsheet, this parameter specifies a particular sheet.
        archive_name: If the file_name is contained in an zip or file, this is the name of archive file.
    Returns:
        Dictionary built from a Pandas dataframe.
    """
    df = make_dataframe(file_name, subset_cols=[], exclude_cols=[], nrows=None, lowercase_col_names=True, \
                        replace_spaces=True, file_type="tsv", delimiter=delimiter, sheet_name=sheet_name, file_archive_name=file_archive_name)
    return df.to_dict(orient="records")



def make_json_string_list(dictionary, nmdc_class, id_key, name_key="", description_key="",
                          part_of_key="", has_input_key="", has_output_key="", characteristic_fields=[]):
    """
    Takes a dictionary in which each item is a record and returns a list of json strings build from each record.
    Args:
        dictionary: A python dictionary containing each record as an item.
        nmdc_class: The NMDC class (found in nmdc.py) that will be used to convert each record.
        id_key: The key in each record whose value is to be used as the id.
        name_key: The key in each record whose value is to be used as the name.
        description_key: The key in each record whose value is to be used as the description.
        part_of_key: The key in each record whose value is to be used as the part of value.
        has_input_key: The key in each record whose value is to be used as the has input value.
        has_output_key: The key in each record whose value is to be used as the has output value.
        characteristic_fields: A list that contains the names of fields whose values will transformed into characteristics.
    Returns:
        A list in which each item is a json string.
      
    """
    dict_list = \
        make_nmdc_dict_list(dictionary, nmdc_class, id_key, name_key=name_key, description_key=description_key,
                            part_of_key=part_of_key, has_input_key=has_input_key, has_output_key=has_output_key, characteristic_fields=characteristic_fields)

    return convert_dict_list_to_json_list(dict_list)


def convert_dict_list_to_json_list(dict_list):
    """
    Takes a list of dictionaries, converts each dictionary into json, and returns a list the json strings.
    Args:
      dict_list: A list in which each item is a dictionary.
    Returns:
      A list in which each item is a json string.
    """
    json_list = [] # list to hold json 

    ## iterate over dict list
    for d in dict_list:
        json_list.append(json.dumps(d))
        
    ## return final list
    return json_list


def make_nmdc_dict_list(dictionary, nmdc_class, id_key, name_key="", description_key="",
                        part_of_key="", has_input_key="", has_output_key="", characteristic_fields=[]):
    """
    Takes a dictionary in which each item is a record and returns a list of dictionaries that conform to the nmdc schema.
    Args:
        dictionary: A python dictionary containing each record as an item.
        nmdc_class: The NMDC class (found in nmdc.py) that will be used to convert each record.
        id_key: The key in each record whose value is to be used as the id.
        name_key: The key in each record whose value is to be used as the name.
        description_key: The key in each record whose value is to be used as the description.
        part_of_key: The key in each record whose value is to be used as the part of value.
        has_input_key: The key in each record whose value is to be used as the has input value.
        has_output_key: The key in each record whose value is to be used as the has output value.
        characteristic_fields: A list that contains the names of fields whose values will transformed into characteristics.
    Returns:
        A list in which each item is a dictionary that conforms to the nmdc schema
      
    """
    def make_characteristic_annotation(obj, key):
        """
        Local function used to create an annotation object with a characteristic that will be added to the set of annotations.
        """
        #print(key, value)
        c = nmdc.Characteristic(name=key)
        #ann = nmdc.Annotation(has_characteristic=c, has_raw_value=value) # this throws an error
        ann = nmdc.Annotation()
        ann.has_characteristic = c
        ann.has_raw_value = value

        return ann

        
    dict_list = [] # list to hold individual dictionary objects

    ## for each record in the dictionary, create an object of type nmdc_class,
    ## and put the object into the list
    for record in dictionary:
        ##  create object with id, name, , description, part of, input, and output info
        obj = nmdc_class()
        obj.id = record[id_key]
        if len(name_key.strip()) > 0:
            obj.name = record[name_key]
        if len(description_key.strip()) > 0:
            obj.description = record[description_key]
        if len(part_of_key.strip()) > 0:
            obj.part_of = record[part_of_key].split(",")
        if len(has_input_key.strip()) > 0:
            obj.has_input = record[has_input_key].split(",")
        if len(has_output_key.strip()) > 0:
            obj.has_output = record[has_output_key].split(",")

        ## add annotations to object
        for key, value in record.items():
            if (not pds.isnull(value)) and ('' != value) and not(value is None) and (key in characteristic_fields):
                obj.annotations.append(make_characteristic_annotation(obj, key))
                #print(obj)

        dict_obj = json.loads(jsonasobj.as_json(obj)) # in order to not save empty values you need to convert to json
        dict_list.append(dict_obj)                    # and then loads json to get dict; this may be a bug
                
    ## return final list
    return dict_list


def save_json_string_list(file_name, json_list):
    """
    Saves a list of json strings to a file.
    Args:
        file_name: The name of the file containing the data for the dataframe. If the file is not in the same directory, then specify the path as part of the file name.
        json_list: The list of json strings to be saved to file.
    Returns:
        Nothing.
    """
    ## merge json list into a single string
    json_str = "[\n" + ", ".join(json_list) + "\n]"

    with open(file_name, "w") as f:
        f.write(json_str)


def load_dict_from_json_file(file_name):
    """
    Creates and returns from a json file.
    Args:
      file_name: The name of the file containing the json formated data.
    Returns:
      A dict object containing the JSON dta.
    """
    with open(file_name, "r") as json_file:
        return json.load(json_file)
    
if __name__ == '__main__':
    print(os.path.abspath("./lib"))
