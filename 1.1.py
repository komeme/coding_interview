def solve(s: str):
    seen = {}

    for c in s:
        if c in seen:
            return False
        seen[c] = True

    return True


def main():
    test_cases = [
        ('a', True),
        ('abc', True),
        ('aaa', False),
    ]

    for i, o in test_cases:
        assert solve(i) == o


if __name__ == '__main__':
    main()
