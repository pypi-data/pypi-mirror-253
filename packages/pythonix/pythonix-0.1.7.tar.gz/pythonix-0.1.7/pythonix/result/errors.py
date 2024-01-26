class ExpectError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class UnwrapError(Exception):
    def __init__(self):
        super().__init__("Found an unexpected value while unwrapping")


class IsNoneError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
