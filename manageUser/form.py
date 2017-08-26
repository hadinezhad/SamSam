from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.EmailField(label="ایمیل", error_messages={
        'invalid': "This value may contain only letters, numbers and _ characters."})
    password1 = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")
    password2 = forms.CharField(widget=forms.PasswordInput, label="تکرار رمز عبور")

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

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        username = cleaned_data.get('username')

        if password1 and password1 != password2:
            raise forms.ValidationError('password kiri')#TODO

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('email mojode')#TODO

        return self.cleaned_data


class UserLoginForm(forms.ModelForm):
    username = forms.EmailField(label="ایمیل", error_messages={
        'invalid': "This value may contain only letters, numbers and _ characters."})
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': "ایمیل",
            'password': 'رمز عبور'
        }
