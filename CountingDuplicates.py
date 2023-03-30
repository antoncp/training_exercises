def duplicate_count(text):
    return len(['1' for i in set(text.lower()) if text.lower().count(i) > 1])
