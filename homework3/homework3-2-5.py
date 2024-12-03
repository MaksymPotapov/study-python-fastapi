print('List of odd numbers from 1 to 50:\n----------------------------------')

for i in range(2, 51):
    simple = True
    for divider in range(2, i):
        if i % divider == 0:
            simple = False
            break
    if simple: print(i)