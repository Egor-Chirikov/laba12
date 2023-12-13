def rec_f(q, n, q1):
    if n <= 1:
        return [q1, q1]
    rem = rec_f(q, n-1, q1)
    w = rem[0] * q
    return [w, rem[1] + w]


print(rec_f(2, 3, 2)[1])
