import random
import string


def inttohex(data_in, mode=0):
    """
    converts list elements from int to hex and back
    mode : int to hex (0) , hex to int (1)
    """
    data_out = []
    if mode == 0:
        for i in range(len(data_in)):
            data_out.append(format(data_in[i], '02x'))
        return data_out
    elif mode == 1:
        for i in range(len(data_in)):
            data_out.append(int(data_in[i], 16))
        return data_out


def strtolist(data_in, mode=0):
    """
    mode 0: splits an ascii string and adds elements to a list.
    mode 1: converts list elements to ascii characters and joins them.
    """
    if mode == 0:
        data_out = []
        for i in range(len(data_in)):
            data_out.append(ord(data_in[i]))  # chr and ord functions for ascii conversions
        return data_out
    elif mode == 1:
        data_out = ''
        for i in range(16):
            data_out += chr(data_in[i])
        return data_out


def pad(str_in, mode=0, in_type=0):
    """
    mode : pad (0) , unpad (1)
    in_type: plaintext (0) , key (1)
    """
    sl = len(str_in)
    if mode == 0:
        if in_type == 0:
            if sl < 16:
                num = 16 - (sl % 16)
                str_in += chr(num) * num  # adds padding elements at the end of the string
        elif in_type == 1:
            if sl not in [16, 24, 32]:
                if sl < 16:
                    str_in += '0' * (16 - sl)
                elif sl < 24:
                    str_in += '0' * (24 - sl)
                elif sl < 32:
                    str_in += '0' * (32 - sl)
    elif mode == 1:
        if in_type == 0:
            str_in = str_in[0:-ord(str_in[-1])]  # removes the padding elements at the end of the string
    return str_in


def generate_key(KL=16):
    """
    Generates random key in ascii format for a given key length [16, 24, or 32]
    """
    random_key = ''.join(random.SystemRandom().
                         choice(string.printable[:95])
                         for i in range(KL))
    return random_key


def transpose(list_in):
    """
    Shuffle/transpose a given 16 element list from
    [ 0,  1,  2,  3,
      4,  5,  6,  7,
      8,  9, 10, 11,
     12, 13, 14, 15] to
    [ 0,  4,  8, 12,
      1,  5,  9, 13,
      2,  6, 10, 14,
      3,  7, 11, 15]
    """
    list_out = []
    for i in range(4):
        for j in range(4):
            list_out.append(list_in[i + 4 * j])
    return list_out


def gf_mul(multiplicand, multiplier):
    """
    Galois Field multiplication function for AES using irreducible polynomial
    x^8 + x^4 + x^3 + x^1 + 1
    """
    product = 0
    a = multiplicand
    b = multiplier
    while a * b:
        if b % 2:
            product ^= a
        if a > 128:
            a = (a << 1) ^ 283
        else:
            a <<= 1
        b >>= 1
    return product


def listxor(list1, list2):
    """
    returns list1 elements (xor) list2 elements
    """
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] ^ list2[i])
    return list3
