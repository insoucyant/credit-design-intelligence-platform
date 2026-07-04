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
    Application Setting provider.
    
    This module creates and exposes the validated application settings object used across the
    Credit Decision Intelligence Platform.
"""

from functools import lru_cache
from pathlib import Path

from credit_decision_intelligence.config.reader import load_yaml_config
from credit_decision_intelligence.config.schema import Settings

DEFAULT_CONFIG_PATH = Path("configs/config.yaml")

# Why use @lru_cache?
# The @lru_cache decorator is used to cache the results of the get_settings function based on its input arguments. This means that if the function is called multiple times with the same config_path, it will return the cached result instead of reloading and parsing the configuration file again. This improves performance by avoiding redundant computations and ensures that the application uses a consistent set of configuration values throughout its lifecycle.
@lru_cache
def get_settings(
    config_path: Path = DEFAULT_CONFIG_PATH
    ) -> Settings:
    """Load, validate and return the application settings as a singleton."""

    raw_config = load_yaml_config(config_path)
    return Settings.model_validate(raw_config)


# Global Application Settings Singleton
settings = get_settings()

# Current Flow:
#   settings.py calls reader.py to read config.yaml
#   settings.py uses schema.py to validate it.

# RUn following in bash to check whether things are fine:
# python -c "from credit_decision_intelligence.config.settings import settings; print(settings.project.name); print(settings.api.port)"
