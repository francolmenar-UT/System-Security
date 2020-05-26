# Code copied  - Review
def exp_func(x, y):
    exp = bin(y)
    value = x

    for i in range(3, len(exp)):
        value = value * value
        if (exp[i:i + 1] == '1'):
            value = value * x
    return value
