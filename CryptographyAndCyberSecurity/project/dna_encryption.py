import argparse
from more_itertools import chunked
from bidict import bidict
from typing import Tuple

"""
some explenations
     - bidict - allows for bi-directional dictionary access, for ex. DNA_LOOKUP["00"] == 'A', DNA_LOOKUP.inv['A'] == "00"
     - argparse - module for simple script argument parsing, we provide it with expected arguments, like text, key and so on
     - len(sth) - returns length of sth (might be a string, list or any iterable)
     - int(sth) - converts sth to integer
     - "0" * 3 == "000"
     - ord('a') == 97 - returns number in ascii table of given character
     - chr(97) == 'a' - returns a character from ascii table from given number
     - a ^ b - XOR of a and b
     - range(0, 3) - creates an iterable [0, 1, 2]
     - zip([1,2,3], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b'), (3, 'c')]
     - '123456'[1:3] == '234'
     - '123456'[:3] == '1234'
     - chunked([1,2,3,4], 2) == ([1,2], [3,4])
"""

DNA_LOOKUP = bidict({
    '00': 'A',
    '01': 'G',
    '10': 'C',
    '11': 'T'
})


def parse_args() -> Tuple[str, str, bool, bool]:
    """Function for script argument parsing"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", help="plain text to encrypt", type=str)
    parser.add_argument("-k", "--key", help="OTP encription key", type=str)
    parser.add_argument("-e", "--encrypt", help="encryption flag", action='store_true')
    parser.add_argument("-d", "--decrypt", help="decryption flag", action='store_true')
    args = parser.parse_args()
    return args.text, args.key, args.encrypt, args.decrypt


def prepare_key(text: str, key: str) -> str:
    """Function adjusting key length to given text

    :param text: plain text in DNA notation to decrypt
    :param key: OTP key
    """
    return (key * int((len(text) / len(key)) + 1))[:len(text)]


def left_pad(number: str) -> str:
    """Function feeling string with trailing zeros at the begining
    :param number: string representing binary number
    """
    return ("0" * (8 - len(number))) + number


def encrypt(text: str, key: str) -> str:
    """Function encrypting given text with the key to DNA notation

    :param text: plain text in DNA notation to decrypt
    :param key: OTP key
    """

    binary = "".join([left_pad(format(ord(a) ^ ord(b), 'b')) for a, b in zip(text, key)])
    dna = "".join([DNA_LOOKUP["".join(chunk)] for chunk in chunked(binary, 2)])
    return dna


def decrypt(text: str, key: str) -> str:
    """Function decrypting given text with the key from DNA notation

    :param text: plain text in DNA notation to decrypt
    :param key: OTP key
    """
    reverse_dna = "".join([DNA_LOOKUP.inv[letter] for letter in text])
    bin_string = (reverse_dna[i:i + 8] for i in range(0, len(reverse_dna), 8))
    string = ''.join(chr(int(char, 2) ^ ord(key)) for char, key in zip(bin_string, key))
    return string


text, key, encryption, decryption = parse_args()
key = prepare_key(text, key)
if encryption:
    print(encrypt(text, key))
if decryption:
    print(decrypt(text, key))
