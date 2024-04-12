import sys
sys.path.insert(0, "..")    #look for "chemparse" module in the directory ".." in the first place
import pytest, chemparse, os
from chemparse.exceptions import ParenthesesMismatchError, ClosedParenthesesBeforeOpenError

print(f"{os.path.basename(__file__)}:\nLoading module {chemparse.__file__}")

species: dict[str,list[str]] = {
    "formula_NestedParenthesesError":['((CH3)2)3'],
    "formula_ParenthesesMismatchError":["(CH3)3)"],
    "formula_ClosedParenthesesBeforeOpenError":[")(CH3)3("]
}


def test_ParenthesesMismatchError(formula_ParenthesesMismatchError:str):
    with pytest.raises(ParenthesesMismatchError):
        chemparse.parse_formula(formula_ParenthesesMismatchError)


def test_ClosedParenthesesBeforeOpenError(formula_ClosedParenthesesBeforeOpenError:str):
    with pytest.raises(ClosedParenthesesBeforeOpenError):
        chemparse.parse_formula(formula_ClosedParenthesesBeforeOpenError)


def pytest_generate_tests (metafunc:pytest.Metafunc):
    metafunc.parametrize(metafunc.fixturenames[0], species[metafunc.fixturenames[0]])