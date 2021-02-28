# Insertion Sort

table = [6, 33, 1, 99, 35, 11, 95, 36, 86, 65, 77]

i = 1
while i < len(table):
    actual = table[i]
    j = i - 1
    while j >= 0 and actual < table[j]:
        table[j + 1] = table[j]
        j -= 1
    table[j + 1] = actual
    i += 1
    print(table)
