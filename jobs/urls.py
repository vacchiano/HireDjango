from django.urls import path

from .views import (index, BusinessCreateView, 
                    FreelancerCreateView, FreelancerDetailView, 
                    FreelancerListView, handle_login)

urlpatterns = [
    path('', index, name='home'),
    path('developers/', FreelancerListView.as_view(), name='freelancer-list'),
    path('account-setup/', handle_login, name='handle-login'),
    path('developer/<int:pk>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
    path('developer/create/', FreelancerCreateView.as_view(), name="freelancer-create"),
    path('business/create/', BusinessCreateView.as_view(), name="business-create"),
]