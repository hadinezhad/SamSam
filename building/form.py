from django import forms
from .models import Building, Unit


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
