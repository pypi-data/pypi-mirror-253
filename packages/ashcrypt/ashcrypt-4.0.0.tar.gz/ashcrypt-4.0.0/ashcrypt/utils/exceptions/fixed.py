class MessageTamperingError(Exception):
    def __init__(self) -> None:
        self.display = (
            "HMAC mismatch ! Message has been TAMPERED with ,\n"
            " or Possible key difference"
        )
        super().__init__(self.display)


class EmptyContentError(Exception):
    def __init__(self):
        self.display = "Empty content !"
        super().__init__(self.display)


class GivenDirectoryError(Exception):
    def __init__(self):
        self.display = "Given directory instead of file"
        super().__init__(self.display)


class FileDoesNotExistError(Exception):
    def __init__(self):
        self.display = "Given path does not contain the specified file !"
        super().__init__(self.display)


class SysError(Exception):
    def __init__(self):
        self.display = "System related Error. Check if the file is busy !"
        super().__init__(self.display)


class FileCryptError(Exception):
    def __init__(self):
        self.display = "Error in enc/dec probable file distortion, message tampering or wrong key !"
        super().__init__(self.display)


class CryptError(Exception):
    def __init__(self):
        self.display = "Message tampering or wrong key !"
        super().__init__(self.display)


class AlreadyEncryptedError(Exception):
    def __init__(self):
        self.display = "File is already encrypted !"
        super().__init__(self.display)


class AlreadyDecryptedError(Exception):
    def __init__(self):
        self.display = "File is already decrypted !"
        super().__init__(self.display)
