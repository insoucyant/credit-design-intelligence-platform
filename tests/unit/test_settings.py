from pathlib import Path

from credit_decision_intelligence.config.settings import get_settings


def test_get_settings_loads_config_from_repo_root():
    settings = get_settings(str(Path("configs/config.yaml")))

    assert settings.project.name == "credit-decision-intelligence-platform"
    assert settings.api.port == 8000
