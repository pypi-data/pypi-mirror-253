from ashcrypt.utils.consts import Size


class IterationsOutofRangeError(Exception):
    def __init__(self, num: any) -> None:
        self.display = (
            f"Iterations must be between {Size.MIN_ITERATIONS} and {Size.MAX_ITERATIONS}."
            f" RECEIVED : {num}"
        )
        super().__init__(self.display)


class KeyLengthError(Exception):
    def __init__(self):
        self.display = f"Key must be hexadecimal and {Size.MAIN_KEY} bytes long !"
        super().__init__(self.display)
