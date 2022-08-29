from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from jobs.models import Freelancer
from jobs.views import profile


User = get_user_model()

# Create your tests here.
class JobsViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser', password='password')
        Freelancer.objects.create(
            owner=user,
            name='Test User',
            tagline='Some tagline',
            profile_pic='random.jpg'
        )

    def test_freelancer_detail_is_accessible(self):
        freelancer = Freelancer.objects.get(owner__username='testuser')
        response = self.client.get(reverse('freelancer-detail', kwargs={'username': freelancer.owner.username}))
        self.assertEqual(response.status_code, 200)