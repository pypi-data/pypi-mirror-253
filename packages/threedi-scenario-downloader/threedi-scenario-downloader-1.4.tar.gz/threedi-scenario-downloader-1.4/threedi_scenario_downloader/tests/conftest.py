"""Test setup for all the tests, handled automatically by pytest"""
from pathlib import Path

import pytest

from threedi_scenario_downloader import downloader

API_KEY_FILENAME = "test_api_key.txt"


@pytest.fixture(scope="session", autouse=True)
def api_key_for_lizard() -> str:
    """Set up api key and return it"""
    api_key_file = Path(API_KEY_FILENAME)
    if not api_key_file.exists():
        raise RuntimeError(
            f"{API_KEY_FILENAME} not found: see the end of the README"
        )  # pragma: no cover
    api_key = api_key_file.read_text().strip()
    downloader.set_api_key(api_key)
    return api_key
