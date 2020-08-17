def Triple(n1, n2, n3):
    s1 = n1 ** 2
    s2 = n2 ** 2
    s3 = n3 ** 2
    if s1 + s2 == s3:
        return 1
    elif s2 + s3 == s1:
        return 1
    elif s3 + s1 == s2:
        return 1
    else:
        return 0


def tripleSquareSum(a):
    ans = list()
    for i in range(len(a) - 2):
        ans.append(Triple(a[i], a[i + 1], a[i + 2]))
    return ans


a = [0, 5, 5, 0, 5, 13, 12]
print(tripleSquareSum(a))

