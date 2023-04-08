def sort_array(source_array):
    sort_odds = sorted([i for i in source_array if i % 2 != 0])
    final_array = []
    for i in source_array:
        if i % 2 == 0:
            final_array.append(i)
        else:
            final_array.append(sort_odds.pop(0))
    return final_array
