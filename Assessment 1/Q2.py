def char_to_num(ch):
    if type(ch) is not str or len(ch) != 1:
        raise Exception(
            f"Incorrect usage of char_to_num. Expect a single character but got {ch} of type: {type(ch)}"
        )

    ascii_char = ord(ch)

    if ascii_char < ord("a") or ascii_char > ord("z"):
        raise Exception(
            f"Incorrect usage of char_to_num. We expect the character to be a from a to z . Received: {ch}"
        )
    return ord(ch) - ord("a") + 1

def num_to_char(num):
    if type(num) is not int or num < 0:
        raise Exception(
            f"Incorrect usage of num_to_char. We expect a positive integer. Received: {num}"
        )
    return chr(((num - 1) % 26) + ord("a"))

# a)

def encrypt_char(ch):
    num = char_to_num(ch)
    if num % 6 == 0:
        num = num * 17
    elif num % 2 == 0:
        num = num * 8
    elif num % 3 == 0:
        num = num + 101
    return num_to_char(num)

print(encrypt_char("a"))

# b)
def encrypt_word(word):
    encrypted_word = ""
    for ch in word:
        encrypted_word += encrypt_char(ch)
    return encrypted_word
print(encrypt_word("b"))


