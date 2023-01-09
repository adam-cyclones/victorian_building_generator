# Math shortcuts for easier to reason about code


def half(n):
    return n / 2


def pos_neg(n):
    calculated = {
        "pos": n,
        "neg": n * -1
    }
    return calculated


def foot(imperial_value):
    return imperial_value * 0.3048
