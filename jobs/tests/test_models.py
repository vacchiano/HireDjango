from django.test import TestCase
from jobs.models import Role, Level, Freelancer, Business
from django.contrib.auth import get_user_model
User = get_user_model()



class TestFreelanceModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser",password="password",email="test@mail.com")
        self.user = user
        role = Role.objects.create(name='contract')
        self.role = role
        level = Level.objects.create(name="senior")
        self.level = level
        freelancer = Freelancer.objects.create(owner=self.user,profile_pic="pic.jpg",name="man",tagline="test",bio="mybio")
        self.freelancer = freelancer
        business = Business.objects.create(owner=self.user, profile_pic="prof.jpg",name="my_bus")
        self.business = business

    def test_role_model_str(self):
        self.assertEqual(self.role.name, 'contract')
        self.assertEqual(str(self.role), 'contract')

    def test_level_model_str(self):
        self.assertEqual(self.level.name,'senior')
        self.assertEqual(str(self.level), 'senior')

    def test_freelance_model_str(self):
        self.assertEqual(self.freelancer.owner, self.user)
        self.assertEqual(str(self.freelancer), '1 | man')

    def test_business_model_str(self):
        self.assertEqual(self.business.owner, self.user)
        self.assertEqual(str(self.business), '1 | my_bus')

# class TestRoleModel(TestCase):
#
#     def test_role_str(self):
#         role = Role.objects.create(name="contract")
#         self.assertEqual(str(role), "contract")
#
# class TestLevelModel(TestCase):
#
#     def test_level_str(self):
#         level = Level.objects.create(name="junior")
#         self.assertEqual(str(level),'junior')
#
# class TestFreelancerModel(TestCase):
#     def test_freelance_str(self):
#         owner = User.objects.create_user(id=1, username='max', email='test@test.com', password='password')
#         freelancer = Freelancer.objects.create(id=1, name='test', owner=owner)
#         self.assertEqual(str(freelancer), '1 | test')


# class TestBusinessModel(TestCase):
#     def test_freelance_str(self):
#         owner = User.objects.create_user(id=1, username='max', email='test@test.com', password='password')
#         business = Business.objects.create(id=1, name='test', owner=owner)
#         self.assertEqual(str(business), '1 | test')
