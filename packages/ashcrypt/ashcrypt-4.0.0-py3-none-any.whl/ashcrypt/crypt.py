"""This module provides classes and functions for AES-256 encryption and decryption"""


import base64
import hmac as hmc
import os
import struct
from typing import Optional, Union

import bcrypt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from ashcrypt.utils import exceptions
from ashcrypt.utils.consts import Size


class Enc:
    """Class to encrypt data of either type bytes or str"""

    def __init__(
        self,
        message: Union[str, bytes],
        mainkey: str,
        *,
        iterations: Optional[int] = Size.MIN_ITERATIONS
    ) -> None:
        if isinstance(message, str):
            self.message = message.encode()
        elif isinstance(message, bytes):
            self.message = message

        self.mainkey = mainkey
        if not self.keyverify(self.mainkey):
            raise exceptions.dynamic.KeyLengthError()
        self.iv = os.urandom(Size.IV)
        self.salt = os.urandom(Size.SALT)
        self.pepper = os.urandom(Size.PEPPER)
        self.iterations = iterations
        if (
            self.iterations < Size.MIN_ITERATIONS
            or self.iterations > Size.MAX_ITERATIONS
        ):
            raise exceptions.dynamic.IterationsOutofRangeError(self.iterations)

        self.enc_key = self.derkey(self.mainkey, self.salt, self.iterations)
        self.hmac_key = self.derkey(self.mainkey, self.pepper, self.iterations)

    @staticmethod
    def derkey(mainkey: str, salt_pepper: bytes, iterations: int) -> bytes:
        """AES Key & HMAC derivation function"""
        return bcrypt.kdf(
            password=mainkey.encode("UTF-8"),
            salt=salt_pepper,
            desired_key_bytes=Size.AES_KEY,
            rounds=iterations,
        )

    @staticmethod
    def genkey(desired_bytes: Optional[int] = 32) -> Union[str, bytes]:
        """Generates a random 256-bit ( by default )
        key as a hex string. Set the number of desired_bytes to a greater or equal to 32
        to override the default value"""
        if desired_bytes < 32:
            raise ValueError("desired_bytes must be greater or equal to 32")
        key = os.urandom(desired_bytes)
        return key.hex()

    @staticmethod
    def keyverify(key: str) -> int:
        try:
            a = bytes.fromhex(key.strip())
            if len(a) >= Size.MAIN_KEY:
                return 1
        except ValueError:
            return 0

    def _mode(self):
        """Returns AES Cipher Block Chaining (CBC) mode with the chosen initialization vector"""
        return modes.CBC(self.iv)

    def _cipher(self):
        """Creates AES cipher object using the encryption key and CBC mode"""
        return Cipher(
            algorithms.AES(key=self.enc_key),
            mode=self._mode(),
            backend=default_backend(),
        )

    def _cipher_encryptor(self):
        """Returns the encryptor for the AES cipher"""
        return self._cipher().encryptor()

    def padded_message(self) -> bytes:
        """Pads the message to a multiple of the block size using PKCS#7 padding"""
        padder = padding.PKCS7(Size.BLOCK * 8).padder()
        return padder.update(self.message) + padder.finalize()

    def ciphertext(self) -> bytes:
        """Encrypts the padded message using AES and returns the ciphertext"""
        return (
            self._cipher_encryptor().update(self.padded_message())
            + self._cipher_encryptor().finalize()
        )

    def iterations_bytes(self) -> bytes:
        """Packs the number of iterations into bytes using the 'big-endian' format"""
        iters_bytes = struct.pack("!I", self.iterations)
        return iters_bytes

    def hmac_final(self) -> bytes:
        """Computes the HMAC-SHA256 of the ciphertext bundle"""
        hmac_ = self.hmac_key
        hmac_ = hmac.HMAC(hmac_, hashes.SHA256())
        hmac_.update(
            self.iv
            + self.salt
            + self.pepper
            + self.iterations_bytes()
            + self.ciphertext()
        )
        return hmac_.finalize()

    def encrypt(self, get_bytes: Optional[bool] = False) -> Union[str, bytes]:
        """Returns the encrypted data as bytes in the form 'HMAC' -> 'IV'
        -> 'Salt value' -> 'pepper value' -> 'iterations' -> 'ciphertext.
        Or as a URL safe base 64 encoded string of the encrypted bytes data,
        which is the default return value"""
        raw = (
            self.hmac_final()
            + self.iv
            + self.salt
            + self.pepper
            + self.iterations_bytes()
            + self.ciphertext()
        )
        return raw if get_bytes else base64.urlsafe_b64encode(raw).decode("UTF-8")


class Dec:
    """Class to decrypt data of either type bytes or str"""

    def __init__(self, message: Union[str, bytes], mainkey: str) -> None:
        if isinstance(message, str):
            mess = message.encode("UTF-8")
            self.message = base64.urlsafe_b64decode(mess)
        elif isinstance(message, bytes):
            self.message = message

        _i = Size.IV
        _s = Size.SALT
        _p = Size.PEPPER
        _h = Size.HMAC
        self.key = mainkey
        self.rec_hmac = self.message[:_h]
        self.rec_iv = self.message[_h: _h + _i]
        self.rec_salt = self.message[_h + _i: _h + _i + _s]
        self.rec_pepper = self.message[_h + _i + _s: _h + _i + _s + _p]
        self.rec_iters_raw = self.message[_h + _i + _s + _p: _h + _i + _s + _p + 4]
        self.rec_iterations = struct.unpack("!I", self.rec_iters_raw)[0]
        if (
            self.rec_iterations < Size.MIN_ITERATIONS
            or self.rec_iterations > Size.MAX_ITERATIONS
        ):
            raise exceptions.dynamic.IterationsOutofRangeError(self.rec_iterations)

        self.rec_ciphertext = self.message[_h + _i + _s + _p + 4:]
        self.dec_key = Enc.derkey(self.key, self.rec_salt, self.rec_iterations)
        self.hmac_k = Enc.derkey(self.key, self.rec_pepper, self.rec_iterations)

        if self.verify_hmac() is False:
            raise exceptions.fixed.MessageTamperingError()

    def calculated_hmac(self) -> bytes:
        """Computes the HMAC-SHA256 of the received ciphertext bundle"""
        hmac_ = self.hmac_k
        hmac_ = hmac.HMAC(hmac_, hashes.SHA256())
        hmac_.update(
            self.rec_iv
            + self.rec_salt
            + self.rec_pepper
            + self.rec_iters_raw
            + self.rec_ciphertext
        )
        return hmac_.finalize()

    def verify_hmac(self) -> bool:
        """Verifies the received HMAC-SHA256 against the calculated HMAC"""
        return hmc.compare_digest(self.calculated_hmac(), self.rec_hmac)

    def _mode(self):
        """Returns the AES Cipher Block Chaining (CBC) mode with the received  IV"""
        return modes.CBC(self.rec_iv)

    def _cipher(self):
        """Creates an AES cipher object using the decryption key and CBC mode"""
        return Cipher(
            algorithms.AES(key=self.dec_key),
            mode=self._mode(),
            backend=default_backend(),
        )

    def _cipher_decryptor(self):
        """Returns the decryptor object for the AES cipher"""
        return self._cipher().decryptor()

    def _pre_unpadding(self) -> bytes:
        """Decrypts the received ciphertext and returns the pre-unpadded data"""
        return (
            self._cipher_decryptor().update(self.rec_ciphertext)
            + self._cipher_decryptor().finalize()
        )

    def unpadded_message(self) -> bytes:
        """Unpads the data and returns the original message"""
        unpadder = padding.PKCS7(Size.BLOCK * 8).unpadder()
        return unpadder.update(self._pre_unpadding()) + unpadder.finalize()

    def decrypt(self, get_bytes: Optional[bool] = False) -> Union[str, bytes]:
        """Returns the decrypted data as bytes if 'get_bytes' is set to True
           Or as a URL safe base 64 encoded string of the decrypted bytes data,
           which is the default return value"""
        raw = self.unpadded_message()
        return raw if get_bytes else raw.decode('UTF-8')
