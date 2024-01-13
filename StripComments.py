def strip_comments(strng, markers):
    parts = strng.split("\n")
    for i in range(len(parts)):
        sentence = parts[i]
        for letter in sentence:
            if letter in markers:
                parts[i] = sentence[: sentence.index(letter)].rstrip()
                break
    return "\n".join(parts)
