import os
import pytest

# Fixtures defined in conftest.py are available to all
# modules without needing to import them.
@pytest.fixture(autouse=True)
def setup_env():
    os.environ["UT_FRAMEWORK"] = "PYTEST"
