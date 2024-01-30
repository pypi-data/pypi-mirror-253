"""This module is used to encrypt and decrypt text data"""

from dataclasses import dataclass, field
from typing import Union, Optional

from ashcrypt import crypt as ac
from ashcrypt.utils import exceptions


@dataclass()
class Crypt:
    """Class to encrypt & decrypt data of type bytes or str"""
    data: Union[str, bytes] = field()
    key: str = field()

    def __post_init__(self):
        if self.keyverify(self.key) != 1:
            raise exceptions.dynamic.KeyLengthError()

    @staticmethod
    def genkey() -> str:
        """Generates a random 256-bit key as a hex string"""
        return ac.Enc.genkey()

    @staticmethod
    def keyverify(key: str) -> int:
        """Method to verify if the key is valid for usage"""
        try:
            a = bytes.fromhex(key.strip())
            if len(a) == 32:
                return 1
        except ValueError:
            return 0

    def encrypt(self,get_bytes: Optional[bool] = False) -> Union[bytes,str]:
        """Encrypts the given content of type bytes or str then returns the output
        as a URL-safe base64 encoded string or a bytes object if: get_bytes = True"""
        if self.data:
            try:
                ins = ac.Enc(self.data, self.key)
                return ins.encrypt() if get_bytes else ins.encrypt(get_bytes=True)
            except BaseException:
                raise exceptions.fixed.CryptError()
        else:
            raise exceptions.fixed.EmptyContentError()

    def decrypt(self,get_bytes: Optional[bool] = False) -> Union[bytes,str]:
        """Decrypts the given content of type bytes or str then returns the output
            as a UTF-8 encoded string or a bytes object if: get_bytes = True"""
        if self.data:
            try:
                dec_instance = ac.Dec(message=self.data, mainkey=self.key)
                return dec_instance.decrypt(get_bytes=True) if get_bytes else dec_instance.decrypt()
            except BaseException:
                raise exceptions.fixed.CryptError()
        else:
            raise exceptions.fixed.EmptyContentError()
