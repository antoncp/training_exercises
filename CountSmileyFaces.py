import re


def count_smileys(arr):
    mask = "[:;][-~]?[)D]"
    count = 0
    for i in arr:
        if re.search(mask, i):
            count += 1
    return count
