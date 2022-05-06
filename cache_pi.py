DIGITS = 150_000


def pi_digits(x):
    """Generate x digits of Pi."""
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while x > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1 and x > 0:
            if x % 50 == 0:
                print(".", end="", flush=True)
            yield int(d)
            x -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1


if __name__ == "__main__":
    print(f"Generating {DIGITS} digits of Pi", end="")

    with open("pi.txt", "w", buffering=8) as f:
        [f.write(str(n)) for n in list(pi_digits(DIGITS + 1))]

    print(" Done.")
