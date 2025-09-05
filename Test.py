x = {1:[2], 3:[4], 5:[6]}
c = {key:value.copy() for key, value in x.items()}
c[1].append(66)
print(c)
print(x)
