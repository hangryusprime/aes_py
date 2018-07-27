"""
Test module for aespy.py
"""
import time
from test import test
from tqdm import tqdm
from aes import AES


def aespy_test(nIter=10**5):
    """
    Test module for key generation, Ascii to hex and Hex to ascii conversions.
    """
    # Initialization block
    aes = ['', '', '']
    ascii_key = ['', '', '']
    hex_key = ['', '', '']
    rand_ascii = ['', '', '']
    rand_hex = ['', '', '']
    rand_ascii2 = ['', '', '']
    # End of Initialization block

    def key_gen_timing(nIter=10**3):
        """
        Timing Module
        """
        exec_time = [0]*3
        min_time = [0]*3
        max_time = [0]*3
        avg_exec_time = [0]*3
        random_key = ['']
        for i in range(3):
            for j in tqdm(range(nIter), desc=f"Timing({(i+2)*8}B key "
                                                  f"Generation)"):
                start_time = time.clock()
                random_key[0] = aes[i].generate_key()
                iter_time = (time.clock() - start_time)
                exec_time[i] += iter_time
                if j == 0:
                    min_time[i] = max_time[i] = iter_time
                else:
                    if iter_time < min_time[i]:
                        min_time[i] = iter_time
                    elif iter_time > max_time[i]:
                        max_time[i] = iter_time
            avg_exec_time[i] = exec_time[i]/nIter
            result_str = (f"Execution times for {(i+2)*8} Bytes over "
                          f"{nIter} iterations\n"
                          f"Mean \t: {round(avg_exec_time[i]*1000,3)} ms\n"
                          f"Fastest\t: {round(min_time[i]*1000,3)} ms\n"
                          f"Slowest\t: {round(max_time[i]*1000,3)} ms")
            print(result_str)
        return "Timing Completed"

    aes[0] = AES(KL=16)
    aes[1] = AES(KL=24)
    aes[2] = AES(KL=32)
    ascii_key[0] = r'''t~S~\"L"I\n2LE<n'''
    hex_key[0] = b'747e537e5c224c22495c6e324c453c6e'
    ascii_key[1] = r'''L&5/f\fdy]\N{+}3\tL*GoY{'''
    hex_key[1] = b'4c26352f665c6664795d5c4e7b2b7d335c744c2a476f597b'
    ascii_key[2] = r'''-\'<W<\a@Wh"@]!mz\bE4,@s\rF9"\\a;'''
    hex_key[2] = b'2d5c273c573c5c6140576822405d216d7a5c6245342c40735c724639225c5c613b'

    print(key_gen_timing(nIter))

    for i in tqdm(range(3), desc=f"ascii to hex conversion"):
        test(hex_key[i], aes[i].ascii_to_hex(ascii_key[i]))

    for i in tqdm(range(3), desc=f"hex to ascii conversion"):
        test(ascii_key[i], aes[i].hex_to_ascii(hex_key[i]))

    for i in range(3):
        for _ in tqdm(range(nIter), desc=f"{(i+2)*8}B a2h and back"):
            rand_ascii[i] = aes[i].generate_key()
            rand_hex[i] = aes[i].ascii_to_hex(rand_ascii[i])
            rand_ascii2[i] = aes[i].hex_to_ascii(rand_hex[i])
            test(rand_ascii[i], rand_ascii2[i])


if __name__ == "__main__":
    aespy_test(10**5)
