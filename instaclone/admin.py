from django.contrib import admin
from .models import Profile,User,Item,Category



class User(admin.ModelAdmin):
    model = User
    

admin.site.register(Profile,User)

class User(admin.ModelAdmin):
    model = Category

admin.site.register(Category,User)
    

