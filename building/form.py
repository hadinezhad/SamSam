from django import forms
from .models import Building, Unit, Message, FailureReport, News, Poll, Debt, Feature
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from manageUser.models import Account
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.admin.widgets import AdminSplitDateTime


class CreateBuildingForm(forms.ModelForm):

    class Meta:
        model = Building
        fields = ['name', 'Address', 'info']
        labels = {
            'name': 'نام ساختمان',
            'Address': 'آدرس',
            'info': 'توضیحات',
        }


class CreateUnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ['size', 'info', 'number', 'account']
        labels = {
            'size': 'اندازه',
            'info': 'توضیحات',
            'number': 'تعداد',
            'account': 'نام ساکن'
        }


class CreateNeighborForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
        }


class UpdateUserProfile(forms.ModelForm):
    username = forms.EmailField(label="ایمیل", error_messages={
        'invalid': "This value may contain only letters, numbers and _ characters."})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', ]
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'username': 'ایمیل',
        }

    def clean(self):
        cleaned_data = super(UpdateUserProfile, self).clean()
        username = cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('email mojode')  # TODO

        return self.cleaned_data


class CreateMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'text']
        labels = {
            'subject': 'عنوان',
            'text': 'متن',
            'receiver': 'گیرنده',
        }


class CreateMessageSupportForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['subject', 'text']
        labels = {
            'subject': 'عنوان',
            'text': 'متن',
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="تکرار رمز عبور")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="تکرار رمز عبور")

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']
        labels = {
            'password': 'رمز عبور فعلی',
            'new_password1': 'نیرشسلرحخاشصل',
            'new_password2': ' ادصعثع',
        }


class CreateFailureReportForm(forms.ModelForm):

    class Meta:
        model = FailureReport
        fields = ['subject', 'text']
        labels = {
            'subject': 'عنوان',
               'text': 'متن',
        }


class CreatePollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ['subject', 'startDate', 'endDate', 'text']
        labels = {
            'subject': 'عنوان',
               'startDate': 'تاریخ شروع',
               'endDate': 'تاریخ پایان',
            'text': 'متن',
        }


class CreateNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['subject', 'text']
        labels = {
            'subject': 'عنوان',
            'text': 'متن',
        }


class CreateDebtForm(forms.ModelForm):

    class Meta:
        model = Debt
        fields = ['account', 'amount', 'type']
        labels = {
            'amount': 'مبلغ',
               'account': 'بدهکار',
               'type': 'نوع بدهی',
        }


class CreateFeatureForm(forms.ModelForm):
    startDate = forms.DateTimeField(widget=forms.SplitDateTimeWidget(), label='تاریخ شروع')
    endDate = forms.DateTimeField(widget=forms.SplitDateTimeWidget(), label='تاریخ پایان')

    class Meta:
        model = Feature
        fields = ['title', 'startDate', 'endDate', 'price']
        labels = {
            'title': 'عنوان',
            'startDate': 'تاریخ شروع',
            'endDate': 'تاریخ پایان',
            'price': 'هزینه',
        }


