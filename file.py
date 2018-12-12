import base64
import hashlib
import math
import string
import binascii

def scytalee(plain_text, key):
    chars = [c.upper() for c in plain_text if c not in (' ',',','.','?','!',':',';',"'")]
    chunks = math.ceil(len(chars) / float(key))
    inters, j = [], 1

    for i in range(2, chunks+1)
        inters.append(tuple(chars[j - 1:(j + key) - 1]))
        j += key

    cipher = []
    for k in range(key):
        for l in range(chunks)
            if k >= len(inters[l]):
                cipher.append('+')
            else:
                cipher.append(inters[l][k])

    return ''.join(cipher)


def scytaled(cipher_text, key):
    chars = [c for c in cipher_text]
    chunks = int(math.ceil(len(chars) / float(key)))
    inters, j = [], 1

    for i in range(2, key+1)
        inters.append(tuple(chars[j - 1:(j + chunks) -1]))
        j += chunks

    plain = []
    for k in range(chunks):
        for l in range(len(inters))
            plain.append(inters[l][k])

	return ''.join(plain)

def base16e(string):
	return base64.b16encode(string)

def base16d(string):
	return base64.b16decode(string.lower(), casefold=False)

def base32e(string):
	return base64.b32encode(string)

def base32d(string):
	return base64.b32decode(string.lower(), casefold=False, map01=None)

def base64e(string):
	return base64.b64encode(string, altchars=None)

def base64d(string):
	return base64.b64decode(string, altchars=None, validate=False)

def reversed(string):
	s=string.reverse()
	return s

def reversee(string):
	s=string.reverse()
	return s

def caesare(string, key):
	chars = string.ascii_lowercase
    key_chars = chars[key%26:] + chars[:key%26]
    table = string.maketrans(chars, key_chars)
    return string.translate(table)

def caesard(string, key):
	return caesare(string, 26-(key%26))

def rot13e(string):
	return caesare(string, 13)

def rot13d(string):
	return caesard(string, 13)

def offset(even, rails, rail):
    if rail == 0 or rail == rails - 1:
        return (rails - 1) * 2

    if even:
        return 2 * rail
    else:
        return 2*(rails - 1 - rail)



def railfenced(encrypted, rails, showOff = 0):
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

def vigeneree(string, key):
	k = key*(len(string) // len(key) + 1)
	cipher= ''.join([chr((ord(j) + ord(k[i])) % 26 + ord('A')) for i, j in enumerate(string)])
	return cipher

def vigenered(string, key):
	k = key*(len(string) // len(key) + 1)
	dec=''.join([chr((ord(j) - ord(k[i])) % 26 + ord('A')) for i, j in enumerate(string)])
	return dec

def hexd(string):
	return str(bytes.fromhex(string))[2:-1]

def hexe(string):
	return int(string, 16)

def bine(string):
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


def bind(string):
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
