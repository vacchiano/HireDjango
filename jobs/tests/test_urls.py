from django.test import SimpleTestCase
from django.urls import reverse, resolve

from jobs.views import (
 index,
 profile,
 about,
 pricing,
 list_developers,
 FreelancerDetailView,
 FreelancerCreateView,
 BusinessCreateView,
 FreelancerUpdateView,
 handle_login
)


class TestJobsUrl(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func,index)

    def test_profile_url_is_resolved(self):
        url = reverse("profile")
        self.assertEqual(resolve(url).func,profile)

    def test_pricing_url_is_resolved(self):
        url = reverse("pricing")
        self.assertEqual(resolve(url).func,pricing)

    def test_list_developers_url_is_resolved(self):
        url = reverse("list-developers")
        self.assertEqual(resolve(url).func,list_developers)

    def test_freelancer_detail_url_is_resolved(self):
        url = reverse("freelancer-detail", args=['1'])
        self.assertEqual(resolve(url).func.view_class, FreelancerDetailView)

    def test_freelancer_create_view(self):
        url = reverse("freelancer-create")
        self.assertEqual(resolve(url).func.view_class, FreelancerCreateView)

    def test_business_create_view(self):
        url = reverse("business-create")
        self.assertEqual(resolve(url).func.view_class, BusinessCreateView)

    def test_freelancer_update_view(self):
        url = reverse("freelancer-update")
        self.assertEqual(resolve(url).func.view_class, FreelancerUpdateView)

    def test_handler_login_view(self):
        url = reverse("handle-login")
        self.assertEqual(resolve(url).func, handle_login)
