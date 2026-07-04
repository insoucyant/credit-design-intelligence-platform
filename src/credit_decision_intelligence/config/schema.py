"""
Configuration Schema Definitions.

The module defines the "typed configuration objects" used across 
the Credit Decision Intelligence Platform. 
These objects are designed to provide a structured and type-safe 
way to manage configuration settings, ensuring consistency and 
reliability throughout the system.

settings.py will load the configuration from a YAML file and instantiate these
objects, making them available for use in various components of the platform.
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
