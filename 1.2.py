def solve(s1, s2):
    cnt = {}

    for c1 in s1:
        if c1 in cnt:
            cnt[c1] += 1
        else:
            cnt[c1] = 1

    for c2 in s2:
        if c2 in cnt:
            cnt[c2] -= 1
        else:
            cnt[c2] = -1

    for k, v in cnt.items():
        if v != 0:
            return False

    return True


def main():
    test_cases = [
        ('abc', 'acb', True),
        ('abc', 'acd', False),
    ]

    for s1, s2, out in test_cases:
        assert solve(s1, s2) == out


if __name__ == '__main__':
    main()
