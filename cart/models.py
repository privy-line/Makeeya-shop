from django.db import models
from django.conf import settings
 

 

class Buyer(models.Model):
    first_name = models.CharField(max_length =300)
    last_name = models.CharField(max_length =300)
    email = models.EmailField()
    password = models.CharField(max_length = 300, null=False)


    def save_buyer(self):
        self.save()
 
