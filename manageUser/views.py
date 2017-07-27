from django.shortcuts import render, get_object_or_404
from .models import Account
# Create your views here.


def home(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/home.html', {'all_accounts': all_accounts})


def signup(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/signup.html', {'all_accounts': all_accounts})


def callus(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/callus.html', {'all_accounts': all_accounts})


def login(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/login.html', {'all_accounts': all_accounts})


def guide(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/guide.html', {'all_accounts': all_accounts})