# 数一个字符串各个字符的个数


def count_chars(s):
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts


if __name__ == "__main__":
    print(count_chars('hello'))
