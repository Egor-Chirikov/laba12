def rec_f(q, n, q1):
    if n <= 1:
        return q1
    return q * rec_f(q, n-1, q1)


print(rec_f(2, 3, 2))
