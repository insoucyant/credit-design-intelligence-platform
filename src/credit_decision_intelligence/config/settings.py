# Why does settings.py exist? 
# It exists to provide a centralized location for configuration settings that can be easily accessed and modified throughout the application.
# This allows for better maintainability, as changes to configuration values can be made in one place rather than scattered throughout the codebase.
# Additionally, it helps to keep sensitive information, such as API keys or database credentials, separate from the main application logic, enhancing security and reducing the risk of accidental exposure.

# What problem does settings.py solve?
# settings.py solves the problem of managing configuration settings in a consistent and organized manner.
# It provides a single source of truth for configuration values, making it easier to update and maintain them.
# This is especially important in larger applications where configuration settings may be used in multiple places. 
# By centralizing these settings, developers can avoid duplication and ensure that changes are applied consistently across the application. 
# Additionally, it helps to prevent hardcoding sensitive information directly into the codebase, which can lead to security vulnerabilities.

# What should settings.py do?
# It should:
# 1. Define configuration variables that are used throughout the application.
# 2. Provide default values for these variables, which can be overridden by environment-specific settings
# 3. Load environment-specific settings from a separate file or environment variables, allowing for easy customization based on the deployment environment. 
# 4. Ensure that sensitive information, such as API keys or database credentials, is kept secure and not exposed in the codebase.


# Things to learn
# pathlib vs os.path: pathlib is a modern library for handling filesystem paths in a more object-oriented way, while os.path is an older module that provides functions for manipulating paths as strings. pathlib offers a more intuitive and readable syntax, making it easier to work with paths.
# BaseSettings VS BaseModel: BaseSettings is a class provided by Pydantic that is specifically designed for managing configuration settings. It allows you to define settings as class attributes and provides features like environment variable support and validation. BaseModel, on the other hand, is a more general-purpose class for defining data models with validation and serialization capabilities. While both classes can be used for configuration management, BaseSettings is more tailored for this purpose.
# lru_cache: lru_cache is a decorator provided by the functools module that allows you to cache the results of a function based on its input arguments. This can improve performance by avoiding redundant computations for the same inputs. In the context of settings.py, lru_cache can be used to cache configuration values that are expensive to compute or retrieve, reducing the overhead of repeatedly accessing them.
# Singleton pattern: The singleton pattern is a design pattern that restricts the instantiation of a class to a single instance. In the context of settings.py, it can be used to ensure that there is only one instance of the configuration settings throughout the application, preventing inconsistencies and ensuring that all parts of the application use the same configuration values.
# Typed configuration: Typed configuration refers to the practice of defining configuration settings with specific data types, allowing for better validation and type checking. This can help catch errors early and ensure that configuration values are used correctly throughout the application. By using typed configuration, developers can take advantage of features like autocompletion and type hints, improving code readability and maintainability.
# Environment variable overrides: Environment variable overrides allow developers to customize configuration settings based on the deployment environment. By using environment variables, developers can easily switch between different configurations without modifying the codebase. This is particularly useful for managing sensitive information, such as API keys or database credentials, as they can be stored securely in environment variables rather than hardcoded in the code.
# Why configuration loading should happen once: Configuration loading should happen once to ensure that the application has a consistent and reliable set of configuration values throughout its lifecycle. Loading configuration multiple times can lead to inconsistencies, increased overhead, and potential errors if different parts of the application are using different configurations. By loading configuration once, developers can ensure that all components of the application are using the same settings, improving maintainability and reducing the risk of bugs related to configuration mismatches.
# How FastAPI and MLflow will reuse the same settings: FastAPI and MLflow can reuse the same settings by importing the configuration module and accessing the configuration values as needed. This allows both frameworks to share a consistent set of configuration values, ensuring that they are using the same settings for things like database connections, API keys, or other environment-specific configurations. By centralizing the configuration in a single module, developers can easily manage and update settings for both FastAPI and MLflow without duplicating code or risking inconsistencies.

# Create settings.py in 5 small steps:
# 1. Design the configuration schema using Pydantic models (project, paths, logging, model, API, etc.)
# 2. Load and validate config.yaml
# 3. Support environment variables overrides when appropriate
# 4. Expose a cached singleton (settings) for the rest of the application to use
# 5. Write unit tests to verify configuration loading and validation

"""
    Application Configuration Schema.
    
    This module defines the typed configuration objects used across the
    Credit Decision Intelligence Platform.
"""

from pathlib import Path
from pydantic import BaseModel, Field

class ProjectConfig(BaseModel):
    """ Project Configuration Schema. Project Level Metadata."""
    
    name: str
    version: str
    environment: str = Field(default="development", description="The current environment of the application (e.g., development, production).")
    
class PathsConfig(BaseModel):
    """ Paths Configuration Schema. Defines important paths used in the application."""
    
    data: Path
    raw_data: Path
    interim_data: Path
    processed_data: Path
    models: Path
    reports: Path
    logs: Path
    
class LoggingConfig(BaseModel):
    """ Logging Configuration Schema. Defines Logging settings for the application."""
    level: str = Field(default="INFO", description="The logging level (e.g., DEBUG, INFO, WARNING, ERROR).")
    format: str = "json"  # Default logging format
    
class ModelConfig(BaseModel):
    """ Model Configuration Schema. Defines settings related to machine learning models."""
    
    random_seed: int = Field(default=42, ge=0, description="Random seed for reproducibility.")
    
    
class APIConfig(BaseModel):
    """ API Configuration Schema. Defines settings related to the API."""
    
    host: str = Field(default="0.0.0.0", description="The host address of the API server.")
    port: int = Field(default=8000, description="The port number on which the API server will listen.")
    
class MLflowConfig(BaseModel):
    """ MLflow Configuration Schema. Defines settings related to MLflow tracking and experiments."""
    
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