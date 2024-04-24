def memesorting(meme):
    receivers = {
        'Roma': ['b', 'u', 'g'],
        'Maxim': ['b', 'o', 'o', 'm'],
        'Danik': ['e', 'd', 'i', 't', 's'],
    }
    for i in meme:
        for col in receivers.values():
            if i.lower() == col[0]:
                col.pop(0)
        for name, col in receivers.items():
            if not col:
                return name
    return 'Vlad'
