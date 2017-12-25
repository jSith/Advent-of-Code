def compare_lowest(a, b):
    bin_a = list(reversed(list('{0:b}'.format(a))))
    bin_b = list(reversed(list('{0:b}'.format(b))))
    if len(bin_a) < 16 or len(bin_b) < 16:
        return False
    for i in range(0, 16):
        if bin_a[i] != bin_b[i]:
            return False
    return True


def generate_value(previous, a):
    factor_a = 16807
    factor_b = 48271
    value = 1
    if a:
        while value % 4 != 0:
            value = previous * factor_a % 2147483647
            previous = value
    else:
        while value % 8 != 0:
            value = previous * factor_b % 2147483647
            previous = value
    return value


def count_matches(value_a, value_b):
    similarities = 0
    i = 0
    next_a = value_a
    next_b = value_b
    while i < 5000000:
        next_a = generate_value(next_a, True)
        next_b = generate_value(next_b, False)
        if compare_lowest(next_a, next_b):
            similarities = similarities + 1
        i = i + 1

    return similarities


def main():
    gen_a = 277
    gen_b = 349
    print(count_matches(gen_a, gen_b))


if __name__ == '__main__':
    main()