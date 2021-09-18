from unittest import mock
from unittest.mock import patch

import openeihttp
import pytest


pytest_plugins = "pytest_homeassistant_custom_component"


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    yield


@pytest.fixture(name="mock_api")
def mock_api():
    """Mock the library calls."""
    with patch("custom_components.openei.openeihttp.Rates") as mock_api:
        # mock_api = mock.Mock(spec=openeihttp.Rates)
        mock_api.return_value.current_rate = 0.24477
        mock_api.return_value.distributed_generation = "Net Metering"
        mock_api.return_value.approval = True
        mock_api.return_value.rate_name = 0.24477
        mock_api.return_value.mincharge = (10, "$/month")
        mock_api.return_value.lookup_plans = (
            '"Fake Utility Co": [{"name": "Fake Plan Name", "label": "randomstring"}]'
        )

        yield mock_api


@pytest.fixture(name="mock_api_config")
def mock_api_config():
    """Mock the library calls."""
    with patch("custom_components.openei.config_flow.openeihttp.Rates") as mock_api:
        # mock_api = mock.Mock()
        mock_api.return_value.lookup_plans = {
            "Fake Utility Co": [{"name": "Fake Plan Name", "label": "randomstring"}]
        }

        yield mock_api


@pytest.fixture(name="mock_sensors")
def mock_get_sensors():
    """Mock of get sensors function."""
    with patch("custom_components.openei.get_sensors", autospec=True) as mock_sensors:
        mock_sensors.return_value = {
            "current_rate": 0.24477,
            "distributed_generation": "Net Metering",
            "approval": True,
            "rate_name": "Fake Test Rate",
            "mincharge": 10,
            "mincharge_uom": "$/month",
        }
    yield mock_sensors
