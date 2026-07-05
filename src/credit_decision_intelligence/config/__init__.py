"""
    Configuration Package.
    
    Exposes the validated application settings object 
    and configuration schema.
"""
    
from credit_decision_intelligence.config.schema import Settings
from credit_decision_intelligence.config.settings import get_settings, settings
    
__all__ = [
    "Settings",
        "Settings",
    "get_settings",
    "settings",
]
    
# Test by running in bash :
# python -c "from credit_decision_intelligence.config import settings; print(settings.project.name)"


# So what we have now?
# config.yaml --> reader.py --> schema.py --> settings.py --> __init__.py --> rest of app
# When did config become a package?
# The moment we created a __init__.py empty file.
# What happened when we wrote what we wrote in this __init__.py file?
# We designed the public interface of the package. 
# Now another module can simply do: from credit_decision_intelligence.config import settings
# INSTEAD OF Ealier:
# from credit_decision_intelligence.config.settings import Settings
# It no longer cares whether settings comes from: 
# settings.py/provider.py/service.py/unicorn.py 
# This is called an API
# Every Package has two things:
# 1. Internal Implementation: schema.py, reader.py, settings.py
# 2. Public API: from credit_decision_intelligence.config import settings
# Expose the public API through package implementation 
# e.g., you do "import pandas as pd"
#  and NOT
# from pandas.core.frame.frame import DataFrame
# If we chnage settings.py to provider.py, nothing changes in outside code
# What does __all__ do?
# It simply tells Python:
# "These are the public things this package intentionally exports."
# Everything is considered internal 
# Think in terms of : "How should another developer use my package"
# The current architecture:
# train.py --> from credit_decision_intelligence.config import settings -->
# --> __init__.py
# __init__.py --> schema.py
# __init__.py --> settings.py --> reader.py --> config.yaml

