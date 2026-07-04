"""
    Configuration File Reader.
    
    This module is reponsible only for reading and parsing configuration files.
    It does not validate the configuration schema. 
"""

from pathlib import Path
from typing import Any

import yaml 


def load_yaml_config(config_path: Path) -> dict[str, Any]:
    """ 
    Load and parse a YAMLconfiguration file into a dictionary.
    """
    
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as file:
        config_data = yaml.safe_load(file)
        
    if not isinstance(config_data, dict):
        raise ValueError(f"Configuration file must contain a dictionary at the root level/a YAML mapping: {config_path}")
    
    return config 
        