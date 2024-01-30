#!/usr/bin/env python
import shutil 
import typer
from typing_extensions import Annotated
from typing import Optional
from pathlib import Path
from cookiecutter.main import cookiecutter

from datasource_tools.logic.process import metadata_process
from datasource_tools.logic.utils import (
    load_json, 
    write_json,
    check_filepaths_validity,
    remove_directory_files,
)

BASE_DIR: Path = Path(__file__).parent
CONFIG_DIR: Path = BASE_DIR / 'config'
TEMPLATE_DIR: Path = BASE_DIR / 'template_api'
TEMPLATE_DATAFILES_DIR: Path = TEMPLATE_DIR / '{{ cookiecutter.module_name }}' / 'files'
TEMPLATE_METADATAFILES_DIR: Path = TEMPLATE_DIR / '{{ cookiecutter.module_name }}' / 'metadata'


app = typer.Typer()


@app.callback()
def callback():
    """
    Kudaf Datasource Tools
    """
    ...


@app.command(name='metadata')
def gen_metadata(
    config_yaml_path: Annotated[Path, typer.Option(
        help="Absolute path to the YAML configuration file"
    )] = Path.cwd() / 'config.yaml',
    input_data_files_dir: Annotated[Path, typer.Option(
        help="Absolute path to the data files directory"
    )] = Path.cwd(),
    output_metadata_dir: Annotated[Path, typer.Option(
        help="Absolute path to directory where the Metadata files are to be written to" 
    )] = Path.cwd(),
):
    """
    Generate Variables/UnitTypes Metadata  

    JSON metadata files ('variables.json' and maybe 'unit_types.json') will be written to the \n
    (optionally) given output directory. \n

    If any of the optional directories is not specified, the current directory is used as default.

    """
    check_filepaths_validity([config_yaml_path, input_data_files_dir, output_metadata_dir])

    variables, mappings = metadata_process.generate(
        config_yaml_path, input_data_files_dir, output_metadata_dir, generate_api_files=False,
    )

    print(f"Generated Metadata (Variables and UnitTypes) available at: {output_metadata_dir}")

    return variables, mappings


@app.command(name='api')
def gen_api(
    config_yaml_path: Annotated[Path, typer.Option(
        help="Absolute path to the YAML configuration file"
    )] = Path.cwd() / 'config.yaml',
    input_data_files_dir: Annotated[Path, typer.Option(
        help="Absolute path to the data files directory"
    )] = Path.cwd(),
    output_api_dir: Annotated[Path, typer.Option(
        help="Absolute path to directory where the Datasource API folder is to be written to" 
    )] = Path.cwd(),
):
    """
    Generate a Kudaf Datasource REST API back-end 
    """
    check_filepaths_validity([config_yaml_path, input_data_files_dir, output_api_dir])

    variables, mappings = metadata_process.generate(
        config_yaml_path, input_data_files_dir, generate_api_files=True,
    )

    # # Update data mappings in cookiecutter config file
    # cookiecutter_config = load_json(TEMPLATE_DIR / "cookiecutter.json")
    # cookiecutter_config["variable_mappings"] = mappings
    # write_json(TEMPLATE_DIR / "cookiecutter.json", cookiecutter_config)
    
    # Initiate cookiecutter
    cookiecutter(
        template=str(TEMPLATE_DIR), 
        output_dir=str(output_api_dir), 
        overwrite_if_exists=True,
        no_input=True
    )
    
    # Clean up data files from template folders
    remove_directory_files(directory=TEMPLATE_DATAFILES_DIR)
    remove_directory_files(directory=TEMPLATE_METADATAFILES_DIR)
    
    # Reset cookiecutter.json file
    shutil.copyfile(src=CONFIG_DIR / 'cookiecutter.json', dst=TEMPLATE_DIR / 'cookiecutter.json')

    print(f"Generated FastAPI Datasource Backend API available at: {output_api_dir}")
    print(f"Generated Metadata (Variables and UnitTypes) available "
          "in the /metadata folder")

    return variables, mappings
