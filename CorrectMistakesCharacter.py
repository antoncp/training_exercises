def correct(s):
    changes = {"5": "S", "0": "O", "1": "I"}
    return "".join(changes[i] if i in "501" else i for i in s)
