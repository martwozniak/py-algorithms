# Selection Sort

table = [12,5,1,56,96,63,11,16]

i = 0
while i < len(table) - 1:
    minimal = i # Store index, not value
    j = i + 1
    while j < len(table):
        if table[minimal] > table[j]:
            minimal = j
        j += 1
    table[i], table[minimal] = table[minimal], table[i]
    i += 1
    print(table)