from django.test import TestCase
from jobs.models import Role, Level, Freelancer, Business
from django.contrib.auth import get_user_model
User = get_user_model()



class TestRoleModel(TestCase):

    def test_role_str(self):
        role = Role.objects.create(name="contract")
        self.assertEqual(str(role), "contract")

class TestLevelModel(TestCase):

    def test_level_str(self):
        level = Level.objects.create(name="junior")
        self.assertEqual(str(level),'junior')

class TestFreelancerModel(TestCase):
    def test_freelance_str(self):
        owner = User.objects.create_user(id=1, username='max', email='test@test.com', password='password')
        freelancer = Freelancer.objects.create(id=1, name='test', owner=owner)
        self.assertEqual(str(freelancer), '1 | test')


class TestBusinessModel(TestCase):
    def test_freelance_str(self):
        owner = User.objects.create_user(id=1, username='max', email='test@test.com', password='password')
        business = Business.objects.create(id=1, name='test', owner=owner)
        self.assertEqual(str(business), '1 | test')
