from django import forms
from django.forms.widgets import NumberInput

from jobs.models import Freelancer, Level, Role


class DeverloperSearchForm(forms.Form):
    search_profile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Developers', 'class':'my-0 w-full mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}), label="", max_length=100)



class FreelancerForm(forms.ModelForm):

    tagline = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    bio = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    contact_email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    github = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    linkedin = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    twitter = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    stackoverflow = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))

    STATUS_CHOICES = [
    ('active' , 'Active'),
    ('open' , 'Open'),
    ('interested' , 'Interested'),
    ('invisible' , 'Invisible'),
    ]

    search_status = forms.ChoiceField(
    choices=STATUS_CHOICES,
    widget = forms.Select(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'})

    )

    role_type = forms.ModelMultipleChoiceField(
        required=False,
        queryset = Role.objects.all(),
        initial = 0,
        widget = forms.CheckboxSelectMultiple(attrs={'class':'mt-2 mb-3 focus:border-blue-600 px-3',})
        )

    role_level = forms.ModelMultipleChoiceField(
        required=False,
        queryset = Level.objects.all(),
        initial = 0,
        widget = forms.CheckboxSelectMultiple(attrs={'class':'mt-2 mb-3 focus:border-blue-600 px-3'})
        )

    available_date = forms.DateField(required=False, widget=NumberInput(attrs={'type': 'date','class':'border rounded focus:outline-none mt-2 mb-3 block w-fit focus:border-blue-600 px-3 py-1'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    state = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))
    country = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none mt-2 mb-3 block w-full focus:border-blue-600 px-3 py-1'}))

    class Meta:
        model = Freelancer
        fields = fields = ['name', 'tagline', 'profile_pic', 'bio', 'contact_email', 'website', 'github', 'linkedin', 'twitter', 'stackoverflow', 'search_status', 'role_type', 'role_level', 'available_date', 'city', 'state','country']
