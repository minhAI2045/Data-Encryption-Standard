# Hàm chuyển đổi binary sang decimal
def binary_to_decimal(binary_string):
    decimal = 0
    for digit in binary_string:
        decimal = decimal * 2
        if digit == '1':
            decimal = decimal + 1
    return decimal

# Hàm chuyển đổi hex sang binary
def hex_to_binary(character):
        hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', 
                    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 
                    'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 
                    'f': '1111'}
        return hex_dict[character]

# Hàm xor
def xor(a, b):
    result = [(ord(x) ^ ord(y)) for x, y in zip(a, b)]
    result = "".join(str(x) for x in result)
    return result

# Hàm swap:
def swap(string, a, b):
    string = list(string)
    string[a], string[b] = string[b], string[a]
    string = "".join(string)
    return string

# Hàm rotate
def left_rotate(string, a):
    return string[a:] + string[:a]

def binary_to_decimal(binary_string):
    decimal = 0
    for digit in binary_string:
        decimal = decimal * 2
        if digit == '1':
            decimal = decimal + 1
    return decimal

def decimal_to_binary(decimal):
    binary_dict = {0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100', 
                    5: '0101', 6: '0110', 7: '0111', 8: '1000', 9: '1001', 
                    10: '1010', 11: '1011', 12: '1100', 13: '1101', 14: '1110', 
                    15: '1111'}
    return binary_dict[decimal]

def hex_to_binary(character):
        hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', 
                    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 
                    'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 
                    'f': '1111'}
        return hex_dict[character]

def convert_text_to_binary(plaintext, key):
    plaintext_binary = ""
    key_binary = ""
    for i in range(0, len(plaintext)):
        plaintext_binary += hex_to_binary(plaintext[i])
    for i in range(0, len(key)):
        key_binary += hex_to_binary(key[i])
    return plaintext_binary, key_binary

def convert_binary_to_hex(string):
    chunked = [string[i:i+4] for i in range(0, len(string), 4)]
    hex_list = [hex(int(chunk, 2))[2:] for chunk in chunked]
    return "".join(hex_list)