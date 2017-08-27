import hashlib
import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import View

from .form import UserRegisterForm, UserLoginForm
from .models import Account
from .models import UserType
from django.core.mail import send_mail


# Create your views here.


def home(request):
    # TODO agar karbar login karde bashad va darkhst in shfe ra bedahad
    return render(request, 'manageUser/home.html')


class UserFormView(View):
    form_class = UserRegisterForm
    template_name = 'manageUser/user_form.html'
    data = "عضویت"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'data': self.data})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_active = False
            user.save()

            activation_key = hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest()[:5]

            Account.objects.create(user=user, type=UserType.MANAGER, activation_key=activation_key)
            user.account.save()

            email_subject = 'SamSam account confirmation' #TODO
            email_body = "Hello, %s, and thanks for signing up for an \
            example.com account!\n\nTo activate your account, click this link within 48 \
                hours:\n\nhttp://127.0.0.1:8001/home/confirm/%s" % (
                user.first_name,
                activation_key)
            send_mail(email_subject,
                      email_body,
                      'samsamcompany2@gmail.com',
                      [user.email])

            messages.info(request, "email khode ra check konid ") #TODO
            return HttpResponseRedirect(reverse('manageUser:signup'))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('manageUser:signup'))


class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'manageUser/user_form.html'
    data = "ورود"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'data': self.data})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('building:building'))
        messages.info(request, 'namkarbari ya password eshteba')#TODO ya inactive
        return HttpResponseRedirect(reverse('manageUser:login'))


def callus(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/callus.html', {'all_accounts': all_accounts})


def guide(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/guide.html', {'all_accounts': all_accounts})


class UserLogoutFormView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('manageUser:home'))


def confirm(request, activation_key):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('building:building'))
    user_profile = get_object_or_404(Account,
                                     activation_key=activation_key)

    user_account = user_profile.user
    user_account.is_active = True
    user_account.save()
    login(request, user_profile.user)
    return HttpResponseRedirect(reverse('building:building'))