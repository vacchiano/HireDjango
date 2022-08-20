from django import forms

class DeverloperSearchForm(forms.Form):
    search_profile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Profiles'}),label="Search Profile" , max_length=100)
