from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()



class TestFreelanceModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="test.user",password="password",email="test@mail.com")
        self.user = user

    def test_user_model_username(self):
        self.assertNotEqual(self.user.username, 'test.user')
        self.assertEqual(self.user.username, 'test-user')
