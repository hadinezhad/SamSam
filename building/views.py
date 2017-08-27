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
from django.utils import timezone
import hashlib
import random
from manageUser.models import UserType
from django.core.mail import send_mail
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


def deleteBuilding(request, pk):
    Building.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('building:building'))


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

    def post(self, request, building_id):
        instance = Building.objects.get(pk=building_id)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('building:showdash', kwargs={'building_id': building_id}))#todo
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:updateBuilding', kwargs={'building_id': building_id}))




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


def failureReport(request, building_id):
    context = {'all_failureReport':FailureReport.objects.filter(building=building_id),
               'Listname': 'گزارش های خرابی',
               'title1': 'عنوان',
               'title2': 'تاریخ',
               'title3': 'گزارش دهنده',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type
               }
    return render(request, 'building/failureReport.html', context)


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


class Sendmessages(View):
    form_class = myForm.CreateMessageSupportForm
    template_name = 'building/sendmessage.html'
    data = 'ارسال پیام جدید'

    def get(self, request, pk):
        form = self.form_class
        #todo form.fields["receiver"].queryset = afwfhawi
        return render(request, self.template_name, {'form': form, 'data': self.data})

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.sender = request.user.account
            obj.receiver = Account.objects.get(pk=pk)
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


def changereservefeature(request, building_id, pk):
    if ReservedFeature.objects.filter(feature=Feature.objects.get(pk=pk)).count() == 0:
        ReservedFeature.objects.create(feature=Feature.objects.get(pk=pk), account=Account.objects.get(user=request.user))
    else:
        ReservedFeature.objects.get(feature=Feature.objects.get(pk=pk)).delete()

    return HttpResponseRedirect(reverse('building:feature', kwargs={'building_id': building_id}))


class Cfeature(View):
    form_class = myForm.CreateFeatureForm
    template_name = 'building/cfeature.html'
    bool = "yes"

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
        'bool': self.bool,
        }
        return render(request, self.template_name, context)

    def post(self, request, building_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.building = Building.objects.get(pk=building_id)
            obj.save()
            return HttpResponseRedirect(reverse('building:cfeature', kwargs={'building_id': building_id}))
        #TODO agar form valid nashod che kone ... payini javab nist
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:cfeature', kwargs={'building_id': building_id}))


class Ufeature(View):
    form_class = myForm.CreateFeatureForm
    data = "تغییر امکانات"
    template_name = 'building/ufeature.html'
    bool = "no"

    def post(self, request, pk, building_id):
        instance = Feature.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('building:cfeature', kwargs={'building_id': building_id}))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:ufeature', kwargs={'building_id': building_id, 'pk': pk}))

    def get(self, request, pk, building_id):
        feature = Feature.objects.get(pk=pk)
        context = {'feature': feature,
                   'building': Building.objects.get(pk=building_id),
                   'accountType': Account.objects.get(user=request.user).type,
                   'form': myForm.CreateFeatureForm,
                   'bool': self.bool,
                   'pk': pk,
                   'data': self.data,
                   }
        return render(request, self.template_name, context)


def dfeature(request, building_id, pk):
    Feature.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('building:cfeature', kwargs={'building_id': building_id}))


def rfeature(request, building_id, pk):
    template_name = 'building/rfeature.html'
    data = 'مشاهده امکان'
    feature = Feature.objects.get(pk=pk)
    context = {
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': myForm.CreateFeatureForm(instance=feature),
               'data': data,
               }
    return render(request, template_name, context)


def dmessage(request, pk):
    Message.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('building:inbox'))


def rmessage(request, pk):
    template_name = 'building/rmessage.html'
    data = 'مشاهده پیام'
    message = Message.objects.get(pk=pk)
    context = {
               'accountType': Account.objects.get(user=request.user).type,
               'form': myForm.ShowMessageForm(instance=message),
               'data': data,
               }
    return render(request, template_name, context)


class CfailureReport(View):
    form_class = myForm.CreateFailureReportForm
    template_name = 'building/cfailureReport.html'

    def get(self, request, building_id):
        context = {'all_failureReport': FailureReport.objects.filter(building=building_id, account=Account.objects.get(user=request.user)),
               'Listname': 'گزارش های خرابی',
               'title1': 'عنوان',
               'title2': 'تاریخ',
               'title3': 'متن',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': self.form_class,
               }
        return render(request, self.template_name, context)

    def post(self, request, building_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.building = Building.objects.get(pk=building_id)
            obj.account = request.user.account
            obj.date = timezone.now()
            obj.save()
            return HttpResponseRedirect(reverse('building:cfailureReport', kwargs={'building_id': building_id}))
        # TODO agar form valid nashod che kone ... payini javab nist
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:cfailureReport', kwargs={'building_id': building_id}))


class UfailureReport(View):
    form_class = myForm.CreateFailureReportForm
    data = "تغییر گزارش خرابی"
    template_name = 'building/ufeature.html'

    def post(self, request, pk, building_id):
        instance = FailureReport.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.date = timezone.now()
            obj.save()
            return HttpResponseRedirect(reverse('building:cfailureReport', kwargs={'building_id': building_id}))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:ufailureReport', kwargs={'building_id': building_id, 'pk': pk}))

    def get(self, request, pk, building_id):
        failureReport = FailureReport.objects.get(pk=pk)
        context = {'failureReport': failureReport,
                   'building': Building.objects.get(pk=building_id),
                   'accountType': Account.objects.get(user=request.user).type,
                   'form': self.form_class,
                   'pk': pk,
                   'data': self.data,
                   }
        return render(request, self.template_name, context)


def dfailureReport(request, building_id, pk):
    FailureReport.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('building:cfailureReport', kwargs={'building_id': building_id}))


def rfailureReport(request, building_id, pk):
    template_name = 'building/rfailureReport.html'
    data = 'مشاهده گزارش خرابی'
    instance = FailureReport.objects.get(pk=pk)
    form_class = myForm.ShowFailureReportForm
    context = {
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': form_class(instance=instance),
               'data': data,
               }
    return render(request, template_name, context)


def rfailureReportm(request, building_id, pk):
    template_name = 'building/rfailureReportm.html'
    data = 'مشاهده گزارش خرابی'
    instance = FailureReport.objects.get(pk=pk)
    form_class = myForm.ShowFailureReportForm
    context = {
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': form_class(instance=instance),
               'data': data,
               }
    return render(request, template_name, context)


class Cnews(View):
    form_class = myForm.CreateNewsForm
    template_name = 'building/cnews.html'

    def get(self, request, building_id):
        context = {'all_news': News.objects.filter(building=building_id),
               'Listname': 'اخبار و اطلاعیه ها',
               'title1': 'عنوان',
               'title2': 'تاریخ',
               'title3': 'متن',
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form' : self.form_class
               }
        return render(request, self.template_name, context)

    def post(self, request, building_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.building = Building.objects.get(pk=building_id)
            obj.date = timezone.now()
            obj.save()
            return HttpResponseRedirect(reverse('building:cnews', kwargs={'building_id': building_id}))
        # TODO agar form valid nashod che kone ... payini javab nist
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:cnews', kwargs={'building_id': building_id}))


class Unews(View):
    form_class = myForm.CreateNewsForm
    data = "تغییر اطلاعیه"
    template_name = 'building/unews.html'

    def post(self, request, pk, building_id):
        instance = News.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.date = timezone.now()
            obj.save()
            return HttpResponseRedirect(reverse('building:cnews', kwargs={'building_id': building_id}))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:unews', kwargs={'building_id': building_id, 'pk': pk}))

    def get(self, request, pk, building_id):
        news = News.objects.get(pk=pk)
        context = {'news': news,
                   'building': Building.objects.get(pk=building_id),
                   'accountType': Account.objects.get(user=request.user).type,
                   'form': self.form_class,
                   'pk': pk,
                   'data': self.data,
                   }
        return render(request, self.template_name, context)


def dnews(request, building_id, pk):
    News.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('building:cnews', kwargs={'building_id': building_id}))


def rnews(request, building_id, pk):
    template_name = 'building/rnews.html'
    data = 'مشاهده اطلاعیه'
    news = News.objects.get(pk=pk)
    form_class = myForm.ShowNewsForm
    context = {
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': form_class(instance=news),
               'data': data,
               }
    return render(request, template_name, context)


def rnewsm(request, building_id, pk):
    template_name = 'building/rnewsm.html'
    data = 'مشاهده اطلاعیه'
    news = News.objects.get(pk=pk)
    form_class = myForm.ShowNewsForm
    context = {
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': form_class(instance=news),
               'data': data,
               }
    return render(request, template_name, context)


class Cpoll(View):
    form_class = myForm.CreatePollForm
    template_name = 'building/cpoll.html'

    def get(self, request, building_id):
        context = {'all_polls': Poll.objects.filter(building=building_id),
                   'Listname': 'نظرسنجی ها',
                   'title1': 'عنوان',
                   'title2': 'تاریخ شروع',
                   'title3': 'تاریخ پایان',
                   'building': Building.objects.get(pk=building_id),
                   'accountType': Account.objects.get(user=request.user).type,
                   'form': self.form_class
                   }
        return render(request, self.template_name, context)

    def post(self, request, building_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.building = Building.objects.get(pk=building_id)
            obj.save()
            return HttpResponseRedirect(reverse('building:cpoll', kwargs={'building_id': building_id}))
        # TODO agar form valid nashod che kone ... payini javab nist
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:cpoll', kwargs={'building_id': building_id}))


class Upoll(View):
    form_class = myForm.CreatePollForm
    data = "تغییر نظرسنجی"
    template_name = 'building/upoll.html'

    def post(self, request, pk, building_id):
        instance = Poll.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect(reverse('building:cpoll', kwargs={'building_id': building_id}))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:upoll', kwargs={'building_id': building_id, 'pk': pk}))

    def get(self, request, pk, building_id):
        poll = Poll.objects.get(pk=pk)
        context = {'poll': poll,
                   'building': Building.objects.get(pk=building_id),
                   'accountType': Account.objects.get(user=request.user).type,
                   'form': self.form_class,
                   'pk': pk,
                   'data': self.data,
                   }
        return render(request, self.template_name, context)


def dpoll(request, building_id, pk):
    Poll.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('building:cpoll', kwargs={'building_id': building_id}))


def rpoll(request, building_id, pk):
    template_name = 'building/rpoll.html'
    data = 'مشاهده نظرسنجی'
    poll = Poll.objects.get(pk=pk)
    form_class = myForm.ShowPollForm
    context = {
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': form_class(instance=poll),
               'data': data,
               }
    return render(request, template_name, context)


def rpollm(request, building_id, pk):
    template_name = 'building/rpollm.html'
    data = 'مشاهده نظرسنجی'
    poll = Poll.objects.get(pk=pk)
    form_class = myForm.ShowPollForm
    context = {
        'building': Building.objects.get(pk=building_id),
        'accountType': Account.objects.get(user=request.user).type,
        'form': form_class(instance=poll),
        'data': data,
    }
    return render(request, template_name, context)


class Cdebt(View):
    form_class = myForm.CreateDebtForm
    template_name = 'building/cdebt.html'

    def get(self, request, building_id):
        context = {'all_debt': Debt.objects.filter(account=Account.objects.filter(building=building_id)),
                   'Listname2': 'بدهی ها',
                   'title1': 'مبلغ',
                   'title2': 'تاریخ',
                   'title4': 'نوع بدهی',
                   'building': Building.objects.get(pk=building_id),
                   'accountType': Account.objects.get(user=request.user).type,
                   'form': self.form_class
                   }
        return render(request, self.template_name, context)

    def post(self, request, building_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.date = timezone.now()
            obj.save()
            return HttpResponseRedirect(reverse('building:cdebt', kwargs={'building_id': building_id}))
        # TODO agar form valid nashod che kone ... payini javab nist
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:cdebt', kwargs={'building_id': building_id}))


class Udebt(View):
    form_class = myForm.CreateDebtForm
    data = "ویرایش بدهی"
    template_name = 'building/udebt.html'

    def post(self, request, pk, building_id):
        instance = Debt.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.date = timezone.now()
            obj.save()
            return HttpResponseRedirect(reverse('building:cdebt', kwargs={'building_id': building_id}))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:udebt', kwargs={'building_id': building_id, 'pk': pk}))

    def get(self, request, pk, building_id):
        debt = Debt.objects.get(pk=pk)
        context = {'debt': debt,
                   'building': Building.objects.get(pk=building_id),
                   'accountType': Account.objects.get(user=request.user).type,
                   'form': self.form_class,
                   'pk': pk,
                   'data': self.data,
                   }
        return render(request, self.template_name, context)


def ddebt(request, building_id, pk):
    Debt.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('building:cdebt', kwargs={'building_id': building_id}))


def rdebt(request, building_id, pk):
    template_name = 'building/rdebt.html'
    data = 'مشاهده بدهی'
    debt = Debt.objects.get(pk=pk)
    form_class = myForm.ShowDebtForm
    context = {
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': form_class(instance=debt),
               'data': data,
               }
    return render(request, template_name, context)


class Cunit(View):
    form_class = myForm.CreateUnitForm
    template_name = 'building/cunit.html'

    def get(self, request, building_id):
        getbuilding = Building.objects.get(pk=building_id)
        context = {'building': getbuilding,
                   'accountType': Account.objects.get(user=request.user).type,
                   'all_units': Unit.objects.filter(building=getbuilding),
                   'createUnitForm': myForm.CreateUnitForm,
                   }
        return render(request, self.template_name, context)

    def post(self, request, building_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.building = Building.objects.get(pk=building_id)
            obj.save()
            return HttpResponseRedirect(reverse('building:cunit', kwargs={'building_id': building_id}))
        # TODO agar form valid nashod che kone ... payini javab nist
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:cunit', kwargs={'building_id': building_id}))


class Uunit(View):
    form_class = myForm.CreateUnitForm
    data = "ویرایش واحد"
    template_name = 'building/uunit.html'

    def post(self, request, pk, building_id):
        instance = Unit.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect(reverse('building:cunit', kwargs={'building_id': building_id}))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:uunit', kwargs={'building_id': building_id, 'pk': pk}))

    def get(self, request, pk, building_id):
        unit = Unit.objects.get(pk=pk)
        context = {'unit': unit,
                   'building': Building.objects.get(pk=building_id),
                   'accountType': Account.objects.get(user=request.user).type,
                   'form': self.form_class,
                   'pk': pk,
                   'data': self.data,
                   }
        return render(request, self.template_name, context)


def dunit(request, building_id, pk):
    Unit.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('building:cunit', kwargs={'building_id': building_id}))


def runit(request, building_id, pk):
    template_name = 'building/runit.html'
    data = 'مشاهده واحد'
    unit = Unit.objects.get(pk=pk)
    form_class = myForm.CreateUnitForm
    context = {
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': form_class(instance=unit),
               'data': data,
               }
    return render(request, template_name, context)


class Cneighbor(View):
    form_class = myForm.CreateNeighborForm
    template_name = 'building/cneighbor.html'

    def get(self, request, building_id):
        getbuilding = Building.objects.get(pk=building_id)
        neighbor_unit = {}
        for unit in Unit.objects.filter(building=getbuilding):
            if unit.account is not None:
                neighbor_unit[unit.account] = Unit.objects.filter(account=unit.account)

        context = {'building': getbuilding,
                    'accountType':  Account.objects.get(user=request.user).type,
                    'neighbor_unit': neighbor_unit,
                    'createNeighborForm': self.form_class,
                    }
        return render(request, self.template_name, context)

    def post(self, request, building_id):
        form = self.form_class(request.POST)
        if form.is_valid():#todo
            user = form.save()
            password = hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest()[:8] #todo password
            user.is_active = False
            user.save()
            #obj = User.objects.get(username=request.POST['username'])
            #obj.set_password(str(password))
            #obj.save()
            #activation_key = hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest()[:5]

            Account.objects.create(user=user, type=UserType.NEIGHBOR, activation_key=password)
            user.account.save()
            return HttpResponseRedirect(reverse('building:cneighbor', kwargs={'building_id': building_id}))
        # TODO agar form valid nashod che kone ... payini javab nist
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:cneighbor', kwargs={'building_id': building_id}))


class Uneighbor(View):
    form_class = myForm.CreateNeighborForm
    data = "ویرایش همسایه"
    template_name = 'building/uneighbor.html'

    def post(self, request, pk, building_id):
        instance = Account.objects.get(pk=pk)#todo
        form = self.form_class(request.POST, instance=instance.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.email = obj.username
            obj.save()
            return HttpResponseRedirect(reverse('building:cneighbor', kwargs={'building_id': building_id}))
        for m in form.non_field_errors():
            messages.info(request, m)
        return HttpResponseRedirect(reverse('building:uneighbor', kwargs={'building_id': building_id, 'pk': pk}))

    def get(self, request, pk, building_id):
        account = Account.objects.get(pk=pk)#todo
        context = {'account': account,
                   'building': Building.objects.get(pk=building_id),
                   'accountType': Account.objects.get(user=request.user).type,
                   'form': self.form_class,
                   'pk': pk,
                   'data': self.data,
                   }
        return render(request, self.template_name, context)


def dneighbor(request, building_id, pk):
    Account.objects.get(pk=pk).delete()#todo
    return HttpResponseRedirect(reverse('building:cneighbor', kwargs={'building_id': building_id}))


def rneighbor(request, building_id, pk):
    template_name = 'building/rneighbor.html'
    data = 'مشاهده همسایه'
    account = Account.objects.get(pk=pk)#todo
    form_class = myForm.CreateNeighborForm
    context = {
               'building': Building.objects.get(pk=building_id),
               'accountType': Account.objects.get(user=request.user).type,
               'form': form_class(instance=account.user),
               'data': data,
               }
    return render(request, template_name, context)


def sneighbor(request, building_id, pk):
    account = Account.objects.get(pk=pk)
    email_subject = 'SamSam account confirmation'  # TODO
    email_body = "Hello, %s, and thanks for signing up for an \
                example.com account!\n\nTo activate your account, click this link within 48 \
                    hours:\n\nhttp://127.0.0.1:8001/home/confirm/%s" % (
        account.user.first_name,
        account.activation_key)
    send_mail(email_subject,
              email_body,
              'samsamcompany2@gmail.com',
              [account.user.email])

    form_class = myForm.CreateNeighborForm
    template_name = 'building/cneighbor.html'
    getbuilding = Building.objects.get(pk=building_id)
    neighbor_unit = {}
    for unit in Unit.objects.filter(building=getbuilding):
        if unit.account is not None:
            neighbor_unit[unit.account] = Unit.objects.filter(account=unit.account)

    context = {'building': getbuilding,
               'accountType': Account.objects.get(user=request.user).type,
               'neighbor_unit': neighbor_unit,
               'createNeighborForm': form_class,
               }
    return render(request, template_name, context)