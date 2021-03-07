from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AppUser


class AppUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = AppUser
        #fields = ('email',)
        fields = ['firstname', 'lastname', 'email', 'phone', 'country']


class AppUserChangeForm(UserChangeForm):

    class Meta:
        model = AppUser
        #fields = ('email',)
        fields = ['firstname', 'lastname', 'email', 'phone', 'country']