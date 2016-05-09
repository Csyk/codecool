ajto = [0 for i in range (100)]
j = 1
while j <= 100:
    i = j - 1
    while i < 100:
        if ajto [i] == 0:
            ajto [i] = 1
        else:
            ajto [i] = 0
        i = i + j
    j = j + 1

for i in range (0, 100):
    if ajto[i] == 1:
        print(i + 1)
