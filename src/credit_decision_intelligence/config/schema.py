"""
Configuration Schema Definitions.

The module defines the "typed configuration objects" used across 
the Credit Decision Intelligence Platform. 
These objects are designed to provide a structured and type-safe 
way to manage configuration settings, ensuring consistency and 
reliability throughout the system.

settings.py will load the configuration from a YAML file and instantiate these
objects, making them available for use in various components of the platform.


One concept --> One class:
* ForecastingConfig should only contain forecasting settings.
* EvaluationConfig should only contain evaluation related settings.

Separation-of-Concerns.
"""


from pathlib import Path

from pydantic import BaseModel, Field

class ProjectConfig(BaseModel):
    """
    
    ProjectConfig defines the configuration schema for a project within the 
    Crdeit Decision Intelligence Platform. It includes essential settings 
    such as the project name, description, and the path to the project's 
    configuration file. 
    """
    
    name: str = Field(..., description="The name of the project.")
    description: str = Field(None, description="A brief description of the project.")
    version: str = Field("0.1.0", description="The version of the project, defaulting to 0.1.0.")
    environment: str = Field("development", description="The environment for the project, defaulting to 'development'.")
    
    
class PathsConfig(BaseModel):
    """
    PathsConfig defines the configuration schema for various file paths used by the platform. 
    It includes paths for data storage, logs, and temporary files, ensuring that all components
    of the platform can access the necessary resources in a consistent manner.
    """
    
    data:Path = Field(..., description="The path to the data directory.")
    raw_data:Path = Field(..., description="The path to the raw data directory.")
    interim_data:Path = Field(..., description="The path to the interim data directory.")
    processed_data:Path = Field(..., description="The path to the processed data directory.")
    models:Path = Field(..., description="The path to the model directory")
    reports:Path = Field(..., description="The path to the reports directory.")
    logs:Path =  Field(..., description="The path to the logs directory.")
    
class LoggingConfig(BaseModel):
    """
    Logging Configuration 
    """
    """ Logging Configuration Schema. Defines Logging settings for the application."""
    level: str = Field(default="INFO", description="The logging level (e.g., DEBUG, INFO, WARNING, ERROR).")
    format: str = "json"  # Default logging format
    
class ModelConfig(BaseModel):
    """ Model Level Configuration"""
    """ Model Configuration Schema. Defines settings related to machine learning models."""
    
    random_seed: int = Field(default=42, ge=0, description="Random seed for reproducibility.")
    
class APIConfig(BaseModel):
    """ FastAPI service configuration."""
    
    host: str = Field(default="0.0.0.0", description="The host address of the API server.")
    port: int = Field(default=8000, ge=1, le=65535,  description="The port number on which the API server will listen.")
    
class MLflowConfig(BaseModel):
    """ MLflow experiment tracking configuration. """
    
    tracking_uri: str = Field(default="http://localhost:5000", description="The URI of the MLflow tracking server.")
    experiment_name: str = Field(default="default", description="The name of the MLflow experiment to use.")

class MonitoringConfig(BaseModel):
    """ Monitoring Configuration Schema. Defines settings related to monitoring and alerting."""
    
    enabled: bool = Field(default=True, description="Flag to enable or disable monitoring.")
    
    
class Settings(BaseModel):
    """ Main Settings Schema. Aggregates all configuration schemas into a single object."""
    
    project: ProjectConfig
    paths: PathsConfig
    logging: LoggingConfig
    model: ModelConfig
    api: APIConfig
    mlflow: MLflowConfig
    monitoring: MonitoringConfig  
    