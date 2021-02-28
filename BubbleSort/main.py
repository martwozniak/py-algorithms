# BubbleSort

table = [1,6,83,25,74,90,150, 4, 2]

i = 0
while i < len(table) - 1:
    j = 0
    while j < len(table) - 1: # -i
        if table[j] > table[j + 1]:
            table[j], table[j + 1] = table[j + 1], table[j]
        j += 1
    i += 1
    print(table)