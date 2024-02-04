from preloaded import NATO  # NATO['A'] == 'Alfa', etc


def to_nato(words: str) -> str:
    return " ".join(
        " ".join(NATO[i] if i.isalpha() else i for i in words.upper()).split()
    )
