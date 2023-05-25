# Задача "Ближайший ноль". ID решения в Я.Контесте 87652874

from typing import List


def get_distance_to_zeros(street: List[str]) -> List[int]:
    """Calculates distance between zero numbers in the street."""
    new_street, current_frame = [], []
    no_zero_yet, last_zero_counter = True, 0
    for i in street:
        if i == '0':
            if no_zero_yet:
                new_street.extend(current_frame[::-1])
            else:
                end = last_zero_counter // 2
                start = last_zero_counter - end - 1
                new_street.extend((current_frame[:end]))
                new_street.extend((current_frame[start::-1]))
            new_street.append(0)
            current_frame = []
            last_zero_counter = 0
            no_zero_yet = False
            continue
        last_zero_counter += 1
        current_frame.append(last_zero_counter)
    return new_street + current_frame


if __name__ == '__main__':
    num_houses, street = int(input()), input().split()
    print(*get_distance_to_zeros(street))
