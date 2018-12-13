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


def scytale_decrypt(cipher_text, key): # scytale cipher decrypt function
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

def base16_encrypt(string): # base16 cipher encrypt function
	return base64.b16encode(string)

def base16_decrypt(string): # base16 cipher decrypt function
	return base64.b16decode(string.lower(), casefold=False)

def base32_encrypt(string): # base32 cipher encrypt function
	return base64.b32encode(string)

def base32_decrypt(string): # base32 cipher decrypt function
	return base64.b32decode(string.lower(), casefold=False, map01=None)

def base64_encrypt(string): # base64 cipher encrypt function
	return base64.b64encode(string, altchars=None)

def base64_decrypt(string): # base64 cipher decrypt function
	return base64.b64decode(string, altchars=None, validate=False)

def reverse_decrypt(string): # reverse cipher decrypt function
	s=string.reverse()
	return s

def reverse_encrypt(string): # reverse cipher encrypt function
	s=string.reverse()
	return s

def caesar_encrypt(string, key): # caesar cipher encrypt function
    chars = strin.ascii_lowercase # not stepped alphabet
    key_chars = chars[key%26:] + chars[:key%26] # getting alphabet stepped with key
    table = string.maketrans(chars, key_chars) # making a table using the maketrans method
    return string.translate(table) # returning str(table)

def caesar_decrypt(string, key): # caesar cipher decrypt function
	return caesar_encrypt(string, 26-(key%26)) # caesar cipher decode function with key is similar to caesar cipher encode function with key=26-(key%26)

def rot13_encrypt(string): # rot13 cipher encrypt function
	return caesar_encrypt(string, 13) # rot13 cipher is similiar to caesar with key 13

def rot13_decrypt(string):  # rot13 cipher decrypt function
	return caesar_decrypt(string, 13) # rot13 cipher is similiar to caesar with key 13

def offset(even, rails, rail): # function that makes railfence calculating easier
    if rail == 0 or rail == rails - 1:
        return (rails - 1) * 2

    if even:
        return 2 * rail
    else:
        return 2*(rails - 1 - rail)



def railfence_decrypt(encrypted, rails, showOff = 0):  # railfence cipher decrypt function
    array = [[" " for col in range(len(encrypted))] for row in range(rails)]
    read = 0
    
    for rail in range(rails):
        pos = offset(1, rails, rail)
        even = 0;
        
        if rail == 0:
            pos = 0
        else:
            pos = int(pos / 2)
        
        while pos < len(encrypted):
            if read == len(encrypted):
                break

            array[rail][pos] = encrypted[read];
            read = read + 1

            pos = pos + offset(even, rails, rail)
            even = not even


    if showOff:
        for row in array:
            print row

    decoded = ""

    for x in range(len(encrypted)):
        for y in range(rails):
            if array[y][x] != " ":
                decoded += array[y][x]

    return decoded

def vigenere_encrypt(string, key): # vigenere cipher encrypt function
	k = key*(len(string) // len(key) + 1)
	cipher= ''.join([chr((ord(j) + ord(k[i])) % 26 + ord('A')) for i, j in enumerate(string)])
	return cipher

def vigenere_decrypt(string, key): # vigenere cipher decrypt function
	k = key*(len(string) // len(key) + 1)
	dec=''.join([chr((ord(j) - ord(k[i])) % 26 + ord('A')) for i, j in enumerate(string)])
	return dec

def hex_decrypt(string): # hex cipher decrypt function
	return str(bytes.fromhex(string))[2:-1]

def hex_encrypt(string): # hex cipher encrypt function
	return int(string, 16)

def bin_encrypt(string): # binary cipher encrypt function
	st=string.lower()
	keys='a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 { } ; , . [ ] ( )'
	keys.split()
	values='1100001 100000 1100010 100000 1100011 100000 1100100 100000 1100101 100000 1100110 100000 1100111 100000 1101000 100000 1101001 100000 1101010 100000 1101011 100000 1101100 100000 1101101 100000 1101110 100000 1101111 100000 1110000 100000 1110001 100000 1110010 100000 1110011 100000 1110100 100000 1110101 100000 1110110 100000 1110111 100000 1111000 100000 1111001 100000 1111010 100000 110001 100000 110010 100000 110011 100000 110100 100000 110101 100000 110110 100000 110111 100000 111000 100000 111001 100000 110000 1111011 100000 1111101 100000 111011 100000 101100 100000 101110 100000 1011011 100000 1011101 100000 101000 100000 101001'
	values.split()
	table={}
	ciph=''
	for i in range(len(keys)):
		table[keys[i]]=values[i]
	for j in st:
		if j in table:
			ciph += table[j]
		else:
			ciph += '-UnknownSymbol-'
	return ciph


def bin_decrypt(string): # binary cipher decrypt function
	st=string.split()
	values='a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 { } ; , . [ ] ( )'
	keys.split()
	keys='1100001 100000 1100010 100000 1100011 100000 1100100 100000 1100101 100000 1100110 100000 1100111 100000 1101000 100000 1101001 100000 1101010 100000 1101011 100000 1101100 100000 1101101 100000 1101110 100000 1101111 100000 1110000 100000 1110001 100000 1110010 100000 1110011 100000 1110100 100000 1110101 100000 1110110 100000 1110111 100000 1111000 100000 1111001 100000 1111010 100000 110001 100000 110010 100000 110011 100000 110100 100000 110101 100000 110110 100000 110111 100000 111000 100000 111001 100000 110000 1111011 100000 1111101 100000 111011 100000 101100 100000 101110 100000 1011011 100000 1011101 100000 101000 100000 101001'
	values.split()
	table={}
	enc=''
	for i in range(len(keys)):
		table[keys[i]]=values[i]
	for j in st:
		if j in table:
			enc += table[j]
		else:
			enc += ('-UnknownSymbol-:'+j)
	return enc

def md5(string): # md5 string to hash function
	return hashlib.md5().update(string).digest()

def sha1(string): # sha1 string to hash function
	return hashlib.sha1().update(string).digest()

def sha224(string): # sha224 string to hash function
	return hashlib.sha224().update(string).digest()

def sha256(string): # sha256 string to hash function
	return hashlib.sha256().update(string).digest()

def sha384(string): # sha384 string to hash function
	return hashlib.sha384().update(string).digest()

def sha512(string): # sha512 string to hash function
	return hashlib.sha512().update(string).digest()
