from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.EmailField(label="Username", error_messages={
        'invalid': "This value may contain only letters, numbers and _ characters."})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',  'password1', 'password2']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'username': 'نام کاربری',
            'password1': 'رمز عبور',
            'password2': 'تکرار رمز عبور',
        }

'''forms.RegexField(label=_("Email"), max_length=30, regex=r'^[\w.@+-]+$',
        help_text = _("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages = {'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})'''


class UserLoginForm(forms.ModelForm):
    username = forms.EmailField(label="Username", error_messages={
        'invalid': "This value may contain only letters, numbers and _ characters."})
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': "ایمیل",
            'password': 'رمز عبور'
        }
