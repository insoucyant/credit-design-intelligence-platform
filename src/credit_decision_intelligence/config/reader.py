"""
    Configuration File Reader.
    
    This module is reponsible only for reading and parsing configuration files.
    It does not validate the configuration schema. 
"""

from pathlib import Path
from typing import Any

import yaml # What does yaml_safeload do? 
#It is a function provided by the PyYAML library that safely loads YAML data from a string or file. 
# It parses the YAML content and converts it into Python objects, such as dictionaries, lists, and strings.
#The "safe" aspect of yaml.safe_load means that it only allows a subset of YAML features that are considered 
# safe to use, preventing the execution of arbitrary code or potentially harmful constructs that could be present
# in untrusted YAML input.


def load_yaml_config(config_path: Path) -> dict[str, Any]:
    """Load and parse a YAML configuration file into a dictionary."""

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as file:
        config_data = yaml.safe_load(file)

    if not isinstance(config_data, dict):
        raise ValueError(
            f"Configuration file must contain a dictionary at the root level/a YAML mapping: {config_path}"
        )

    return config_data

# reader.py should  not import "Pydantic" or "Settings".
# Its only job is: YAML file --> Python Dictionary
# Next is settings.py ST:
#   reader.py + schema.py --> va;idated settings object.
# settings.py decides which config file to use. 
# It passes the path into reader.py
# The reader open the YAMLfile and parses it. 
# In short, reader.py reads the YAMLfilr passed to it
# In this project that file is usually config.yaml

        