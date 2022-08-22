from django import forms

class DeverloperSearchForm(forms.Form):
    search_profile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Developers', 'class':'my-0 w-full md:w-auto'}), label="", max_length=100)
