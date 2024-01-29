import shutil
from pathlib import Path
from healdata_utils.conversion import convert_to_vlmd,input_short_descriptions,choice_fxn
import json

from conftest import compare_vlmd_tmp_to_output
from conftest import valid_input_params,valid_output_json,valid_output_csv,fields_propname

def test_convert_to_vlmd_with_registered_formats():

    outputdir="tmp"
    for inputtype,_valid_input_params in valid_input_params.items():
   
        # make an empty temporary output directory
        try:
            Path(outputdir).mkdir()
        except FileExistsError:
            shutil.rmtree(outputdir)
            Path(outputdir).mkdir()

        data_dictionaries = convert_to_vlmd(**_valid_input_params)
        compare_vlmd_tmp_to_output(_valid_input_params)
    
        # clean up
        shutil.rmtree(outputdir)

def test_short_descriptions():
    
    assert input_short_descriptions.keys() == choice_fxn.keys()