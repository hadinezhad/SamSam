from django import forms
from .models import Building, Unit, Message
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
        fields = ['size', 'info', 'number']
        labels = {
            'size': 'اندازه',
            'info': 'توضیحات',
            'number': 'تعداد',
        }


class CreateNeighborForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
        }


class CreateMessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'text']


