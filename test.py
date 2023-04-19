from User_class import User

u1 = User('Name', 'Password', 'loc')
u2 = User('Nam1', 'Password1', 'loc1')
u1.user_list.append(u1)
u1.user_list.append(u2)


u1.login = 'Nam1'
