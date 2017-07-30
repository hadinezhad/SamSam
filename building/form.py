from django import forms
from .models import Building, Unit, Message, FailureReport, News, Poll, Debt, Feature
from django.contrib.auth.models import User
from manageUser.models import Account


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
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
        }


class CreateMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'text']


class ChangePasswordForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['password', 'password', 'password']
        labels = {
            'password': 'رمز عبور فعلی',
            'password': 'رمز عبور جدید',
            'password': 'تکرار رمز عبور',
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

    class Meta:
        model = Feature
        fields = ['title', 'startDate', 'endDate', 'price']
        labels = {
            'title': 'عنوان',
            'startDate': 'تاریخ شروع',
            'endDate': 'تاریخ پایان',
            'price': 'هزینه',
        }

