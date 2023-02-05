import re


def top_3_words(text):
    clean_text = re.sub(r"[^a-zA-Z\s+']", '', text.lower())
    word_list = {}
    for word in clean_text.split():
        if word.replace("'", "") == "":
            continue
        if word not in word_list:
            word_list[word] = 1
        else:
            word_list[word] += 1
    top_list = dict(sorted(word_list.items(),
                           key=lambda item: item[1], reverse=True))
    return list(top_list.keys())[:3]
