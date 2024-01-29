''' 
takes the filled out variable level metadata template
and converts to json, validates, and saves json template to file
based on an explicit set of mapping functions

goes the other way (from json to csv as well)

see convert_templatecsv_to_json and convert_json_to_templatecsv
''' 
import petl as etl
import pandas as pd
from pathlib import Path
import collections
# from frictionless import Resource,Package
from healdata_utils.io import read_delim
from healdata_utils import schemas,utils,mappings
from healdata_utils.mappings import versions
from os import PathLike

def convert_templatecsv(
    csvtemplate: str,
    data_dictionary_props: dict,
    renamemap:dict=None,
    recodemap:dict=None,
    droplist:dict=None,
    item_sep:str="|", 
    keyval_sep:str="=",
    **kwargs
) -> dict:
    """
    [shortdesc]
    Converts a CSV conforming to HEAL specifications (but see 2 additional notes below) 
    into a HEAL-specified data dictionary in both csv format and json format.

    Converts an in-memory data dictionary or a path to a data dictionary file into a HEAL-specified tabular template by:
        1. Adding missing fields, and
        2. Converting fields from a specified mapping.
            NOTE: currently this mapping is only float/num to number or text/char to string (case insensitive)
                In future versions, there will be a specified module for csv input mappings.
    [shortdesc]
    
    Parameters
    ----------
    csvtemplate : str or path-like or an object that can be inferred as data by frictionless's Resource class.
        Data or path to data with the data being a tabular HEAL-specified data dictionary.
        This input can be any data object or path-like string excepted by a frictionless Resource object.
    data_dictionary_props : dict
        The HEAL-specified data dictionary properties.
    renamemap: A mapping of source (current) column headers to target (desired -- conforming to CVS HEAL spec)
        column headers 
    recodemap: A mapping of values for each column in HEAL spec -- {..."colname":{"oldvalue":"newvalue"...}...}
    droplist: a list of variables to drop from headers before processing
    item_sep:str (default:"|") Used to split stringified items (in objects and arrays)
    keyval_sep:str (default:"=") Used to split stringified each key-value pair

    Returns
    -------
    dict
        A dictionary with two keys:
            - 'templatejson': the HEAL-specified JSON object.
            - 'templatecsv': the HEAL-specified tabular template.

    """
    # get transforms
    # cast numbers explicitly based on schema
    # this is needed in case there is only one record in a string column that is a number (ie don't want to convert)


    def castnumbers(df,fields_schema):
        for fieldname,field in fields_schema.items(): 
            if fieldname in df:
                if field["type"] == "integer":
                    df[fieldname] = df[fieldname].apply(lambda s: int(float(s)) if s else s)
                elif field["type"] == "number":
                    df[fieldname] = df[fieldname].astype(float)
        
        return df

    def parse_dicts_and_lists(df,fields_schema):
        for fieldname,field in fields_schema.items(): 
            if fieldname in df:
                if field["type"] == "object":
                    newcol = df[fieldname].apply(utils.parse_dictionary_str,item_sep=item_sep,keyval_sep=keyval_sep)
                    df[fieldname] = newcol
                elif field["type"] == "array":
                    df[fieldname] = df[fieldname].apply(utils.parse_list_str,item_sep=item_sep)

        return df

    if isinstance(csvtemplate,(str,PathLike)):
        template_tbl = read_delim(str(Path(csvtemplate)))
    else:
        template_tbl = pd.DataFrame(csvtemplate)

    if not renamemap:
        renamemap = {}

    if not recodemap:
        recodemap = {}

    if not droplist:
        droplist = []

    fields_schema = utils.flatten_properties(schemas.healjsonschema["properties"]["fields"]["items"]["properties"])
    tbl_csv = (
        template_tbl
        .rename(columns=renamemap)
        .replace(recodemap)
        .drop(columns=droplist,errors="ignore")
        .pipe(castnumbers,fields_schema=fields_schema)
        .applymap(lambda v: utils.join_dictitems(v) if isinstance(v,collections.abc.MutableMapping) else v)
        .applymap(lambda v: utils.join_iter(v) if isinstance(v,collections.abc.MutableSequence) else v)
    )
    fields_csv = tbl_csv.to_dict(orient="records")

    refactored_props,tbl_json = (
        tbl_csv
        .pipe(parse_dicts_and_lists,fields_schema=fields_schema)
        .pipe(utils.refactor_field_props,schema=schemas.healjsonschema)
    )
    fields_json = [utils.unflatten_from_jsonpath(record) 
        for record in tbl_json.to_dict(orient="records")]

    data_dictionary_props_csv = dict(data_dictionary_props)
    data_dictionary_props_json = {**data_dictionary_props,**utils.unflatten_from_jsonpath(refactored_props)}

    template_json = dict(**data_dictionary_props_json,fields=fields_json)
    template_csv = dict(**data_dictionary_props_csv,fields=fields_csv)

    return {"templatejson":template_json,"templatecsv":template_csv}


def update_templatecsv_version(csvtemplate,data_dictionary_props,**kwargs):
    params = {
        "renamemap":mappings.versions.fields_renamemap,
        "recodemap":mappings.versions.fields_recodemap,
        "droplist":mappings.versions.fields_droplist,
        **kwargs
    }
    return convert_templatecsv(csvtemplate,data_dictionary_props,**params)
