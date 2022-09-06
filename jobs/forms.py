from django import forms
from django.forms.widgets import NumberInput

from jobs.models import Freelancer, Level, Role


class DeverloperSearchForm(forms.Form):
    search_profile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Developers', 'class':'my-0 w-full md:w-auto'}), label="", max_length=100)



class FreelancerForm(forms.ModelForm):

    tagline = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':''}))
    bio = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))
    contact_email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))
    github = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))
    linkedin = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))
    twitter = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))
    stackoverflow = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))

    STATUS_CHOICES = [
    ('active' , 'Active'),
    ('open' , 'Open'),
    ('interested' , 'Interested'),
    ('invisible' , 'Invisible'),
    ]

    search_status = forms.ChoiceField(
    choices=STATUS_CHOICES,
    widget = forms.Select(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'})

    )

    role_type = forms.ModelMultipleChoiceField(
        required=False,
        queryset = Role.objects.all(),
        initial = 0,
        widget = forms.CheckboxSelectMultiple(attrs={'class':'',})
        )

    role_level = forms.ModelMultipleChoiceField(
        required=False,
        queryset = Level.objects.all(),
        initial = 0,
        widget = forms.CheckboxSelectMultiple(attrs={'class':''})
        )

    available_date = forms.DateField(required=False, widget=NumberInput(attrs={'type': 'date','class':'border rounded focus:outline-none focus:shadow-outline'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))
    state = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))
    country = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'border rounded focus:outline-none focus:shadow-outline'}))

    class Meta:
        model = Freelancer
        fields = fields = ['name', 'tagline', 'profile_pic', 'bio', 'contact_email', 'website', 'github', 'linkedin', 'twitter', 'stackoverflow', 'search_status', 'role_type', 'role_level', 'available_date', 'city', 'state','country']
