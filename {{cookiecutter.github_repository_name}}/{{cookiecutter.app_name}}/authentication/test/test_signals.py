from django.test import TestCase
from nose.tools import ok_
from users.test.factories import UserFactory

class AuthTokenTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_new_users_get_auth_token(self):
        ok_(self.user.auth_token)
