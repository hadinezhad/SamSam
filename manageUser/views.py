from django.shortcuts import render, get_object_or_404
from .models import Account
# Create your views here.


def home(request):
    all_accounts = Account.objects.all()
    return render(request, 'manageUser/home.html', {'all_accounts': all_accounts})