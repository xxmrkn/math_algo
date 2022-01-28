r = 2.0
a = 2.0
repeats = 5

for i in range(1, repeats+1):
    zahyou_x, zahyou_y = a, a*a

    sessen_a = 2.0 * zahyou_x
    sessen_b = zahyou_y - sessen_a * zahyou_x

    next_a = (r-sessen_b)/sessen_a
    print("Step #%d: a = %.12f -> %.12f" % (i, a, next_a))
    a = next_a
