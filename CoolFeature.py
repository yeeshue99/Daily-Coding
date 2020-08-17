from itertools import product


def coolFeature(a, b, query):
    queries = []
    for q in query:
        if len(q) == 3:
            b[q[1]] = q[2]

        elif len(q) == 2:
            c = product(a, b)
            queryAdd = 0
            for comb in c:
                if sum(comb) == q[1]:
                    queryAdd += 1
            queries.append(queryAdd)
    return queries


a = [1, 2, 3]
b = [3, 4]
query = [[1, 5], [0, 0, 1], [1, 5]]
print(coolFeature(a, b, query))
