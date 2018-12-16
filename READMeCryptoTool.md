# CyberSecurityTool/CryptoTool
## A: Theoretical section.
### 0. Hashes:
  We know how they work but its to hard to explane, so know we should just know that they are working in our program and you can encrypt using it
### 1. Reverse cipher:
  We just reverse the string to encrypt it:
  ```python
  reverse('lewa<3')='3<awel'
  ```
### 2. Scytale cipher:
  Scytale is one of the most ancient ciphers, it works this way:
  ![alt text](https://pp.userapi.com/c850636/v850636941/6877b/gbOzJGiT0Ug.jpg)<br />
  _______________________________________
       |   |   |   |   |   |  |
       | I | a | m | h | u |  |
     __| r | t | v | e | r |__|                                 
    |  | y | b | a | d | l |                                   
    |  | y | H | E | L | P |
    |  |   |   |   |   |   |
_________________________________________
  ```python
  scytale('I am hurt very badly HELP', key=5)="IryyatbHmvaEhedLurlP"
  ```
### 3. Caesar cipher:
  Caesar cipher is one of the most ancient ciphers, even Julius Caesar used it.
  We just replace all the letters to the letter that is righter than the current letter for "key" step
  ![alt text](https://pp.userapi.com/c850636/v850636941/68763/6BJesbouhPw.jpg)<br />
  ```python
  caesar('ABCDEFGHIJKLMNOPQRSTUVWXYZ', key=23)='XYZABCDEFGHIJKLMNOPQRSTUVW'
  ```
### 4. ROT13:
  ROT13 is a Caesar cipher with key=13
  ![alt text](https://pp.userapi.com/c850636/v850636941/687ba/1gOHp5cmF_g.jpg)<br />
  ```python
  rot13('hello')='uryyb'
  ```
### 5. Binary cipher:
  ```python
  binary('c')=str(int(ord('c'), 2))=1100011
  ```
### 6. hex cipher:
  ```python
  hex('s')=[str(hex(ord(char)))[2:] for char in 's']
  ```
### 7. Base16/32/64 cipher:
  It's group of similar binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-16/32/64 representation
  ```python
  string='hello'
  base16(string)='68656C6C6F'
  base32(string)='NBSWY3DPBI======'
  base64(string)='aGVsbG8='
  ```
### 8. RailFence cipher:
  Sometimes it's called "Zigzag cipher". It's a form of transposition cipher. It derives its name from the way in which it is encoded.<br />
  ![alt text](https://pp.userapi.com/c844416/v844416560/15d64c/eX2b8A6eFh4.jpg)<br />
  ```python
  railfence('WE ARE DISCOVERED. FLEE AT ONCE', key=3)='WECRLTEERDSOEEFEAOCAIVDEN'
  ```
### 9. Vigenere cipher:
  ![alt text](https://pp.userapi.com/c850636/v850636318/68da1/rL1AIO99qVg.jpg)<br />
  To encrypt, a table of alphabets can be used, termed a tabula recta, Vigenère square or Vigenère table. It has the alphabet written out 26 times in different rows, each alphabet shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar ciphers. At different points in the encryption process, the cipher uses a different alphabet from one of the rows. The alphabet used at each point depends on a repeating keyword.[citation needed]
For example, suppose that the plaintext to be encrypted is ATTACKATDAWN.
The person sending the message chooses a keyword and repeats it until it matches the length of the plaintext, for example, the keyword "LEMON": LEMONLEMONLE
Each row starts with a key letter. The rest of the row holds the letters A to Z (in shifted order). Although there are 26 key rows shown, a code will use only as many keys (different alphabets) as there are unique letters in the key string, here just 5 keys: {L, E, M, O, N}. For successive letters of the message, successive letters of the key string will be taken and each message letter enciphered by using its corresponding key row. The next letter of the key is chosen, and that row is gone along to find the column heading that matches the message character. The letter at the intersection of [key-row, msg-col] is the enciphered letter.
For example, the first letter of the plaintext, A, is paired with L, the first letter of the key. Therefore, row L and column A of the Vigenère square are used, namely L. Similarly, for the second letter of the plaintext, the second letter of the key is used. The letter at row E and column T is X.
  ![alt text](https://pp.userapi.com/c850636/v850636318/68dca/aKMZEmwpJj8.jpg)<br />
  ```python
  vigenere('ATTACKATDAWN',key='LEMON')='LXFOPVEFRNHR'
  ```
____
## B: How to work with this app:
  ![alt text](https://pp.userapi.com/c850636/v850636318/68dd1/YT7GShyupmw.jpg)<br />
  There are 5 main parts in this app:
  ### Input lineEdit:
   ![alt text](https://pp.userapi.com/c852124/v852124318/6a7f3/XtaIg-ww0KU.jpg)<br />
    You should just type into it encrypted text or text you want to encrypt
  ### What_to_do buttons:
   ![alt text](https://pp.userapi.com/c852124/v852124318/6a7ec/H8E9rbW9KS0.jpg)<br />
    You can choose what to do, decrypt or encrypt
  ### Choose encoding/decoding type:
   ![alt text](https://pp.userapi.com/c849520/v849520560/e15b4/p-m5WOkiKEE.jpg)<br />
    Here you can choose a cipher which you want to use during encryption/decryption
  ### Write a key window:
    If you use a cipher from this list: Scytale, Caesar, RailFence, Vigenere; Program will ask you to write a key:
   ![alt text](https://pp.userapi.com/c851224/v851224318/68775/O-zclEn6tUA.jpg)
  ### Output lineEdit:
   ![alt text](https://pp.userapi.com/c844416/v844416560/15d54b/w8ieQL7gIzY.jpg)<br />
    Here you will see your encrypted/decrypted text.
   #### Be caerful! In some cases(not valid key("abc" key in caesar cipher e.g.) or not valid text("64538" decrypt in binary cipher e.g.) may cause -Error- message to output, app will work correctly, but its just good for you not to do mistakes like this):
   ![alt text](https://pp.userapi.com/c844416/v844416560/15d56a/ROsVznJXHhg.jpg)<br />
