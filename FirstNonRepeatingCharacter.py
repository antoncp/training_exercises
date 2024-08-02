def first_non_repeating_letter(s):
    checked = set()
    for i in s:
        if i.lower() not in checked:
            if s.lower().count(i.lower()) > 1:
                checked.add(i.lower)
            else:
                return i
    return ''
