from django.contrib import admin
from .models import Profile,User



class User(admin.ModelAdmin):
    model = User
    

admin.site.register(Profile,User)

