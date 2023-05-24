# Задача "Ближайший ноль". ID решения в Я.Контесте 87634286

num_houses, street = int(input()), input().split()
new_street = []
current_frame = []
first_zero = False
last_zero = 0
for i in street:
    if i == '0':
        if not first_zero:
            new_street.extend(current_frame[::-1])
        else:
            end = last_zero // 2
            start = last_zero - end - 1
            new_street.extend((current_frame[:end]))
            new_street.extend((current_frame[start::-1]))
        new_street.append(0)
        current_frame = []
        last_zero = 0
        first_zero = True
        continue
    last_zero += 1
    current_frame.append(last_zero)
print(" ".join(str(i) for i in (new_street + current_frame)))
