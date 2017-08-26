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
        fields = ['account', 'number', 'size', 'info']
        labels = {
            'size': 'اندازه',
            'info': 'توضیحات',
            'number': 'شماره واحد',
            'account': 'نام ساکن'
        }


class CreateNeighborForm(UserCreationForm):
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

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CreateNeighborForm, self).save(commit=False)

        #default_password = somefuntion()  # Generate the default password

        user.set_password( 'passwrod123')  # Set de default password
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(CreateNeighborForm, self).clean()
        username = cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('email mojode')#TODO

        return self.cleaned_data



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


class ShowMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'date', 'subject', 'text']
        labels = {
            'subject': 'عنوان',
            'text': 'متن',
            'receiver': 'گیرنده',
            'sender': 'فرستنده',
            'date': 'تاریخ',
        }

    def __init__(self, *args, **kwargs):
        super(ShowMessageForm, self).__init__(*args, **kwargs)
        self.fields['sender'].label_from_instance = lambda obj: "%s %s" % (obj.user.last_name, obj.user.first_name)
        self.fields['receiver'].label_from_instance = lambda obj: "%s %s" % (obj.user.last_name, obj.user.first_name)
        self.fields['sender'].initial = self.instance.sender.user.first_name


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


class ShowFailureReportForm(forms.ModelForm):

    class Meta:
        model = FailureReport
        fields = ['account', 'subject', 'date', 'text']
        labels = {
            'subject': 'عنوان',
            'text': 'متن',
            'account': 'گزارش دهنده',
            'date': 'تاریخ',
        }


class CreatePollForm(forms.ModelForm):
    startDate = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(), label='تاریخ شروع')
    endDate = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(), label='تاریخ پایان')
    class Meta:
        model = Poll
        fields = ['subject', 'startDate', 'endDate', 'text']
        labels = {
            'subject': 'عنوان',
               'startDate': 'تاریخ شروع',
               'endDate': 'تاریخ پایان',
            'text': 'متن',
        }

    def __init__(self, *args, **kwargs):
        super(CreatePollForm, self).__init__(*args, **kwargs)
        self.fields['startDate'].widget = AdminSplitDateTime()
        self.fields['endDate'].widget = AdminSplitDateTime()


class ShowPollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ['subject', 'startDate', 'endDate', 'text']
        labels = {
            'subject': 'عنوان',
               'startDate': 'تاریخ شروع',
               'endDate': 'تاریخ پایان',
            'text': 'متن',
        }


class ShowNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['subject', 'date', 'text']
        labels = {
            'subject': 'عنوان',
            'text': 'متن',
            'date': 'تاریخ',
        }


class CreateNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['subject', 'text']
        labels = {
            'subject': 'عنوان',
            'text': 'متن',
        }


class ShowDebtForm(forms.ModelForm):

    class Meta:
        model = Debt
        fields = ['account', 'date', 'amount', 'type']
        labels = {
            'amount': 'مبلغ',
               'account': 'بدهکار',
               'type': 'نوع بدهی',
            'date': 'تاریخ',
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
    startDate = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(), label='تاریخ شروع')
    endDate = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(), label='تاریخ پایان')
    class Meta:
        model = Feature
        fields = ['title', 'startDate', 'endDate', 'price']
        labels = {
            'title': 'عنوان',
            'startDate': 'تاریخ شروع',
            'endDate': 'تاریخ پایان',
            'price': 'هزینه',
        }

    def __init__(self, *args, **kwargs):
        super(CreateFeatureForm, self).__init__(*args, **kwargs)
        self.fields['startDate'].widget = AdminSplitDateTime()
        self.fields['endDate'].widget = AdminSplitDateTime()
