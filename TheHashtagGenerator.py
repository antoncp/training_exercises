def generate_hashtag(s: str):
    final = ''.join(s.title().split())
    if len(final) > 140 or not final:
        return False
    return '#' + final
