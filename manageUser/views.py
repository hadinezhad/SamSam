from django.shortcuts import render, get_object_or_404, redirect
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .form import UserRegisterForm, UserLoginForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


def home(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/home.html', {'all_accounts': all_accounts})


class UserFormView(View):
    form_class = UserRegisterForm
    template_name = 'manageUser/user_form.html'
    data = "Sign Up"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'data': self.data})

    def post(self, request):
        '''
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("")
        return render(request, self.template_name, {'form': form})
        '''

class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'manageUser/user_form.html'
    data = "Login"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'data': self.data})


def callus(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/callus.html', {'all_accounts': all_accounts})


def login(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/login.html', {'all_accounts': all_accounts})


def guide(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/guide.html', {'all_accounts': all_accounts})