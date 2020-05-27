# Code copied  - Review
def square_mult(m, d, n):
    m = m % n  # Calculate the modulus at first
    d_bin = bin(d)
    d_bin = d_bin[:0] + d_bin[0 + 2:]  # Remove first two characters to have a bit array

    a = 1  # a <- 1

    # print("d_bin: {}".format(d_bin))
    # print("len d_bin: {}".format(len(d_bin)))

    # for i in reversed(range(0, len(d_bin))):
        # print("d_bin[{}]: {}".format(i, d_bin[i]))

    # print("Innnn")

    for i in range(0, len(d_bin) ):
        # print("d_bin[{}]: {}".format(i, d_bin[i]))

        a = (a * a) % n  # a <- a^2  mod n
        if d_bin[i:i+1] == '1':
            a = (a * m) % n  # a x m mod n
    return a % n
