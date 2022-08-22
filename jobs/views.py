from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from jobs.forms import DeverloperSearchForm
from django.db.models import Q
from .models import Freelancer, Business

def index(request):
    return render(request, 'jobs/index.html')

@login_required
def profile(request):
    # print(dir(request.user))
    # if the user has a freelance/biz acct -> take them to their profile
    if request.user.get_freelancer():
        freelancer = Freelancer.objects.get(owner=request.user)
        context = {
            'object': freelancer
        }
        return render(request, 'jobs/freelancer_detail.html', context)

    if request.user.get_business():
        business = Business.objects.get(owner=request.user)
        context = {
            'object': business
        }
        return render(request, 'jobs/business_profile.html', context)

    return render(request, 'jobs/choose_account.html', {})

def about(request):
    return render(request, 'jobs/about.html')

def pricing(request):
    return render(request, 'jobs/pricing.html')

# class FreelancerListView(ListView):
#
#     def get_queryset(self):
#         queryset = Freelancer.objects.exclude(search_status="invisible")
#         return queryset

def list_developers(request):
    form = DeverloperSearchForm
    developers = Freelancer.objects.exclude(search_status="invisible")
    query = request.GET.get("search_profile")
    if query:
        developers = Freelancer.objects.exclude(search_status="invisible").filter(
        Q(tagline__icontains=query)|
        Q(bio__icontains=query)|
        Q(city__icontains=query)|
        Q(state__icontains=query) |
        Q(country__icontains=query) |
        Q(role_type__name__icontains=query)|
        Q(role_level__name__icontains=query)
        )
    context = {'developers':developers,'form':form,'query':query}

    return render(request, 'jobs/freelancer_list.html', context)

class FreelancerDetailView(DetailView):
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
    fields = ['name', 'tagline', 'profile_pic', 'bio', 'contact_email', 'website', 'github', 'linkedin', 'twitter', 'stackoverflow', 'search_status', 'role_type', 'role_level', 'available_date', 'city', 'state','country']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FreelancerCreateView, self).form_valid(form)

class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['name', 'profile_pic', 'bio', 'website', 'job_title']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BusinessCreateView, self).form_valid(form)

class FreelancerUpdateView(LoginRequiredMixin, UpdateView):
    model = Freelancer
    fields = ['name', 'tagline', 'profile_pic', 'bio', 'contact_email', 'website', 'github', 'linkedin', 'twitter', 'stackoverflow', 'search_status', 'role_type', 'role_level', 'available_date', 'city', 'state','country']
    success_url = reverse_lazy('freelancer-list')

    def get_object(self, queryset=None):
        return Freelancer.objects.get(owner=self.request.user)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FreelancerUpdateView, self).form_valid(form)

@login_required
def handle_login(request):
    # if the user has a freelance/biz acct -> take them to home
    # print(request.user)
    # print(request.user.get_freelancer())
    if request.user.get_freelancer() or request.user.get_business():
        return redirect(reverse_lazy('freelancer-list'))

    return render(request, 'jobs/choose_account.html', {})
