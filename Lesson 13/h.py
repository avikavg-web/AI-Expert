string = "ABCDEFGHIJK"
L = len(string) - 2
for i in range(0, L, 3):
    print(string[i: i + 3], end = " ")
