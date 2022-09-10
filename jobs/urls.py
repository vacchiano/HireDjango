from django.urls import path

from .views import (BusinessCreateView, FreelancerCreateView,
                    FreelancerDetailView, FreelancerUpdateView, about,
                    handle_login, index, list_developers, pricing, profile)

urlpatterns = [
    path('', index, name='home'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
    path('pricing/', pricing, name='pricing'),
    # path('developers/', FreelancerListView.as_view(), name='freelancer-list'),
    path('account-setup/', handle_login, name='handle-login'),
    path('developer/create/', FreelancerCreateView.as_view(), name="freelancer-create"),
    path('developer/update/', FreelancerUpdateView.as_view(), name="freelancer-update"),
    path('business/create/', BusinessCreateView.as_view(), name="business-create"),
    path('developers/',list_developers,name="list-developers"),
    path('developer/<slug:username>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
]