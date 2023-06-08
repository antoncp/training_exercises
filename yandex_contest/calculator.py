# Задача "Калькулятор". ID решения в Я.Контесте 88045593

OPERATORS = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x // y}


def calculate_the_list(entry_list: list) -> int:
    """Handles all mathematical operations inside the list with polish
    notation.
    """
    processing_list = []
    for i in entry_list:
        if i in OPERATORS:
            y = processing_list.pop()
            x = processing_list.pop()
            result = OPERATORS[i](x, y)
            processing_list.append(result)
        else:
            processing_list.append(int(i))
    return processing_list[-1]


if __name__ == '__main__':
    print(calculate_the_list(input().split()))
