def reverse_fizzbuzz(st):
    for num, i in enumerate(st.split()):
        if i.isdigit():
            start = int(i) - num
            new_st = []
            for x in range(len(st.split())):
                new_st.append(start)
                start += 1
            return new_st
    vars = {
        "Fizz Buzz": [9, 10],
        "Buzz Fizz": [5, 6],
        "Fizz": [3],
        "FizzBuzz": [15],
        "Buzz": [5],
    }
    return vars.get(st)
