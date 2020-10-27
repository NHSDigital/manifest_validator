import pytest
import toml
from manifest_validator.validator import validate


def get_manifest(example_name):
    with open(f'tests/examples/{example_name}.toml', 'r') as f:
        return toml.load(f)


@pytest.fixture
def good_manifest():
    return get_manifest("good")

@pytest.fixture
def bad_manifest():
    return get_manifest("bad")

def test_good_manifest(good_manifest):
    assert(validate(good_manifest) == (True, {}))

def test_bad_manifest(bad_manifest):
    assert(validate(bad_manifest)[0] == False)
