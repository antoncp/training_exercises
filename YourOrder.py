def order(sentence):
    result = {}
    words = sentence.split()
    for word in words:
        for letter in word:
            if letter.isdigit():
                result[letter] = word
    return " ".join([word[1] for word in sorted(result.items())])
