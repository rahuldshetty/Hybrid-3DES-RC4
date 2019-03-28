def get_val(text):
    for character in text:
        return ord(character)


def get_keys(key):

    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + get_val(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]
    return S  # Swap


key = "password"


