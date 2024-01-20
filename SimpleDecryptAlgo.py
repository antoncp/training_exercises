def decrypt(test_key):
    key = [i for i in test_key if i.isalpha()]
    alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    repeats = {}
    for i in set(key):
        repeats[i] = key.count(i)
    return "".join(
        str(repeats[i]) if i in repeats.keys() else "0" for i in alphabet
    )
