password = 'password123'

user_list = []

user_1 = {'password': 'password123'}
user_list.append(user_1)

user_2 = {'password': 'hello'}
user_list.append(user_2)

for user in user_list:
    if user['password'] == 'password123':
        print('Welcome to the system')
    else:
        print('Wrong password')