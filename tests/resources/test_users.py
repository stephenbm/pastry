import mock
import unittest

from pastry.resources.users import Users


class UsersTestCase(unittest.TestCase):

    @mock.patch('pastry.resources.users.Base.index', return_value='index')
    def test_index(self, base):
        self.assertEqual(Users.index(), 'index')

    @mock.patch('pastry.resources.users.Base.get', return_value='user')
    def test_get(self, base):
        self.assertEqual(Users.get('username'), 'user')
