def unscramble(scramble):
    global word_list # available in preloaded
    suspects = list(filter(lambda x: len(x) == len(scramble), word_list))
    result = []
    for word in suspects:
        letters = list(scramble)
        for i in word:
            if i in letters:
                letters.remove(i)
            else:
                break
        if not letters:
            result.append(word)
    return result
