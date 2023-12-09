def remove_smallest(numbers):
    numbers2 = list(numbers)
    if numbers2:
        numbers2.remove(min(numbers2))
    return numbers2
