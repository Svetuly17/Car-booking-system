class User:

    #конструктор создания пользователя
    def __init__(self, login, password, userLocation='Местоположение не указано'):
        self.login = login
        self.password = password
        self.userLocation = userLocation

    # создание списка
    user_list = []

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.validateLogin(value)
        self.matchSearch(value)
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.validatePassword(value)
        self.__password = value

    def validateLogin(self, value):
        if (len(value) != 4) :
            raise Exception("Login must be equal to 4 characters")


    def validatePassword(self, value):
        if len(value) < 8:
            raise Exception("The password must contain 8 or more characters")

    def matchSearch(self, value):
        for j in self.user_list:
            if j.login == value:
                raise Exception("Same login")
        # j = 0
        # i = len(self.user_list)
        # while i != 0:
        #     if value == self.user_list[j].login:
        #         i = i - 1
        #         j = j + 1
        #         raise Exception("Same login and password")

    #удаление пользователя
    def __del__(self):
        print('User is deleted')


