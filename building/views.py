from django.shortcuts import render
from .models import Building, Message, Unit
from manageUser.models import Account
from django.views import generic
from django.views.generic import View
from django.urls import reverse_lazy
from . import form as myForm
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def building(request):
    return render(request, 'building/buildingList.html', {'all_building': Building.objects.all(),
                                                          'createBuildingForm': myForm.CreateBuildingForm})


def showdash(request, building_id):
    context = {'building': Building.objects.get(pk=building_id), 'accountType':  Account.objects.get(user=request.user).type}
    return render(request, 'building/dashBoard.html', context)


class DeleteBuilding(generic.DeleteView):
    model = Building
    success_url = reverse_lazy('building:building')


class CreateBuildingFormView(View):
    form_class = myForm.CreateBuildingForm
    template_name = 'building/createBuilding.html'
    data = "ورود"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    })


class UpdateBuildingFormView(View):
    form_class = myForm.CreateBuildingForm
    template_name = 'building/updateBuilding.html'
    data = "ورود"

    def get(self, request, building_id):
        getbuilding = Building.objects.get(pk=building_id)
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    'building': getbuilding,
                                                    'accountType': Account.objects.get(user=request.user).type,
                                                    })


def neighbor(request, building_id):
    getbuilding = Building.objects.get(pk=building_id)
    neighbor_unit = {}
    for unit in Unit.objects.all():
        if unit.account is not None:
            neighbor_unit[unit] = unit.account
        else:
            neighbor_unit[unit] = 'empty'
    context = {'building': getbuilding,
               'accountType':  Account.objects.get(user=request.user).type,
               'neighbor_unit': neighbor_unit,
               'createNeighborForm': myForm.CreateNeighborForm
               }
    return render(request, 'building/neighbor&staff.html', context)


class CreateNeighborFormView(View):
    form_class = myForm.CreateNeighborForm
    template_name = 'building/createNeighbor.html'
    data = "ورود"

    def get(self, request, building_id):
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    'building': Building.objects.get(pk=building_id),
                                                    'accountType': Account.objects.get(user=request.user).type
                                                    })


class CreateUnitFormView(View):
    form_class = myForm.CreateUnitForm
    template_name = 'building/createUnit.html'
    data = "ورود"

    def get(self, request, building_id):
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    'building': Building.objects.get(pk=building_id),
                                                    'accountType': Account.objects.get(user=request.user).type
                                                    })


def unit(request, building_id):
    getbuilding = Building.objects.get(pk=building_id)
    context = {'building': getbuilding,
               'accountType':  Account.objects.get(user=request.user).type,
               'all_units': Unit.objects.filter(building=getbuilding),
               'createUnitForm': myForm.CreateUnitForm,
                    }
    return render(request, 'building/unit.html', context)


def activities(request):
    pass


def inbox(request):
    context = {'receiveMessages': Message.objects.filter(receiver=Account.objects.get(user=request.user)),
               'sendMessages': Message.objects.filter(sender=Account.objects.get(user=request.user))}
    return render(request, 'building/inbox.html', context)


class UpdateUserProfileFormView(View):
    form_class = myForm.UpdateUserProfile
    template_name = 'building/updateProfile.html'
    data = "ورود"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    })


class ChangePasswordFormView(View):
    form_class = myForm.ChangePasswordForm
    template_name = 'building/changePassword.html'
    data = "ورود"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    })
