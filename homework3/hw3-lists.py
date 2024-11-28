# 1
list1 = [10, 20]
print(f'#1\tInitial list: {list1}')
list1.remove(10)
print(f'  \tResulting list: {list1}\n--------------------')

# 2
list2 = [9, 16, 34, 4, 5]
result = 0
for num in list2:
    result += num
print(f'#2\tList: {list2}')
print(f'  \tSum: {result}\n--------------------')

# 3
list3 = [5, 3, 2, 6, 10]
print(f'#3\tInitial list: {list3}')
for i in range(len(list3)):
    list3[i] *= 2
print(f'  \tResulting list: {list3}\n--------------------')