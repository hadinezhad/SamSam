from django.shortcuts import render
from .models import Building, Message, Unit
from manageUser.models import Account
from django.views import generic
from django.views.generic import View
from django.urls import reverse_lazy
from .form import CreateBuildingForm, CreateUnitForm, CreateNeighborForm
# Create your views here.


def building(request):
    return render(request, 'building/buildingList.html', {'all_building': Building.objects.all(),
                                                          'createBuildingForm': CreateBuildingForm})


def unit(request, building_id):
    getbuilding = Building.objects.get(pk=building_id)
    context = {'building': getbuilding,
               'accountType':  Account.objects.get(user=request.user).type,
               'all_units': Unit.objects.filter(building=getbuilding),
                    }
    return render(request, 'building/unit.html', context)


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
               }
    return render(request, 'building/neighbor&staff.html', context)


def showdash(request, building_id):
    context = {'building': Building.objects.get(pk=building_id), 'accountType':  Account.objects.get(user=request.user).type}
    return render(request, 'building/dashBoard.html', context)


class DeleteBuilding(generic.DeleteView):
    model = Building
    success_url = reverse_lazy('building:building')


class CreateBuildingFormView(View):
    form_class = CreateBuildingForm
    template_name = 'building/createBuilding.html'
    data = "ورود"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    })


class CreateUnitFormView(View):
    form_class = CreateUnitForm
    template_name = 'building/createUnit.html'
    data = "ورود"

    def get(self, request, building_id):
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    'building': Building.objects.get(pk=building_id),
                                                    'accountType': Account.objects.get(user=request.user).type
                                                    })


class CreateNeighborFormView(View):
    form_class = CreateNeighborForm
    template_name = 'building/createNeighbor.html'
    data = "ورود"

    def get(self, request, building_id):
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    'building': Building.objects.get(pk=building_id),
                                                    'accountType': Account.objects.get(user=request.user).type
                                                    })


def activities(request):
    pass


def inbox(request):
    context = {'receiveMessages': Message.objects.filter(receiver=Account.objects.get(user=request.user)),
                'sendMessages': Message.objects.filter(sender=Account.objects.get(user=request.user))}
    return render(request, 'building/inbox.html', context)
