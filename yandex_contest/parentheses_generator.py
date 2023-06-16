def gen_par(open, close, current, result):
    if open == 0 and close == 0:
        result.append(current)
        return
    if open > 0:
        gen_par(open - 1, close, current + '(', result)
    if close > open:
        gen_par(open, close - 1, current + ')', result)


result = []
n = int(input())
gen_par(n, n, '', result)
for i in result:
    print(i)
