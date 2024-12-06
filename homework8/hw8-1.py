class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    #--------------------------

    def set_name(self, value):
        self.__name = value

    def set_email(self, value):
        self.__email = value

    def set_password(self, value):
        self.__password = value


user1 = User('Oleg', 'oleg1995@gmail.com', 'oleg1995')
print(f'Data: {user1.get_name(), user1.get_email(), user1.get_password()}')
print('Changing data...')
user1.set_name('Ivan'); user1.set_email('ivan2008@hotmail.com'); user1.set_password('ivan2008')
print(f'New data: {user1.get_name(), user1.get_email(), user1.get_password()}')