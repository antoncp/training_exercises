def group_anagrams(words):
    out = {}
    for word in words:
        s_word = "".join(sorted(word))
        if out.get(s_word):
            out[s_word] = out[s_word] + [word]
        else:
            out[s_word] = [word]
    return [i for i in out.values()]
