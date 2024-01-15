def max_consec_zeros(s):
    num2words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }
    zeros, cur_zeros = 0, 0
    binar = bin(int(s))
    str_binar = str(binar)
    for i in range(1, len(str_binar)):
        if str_binar[i] == "0" and str_binar[i - 1] == "0":
            if not cur_zeros:
                cur_zeros += 2
            else:
                cur_zeros += 1
        else:
            if cur_zeros:
                zeros = max(zeros, cur_zeros)
                cur_zeros = 0
    zeros = max(zeros, cur_zeros)
    if not zeros and str_binar.count("0") > 1:
        zeros = 1
    return num2words[zeros]
