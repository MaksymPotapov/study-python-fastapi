# Task 1
string = 'Hello World!'
integer = 4
flt = 1.41
boolean = True
lst = ['apple', 'banana', 'orange']
dct = {'fruit': 'apple', 'vegetable': 'tomato', 'citrus': 'orange'}
tpl = (1, 2, 3)
none = None

# Task 2
print('Task 2:\t', len(string) != integer, flt > integer, not boolean, dct['fruit'] in lst, dct.get('citrus') != none, integer in tpl)

# Task 3
 # Strings
  # 1
num_str = 125
num_str = str(num_str)
print('Task 3.1.1:\t', type(num_str))
  #2
message = 'Hi, my name is Python!'
message = message.replace('y', '0').replace('i', '1')
print('Task 3.1.2:\t', message)
  #3
split_test = 'This is a split test'
split_test = split_test.split()
string_join = ' '.join(split_test)
print('Task 3.1.3:\t', split_test, '--', string_join)
  #4
print('Task 3.1.4:\t', len(string_join))
 # Lists
  #1
list_append = [1, 2, 3]
list_append.append(4) ; list_append.append(5)
print('Task 3.2.1:\t', list_append)
  #2
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print('Task 3.2.2:\t', list_extend)
  #3
print('Task 3.2.3:\t', list_extend.index(6))
  #4
print('Task 3.2.4:\t', len(list_extend))
 # Dictionaries
  #1
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print('Task 3.3.1:\t', dict_test['car'], dict_test['where'])
  #2
print('Task 3.3.2:\t', dict_test.keys(), '--', dict_test.values())
  #3
print('Task 3.3.3:\t', dict_test.items())