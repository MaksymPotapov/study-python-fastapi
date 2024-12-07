class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def update_user_data(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password
        return self.__dict__

    def delete_user_data(self):
        self.__dict__.clear()


user1 = User('Oleg', 'oleg123@gmail.com', 'oleg2004')
print(user1.__dict__, '\nchanging data...')
user1.update_user_data('Sergey', 'serezha825@gmail.com', 'serezha1991')
print(user1.__dict__, '\ndeleting data...')
user1.delete_user_data()
print(user1.__dict__)