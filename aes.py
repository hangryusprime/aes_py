"""
AES implementation in Python 3
"""
from __init__ import *


class AES:
    start_time = time.time()

    def __init__(self, plain, key=None):
        plain = pad(plain, 0, 0)
        if key is None:
            key = generate_key(32)
            print(f"Generated Random Key(32B): '{key}'")
        elif len(key) > 32:
            while len(key) > 32 or key == '':
                key = input("Input valid key string (<=32B): ")
            key = pad(key, 0, 1)
        else:
            key = pad(key, 0, 1)
        self.key = str_list(key, 0)
        self.plain = str_list(plain, 0)
        self.round = 0
        self.mode = 0
        if len(self.key) == 16:
            self.round_count = 11
        elif len(self.key) == 24:
            self.round_count = 13
        else:
            self.round_count = 15
        self.byte_count = 16 * self.round_count
        self.round_keys = [0]
        self.key_schedule()

    def key_expansion_core(self, key_seg, index, exp_mode):
        if exp_mode == 0:
            key_seg = key_seg[1:] + key_seg[:1]
        for i in range(len(key_seg)):
            key_seg[i] = sbox[self.mode][key_seg[i]]
        if exp_mode == 0:
            key_seg[0] = key_seg[0] ^ rcon[index]
        return key_seg

    def key_schedule(self):
        round_keys = []
        key_len = len(self.key)
        for i in range(len(self.key)):
            round_keys.append(self.key[i])
        round_index = 1
        while len(round_keys) <= self.byte_count:
            i = 0
            round_index2 = 0
            while i < key_len:
                if i == 0 or (i == 16 and key_len == 32):
                    exp_mode = int(i/16)
                    temp = round_keys[-4:]
                    temp = self.key_expansion_core(temp, round_index, exp_mode)
                    word_index = ((round_index - 1) * key_len) + round_index2
                    round_keys.extend(list_xor(temp, round_keys[word_index: word_index + 4]))
                    i += 4
                else:
                    if key_len == 32:
                        intermediate_steps = 4
                    else:
                        intermediate_steps = int(key_len/4)
                    for j in range(1, intermediate_steps):
                        temp = round_keys[-4:]
                        word_index = ((round_index - 1) * key_len) + round_index2
                        round_keys.extend(list_xor(temp, round_keys[word_index + 4*j: word_index + 4*(j+1)]))
                        i += 4
                if key_len == 32 and i >= 15:
                    round_index2 = 16
            round_index += 1
        self.round_keys = round_keys[:self.byte_count]

    def add_round_key(self):
        self.plain = list_xor(self.plain, self.round_keys[self.round*16: (self.round+1)*16])

    def sub_bytes(self):
        sbox_used = sbox[self.mode]
        for i in range(16):
            self.plain[i] = sbox_used[self.plain[i]]

    def shift_rows(self):
        self.plain = transpose(self.plain)
        inv_index = self.mode * 2
        self.plain[4:8] = self.plain[5 + inv_index:8] + self.plain[4:5 + inv_index]
        self.plain[8:12] = self.plain[10:12] + self.plain[8:10]
        self.plain[-4:] = self.plain[15 - inv_index:] + self.plain[12:15 - inv_index]
        self.plain = transpose(self.plain)

    def mix_columns(self):
        temp_state = [0]*16
        self.plain = transpose(self.plain)
        for i in range(16):
            for (k, l) in matrix_pairs[i]:
                temp_plain = self.plain[l]
                temp_mix = mix_constant[self.mode][k]
                temp_state[i] = temp_state[i] ^ gf_mul(temp_plain, temp_mix)

        self.plain = transpose(temp_state)

    def encrypt(self):
        self.mode = 0
        self.round = 0
        for r in range(0, self.round_count, 1):
            if r == 0:
                self.add_round_key()
                self.round += 1
            elif r != self.round_count-1:
                self.sub_bytes()
                self.shift_rows()
                self.mix_columns()
                self.add_round_key()
                self.round += 1
            else:
                self.sub_bytes()
                self.shift_rows()
                self.add_round_key()
                print(f"Rounds\t\t {self.round} (encryption)")
                time_exec = time.time() - self.start_time
                print(f"Time(ms)\t {time_exec*1000}")
                print(f"Cipher(h)\t {int_hex(self.plain, 0)}")
                return str_list(self.plain, 1)

    def decrypt(self):
        self.mode = 1
        self.round = self.round_count-1
        for r in range(self.round_count - 1, -1, - 1):
            if r == self.round_count-1:
                self.add_round_key()
                self.round -= 1
            elif self.round != 0:
                self.shift_rows()
                self.sub_bytes()
                self.add_round_key()
                self.mix_columns()
                self.round -= 1
            else:
                self.shift_rows()
                self.sub_bytes()
                self.add_round_key()
                print(f"Rounds\t\t {self.round_count - 1 - self.round} (decryption)")
                time_exec = time.time() - self.start_time
                print(f"Time(ms)\t {time_exec*1000}")
                print(f"Plain(h)\t {int_hex(self.plain, 0)}")
                return str_list(self.plain, 1)


if __name__ == "__main__":
    test_plain = 'hahahahahahahaha'
    test_key = 'hahahahahahahahahahahahahahahaha'
    print(f"plain(a)\t {test_plain}")
    aes16 = AES(plain=test_plain, key=test_key)
    cipher = aes16.encrypt()
    print(f"cipher(a)\t {repr(cipher)}")
    aes16 = AES(plain=cipher, key=test_key)
    plain = aes16.decrypt()
    print(f"plain(a)\t {plain}")
