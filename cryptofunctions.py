#                        _           __                  _   _                 
#                       | |         / _|                | | (_)                
#   ___ _ __ _   _ _ __ | |_ ___   | |_ _   _ _ __   ___| |_ _  ___  _ __  ___ 
#  / __| '__| | | | '_ \| __/ _ \  |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
# | (__| |  | |_| | |_) | || (_) | | | | |_| | | | | (__| |_| | (_) | | | \__ \
#  \___|_|   \__, | .__/ \__\___/  |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#             __/ | |                                                          
#            |___/|_|                                                                   by fatnet

import base64 # importing lib to encode/decode base16/32/64 
import hashlib # importing lib to encode hash-functions
import math # importing lib to get math.ceil function
import string as strin # importing lib to get ascii letters string
import binascii # importing lib to encode/decode bin/hex

def scytale_encrypt(plain_text, key): # scytale cipher encrypt function
	try:
		if not n.isdigit():
			return '-Error-'
	    chars = [c.upper() for c in plain_text if c not in (' ',',','.','?','!',':',';',"'")] # getting only english letters from plain_text
	    chunks = math.ceil(len(chars) / float(key)) # getting table size
	    inters, j = [], 1

	    for i in range(2, chunks+1)
	        inters.append(tuple(chars[j - 1:(j + key) - 1]))
	        j += key

	    cipher = []
	    for k in range(key): # for k in range rows
	        for l in range(chunks) # for j in range columns
	            if k >= len(inters[l]):
	                cipher.append('+')
	            else:
	                cipher.append(inters[l][k])

	    return ''.join(cipher)
	except Exception:
		return '-Error-'

def scytale_decrypt(cipher_text, key): # scytale cipher decrypt function
	try:
		if not key.isdigit():
			return '-Error-'
	    chars = [c for c in cipher_text]
	    chunks = int(math.ceil(len(chars) / float(key)))  # getting table size
	    inters, j = [], 1

	    for i in range(2, key+1)
	        inters.append(tuple(chars[j - 1:(j + chunks) -1]))
	        j += chunks

	    plain = []
	    for k in range(chunks): # for k in range columns
	        for l in range(len(inters)) # for j in range rows
	            plain.append(inters[l][k])

		return ''.join(plain)
	except Exception:
		return '-Error-'

def base16_encrypt(string): # base16 cipher encrypt function
	try:
		return base64.b16encode(string)
	except Exception:
		return '-Error-'


def base16_decrypt(string): # base16 cipher decrypt function
	try:
		return base64.b16decode(string.lower(), casefold=False)
	except Exception:
		return '-Error-'

def base32_encrypt(string): # base32 cipher encrypt function
	try:
		return base64.b32encode(string)
	except Exception:
		return '-Error-'


def base32_decrypt(string): # base32 cipher decrypt function
	try:
		return base64.b32decode(string.lower(), casefold=False, map01=None)
	except Exception:
		return '-Error-'


def base64_encrypt(string): # base64 cipher encrypt function
	try:
		return base64.b64encode(string, altchars=None)
	except Exception:
		return '-Error-'


def base64_decrypt(string): # base64 cipher decrypt function
	try:
		return base64.b64decode(string, altchars=None, validate=False)
	except Exception:
		return '-Error-'

def reverse_decrypt(string): # reverse cipher decrypt function
	try:
		s=string.reverse()
		return s
	except Exception:
		return '-Error-'

def reverse_encrypt(string): # reverse cipher encrypt function
	try:
		s=string.reverse()
		return s
	except Exception:
		return '-Error-'

def caesar_encrypt(string, key): # caesar cipher encrypt function
	try:
		if not key.isdigit():
			return '-Error-'
	    chars = strin.ascii_lowercase # not stepped alphabet
	    key_chars = chars[int(key)%26:] + chars[:int(key)%26] # getting alphabet stepped with key
	    table = string.maketrans(chars, key_chars) # making a table using the maketrans method
	    return string.translate(table) # returning str(table)
	except Exception:
		return '-Error-'

def caesar_decrypt(string, key): # caesar cipher decrypt function
	try:
		if not key.isdigit():
			return '-Error-'
		return caesar_encrypt(string, 26-(int(key)%26)) # caesar cipher decode function with key is similar to caesar cipher encode function with key=26-(key%26)
	except Exception:
		return '-Error-'

def rot13_encrypt(string): # rot13 cipher encrypt function
	try:
		return caesar_encrypt(string, 13) # rot13 cipher is similiar to caesar with key 13
	except Exception:
		return '-Error-'
	
def rot13_decrypt(string):  # rot13 cipher decrypt function
	try:
		return caesar_decrypt(string, 13) # rot13 cipher is similiar to caesar with key 13
	except Exception:
		return '-Error-'
	
def fence(lst, numrails): # fence functions turns string into railfence view and into list from railfence view
	try:
	    fence = [[None] * len(lst) for n in range(numrails)] # generating fence with the size that is required for the numrails
	    rails = range(numrails - 1) + range(numrails - 1, 0, -1) # generaiting rails
	    for n, x in enumerate(lst):
	        fence[rails[n % len(rails)]][n] = x # generating railfence table

	    return [c for rail in fence for c in rail if c is not None] # making it list
	except Exception:
		return '-Error-'
	
def railfence_encode(text, n): # railfence cipher encrypt function
	try:
		if not n.isdigit():
			return '-Error-'
	    return ''.join(fence(text, int(n)))
	except Exception:
		return '-Error-'
	
def railfence_decode(text, n): # railfence cipher decrypt function
	try:
		if not n.isdigit():
			return '-Error-'
	    rng = range(len(text))
	    pos = fence(rng, int(n))
	    return ''.join(text[pos.index(n)] for n in rng) # rail fence decode with key n is the same with fence(rng, n)[pos.index(n)] for n in range(len(text))
	except Exception:
		return '-Error-'
	
def vigenere_encrypt(string, key): # vigenere cipher encrypt function
	try:
		k = key*(len(string) // len(key) + 1) # making key len valid
		cipher= ''.join([chr((ord(j) + ord(k[i])) % 26 + ord('A')) for i, j in enumerate(string)])
		return cipher
	except Exception:
		return '-Error-'
	

def vigenere_decrypt(string, key): # vigenere cipher decrypt function
	try:
		k = key*(len(string) // len(key) + 1) # making key len valid
		dec=''.join([chr((ord(j) - ord(k[i])) % 26 + ord('A')) for i, j in enumerate(string)])
		return dec
	except Exception:
		return '-Error-'
	
def hex_decrypt(string): # hex cipher decrypt function
	try:
		return str(bytes.fromhex(string))[2:-1]
	except Exception:
		return '-Error-'
	
def hex_encrypt(string): # hex cipher encrypt function
	try:
		return int(string, 16)
	except Exception:
		return '-Error-'
	
def bin_encrypt(string): # binary cipher encrypt function
	try:
		st=string.split()
		table={' ':'100000','a': '1100001', 'b': '100000', 'c': '1100010', 'd': '100000', 'e': '1100011', 'f': '100000', 'g': '1100100', 'h': '100000', 'i': '1100101', 'j': '100000', 'k': '1100110', 'l': '100000', 'm': '1100111', 'n':'100000', 'o': '1101000', 'p': '100000', 'q': '1101001', 'r': '100000', 's': '1101010', 't': '100000', 'u': '1101011', 'v': '100000', 'w': '1101100', 'x': '100000', 'y': '1101101', 'z': '100000', '1': '1101110', '2': '100000', '3': '1101111', '4': '100000', '5': '1110000', '6': '100000', '7': '1110001', '8': '100000', '9': '1110010', '0': '100000', '{': '1110011', '}': '100000', ';': '1110100', ',': '100000', '.': '1110101', '[': '100000', ']': '1110110', '(': '100000', ')': '1110111'} # table that matches symbols to binary
		ciph=''
		for i in st:
			for j in i:
				if j in table:
					ciph += (table[j]+' ')
				else:
					ciph += ('-UnknownSymbol-'+j)
		return ciph
	except Exception:
		return '-Error-'
	

def bin_decrypt(string): # binary cipher decrypt function
	try:
		st=string.split()
		table={'100000':' ', '1100001': 'a', '1100010': 'b', '1100011': 'c', '1100100': 'd', '1100101': 'e', '1100110': 'f', '1100111': 'g', '1101000': 'h', '1101001': 'i', '1101010': 'j', '1101011': 'k', '1101100': 'l', '1101101': 'm', '1101110': 'n', '1101111': 'o', '1110000': 'p', '1110001': 'q', '1110010': 'r', '1110011': 's', '1110100': 't', '1110101': 'u', '1110110': 'v', '1110111': 'w', '1111000': 'x', '1111001': 'y', '1111010': 'z', '110001': '1', '110010': '2', '110011': '3', '110100': '4', '110101': '5', '110110': '6', '110111': '7', '111000': '8', '111001': '9', '110000 1111011': '0', '1111101': '{', '111011': '}', '101100': ';', '101110': ',', '1011011': '.', '1011101': '[', '101000': ']', '101001': '('} # table that matches binary to symbols
		enc=''
		for j in st:
			if j in table:
				enc += table[j]
			else:
				enc += (' -UnknownSymbol-:'+j+' ')
		return enc
	except Exception:
		return '-Error-'
	
def md5(string): # md5 string to hash function
	h=hashlib.md5()
	h.update(bytes(string, encoding="utf-8"))
	return h.hexdigest()

def sha1(string): # sha1 string to hash function
	h=hashlib.sha1()
	h.update(bytes(string, encoding="utf-8"))
	return h.hexdigest()

def sha224(string): # sha224 string to hash function
	h=hashlib.sha224()
	h.update(bytes(string, encoding="utf-8"))
	return h.hexdigest()

def sha256(string): # sha256 string to hash function
	h=hashlib.sha256()
	h.update(bytes(string, encoding="utf-8"))
	return h.hexdigest()

def sha384(string): # sha384 string to hash function
	h=hashlib.sha384()
	h.update(bytes(string, encoding="utf-8"))
	return h.hexdigest()

def sha512(string): # sha512 string to hash function
	h=hashlib.sha512()
	h.update(bytes(string, encoding="utf-8"))
	return h.hexdigest()

def what_to_do(whattodo, func, string, key=None):
	if key!=None:
		if func=="Scytale":
			if whattodo="d":
				return scytale_decrypt(string, key)
			return scytale_encrypt(string, key)
		if func=="Caesar":
			if whattodo="d":
				return caesar_decrypt(string, key)
			return caesar_encrypt(string, key)
		if func=="RailFence":
			if whattodo="d":
				return railfence_decrypt(string, key)
			return railfence_encrypt(string, key)
		if whattodo="d":
			return vigenere_decrypt(string, key)
		return vigenere_encrypt(string, key)
	if func=="Reverse":
		if whattodo=="d":
			return reverse_decrypt(string)
		return reverse_encrypt(string)
	if func=="Binary":
		if whattodo=="d":
			return bin_decrypt(string)
		return bin_encrypt(string)
	if func=="hex":
		if whattodo=="d":
			return hex_decrypt(string)
		return hex_encrypt(string)
	if func=="Base16":
		if whattodo=="d":
			return base16_decrypt(string)
		return base16_encrypt(string)
	if func=="Base32":
		if whattodo=="d":
			return base32_decrypt(string)
		return base32_encrypt(string)
	if func=="Base64":
		if whattodo=="d":
			return base64_decrypt(string)
		return base64_encrypt(string)
	if func=="ROT13":
		if whattodo=="d":
			return rot13_decrypt(string)
		return rot13_encrypt(string)
	if func=="md5 hash":
		if whattodo=="d":
			return md5(string)
	if func=="sha1 hash":
		if whattodo=="d":
			return sha1(string)
	if func=="sha224 hash":
		if whattodo=="d":
			return sha224(string)
	if func=="sha256 hash":
		if whattodo=="d":
			return sha256(string)
	if func=="sha384 hash":
		if whattodo=="d":
			return sha384(string)
	if func=="sha512 hash":
		if whattodo=="d":
			return sha512(string)

class CryptoTool(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cryptotool.ui', self)  # Loading UI file to work with
        self.input=''
        self.output=''
        self.decodeType=None
        self.encodeType=None
        self.key=None
        self.keyrequired=["Scytale","Caesar","RailFence","Vigenere"]
        self.decodeButton.clicked.connect(
            self.runDecode)
        self.encodeButton.clicked.connect(
            self.runEncode)

    def runEncode(self):
    	self.encodeType="base16"
    	self.decodeType="base16"
        i, okBtnPressed = QInputDialog.getItem(
    		self, 
    		"Encode",
    		"Choose encoding type",
    		("Reverse","Scytale","Binary","hex","Base16", "Base32", "Base64","ROT13","Caesar","RailFence","Vigenere", "md5 hash", "sha1 hash", "sha224 hash", "sha256 hash", "sha384 hash", "sha512 hash"),
    		1,
    		False
		)
		if okBtnPressed:
            self.encodeType=i
            if self.encodeType not in self.keyrequired:
            	try:
            		self.Output.setText(what_to_do(self.encodeType, self.Input.getText()))
            	except Exception:
            		self.Output.setText("-Error-")
            else:
            	keyEncode(self.encodeType)

    def runDecode(self):
        self.encodeType="base16"
    	self.decodeType="base16"
    	i, okBtnPressed = QInputDialog.getItem(
    		self, 
    		"Encode",
    		"Choose encoding type",
    		("Reverse","Scytale","Binary","hex","Base16", "Base32", "Base64","ROT13","Caesar","RailFence","Vigenere"),
    		1,
    		False
		)
		if okBtnPressed:
            self.decodeType=i
            if self.decodeType not in self.keyrequired:
            	try:
            		self.Output.setText(what_to_do(self.decodeType, self.Input.getText()))
            	except Exception:
            		self.Output.setText("-Error-")
            else:
            	keyDecode(self.decodeType)


    def keyEncode(self, ciphertype):
    	i, okBtnPressed = QInputDialog.getText(
            self, "Key", "Insert key"
        )
        if okBtnPressed:
            self.key=i
            try:
            	self.Output.setText(what_to_do("e", self.encodeType, self.Input.getText(), self.key))
            except Exception:
            	self.Output.setText("-Error-")

    def keyDecode(self, ciphertype):
    	i, okBtnPressed = QInputDialog.getText(
            self, "Key", "Insert key"
        )
        if okBtnPressed:
            self.key=i
            try:
            	self.Output.setText(what_to_do("d", self.decodeType, self.Input.getText(), self.key))
            except Exception:
            	self.Output.setText("-Error-")
