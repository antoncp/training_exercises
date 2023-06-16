import itertools

COMB = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}

in_combs = [COMB[int(i)] for i in input()]
res = list(itertools.product(*in_combs))

print(' '.join([''.join(i) for i in res]))
