from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def get_freelancer(self):
        print('checking freelancer')
        if(hasattr(self, 'freelancer')):
            print(self.freelancer)
            return self.freelancer
        return None

    def get_business(self):
        if(hasattr(self, 'business')):
            return self.business
        return None