import random
import string
import time

sbox = [[ 99, 124, 119, 123, 242, 107, 111, 197,  48,   1, 103,  43, 254, 215, 171, 118,
         202, 130, 201, 125, 250,  89,  71, 240, 173, 212, 162, 175, 156, 164, 114, 192,
         183, 253, 147,  38,  54,  63, 247, 204,  52, 165, 229, 241, 113, 216,  49,  21,
           4, 199,  35, 195,  24, 150,   5, 154,   7,  18, 128, 226, 235,  39, 178, 117,
           9, 131,  44,  26,  27, 110,  90, 160,  82,  59, 214, 179,  41, 227,  47, 132,
          83, 209,   0, 237,  32, 252, 177,  91, 106, 203, 190,  57,  74,  76,  88, 207,
         208, 239, 170, 251,  67,  77,  51, 133,  69, 249,   2, 127,  80,  60, 159, 168,
          81, 163,  64, 143, 146, 157,  56, 245, 188, 182, 218,  33,  16, 255, 243, 210,
         205,  12,  19, 236,  95, 151,  68,  23, 196, 167, 126,  61, 100,  93,  25, 115,
          96, 129,  79, 220,  34,  42, 144, 136,  70, 238, 184,  20, 222,  94,  11, 219,
         224,  50,  58,  10,  73,   6,  36,  92, 194, 211, 172,  98, 145, 149, 228, 121,
         231, 200,  55, 109, 141, 213,  78, 169, 108,  86, 244, 234, 101, 122, 174,   8,
         186, 120,  37,  46,  28, 166, 180, 198, 232, 221, 116,  31,  75, 189, 139, 138,
         112,  62, 181, 102,  72,   3, 246,  14,  97,  53,  87, 185, 134, 193,  29, 158,
         225, 248, 152,  17, 105, 217, 142, 148, 155,  30, 135, 233, 206,  85,  40, 223,
         140, 161, 137,  13, 191, 230,  66, 104,  65, 153,  45,  15, 176,  84, 187,  22],
        [ 82,   9, 106, 213,  48,  54, 165,  56, 191,  64, 163, 158, 129, 243, 215, 251,
         124, 227,  57, 130, 155,  47, 255, 135,  52, 142,  67,  68, 196, 222, 233, 203,
          84, 123, 148,  50, 166, 194,  35,  61, 238,  76, 149,  11,  66, 250, 195,  78,
           8,  46, 161, 102,  40, 217,  36, 178, 118,  91, 162,  73, 109, 139, 209,  37,
         114, 248, 246, 100, 134, 104, 152,  22, 212, 164,  92, 204,  93, 101, 182, 146,
         108, 112,  72,  80, 253, 237, 185, 218,  94,  21,  70,  87, 167, 141, 157, 132,
         144, 216, 171,   0, 140, 188, 211,  10, 247, 228,  88,   5, 184, 179,  69,   6,
         208,  44,  30, 143, 202,  63,  15,   2, 193, 175, 189,   3,   1,  19, 138, 107,
          58, 145,  17,  65,  79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115,
         150, 172, 116,  34, 231, 173,  53, 133, 226, 249,  55, 232,  28, 117, 223, 110,
          71, 241,  26, 113,  29,  41, 197, 137, 111, 183,  98,  14, 170,  24, 190,  27,
         252,  86,  62,  75, 198, 210, 121,  32, 154, 219, 192, 254, 120, 205,  90, 244,
          31, 221, 168,  51, 136,   7, 199,  49, 177,  18,  16,  89,  39, 128, 236,  95,
          96,  81, 127, 169,  25, 181,  74,  13,  45, 229, 122, 159, 147, 201, 156, 239,
         160, 224,  59,  77, 174,  42, 245, 176, 200, 235, 187,  60, 131,  83, 153,  97,
          23,  43,   4, 126, 186, 119, 214,  38, 225, 105,  20,  99,  85,  33,  12, 125]]
rcon = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54, 108, 216, 171, 77, 154]
mix_constant = [[ 2,  3,  1,  1,  1,  2,  3,  1,  1,  1,  2,  3,  3,  1,  1,  2],
                [14, 11, 13,  9,  9, 14, 11, 13, 13,  9, 14, 11, 11, 13,  9, 14]]
matrix_pairs = [[( 0, 0), ( 1, 4), ( 2,  8), ( 3, 12)], [( 0, 1), ( 1, 5), ( 2,  9), ( 3, 13)],
                [( 0, 2), ( 1, 6), ( 2, 10), ( 3, 14)], [( 0, 3), ( 1, 7), ( 2, 11), ( 3, 15)],
                [( 4, 0), ( 5, 4), ( 6,  8), ( 7, 12)], [( 4, 1), ( 5, 5), ( 6,  9), ( 7, 13)],
                [( 4, 2), ( 5, 6), ( 6, 10), ( 7, 14)], [( 4, 3), ( 5, 7), ( 6, 11), ( 7, 15)],
                [( 8, 0), ( 9, 4), (10,  8), (11, 12)], [( 8, 1), ( 9, 5), (10,  9), (11, 13)],
                [( 8, 2), ( 9, 6), (10, 10), (11, 14)], [( 8, 3), ( 9, 7), (10, 11), (11, 15)],
                [(12, 0), (13, 4), (14,  8), (15, 12)], [(12, 1), (13, 5), (14,  9), (15, 13)],
                [(12, 2), (13, 6), (14, 10), (15, 14)], [(12, 3), (13, 7), (14, 11), (15, 15)]]


def int_hex(data_in, mode=0):
    """
    converts list elements from int to hex and back
    mode : int to hex (0) , hex to int (1)
    """
    data_out = []
    if mode == 0:
        for i in range(len(data_in)):
            data_out.append(format(data_in[i], '02x'))
        return data_out
    for i in range(len(data_in)):
        data_out.append(int(data_in[i], 16))
    return data_out


def str_list(data_in, mode=0):
    """
    mode 0: splits an ascii string and adds elements to a list.
    mode 1: converts list elements to ascii characters and joins them.
    """
    if mode == 0:
        data_out = []
        for i in range(len(data_in)):
            data_out.append(ord(data_in[i]))  # chr and ord functions for ascii conversions
        return data_out
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


def generate_key(key_len=16):
    """
    Generates random key in ascii format for a given key length [16, 24, or 32]
    """
    random_key = ''.join(random.SystemRandom().
                         choice(string.printable[:95])
                         for _ in range(key_len))
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
    while a * b > 0:
        if b % 2:
            product ^= a
        if a >= 128:
            a = (a << 1) ^ 283
        else:
            a <<= 1
        b >>= 1
    return product


def list_xor(list1, list2):
    """
    returns list1 elements (xor) list2 elements
    """
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] ^ list2[i])
    return list3
