from click.testing import CliRunner
from healdata_utils.cli import vlmd
from conftest import _compare_vlmd_tmp_to_output,compare_vlmd_tmp_to_output
from conftest import valid_input_params,valid_output_json,valid_output_csv,fields_propname
import shutil
import os
import json
from pathlib import Path

def test_vlmd_extract_all_params():

    for inputtype,_input_params in valid_input_params.items():

        # collect CLI arguments
        cli_params = ['extract']
        
        for paramname,param in _input_params.items():
            
            # add CLI options
            if paramname=="output_filepath":
                cli_params.append("--outputfile")
                cli_params.append(str(param))
            elif paramname=="input_filepath":
                cli_args = str(param)  # click argument
            elif paramname == "data_dictionary_props":
                for _paramname,_param in param.items():
                    cli_params.append("--prop")
                    cli_params.append(_paramname)
                    cli_params.append(_param)
            elif paramname == "sas_catalog_filepath":
                # CLI currently infers sas catalog file
                pass

            elif paramname in ["inputtype"]:
                cli_params.append(f"--{paramname.replace('_','-')}")
                cli_params.append(str(param))

        # make an empty temporary output directory
        _outdir = _input_params["output_filepath"].parent
        try:
            Path(_outdir).mkdir()
        except FileExistsError:
            shutil.rmtree(_outdir)
            Path(_outdir).mkdir()

        # add click arguments at end
        cli_params.append(cli_args)

        #run CLI
        runner = CliRunner()
        result = runner.invoke(vlmd, cli_params)

        assert result.exit_code == 0

        compare_vlmd_tmp_to_output(_input_params)
            # clean up
        shutil.rmtree(_outdir)


def test_vlmd_extract_minimal():

    for testname,testparams in valid_input_params.items():

        filepath = str(Path(testparams["input_filepath"]).resolve())
        inputtype = testparams["inputtype"]

        try:
            Path("tmp").mkdir()
        except FileExistsError:
            shutil.rmtree("tmp")
            Path("tmp").mkdir()

        os.chdir("tmp")

        # collect CLI arguments
        
        cli_params = ['extract',"--inputtype",inputtype,filepath]

        #run CLI
        runner = CliRunner()
        result = runner.invoke(vlmd, cli_params)

        assert result.exit_code == 0,result.output


        # clean up
        os.chdir("..")
        shutil.rmtree("tmp")


def test_vlmd_validate():

    paths = Path("data/valid/output").rglob("*")
    for path in paths:
        if path.is_file():
            runner = CliRunner()
            result = runner.invoke(vlmd, ['validate',str(path)])

            assert result.exit_code == 0,result.output


def test_vlmd_template():

    tmpdir = Path("tmp")

    if tmpdir.exists():
        shutil.rmtree(tmpdir)

    tmpdir.mkdir()

    runner = CliRunner()
    resultjson = runner.invoke(vlmd, ['template',"tmp/templatejson.json","--numfields","2"])
    resultcsv = runner.invoke(vlmd, ['template',"tmp/templatecsv.csv","--numfields","2"])

    assert resultjson.exit_code == 0,resultjson.output
    assert resultcsv.exit_code == 0,resultcsv.output

    # need to rename output files as the compare fxn uses same stem for csv and json
    # however, overwrite check looks for just the stem so need diff names in above fxn
    os.rename("tmp/templatejson.json","tmp/template.json")
    os.rename("tmp/templatecsv.csv","tmp/template.csv")

    csvoutput = Path("data/templates/twofields.csv").read_text().split("\n")
    jsonoutput = json.loads(Path("data/templates/twofields.json").read_text())

    _compare_vlmd_tmp_to_output("tmp/template",csvoutput,jsonoutput,fields_propname)

    shutil.rmtree(tmpdir) 

    



if __name__=="__main__":
    vlmd.main()





