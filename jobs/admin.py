from django.contrib import admin

from .models import Freelancer, Business, Role, Level

admin.site.register(Freelancer)
admin.site.register(Business)
admin.site.register(Role)
admin.site.register(Level)