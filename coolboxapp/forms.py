from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Food
from django.forms import ModelForm
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class FoodForm(ModelForm):

    class Meta:
        model = Food
        fields = ('name', 'deadline', 'quantity','owner')
        widgets = {'owner':forms.HiddenInput()}

class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username','password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        if commit:
            user.save()
        return user


