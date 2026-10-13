def merge_sorted(a,b):
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result

if __name__ == "__main__":
    a = [1, 3, 5, 7]
    b = [2, 4, 6]
    end = merge_sorted(a,b)
    print(end)