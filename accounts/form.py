


from django.forms import models
from .models import User

class SignupForm(models.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'email', 'phone_number')


class LoginForm(models.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
