# from itertools import combinations


def prefixStrings(a, b):
    c = ConcactenateStrings(a)
    for val in b:
        if not val in c:
            return False
    return True


def ConcactenateStrings(a):
    c = set()
    c.add(a[0])
    for i in range(1, len(a) + 2):
        c.add("".join(a[0:i]))
    return c
    # return list(combinations(a, len(a))) + list(combinations(a, 1))


a = ["one", "two", "three"]
b = ["onetwo", "one"]
print(prefixStrings(a, b))
