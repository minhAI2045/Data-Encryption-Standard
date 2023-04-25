from utils import *
# Bước 1: IP
def initial_permutation(plaintext_binary):
    plaintext_ip = ""
    ip_table = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1, 
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7] 
    for i in range(0, 64):
        plaintext_ip += plaintext_binary[ip_table[i] - 1]
    return plaintext_ip

# Bước 3: IP-1
def inverse_initital_permutation(plaintext_binary):
    plaintext_ip = ""
    ip_inverse_table = [40, 8, 48, 16, 56, 24, 64, 32,
                        39, 7, 47, 15, 55, 23, 63, 31,
                        38, 6, 46, 14, 54, 22, 62, 30,
                        37, 5, 45, 13, 53, 21, 61, 29,
                        36, 4, 44, 12, 52, 20, 60, 28,
                        35, 3, 43, 11, 51, 19, 59, 27,
                        34, 2, 42, 10, 50, 18, 58, 26,
                        33, 1, 41, 9, 49, 17, 57, 25] 
    for i in range(0, 64):
        plaintext_ip += plaintext_binary[ip_inverse_table[i] - 1]
    return plaintext_ip

# Bước 2
def key_depend_computation(plaintext_binary_ip, KS):
    LPT = []
    RPT = []
    for i in range(0, 17):
        if i == 0:
            LPT.append(plaintext_binary_ip[:32])
            RPT.append(plaintext_binary_ip[32:])
        else:
            LPT_temp = RPT[-1]
            RPT_temp = xor(LPT[-1], cipher_function(RPT[-1], KS[-i]))
            LPT.append(LPT_temp)
            RPT.append(RPT_temp)
    print("LPT là ", LPT)
    print("RPT là ", RPT)
    return RPT[-1] + LPT[-1]

# Hàm key schedule 
def key_schedule(key_binary):
    # Hàm permuted choice 1
    def permuted_choice_1(key_binary):
        C_temp = ""
        D_temp = ""
        permuted_choice_1_table = """57 49 41 33 25 17 9 
                                    1 58 50 42 34 26 18 
                                    10 2 59 51 43 35 27 
                                    19 11 3 60 52 44 36 
                                    63 55 47 39 31 23 15 
                                    7 62 54 46 38 30 22 
                                    14 6 61 53 45 37 29 
                                    21 13 5 28 20 12 4""".split()
        permuted_choice_1_table = [int(num) for num in permuted_choice_1_table]
        for i in range(0, 28):
            C_temp += key_binary[permuted_choice_1_table[i] - 1]
            D_temp += key_binary[permuted_choice_1_table[i + 28] - 1]
        return C_temp, D_temp
    # Hàm permuted choice 2
    def permuted_choice_2(C, D, a):
        C_temp = left_rotate(C, a)
        D_temp = left_rotate(D, a)
        K = ""
        permuted_choice_2_table = """14 17 11 24 1 5 
                                    3 28 15 6 21 10 
                                    23 19 12 4 26 8 
                                    16 7 27 20 13 2 
                                    41 52 31 37 47 55 
                                    30 40 51 45 33 48 
                                    44 49 39 56 34 53 
                                    46 42 50 36 29 32""".split()
        permuted_choice_2_table = [int(num) for num in permuted_choice_2_table]
        sum = C_temp + D_temp
        for i in range(0, 48):
            K += sum[permuted_choice_2_table[i] - 1]
        return C_temp, D_temp, K

    key_binary_56 = key_binary
    key_binary_56 = list(key_binary_56)
    index_to_delete = [i*8 - 1 for i in range(1, 9)]
    for index in sorted(index_to_delete, reverse=True):
        del key_binary_56[index]
    key_binary_56 = "".join(key_binary_56)
    print("Key binary 56 là: ", key_binary_56)
    KS = []
    KS.append(key_binary_56)
    C = []
    D = []
    number_left_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for i in range(0, 17):
        if i == 0:
            C_temp, D_temp = permuted_choice_1(key_binary)
            C.append(C_temp)
            D.append(D_temp)
        else:
            C_temp, D_temp, K = permuted_choice_2(C[-1], D[-1], number_left_shifts[i-1])
            C.append(C_temp)
            D.append(D_temp)
            KS.append(K)
    print("C là", C)
    print("D là", D)
    return KS
    
    
        
    
# Hàm cipher function từ R và K sang 32 bit P
def cipher_function(R, K):
    # Hàm p initial permutation
    def p_initital_permutation(P):
        p_temp = ""
        ip_inverse_table = """16 7 20 21 
                            29 12 28 17 
                            1 15 23 26 
                            5 18 31 10 
                            2 8 24 14 
                            32 27 3 9 
                            19 13 30 6 
                            22 11 4 25""".split()
        ip_inverse_table = [int(num) for num in ip_inverse_table]
        for i in range(0, 32):
            p_temp += P[ip_inverse_table[i] - 1]
        return p_temp

    E_table = [32, 1, 2, 3, 4, 5, 
                4, 5, 6, 7, 8, 9, 
                8, 9, 10, 11, 12, 13, 
                12, 13, 14, 15, 16, 17, 
                16, 17, 18, 19, 20, 21, 
                20, 21, 22, 23, 24, 25, 
                24, 25, 26, 27, 28, 29, 
                28, 29, 30, 31, 32, 1 ]
    R_48 = ""
    for i in range(0, 48):
        R_48 += R[E_table[i] - 1]
    

    string_temp = xor(R_48, K)
    print("String temp là: ", string_temp)
    parts = [string_temp[i:i+6] for i in range(0, len(string_temp), 6)]
    S = []
    S_table = []
    for i in range(0, 8):
        S.append(parts[i])
        
    S1_table = """14 4 13 1 2 15 11 
        8 3 10 6 12 5 9 0 7 0 15 7 4 14 
        2 13 1 10 6 12 11 9 5 3 8 4 1 14 
        8 13 6 2 11 15 12 9 7 3 10 5 0 15 
        12 8 2 4 9 1 7 5 11 3 14 10 0 6 13""".split()
    S1_table = [int(num) for num in S1_table]

    S2_table = """15 1 8 14 6 11 3 4 9 7 2 13 12 0 5 10 
        3 13 4 7 15 2 8 14 12 0 1 10 6 9 11 5 
        0 14 7 11 10 4 13 1 5 8 12 6 9 3 2 15 
        13 8 10 1 3 15 4 2 11 6 7 12 0 5 14 9 """.split()
    S2_table = [int(num) for num in S2_table]

    S3_table = """10 0 9 14 6 3 15 5 1 13 12 7 11 4 2 8 
        13 7 0 9 3 4 6 10 2 8 5 14 12 11 15 1 
        13 6 4 9 8 15 3 0 11 1 2 12 5 10 14 7 
        1 10 13 0 6 9 8 7 4 15 14 3 11 5 2 12""".split()
    S3_table = [int(num) for num in S3_table]

    S4_table = """7 13 14 3 0 6 9 10 1 2 8 5 11 12 4 15 
        13 8 11 5 6 15 0 3 4 7 2 12 1 10 14 9 
        10 6 9 0 12 11 7 13 15 1 3 14 5 2 8 4 
        3 15 0 6 10 1 13 8 9 4 5 11 12 7 2 14""".split()
    S4_table = [int(num) for num in S4_table]

    S5_table = """2 12 4 1 7 10 11 6 8 5 3 15 13 0 14 9 
        14 11 2 12 4 7 13 1 5 0 15 10 3 9 8 6 
        4 2 1 11 10 13 7 8 15 9 12 5 6 3 0 14 
        11 8 12 7 1 14 2 13 6 15 0 9 10 4 5 3""".split()
    S5_table = [int(num) for num in S5_table]

    S6_table = """12 1 10 15 9 2 6 8 0 13 3 4 14 7 5 11 
        10 15 4 2 7 12 9 5 6 1 13 14 0 11 3 8 
        9 14 15 5 2 8 12 3 7 0 4 10 1 13 11 6 
        4 3 2 12 9 5 15 10 11 14 1 7 6 0 8 13 """.split()
    S6_table = [int(num) for num in S6_table]

    S7_table = """4 11 2 14 15 0 8 13 3 12 9 7 5 10 6 1 
        13 0 11 7 4 9 1 10 14 3 5 12 2 15 8 6 
        1 4 11 13 12 3 7 14 10 15 6 8 0 5 9 2 
        6 11 13 8 1 4 10 7 9 5 0 15 14 2 3 12 """.split()
    S7_table = [int(num) for num in S7_table]

    S8_table = """13 2 8 4 6 15 11 1 10 9 3 14 5 0 12 7 
        1 15 13 8 10 3 7 4 12 5 6 11 0 14 9 2 
        7 11 4 1 9 12 14 2 0 6 10 13 15 3 5 8 
        2 1 14 7 4 10 8 13 15 12 9 0 3 5 6 11""".split()
    S8_table = [int(num) for num in S8_table]

    S_table = [S1_table, S2_table, S3_table, S4_table, S5_table, S6_table, S7_table, S8_table]
    for i in range(0, 8):
        a = binary_to_decimal(S[i][0] + S[i][-1])
        b = binary_to_decimal(S[i][1:-1])
        S[i] = decimal_to_binary(S_table[i][16*a + b])
    
    P = ""
    for i in range(0, 8):
        P += S[i]
        # print(len(S[i]))
    # print("a")
    print("P trước khi IP là", P)
    P = p_initital_permutation(P)
    print("P là", P)
    return P


# Khai báo plaintext 64 bit và key 64 bit
ciphertext = "b5219ee81aa7499d"
key = "752878397493cb70"
ciphertext_binary, key_binary = convert_text_to_binary(ciphertext, key)
print(f"Ciphertext là: {ciphertext} có len {len(ciphertext)}")
print(f"Key là: {key} có len {len(key)}")
print(f"Ciphertext là: {ciphertext_binary} có len {len(ciphertext_binary)}")
print(f"Key là: {key_binary} có len {len(key_binary)}")
# Bước 1: IP plaintext
ciphertext_binary = initial_permutation(ciphertext_binary)
print(f"Ciphertext sau biến đổi IP là: {ciphertext_binary} có len {len(ciphertext_binary)}")
# Bước 2: Key-depend computation
KS = key_schedule(key_binary)
print("KS là", KS)
ciphertext_binary = key_depend_computation(ciphertext_binary, KS)
print(f"Ciphertext sau bước 2 là: {ciphertext_binary} có len {len(ciphertext_binary)}")
# Bước 3: IP-1 plaintext
ciphertext_binary = inverse_initital_permutation(ciphertext_binary)
print(f"Ciphertext sau bước 3 là: {ciphertext_binary} có len {len(ciphertext_binary)}")
plaintext = convert_binary_to_hex(ciphertext_binary)
print(f"Plaintext sau khi mã hóa: {plaintext}")

   
