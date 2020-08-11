def solve(s):
    cnt = {}

    cleaned = s.lower().replace(' ', '')

    for c in cleaned:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1

    odd_count = list(map(lambda x: x % 2, cnt.values())).count(1)

    if len(cleaned) % 2 == 0:
        return odd_count == 0
    else:
        return odd_count <= 1


def main():
    test_cases = [
        ('Tact Coa', True)
    ]

    for s, out in test_cases:
        assert solve(s) == out


if __name__ == '__main__':
    main()
