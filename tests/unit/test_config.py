from pathlib import Path
import pytest 

from credit_decision_intelligence.config.reader import load_yaml_config
from credit_decision_intelligence.config.schema import Settings




def test_load_yaml_config_reads_valid_file(tmp_path: Path) -> None:
    config_file = tmp_path / "config.yaml"
    config_file.write_text(
    """ 
project:
    name: test-project
    version: 0.1.0
    environment: test
    
paths:
    data: data
    raw_data: data/raw
    interim_data: data/interim
    processed_data: data/processed
    models: models
    reports: reports
    logs: logs
    
logging:
    level: INFO
    format: json
    
model:
    random_seed: 42
    
api:
    host: 0.0.0.0
    port: 8000
    
mlflow:
    tracking_uri: http://localhost:5000
    experiment_name: test-experiment
    
monitoring:
    enabled: true

""",
        encoding="utf-8",
    )
    
    config = load_yaml_config(config_file)
    
    assert config["project"]["name"] == "test-project"
    assert config["api"]["port"] == 8000
    
def test_load_yaml_congig_raises_for_missing_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.yaml"
    
    with pytest.raises(FileNotFoundError):
        load_yaml_config(missing_file)



def test_settings_schema_validates_config() -> None:
    raw_config = {
        "project": {
            "name": "test-project",
            "version": "0.1.0",
            "environment": "test",
        },
        "paths": {
            "data": "data",
            "raw_data": "data/raw",
            "interim_data": "data/interim",
            "processed_data": "data/processed",
            "models": "models",
            "reports": "reports",
            "logs": "logs",
        },
        "logging": {
            "level": "INFO",
            "format": "json",
        },
        "model": {
            "random_seed": 42,
        },
        "api": {
            "host": "0.0.0.0",
            "port": 8000,
        },
        "mlflow": {
            "tracking_uri": "http://localhost:5000",
            "experiment_name": "test-experiment",
        },
        "monitoring": {
            "enabled": True,
        },
    }
    
    settings = Settings.model_validate(raw_config)
    
    assert settings.project.name == "test-project"
    assert settings.api.port == 8000
    assert settings.model.random_seed == 42
    
    
# Run in Bash
# "pytest tests/unit/test_config.py" 
# "pytest tests/unit/test_config.py -v"