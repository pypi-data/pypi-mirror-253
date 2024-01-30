## Introducing Ashcrypt: Your Guardian of Secrets 🔒
Tired of wrestling with passwords and entrusting your private files to sketchy apps? protecting your sensitive data now becomes very simple. No more struggling with intricate code  – just powerful data security at your fingertips.


## 🔑  Effortlessly Secure Encryption!
Worried about complex encryption steps? Don't worry! With Ashcrypt, encrypting a file is as simple as can be. Check this out:
```python
from ashcrypt import CryptFile

key = CryptFile.genkey()
CryptFile('passwords.csv', key).encrypt()
# Voila! Your file is now called ==> passwords.csv.crypt
```
## 💾 Secure Database Integration
Got valuable data you want to stash? Ashcrypt has your back:
```python
from ashcrypt import Crypt, CryptFile, Database

binary_data = CryptFile.get_binary('image.png')
key = Crypt.genkey()  # Get a key

encrypted_binary_data = Crypt(binary_data, key).encrypt(get_bytes=True)
conn = Database('data-holder.db')
conn.insert(name='image.png', content=encrypted_binary_data)
```
## 🚀 Or, Simplify with the App

![alt text](docs/assets/GUI.png)

## 📦 What's Under the Hood?
**Library:** Your path to seamless security. It's your companion for performing encryption and decryption on your data using the robust AES-256 (CBC) encryption algorithm. Designed with developers in mind, it makes data protection a breeze.

**App:** Where magic happens. A sleek, unified software solution merging the library's might into a user-friendly application. Whether you're a seasoned developer or just starting, this app is your ultimate ally.




## 🧙‍♂️ Installation Made Easy
Starting is a breeze. If you want to use Ashcrypt as a library, just use pip:
```python
pip install ashcrypt
```
Want the entire repository? Run this command for a simple setup:
```shell
curl -sSfL https://raw.githubusercontent.com/AshGw/ashcrypt/main/important/setup.sh | bash
```
## 📚 Dive into the Docs
I designed this documentation with simplicity in mind. Check out the Docs to unleash Ashcrypt's full potential.


## 🔐 License to Thrill
Ashcrypt is open-source and licensed under the MIT License.
## 🙌 Shout-Outs
Ashcrypt draws its strength from the robust cryptographic practices and the inspiration gleaned from a myriad of open-source implementations. Yet, it stands tall on the shoulders of one true heavyweight – the renowned **'cryptography'** library. With **'cryptography'** as its bedrock, Ashcrypt ensures your data's safety isn't a matter of chance but a guarantee.
