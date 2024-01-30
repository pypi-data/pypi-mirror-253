import struct
import unittest

import ashcrypt.crypt as ac
from ashcrypt.utils import exceptions
from ashcrypt.utils.consts import Size


class CryptModuleTesting(unittest.TestCase):
    def setUp(self) -> None:
        self.message1 = "Hello there testing if it works"
        self.message2 = b"this is bytes now"
        self.mainkey = ac.Enc.genkey()
        self.ins1 = ac.Enc(message=self.message1, mainkey=self.mainkey)
        self.string_message = self.ins1.encrypt()
        self.bytes_message = self.ins1.encrypt(get_bytes=True)
        self.ins2 = ac.Dec(message=self.bytes_message, mainkey=self.mainkey)
        self.h = Size.HMAC
        self.k = Size.MAIN_KEY
        self.i = Size.IV
        self.p = Size.PEPPER
        self.s = Size.SALT

    def tearDown(self) -> None:
        pass

    def test_KeyLength(self):
        self.assertEqual(self.k, bytes.fromhex(ac.Enc.genkey()).__len__())

    def test_KeyType(self):
        self.assertIs(str, type(ac.Enc.genkey()))

    def test_HMAC(self):
        self.assertTrue(self.bytes_message[: self.h] == self.ins1.hmac_final())

    def test_IV(self):
        self.assertTrue(self.bytes_message[self.h : self.h + self.i] == self.ins1.iv)

    def test_Salt(self):
        self.assertTrue(
            self.bytes_message[self.h + self.i : self.h + self.i + self.s]
            == self.ins1.salt
        )

    def test_Pepper(self):
        self.assertTrue(
            self.bytes_message[
                self.h + self.i + self.s : self.h + self.i + self.s + self.p
            ]
            == self.ins1.pepper
        )

    def test_Iterations(self):
        self.assertTrue(
            self.bytes_message[
                self.h
                + self.i
                + self.s
                + self.p : self.h
                + self.i
                + self.s
                + self.p
                + 4
            ]
            == self.ins1.iterations_bytes()
        )

    def test_Ciphertext(self):
        self.assertTrue(
            self.bytes_message[self.h + self.i + self.s + self.p + 4 :]
            == self.ins1.ciphertext()
        )

    def test_TypeIterations(self):
        self.assertIs(bytes, type(self.ins1.iterations_bytes()))

    def test_IterationsFixed_size(self):
        self.assertEqual(4, self.ins1.iterations_bytes().__len__())

    def test_EncOutputBytes(self):
        self.assertIs(bytes, type(self.ins1.encrypt(get_bytes=True)))

    def test_EncOutputString(self):
        self.assertIs(str, type(self.ins1.encrypt()))

    def test_HMAC_Comp(self):
        self.assertEqual(self.ins1.hmac_final(), self.ins2.rec_hmac)

    def test_IV_Comp(self):
        self.assertEqual(self.ins1.iv, self.ins2.rec_iv)

    def test_Salt_Comp(self):
        self.assertEqual(self.ins1.salt, self.ins2.rec_salt)

    def test_Pepper_Comp(self):
        self.assertEqual(self.ins1.pepper, self.ins2.rec_pepper)

    def test_Iterations_Comp(self):
        self.assertEqual(self.ins1.iterations, self.ins2.rec_iterations)

    def test_Ciphertext_Comp(self):
        self.assertEqual(self.ins1.ciphertext(), self.ins2.rec_ciphertext)

    def test_HMAC_MismatchError(self):
        tampered_hmac = self.ins1.encrypt(get_bytes=True)[: self.h - 1] + b"1"
        tampered_message = tampered_hmac + self.ins1.encrypt(get_bytes=True)[self.h :]
        with self.assertRaises(exceptions.fixed.MessageTamperingError):
            ac.Dec(message=tampered_message, mainkey=self.mainkey)

    def test_IterationsOutOfRangeError(self):
        enb = self.ins1.encrypt(get_bytes=True)
        tampered_message = (
            enb[: self.h + self.i + self.s + self.p]
            + struct.pack("!I", 10**7)
            + enb[self.h + self.i + self.s + self.p + 4 :]
        )
        with self.assertRaises(exceptions.dynamic.IterationsOutofRangeError):
            ac.Dec(message=tampered_message, mainkey=self.mainkey)

    def test_DecOutputBytes(self):
        self.assertEqual(bytes, type(self.ins2.decrypt(get_bytes=True)))

    def test_DecOutputString(self):
        self.assertEqual(str, type(self.ins2.decrypt()))


if __name__ == "__main__":
    unittest.main()
