#import Booking_class
#b1 = Booking_class.Booking(15, 20, 30, 1, 'kfkf', 'jvnjk' )
#b2 = Booking_class.Booking(17, 20, 30, 1, 'kfkf', 'jvnjk' )
#status = b2.checkTheBookingStatus()
#print(status)
import User_class
u1 = User_class.User('1l32', "1895689823", 'kjhghf')
u2 = User_class.User('1l32', "1895689823", 'kjhghf')
User_class.User.user_list.append(u1)
User_class.User.user_list.append(u2)
print(User_class.User.user_list[1].login)
u1.login('1l32')
print(User_class.User.user_list)
j = 0
i = len(User_class.User.user_list)

#while i != 0:
    #if u2.login == User_class.User.user_list[j].login:
        #i = i - 1
        #j = j + 1
        #raise Exception ("Same login and password")