""" General utilities/helper functions"""
import re
from collections.abc import MutableMapping
import pandas as pd

def _get_propnames_to_rearrange(schema):
    """ 
    get data dictionary props to search for refactoring or embedding
    
    """

    annotation_names = ["title","description","name","additionalDescription"]
    root_names = flatten_properties(schema["properties"]).keys()
    field_names = flatten_properties(schema["properties"]["fields"]["items"]["properties"]).keys()
    names_to_rearrange = set(root_names).intersection(field_names).difference(annotation_names)

    return list(names_to_rearrange)

def embed_data_dictionary_props(flat_fields,flat_root,schema):
    """ 
    Embed (flattened) root level props in each (flattened) field
    if field level prop is missing but the field level prop exists
    and is not an annotation property (title,description). 
    
    Params
    
    flat_fields: array of dicts or pd.DataFrame (or something that can be converted into DataFrame)
    flat_root: dict or pd.Series or something that can be converted into Series 
    schema: schema for determining what fields should be embedded (note, this is flattened in fxn)
    
    Returns
    
    pd.DataFrame with the flat fields with the embedded root properties
    """
    flat_fields = pd.DataFrame(flat_fields)
    propnames = _get_propnames_to_rearrange(schema)
    flat_root = pd.Series(flat_root).loc[lambda s: s.index.isin(propnames)] # take out annotation props
    if len(flat_root) > 0:
        for propname in propnames:
            if propname in flat_root:
                if not propname in flat_fields:
                    flat_fields.insert(0,propname,flat_root[propname])
                else:
                    flat_fields[propname].fillna(flat_root[propname],inplace=True)

    return flat_fields

def refactor_field_props(flat_fields,schema):
    """ 
    given a flattened array of dicts corresponding to the unflattened schema,
    move up (ie `refactor`) flattened properties that are both in the root 
    (ie table level; level up from field records) and in the fields.

    """  
    flat_fields_df = pd.DataFrame(flat_fields)
    propnames = _get_propnames_to_rearrange(schema)
    flat_record = pd.Series(dtype="object")
    for name in propnames:
        if name in flat_fields_df:
            unique_val = flat_fields_df[name].unique() # NOTE: Includes NA values which is desired
            if len(unique_val) == 1:
                flat_record[name] = unique_val[0]
                flat_fields_df.drop(columns=name,inplace=True)

    return flat_record,flat_fields_df

# individual cell utilities
def strip_html(html_string):
    if html_string:
        return re.sub(r"<[^>]+>", "", html_string)
    else:
        return html_string


def to_int_if_base10(val):
    """
    converts value to a string and if
    float (or a string rep of a float) of base10
    to an integer string representation.

    NOTE:
    """
    string = str(val)

    if "." in string:
        parts = string.split(".")
        if len(parts) == 2 and parts[1] == "0":
            return parts[0]

    return string


def parse_dictionary_str(string, item_sep, keyval_sep):
    """
    parses a stringified dictionary into a dictionary
    based on item separator

    """
    if string != "" and string != None:
        stritems = string.strip().split(item_sep)
        items = {}

        for stritem in stritems:
            if stritem:
                item = stritem.split(keyval_sep, 1)
                items[item[0].strip()] = item[1].strip()
        
        return items
    else:
        return string


def parse_list_str(string, item_sep):
    if string != "" and string != None:
        return string.strip().split(item_sep)
    else:
        return string


# dictionary utilities
def flatten_to_jsonpath(dictionary,schema,parent_key=False, sep="."):
    """
    Turn a nested dictionary into a flattened dictionary (but see schema param)

    :param dictionary: The dictionary to flatten
    :param schema: The schema to indicate which properties to flatten
        This includes dictionaries (properties) with child dictionaries (properties)
        and lists (items) with child dictionaries (properties)
    :param parent_key: The string to prepend to dictionary's keys
    :param sep: The string used to separate flattened keys 
    :return: A flattened dictionary
    """
    # flatten if type array -> type object with properties
    # flatten if type object with properties
    items = []
    for key, value in dictionary.items():
        new_key = str(parent_key) + sep + key if parent_key else key
        prop = schema["properties"].get(key,{})
        childprops = prop.get("properties")
        childitem_props = prop.get("items",{}).get("properties")

        if childitem_props:
            for i,_value in enumerate(value):
                item = flatten_to_jsonpath(
                    dictionary=_value, 
                    schema=prop,
                    parent_key=new_key, 
                    sep=f"[{str(i)}]{sep}")
                items.extend(item.items())
        elif childprops:
            item = flatten_to_jsonpath(
                dictionary=value, 
                schema=prop,
                parent_key=new_key, 
                sep=sep)
            items.extend(item.items())

        else:
            items.append((new_key, value))

    return dict(items)

def stringify_keys(dictionary):
    orig_keys = list(dictionary.keys())
    for key in orig_keys:
        dictionary[str(key)] = dictionary.pop(key)

def unflatten_from_jsonpath(field):
    """
    Converts a flattened dictionary with key names conforming to 
    JSONpath notation to the nested dictionary format.
    """
    field_json = {}

    for prop_path, prop in field.items():
        prop_json = field_json

        # if isinstance(prop,list):
        #     prop = [v for val in prop if if val != None or val != ""]
        # elif isinstance(prop,dict):
        #     # filter falsey  values of "" and None
        #     prop = {key:val for key,val in prop.items() if val != None or val != ""}


        if prop:
            # Get the necessary info from the JSON path 
            nested_names = [re.sub("\[\d+\]$", "", prop_name) for prop_name in prop_path.split(".")]
            nested_indices = [re.findall("\[(\d+)\]$", prop_name)[-1] if re.search("\[(\d+)\]$", prop_name) else None for prop_name in prop_path.split(".")]

            for prop_name, array_index in zip(nested_names, nested_indices):
                is_last_nested = prop_name == nested_names[-1]

                if array_index is not None:
                    # Handle array properties
                    if prop_name not in prop_json:
                        prop_json[prop_name] = [None] * (int(array_index) + 1)

                    if is_last_nested:
                        if prop_json[prop_name][int(array_index)] is None:
                            prop_json[prop_name][int(array_index)] = {}
                        
                        if isinstance(prop_json[prop_name][int(array_index)], dict):
                            prop_json[prop_name][int(array_index)].update({prop_name: prop})
                        else:
                            prop_json[prop_name][int(array_index)] = {prop_name: prop}
                    else:
                        if prop_json[prop_name][int(array_index)] is None:
                            prop_json[prop_name][int(array_index)] = {}
                        
                        prop_json = prop_json[prop_name][int(array_index)]
                else:
                    # Handle non-array properties
                    if is_last_nested:
                        if prop_name not in prop_json:
                            prop_json[prop_name] = prop
                        else:
                            if isinstance(prop_json[prop_name], dict):
                                prop_json[prop_name].update({prop_name: prop})
                            else:
                                prop_json[prop_name] = {prop_name: prop}
                    else:
                        if prop_name not in prop_json:
                            prop_json[prop_name] = {}
                        
                        prop_json = prop_json[prop_name]

    return field_json

# json to csv utils
def join_iter(iterable,sep_list="|"):
    return sep_list.join([str(p) for p in iterable])

def join_dictvals(dictionary:dict,sep:str):
    return sep.join(dictionary.values())

def join_dictitems(dictionary:dict,sep_keyval='=',sep_items='|'):
    """ joins a mappable collection (ie dictionary) into a string
    representation with specified separators for the key and value
    in addition to items. 

    All items are coerced to the string representation (eg if key or value
    is None, this will be coerced to "None")


    """
    dict_list = []
    for key,val in dictionary.items():
        keystr = str(key)
        valstr = str(val)
        dict_list.append(keystr+sep_keyval+valstr)
    return sep_items.join(dict_list)


# documentation building utilities
def find_docstring_desc(fxn):
    """
    return the description part of a docstring
    (ie text before Parameters)
    """
    exp = "^(.*)Parameters\\n"

    if fxn.__doc__:
        docstring = fxn.__doc__.strip()
    else:
        docstring = "No documentation"
    try:
        return re.search(exp, docstring, re.DOTALL).group(1)
    except AttributeError:
        return docstring


# add missing values and order according to the order of a list


def sync_fields(data, field_list,missing_value=None):
    """
    Sorts fields and adds missing fields (with None value).
    If extra fields exist in a record that are not in field_list, then tacks on at 
    end of record.


    Parameters
    --------------
    data [list]: json array of values
    fields [list]: the list of all fields (e.g., from a schema)

    Returns
    -------------
    list: json array with fields added if missing
    """
    data_with_missing = []

    for record in data:
        extra_fields = list(set(list(record)).difference(field_list))
        new_record = {field:record.get(field, missing_value) 
            for field in field_list+extra_fields}
        data_with_missing.append(new_record)

    
    return data_with_missing


# %% 
# Working with schemas
def flatten_properties(properties, parentkey="", sep=".",itemsep="[0]"):
    """
    flatten schema properties
    """
    properties_flattened = {}
    for key, item in properties.items():
        # flattened keys
        if parentkey:
            flattenedkey = parentkey + "." + key
        else:
            flattenedkey = key

        if isinstance(item, MutableMapping):
            props = item.get("properties")
            items = item.get("items",{}).get("properties")
            if props:
                newprops = flatten_properties(props, parentkey=flattenedkey)
                properties_flattened.update(newprops)

            elif items:
                newprops = flatten_properties(items,parentkey=flattenedkey+itemsep)
                properties_flattened.update(newprops)
            else:
                properties_flattened[flattenedkey] = item
        
        else:
            properties_flattened[flattenedkey] = item
    
    return properties_flattened

def flatten_schema(schema):
    schema_flattened = dict(schema)
    properties = schema.get("properties")
    if properties:
        schema_flattened["properties"] = flatten_properties(properties)
    return schema_flattened