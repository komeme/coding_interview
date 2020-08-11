def solve(s, size):
    space_count = 0
    for c in s:
        if c == ' ':
            space_count += 1

    ans = [' '] * (size + space_count * 2)

    idx = 0
    for i in range(size):
        if s[i] == ' ':
            ans[idx] = '%'
            ans[idx + 1] = '2'
            ans[idx + 2] = '0'
            idx += 3
        else:
            ans[idx] = s[i]
            idx += 1

    return ''.join(ans)


def main():
    test_cases = [
        ("Mr John Smith", 13, "Mr%20John%20Smith")
    ]

    for s, size, out in test_cases:
        assert solve(s, size) == out, "expected: {}, actual: {}".format(out, solve(s, size))


if __name__ == '__main__':
    main()
