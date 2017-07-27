from django.shortcuts import render
from .models import Building, Message
from manageUser.models import Account
# Create your views here.


def building(request):
    return render(request, 'building/UserNavBar.html', )#{'building':Building.objects.get(pk=1)})


def showdash(request, building_id):
    pass


def activities(request):
    pass


def inbox(request):
    context = {'receiveMessages': Message.objects.filter(receiver=Account.objects.get(user=request.user)),
                'sendMessages': Message.objects.filter(sender=Account.objects.get(user=request.user))}
    return render(request, 'building/inbox.html', context)
