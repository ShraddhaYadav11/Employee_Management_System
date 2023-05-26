from django.contrib import admin

# Register your models here.
from .models import Login
from .models import Add

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
   list_display=('id','name','password','email')

@admin.register(Add)
class AddAdmin(admin.ModelAdmin):
    list_display=('id','FirstName','MiddelName','LastName','Password','Email','Phone','Address')