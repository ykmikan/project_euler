TAEGET_NUM = 999

n_3 = TAEGET_NUM // 3
sum_3 = n_3 * ( 2 * 3 + (n_3 - 1) * 3) // 2

n_5 = TAEGET_NUM // 5
sum_5 = n_5 * ( 2 * 5 + (n_5 - 1) * 5) // 2

n_15 = TAEGET_NUM // 15
sum_15 = n_15 * ( 2 * 15 + (n_15 - 1) * 15) // 2

print(sum_3 + sum_5 - sum_15)