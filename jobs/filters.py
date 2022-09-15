import django_filters

from jobs .models import Freelancer, Role, Level

class DevelopersFilter(django_filters.FilterSet):
    class Meta:
        model = Freelancer
        fields = ['name','tagline','role_type','role_level','city','country','state']
