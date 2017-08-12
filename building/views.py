from django.shortcuts import render
from .models import Building, Message, Unit, Activity, Transaction, Debt, News, Poll, FailureReport, Feature, ReservedFeature
from manageUser.models import Account
from django.views import generic
from django.views.generic import View, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from . import form as myForm
from django.contrib.auth.models import User
from django.db.models import Q
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def all_debts(building_id):
    building = Building.objects.get(pk=building_id)
    all_units = Unit.objects.filter(building=building)
    all_debt = 0
    for unit in all_units:
        if unit.account is not None:
            for debt in Debt.objects.filter(account=unit.account):
                all_debt += debt.amount

    return all_debt


def all_transactions(building_id):
    all_units = Unit.objects.filter(building=building_id)
    all_trans = 0
    for unit in all_units:
        if unit.account is not None:
            for t in Transaction.objects.filter(account=unit.account):
                all_trans += t.amount

    return all_trans


def all_units(building_id):
    return Unit.objects.filter(building=building_id).count()


def all_polls(building_id):
    return Poll.objects.filter(building=building_id).count()


def all_features(building_id):
    return Feature.objects.filter(building=building_id).count()


class Buildinglist(View):

    def get(self, request):
        all_manager = []
        all_manager.append(request.user.account)
        for u in Unit.objects.filter(account=request.user.account):
            all_manager.append(u.building.manager)
        return render(request, 'building/buildingList.html', {'all_building': Building.objects.filter(manager__in=all_manager),
                                                              'createBuildingForm': myForm.CreateBuildingForm})
    def post(self,request):
        form = myForm.CreateBuildingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.manager = request.user.account
            obj.save()
            return HttpResponseRedirect(reverse('building:building'))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:building'))

def info(request, building_id):
    return render(request, 'building/info.html', {'building': Building.objects.get(pk=building_id),
                                                  'accountType': Account.objects.get(user=request.user).type})


def showdash(request, building_id):
    getBuilding = Building.objects.get(pk=building_id)
    all_debt = all_debts(building_id)
    all_trans = all_transactions(building_id)
    if all_debt == 0:
        chart = 0
    else:
        chart = all_trans/all_debt*100
    print(all_debt)
    print(all_trans)
    print(chart)
    context = {'building': getBuilding,
               'accountType':  Account.objects.get(user=request.user).type,
               'all_debt': all_debt,
               'all_trans': all_trans,
               'chart': chart
               }
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
    data = "تغییر مشخصات ساختمان"

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
    for unit in Unit.objects.filter(building=getbuilding):
        if unit.account is not None:
            neighbor_unit[unit.account] = Unit.objects.filter(account=unit.account)

    context = {'building': getbuilding,
               'accountType':  Account.objects.get(user=request.user).type,
               'neighbor_unit': neighbor_unit,
               'createNeighborForm': myForm.CreateNeighborForm,
               'messageForm':myForm.CreateMessageForm
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


def transaction(request, building_id):
    context = {'all_transaction': Transaction.objects.filter(account=Account.objects.get(user=request.user)),
               'all_debt': Debt.objects.filter(account=Account.objects.get(user=request.user)),
               'Listname': 'تراکنش ها',
               'Listname2': 'بدهی ها',
               'title1': 'مبلغ',
               'title2': 'تاریخ',
               'title3': 'کد رهگیری',
               'title4': 'نوع بدهی',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type
               }
    return render(request, 'building/transaction.html', context)


def cudebt(request, building_id):
    context = {'all_debt': Debt.objects.filter(account=Account.objects.filter(building=building_id)),
               'Listname2': 'بدهی ها',
               'title1': 'مبلغ',
               'title2': 'تاریخ',
               'title4': 'نوع بدهی',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': myForm.CreateDebtForm
               }
    return render(request, 'building/cudebt.html', context)


def activities(request):
    context = {'all_activities': Activity.objects.filter(account=request.user.account),
               'Listname': 'فعالیت ها',
               'title1': 'نوع فعالیت',
               'title2': 'تاریخ',
               }
    return render(request, 'building/activities.html', context)


def news(request, building_id):
    context = {'all_news': News.objects.filter(building=building_id),
               'Listname': 'اخبار و اطلاعیه ها',
               'title1': 'عنوان',
               'title2': 'تاریخ',
               'title3': 'متن',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type
               }
    return render(request, 'building/news.html', context)


def cunews(request, building_id):
    context = {'all_news': News.objects.filter(building=building_id),
               'Listname': 'اخبار و اطلاعیه ها',
               'title1': 'عنوان',
               'title2': 'تاریخ',
               'title3': 'متن',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form' : myForm.CreateNewsForm
               }
    return render(request, 'building/cunews.html', context)


def failureReport(request, building_id):
    context = {'all_failureReport':FailureReport.objects.filter(building=building_id),
               'Listname': 'گزارش های خرابی',
               'title1': 'عنوان',
               'title2': 'تاریخ',
               'title3': 'ایجاد کننده',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type
               }
    return render(request, 'building/failureReport.html', context)


def cufailureReport(request, building_id):
    context = {'all_failureReport': FailureReport.objects.filter(building=building_id, account=Account.objects.get(user=request.user)),
               'Listname': 'گزارش های خرابی',
               'title1': 'عنوان',
               'title2': 'تاریخ',
               'title3': 'متن',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': myForm.CreateFailureReportForm,
               }
    return render(request, 'building/cufailureReport.html', context)


def feature(request, building_id):
    all_feature = Feature.objects.filter(building=building_id)
    all_reservedfeature = []
    all_emptyfeature = []
    for f in all_feature:
        if ReservedFeature.objects.filter(feature=f).count() == 0:
            all_emptyfeature.append(f)
        else:
            all_reservedfeature.append(f)

    context = {'all_emptyfeature': all_emptyfeature,
               'all_reservedfeature': all_reservedfeature,
               'Listname': 'امکانات رزرو شده',
               'Listname2': 'سایر امکانات',
               'title3': 'مبلغ',
               'title2': 'تاریخ شروع/پایان',
               'title1': 'عنوان',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type
               }
    return render(request, 'building/feature.html', context)


class Cfeature(View):
    form_class = myForm.CreateFeatureForm
    template_name = 'building/cfeature.html'

    def get(self, request, building_id):
        all_feature = Feature.objects.filter(building=building_id)

        context = {'all_feature': all_feature,
        'Listname': 'امکانات',
        'title3': 'مبلغ',
        'title2': 'تاریخ شروع/پایان',
        'title1': 'عنوان',
        'building': Building.objects.get(pk=building_id),
        'accountType': Account.objects.get(user=request.user).type,
        'form': myForm.CreateFeatureForm,
        }
        return render(request, self.template_name, context)

    def post(self, request, building_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.building = Building.objects.get(pk=building_id)
            obj.save()
            return HttpResponseRedirect(reverse('building:cfeature', kwargs={'building_id': building_id}))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:cfeature', kwargs={'building_id': building_id}))


def poll(request, building_id):
    context = {'all_polls': Poll.objects.filter(building=building_id),
               'Listname': 'نظرسنجی ها',
               'title1': 'عنوان',
               'title2': 'تاریخ شروع',
               'title3': 'تاریخ پایان',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': myForm.CreatePollForm
               }
    return render(request, 'building/poll.html', context)


def cupoll(request, building_id):
    context = {'all_polls': Poll.objects.filter(building=building_id),
               'Listname': 'نظرسنجی ها',
               'title1': 'عنوان',
               'title2': 'تاریخ شروع',
               'title3': 'تاریخ پایان',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': myForm.CreatePollForm
               }
    return render(request, 'building/cupoll.html', context)


def inbox(request):
    context = {'receiveMessages': Message.objects.filter(receiver=Account.objects.get(user=request.user)),
               'sendMessages': Message.objects.filter(sender=Account.objects.get(user=request.user)),
               'Listname1': 'صندوق دریافتی',
               'Listname2': 'صندوق ارسالی',
               'title1': 'گیرنده',
               'title2': 'فرسنتده',
               'title3': 'تاریخ دریافت',
               'title4': 'تاریخ ارسال',
               'title5': 'متن',
               'title6': 'موضوع',
               }
    return render(request, 'building/inbox.html', context)


class Sendmessage(View):
    form_class = myForm.CreateMessageForm
    template_name = 'building/sendmessage.html'
    data = 'ارسال پیام جدید'

    def get(self, request):
        form = self.form_class
        #todo form.fields["receiver"].queryset = afwfhawi
        return render(request, self.template_name, {'form': form, 'data': self.data})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.sender = request.user.account
            obj.save()
            return HttpResponseRedirect(reverse('building:inbox'))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('manageUser:sendmessage'))


class Support(View):
    form_class = myForm.CreateMessageSupportForm
    template_name = 'building/sendmessage.html'
    data = 'پشتیبانی'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'data': self.data})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.sender = request.user.account
            obj.receiver = Account.objects.get(user__is_staff=True)#bayad yeki bashad
            obj.save()
            return HttpResponseRedirect(reverse('building:inbox'))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('manageUser:support'))


class UpdateUserProfileFormView(View):
    form_class = myForm.UpdateUserProfile
    template_name = 'building/updateProfile.html'
    data = "ویرایش حساب کاربری"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    })

    def post(self, request):
        instance = request.user
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('building:building'))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:updateUserProfile'))


class ChangePasswordFormView(View):
    form_class = myForm.ChangePasswordForm
    template_name = 'building/changePassword.html'
    data = "تغییر رمز عبور"

    def get(self, request):
        form = self.form_class(request.user)
        return render(request, self.template_name, {'form': form,
                                                    'data': self.data,
                                                    })

    def post(self, request):
        form = self.form_class(request.user, request.POST)
        if request.user.is_authenticated():
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')#todo
                return HttpResponseRedirect(reverse('building:building'))

        messages.error(request, 'Please correct the error below.')#todo
        return HttpResponseRedirect(reverse('building:changePassword'))


