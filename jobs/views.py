from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Freelancer, Business

def index(request):
    return render(request, 'jobs/index.html')

class FreelancerListView(ListView):
    model = Freelancer

class FreelancerDetailView(LoginRequiredMixin, DetailView):
    model = Freelancer
    # template 'freelancer_detail.html'

# def freelancer_detail(request, pk):
#     freelancer = Freelancer.objects.get(pk=pk) #get_object_or_404
#     context = {
#         "objects": freelancer
#     }
#     return render(request, 'jobs/freelancer_detail/html', context)

class FreelancerCreateView(LoginRequiredMixin, CreateView):
    model = Freelancer
    fields = ['name', 'profile_pic', 'tagline', 'bio', 'website']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FreelancerCreateView, self).form_valid(form)

class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['name', 'profile_pic', 'bio']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BusinessCreateView, self).form_valid(form)

@login_required
def handle_login(request):
    # if the user has a freelance/biz acct -> take them to home
    print(request.user)
    print(request.user.get_freelancer())
    if request.user.get_freelancer() or request.user.get_business():
        return redirect(reverse_lazy('freelancer-list'))

    return render(request, 'jobs/choose_account.html', {})

    
