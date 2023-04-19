import unittest
from User_class import User


class test_8(unittest.TestCase):
    def test_creatingUser(self):
        user1 = User('Nam1', 'Password', 'loc')
        self.assertEqual(user1.login, 'Nam1')

    def test_location(self):
        user2 = User('Nam2', 'Password')
        self.assertEqual(user2.userLocation, 'Местоположение не указано')

    def test_correctLogin(self):
        user3 = User('Nam3', 'Password', 'loc')
        self.assertEqual(len(user3.login), 4)

    def test_correctPassword(self):
        user4 = User('Nam4', 'Password', 'loc')
        self.assertEqual(len(user4.password), 8)

    def test_uniqueLogin(self):
        user5 = User('Nam5', 'Password', 'loc')
        user6 = User('Nam6', 'Password', 'loc')
        self.assertEqual((user5.login != user6.login), True)

    def test_invalidLogin(self):
        with self.assertRaises(Exception):
            user7 = User('Nam', 'Password', 'loc')

    def test_invalidPassword(self):
        with self.assertRaises(Exception):
            user8 = User('Nam8', 'Pass', 'loc')

    def test_notUniqueLogin(self):
        user9 = User('Name', 'Password', 'loc')
        user2 = User('Nam1', 'Password1', 'loc1')
        user9.user_list.append(user9)
        user9.user_list.append(user2)
        with self.assertRaises(Exception):
            user9.login = 'Nam1'

if __name__ == '__main__':
    unittest.main()
