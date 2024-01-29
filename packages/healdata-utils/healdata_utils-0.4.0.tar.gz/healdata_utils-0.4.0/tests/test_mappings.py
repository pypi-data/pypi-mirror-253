
from healdata_utils import mappings 

def test_versions_mapping_is_updated():
    mess = ("Check that you have the most updated schema version for mappings \n",
            f"Current mapping version: {'.'.join(mappings.versions.VERSION)} \n",
            f"Current schema version: {mappings.versions.healjsonschema['version']}")
    assert mappings.versions.VERSION == mappings.versions.healjsonschema["version"].split(".")[0:2],mess