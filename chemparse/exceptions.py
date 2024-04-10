class ChemparseError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ParenthesesMismatchError(ChemparseError):
    def __init__(self, formula:str) -> None:
        super().__init__(f"Open and closed parentheses mismatch in formula '{formula}'")


class NestedParenthesesError(ChemparseError):
    def __init__(self, formula:str) -> None:
        super().__init__(f"Cannot parse nested parentheses in formula '{formula}'")


class ClosedParenthesesBeforeOpenError(ChemparseError):
    def __init__(self, formula:str) -> None:
        super().__init__(f"Closed parentheses detected before open parentheses in formula '{formula}'")