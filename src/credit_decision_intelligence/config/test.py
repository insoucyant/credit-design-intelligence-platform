from credit_decision_intelligence.config.settings import get_settings, Settings

settings = get_settings()
print("\nChecking settings type: \n")
print(type(settings))
print("\nChecking settings values: \n\n")
print(settings)
print("\nChecking settings attributes: \n\n")
print(settings.__dict__)
print("\nChecking settings model dump: \n\n")
print(settings.model_dump())