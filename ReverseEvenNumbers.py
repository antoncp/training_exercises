def rev_sub(arr):
    new = []
    evens = []
    for i in arr:
        if i % 2 == 0:
            evens.append(i)
        else:
            if evens:
                new = new + list(reversed(evens))
                evens = []
            new.append(i)
    print(new + list(reversed(evens)))
