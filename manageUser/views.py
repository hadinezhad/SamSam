from django.shortcuts import render, get_object_or_404, redirect
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .form import UserRegisterForm, UserLoginForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


def home(request):
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
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return render(request, 'manageUser/home.html') #Todo redirect to vulding lisr
        return render(request, self.template_name, {'form': form, 'data': self.data})


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
                return render(request, 'manageUser/home.html') #Todo redirect to vulding lisr

        return render(request, self.template_name, {'form': self.form_class, 'data': self.data})


def callus(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/callus.html', {'all_accounts': all_accounts})


# def login(request):
#     all_accounts = Account.objects.all()
#     return render(request, 'manageUser/login.html', {'all_accounts': all_accounts})


def guide(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/guide.html', {'all_accounts': all_accounts})
