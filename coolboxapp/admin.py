from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Food


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name']
    


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Food, FoodAdmin)