NODES = {
    'A': list('CF'),
    'B': list('DEFG'),
    'C': list('AFED'),
    'D': list('CB'),
    'E': list('CFB'),
    'F': list('ACEG'),
    'G': list('BF'),
}
WEIGHT = {
    'AC': 3,
    'AF': 2,
    'CF': 2,
    'CE': 1,
    'EF': 3,
    'CD': 4,
    'BD': 1,
    'BG': 2,
    'FG': 5,
    'BF': 6,
    'BE': 2,
}

def get_weight(v1, v2):
    return WEIGHT[''.join(sorted([v1, v2]))]


start = 'A'
end = 'B'

cursor = start
not_explored = {v: float('inf') for v in NODES.keys()}
explored = {cursor: 0}
not_explored.pop(cursor)
reverse_path = {}

while True:
    for v in NODES[cursor]:
        if v in not_explored.keys():
            weight = explored[cursor] + get_weight(cursor, v)
            if weight < not_explored[v]:
                not_explored[v] = weight
                reverse_path[v] = cursor

    v, w = list(sorted(not_explored.items(), key=lambda x: x[1]))[0]
    explored[v] = not_explored.pop(v)
    cursor = v

    if cursor == end:
        break

res = [cursor]

while True:
    v = reverse_path[cursor]
    res.append(f'--{get_weight(cursor, v)}->')
    res.append(v)
    cursor = v
    if cursor == start:
        break

result = ' '.join(reversed(res))
print(result)
