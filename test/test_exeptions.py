import pytest
import chemparse

species: list[str] = [
    ")(CH3)3",
    "(CH3)3)"
]

def test_errors(formula:str):
    with pytest.raises(Exception):
        chemparse.parse_formula(formula)


def pytest_generate_tests (metafunc:pytest.Metafunc):
    metafunc.parametrize("formula", species)