def to_camel_case(text):
    if not text:
        return ""
    splited_text = text.replace('_', ' ').replace('-', ' ').split()
    return splited_text[0] + ''.join(word.capitalize() for word in splited_text[1:])
