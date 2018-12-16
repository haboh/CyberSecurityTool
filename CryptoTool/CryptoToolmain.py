#                        _           __                  _   _
#                       | |         / _|                | | (_)
#   ___ _ __ _   _ _ __ | |_ ___   | |_ _   _ _ __   ___| |_ _  ___  _ __  ___
#  / __| '__| | | | '_ \| __/ _ \  |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
# | (__| |  | |_| | |_) | || (_) | | | | |_| | | | | (__| |_| | (_) | | | \__ \
#  \___|_|   \__, | .__/ \__\___/  |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#             __/ | |
#            |___/|_|                                                                   by fatnet

import base64  # importing lib to encode/decode base16/32/64
import hashlib  # importing lib to encode hash-functions
import math  # importing lib to get math.ceil function
import string  # importing lib to get ascii letters string
# libs to work with GUI correctly
import sys
import itertools
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QInputDialog
from CryptoTool.cryptotoolUI import Ui_CryptoTool


# Debugged. Works Ok.
def base16_encrypt(s):  # base16 cipher encrypt function
    return base64.b16encode(str.encode(s)).decode()


# Debugged. Works Ok.
def base16_decrypt(s):  # base16 cipher decrypt function
    return base64.b16decode(s).decode()


# Debugged. Works Ok.
def base32_encrypt(s):  # base32 cipher encrypt function
    return base64.b32encode(str.encode(s)).decode()


# Debugged. Works Ok.
def base32_decrypt(s):  # base32 cipher decrypt function
    return base64.b32decode(str.encode(s)).decode()


# Debugged. Works Ok.
def base64_encrypt(s):  # base64 cipher encrypt function
    return base64.b64encode(str.encode(s)).decode()


# Debugged. Works Ok.
def base64_decrypt(s):  # base64 cipher decrypt function
    return base64.b64decode(str.encode(s)).decode()


# Debugged. Works Ok.
def sha512(s):  # sha512 string to hash function
    h = hashlib.sha512()
    h.update(bytes(s, encoding="utf-8"))
    return h.hexdigest()


# Debugged. Works Ok.
def sha384(s):  # sha384 string to hash function
    h = hashlib.sha384()
    h.update(bytes(s, encoding="utf-8"))
    return h.hexdigest()


# Debugged. Works Ok.
def sha256(s):  # sha256 string to hash function
    h = hashlib.sha256()
    h.update(bytes(s, encoding="utf-8"))
    return h.hexdigest()


# Debugged. Works Ok.
def sha224(s):  # sha224 string to hash function
    h = hashlib.sha224()
    h.update(bytes(s, encoding="utf-8"))
    return h.hexdigest()


# Debugged. Works Ok.
def sha1(s):  # sha1 string to hash function
    h = hashlib.sha1()
    h.update(bytes(s, encoding="utf-8"))
    return h.hexdigest()


# Debugged. Works Ok.
def md5(s):  # md5 string to hash function
    h = hashlib.md5()
    h.update(bytes(s, encoding="utf-8"))
    return h.hexdigest()


# Debugged. Works Ok.
def hex_encrypt(s):  # hex cipher encrypt function
    return ''.join([str(hex(ord(c)))[2:] for c in s])


# Debugged. Works Ok.
def hex_decrypt(s):  # hex cipher decrypt function
    return str(bytes.fromhex(s))[2:-1]


# Debugged. Works Ok.
def caesar_encrypt(s, key):  # caesar cipher encrypt function
    key = int(key)
    chars = string.ascii_lowercase  # not stepped alphabet
    key_chars = chars[key % 26:] + chars[:key % 26]  # getting alphabet stepped with key
    table = s.maketrans(chars, key_chars)  # making a table using the maketrans method
    return s.translate(table)  # returning str(table)


# Debugged. Works Ok.
def caesar_decrypt(s, key):  # caesar cipher decrypt function
    return caesar_encrypt(s, (26 - int(key)) % 26)
    # caesar cipher decode function with key is similar to caesar cipher encode function with key=26-(key%26)


# Debugged. Works Ok.
def rot13_decrypt(s):  # rot13 cipher decrypt function
    return caesar_decrypt(s, -13)
    # rot13 cipher is similar to caesar with key 13


# Debugged. Works Ok.
def rot13_encrypt(s):  # rot13 cipher encrypt function
    return caesar_encrypt(s, 13)
    # rot13 cipher is similar to caesar with key 13


# Debugged. Works Ok.
def vigenere_encrypt(s, key):  # vigenere cipher encrypt function
    k = key * (len(s) // len(key) + 1)  # making key len valid
    cipher = ''.join([chr((ord(j) + ord(k[i])) % 26 + ord('A')) for i, j in enumerate(s)])
    return cipher


# Debugged. Works Ok.
def vigenere_decrypt(s, key):  # vigenere cipher decrypt function
    k = key * (len(s) // len(key) + 1)  # making key len valid
    dec = ''.join([chr((ord(j) - ord(k[i])) % 26 + ord('A')) for i, j in
                   enumerate(s)])
    return dec


# Debugged. Works Ok.
def fence_create(lst, numrails):  # fence functions turns string into railfence view and into list from railfence view
    numrails = int(numrails)
    fence = [[None] * len(lst) for n in range(numrails)]
    # generating fence with the size that is required for the numrails
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))  # generating rails
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x  # generating railfence table
    return [c for rail in fence for c in rail if c is not None]  # making it list


# Debugged. Works Ok.
def railfence_encode(text, n):  # railfence cipher encrypt function
    n = int(n)
    return ''.join(fence_create(text, n))


# Debugged. Works Ok.
def railfence_decode(text, n):  # railfence cipher decrypt function
    n = int(n)
    rng = range(len(text))
    pos = fence_create(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)
    # rail fence decode with key n is the same with fence(rng, n)[pos.index(n)] for n in range(len(text))


# Debugged. Works Ok.
def scytale_encrypt(plain_text, key):  # scytale cipher encrypt function
    key = int(key)
    chars = []
    for c in plain_text:
        if c not in [' ', ',', '.', '?', '!', ':', ';', "'"]:  # getting only letters from plain_text
            chars.append(c.upper())
    chunks = math.ceil(len(chars) / float(key))  # getting table size
    inters, j = [], 1
    for i in range(2, chunks + 1):
        inters.append(tuple(chars[j - 1:(j + key) - 1]))
        j += key

    cipher = []
    for k in range(key):  # for k in range rows
        for l in range(chunks):  # for j in range columns
            if k >= len(inters[l]):
                cipher.append('+')
            else:
                cipher.append(inters[l][k])
    return ''.join(cipher)


# Debugged. Works Ok.
def scytale_decrypt(cipher_text, key):  # scytale cipher decrypt function
    chars = [c for c in cipher_text]
    chunks = int(math.ceil(len(chars) / float(key)))  # getting table size
    inters, j = [], 1

    for i in range(2, key + 1):
        inters.append(tuple(chars[j - 1:(j + chunks) - 1]))
        j += chunks

    plain = []
    for k in range(chunks):  # for k in range columns
        for l in range(len(inters)):  # for j in range rows
            plain.append(inters[l][k])

    return ''.join(plain)


# Debugged. Works Ok.
def bin_encrypt(s):  # binary cipher encrypt function
    st = s.split()
    ciph = []
    for word in st:
        for letter in word:
            ciph.append(bin(ord(letter))[2:])
    return ' '.join(ciph)


# Debugged. Works Ok.
def bin_decrypt(s):  # binary cipher decrypt function
    st = s.split()
    enc = ''
    for n in st:
        enc += chr(int(n, 2))
    return enc


# Debugged. Works Ok.
def what_to_do(action, func, s, key):
    actions = {
        'ReverseE': reversed,
        'ReverseD': reversed,
        'BinaryD': bin_decrypt,
        'BinaryE': bin_encrypt,
        'hexD': hex_decrypt,
        'hexE': hex_encrypt,
        'Base16D': base16_decrypt,
        'Base16E': base16_encrypt,
        'Base32E': base32_encrypt,
        'Base32D': base32_decrypt,
        'Base64E': base64_encrypt,
        'Base64D': base64_decrypt,
        'ROT13E': rot13_encrypt,
        'ROT13D': rot13_decrypt,
        'md5 hashE': md5,
        'sha1 hashE': sha1,
        'sha224 hashE': sha224,
        'sha256 hashE': sha256,
        'sha384 hashE': sha384,
        'sha512 hashE': sha512,
        'ScytaleE': scytale_encrypt,
        'ScytaleD': scytale_decrypt,
        'CaesarE': caesar_encrypt,
        'CaesarD': caesar_decrypt,
        'RailFenceE': railfence_encode,
        'RailFenceD': railfence_decode,
        'VigenereD': vigenere_decrypt,
        'VigenereE': vigenere_encrypt,
    }
    if key is None:
        return actions[func + action.upper()](s)
    else:
        return actions[func + action.upper()](s, key)


# Debugged. Works Ok.
class CryptoToolMainWindow(QMainWindow, Ui_CryptoTool, QWidget):
    # Debugged. Works Ok.
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.input, self.output = '', ''
        self.decodeType, self.encodeType, self.key = None, None, None
        self.key_required = ["Scytale", "Caesar", "RailFence", "Vigenere"]
        self.decodeButton.clicked.connect(self.run_decode)
        self.encodeButton.clicked.connect(self.run_encode)

    # Debugged. Works Ok.
    def run_encode(self):
        action, ok_button_pressed = QInputDialog.getItem(
            self,
            "Encode",
            "Choose encoding type",
            (
                "Reverse", "Scytale", "Binary", "hex", "Base16", "Base32",
                "Base64",
                "ROT13", "Caesar", "RailFence", "Vigenere", "md5 hash",
                "sha1 hash",
                "sha224 hash", "sha256 hash", "sha384 hash", "sha512 hash"),
            1,
            False
        )
        if ok_button_pressed:
            self.encodeType = action
            if self.encodeType not in self.key_required:
                try:
                    text = what_to_do("e", self.encodeType, self.Input.text(), None)
                    self.Output.setText(text)
                except Exception:
                    self.Output.setText("-Error-")
            else:
                self.key_encode()

    # Debugged. Works Ok.
    def run_decode(self):
        action, ok_button_pressed = QInputDialog.getItem(
            self,
            "Decode",
            "Choose decoding type",
            (
                "Reverse", "Scytale", "Binary", "hex", "Base16", "Base32",
                "Base64",
                "ROT13", "Caesar", "RailFence", "Vigenere"),
            1,
            False
        )
        if ok_button_pressed:
            self.decodeType = action
            if self.decodeType not in self.key_required:
                try:
                    text = what_to_do("d", self.decodeType, self.Input.text(), None)
                    self.Output.setText(text)
                except Exception:
                    self.Output.setText("-Error-")
            else:
                self.key_decode()

    # Debugged. Works Ok.
    def key_encode(self):
        key, ok_button_pressed = QInputDialog.getText(
            self, "Key", "Insert key"
        )
        if ok_button_pressed:
            self.key = key
            try:
                text = what_to_do("e", self.encodeType, self.Input.text(), self.key)
                self.Output.setText(text)
            except Exception:
                self.Output.setText("-Error-")

    # Debugged. Works Ok.
    def key_decode(self):
        key, ok_button_pressed = QInputDialog.getText(
            self, "Key", "Insert key"
        )
        if ok_button_pressed:
            self.key = key
            try:
                text = what_to_do("d", self.decodeType, self.Input.text(), self.key)
                self.Output.setText(text)
            except Exception:
                self.Output.setText("-Error-")


# Debugged. Works Ok.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    prog = CryptoToolMainWindow()
    prog.show()
    sys.exit(app.exec())
