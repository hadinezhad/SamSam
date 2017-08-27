from django.conf.urls import url
from . import views
# building/
app_name = 'building'
urlpatterns = [
    url(r'^$', views.Buildinglist.as_view(), name="building"),

    url(r'^(?P<building_id>[0-9]+)/$', views.showdash, name="showdash"),
    url(r'^(?P<building_id>[0-9]+)/info/$', views.info, name="info"),

    url(r'^create/$', views.CreateBuildingFormView.as_view(), name="createBuilding"),
    url(r'^(?P<building_id>[0-9]+)/update/$', views.UpdateBuildingFormView.as_view(), name="updateBuilding"),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.deleteBuilding, name="deleteBuilding"),

    url(r'^activities/$', views.activities, name="activities"),
    url(r'^inbox/$', views.inbox, name="inbox"),
    url(r'^sendmessage/$', views.Sendmessage.as_view(), name="sendmessage"),
    url(r'^sendmessage/(?P<pk>[0-9]+)/$', views.Sendmessages.as_view(), name="sendmessages"),
    url(r'^deletemessage/(?P<pk>[0-9]+)/$', views.dmessage, name="dmessage"),
    url(r'^retrivemessage/(?P<pk>[0-9]+)/$', views.rmessage, name="rmessage"),
    url(r'^support/$', views.Support.as_view(), name="support"),
    url(r'^updateProfile/$', views.UpdateUserProfileFormView.as_view(), name="updateUserProfile"),
    url(r'^changePassword/$', views.ChangePasswordFormView.as_view(), name="changePassword"),



    url(r'^(?P<building_id>[0-9]+)/cunit/$', views.Cunit.as_view(), name="cunit"),
    url(r'^(?P<building_id>[0-9]+)/uunit/(?P<pk>[0-9]+)/$', views.Uunit.as_view(), name="uunit"),
    url(r'^(?P<building_id>[0-9]+)/dunit/(?P<pk>[0-9]+)/$', views.dunit, name="dunit"),
    url(r'^(?P<building_id>[0-9]+)/runit/(?P<pk>[0-9]+)/$', views.runit, name="runit"),

    url(r'^(?P<building_id>[0-9]+)/cneighbor/$', views.Cneighbor.as_view(), name="cneighbor"),
    url(r'^(?P<building_id>[0-9]+)/uneighbor/(?P<pk>[0-9]+)/$', views.Uneighbor.as_view(), name="uneighbor"),
    url(r'^(?P<building_id>[0-9]+)/dneighbor/(?P<pk>[0-9]+)/$', views.dneighbor, name="dneighbor"),
    url(r'^(?P<building_id>[0-9]+)/rneighbor/(?P<pk>[0-9]+)/$', views.rneighbor, name="rneighbor"),
    url(r'^(?P<building_id>[0-9]+)/sneighbor/(?P<pk>[0-9]+)/$', views.sneighbor, name="sneighbor"),



    url(r'^(?P<building_id>[0-9]+)/transaction/$', views.transaction, name="transaction"),

    url(r'^(?P<building_id>[0-9]+)/cdebt/$', views.Cdebt.as_view(), name="cdebt"),
    url(r'^(?P<building_id>[0-9]+)/udebt/(?P<pk>[0-9]+)/$', views.Udebt.as_view(), name="udebt"),
    url(r'^(?P<building_id>[0-9]+)/ddebt/(?P<pk>[0-9]+)/$', views.ddebt, name="ddebt"),
    url(r'^(?P<building_id>[0-9]+)/rdebt/(?P<pk>[0-9]+)/$', views.rdebt, name="rdebt"),

    url(r'^(?P<building_id>[0-9]+)/news/$', views.news, name="news"),

    url(r'^(?P<building_id>[0-9]+)/cnews/$', views.Cnews.as_view(), name="cnews"),
    url(r'^(?P<building_id>[0-9]+)/unews/(?P<pk>[0-9]+)/$', views.Unews.as_view(), name="unews"),
    url(r'^(?P<building_id>[0-9]+)/dnews/(?P<pk>[0-9]+)/$', views.dnews, name="dnews"),
    url(r'^(?P<building_id>[0-9]+)/rnews/(?P<pk>[0-9]+)/$', views.rnews, name="rnews"),
    url(r'^(?P<building_id>[0-9]+)/rnewsm/(?P<pk>[0-9]+)/$', views.rnewsm, name="rnewsm"),#todo age beshe ba balayi yeki shan

    url(r'^(?P<building_id>[0-9]+)/feature/$', views.feature, name="feature"),
    url(r'^(?P<building_id>[0-9]+)/feature/(?P<pk>[0-9]+)/$', views.changereservefeature, name="crfeature"),

    url(r'^(?P<building_id>[0-9]+)/cfeature/$', views.Cfeature.as_view(), name="cfeature"),
    url(r'^(?P<building_id>[0-9]+)/ufeature/(?P<pk>[0-9]+)/$', views.Ufeature.as_view(), name="ufeature"),
    url(r'^(?P<building_id>[0-9]+)/dfeature/(?P<pk>[0-9]+)/$', views.dfeature, name="dfeature"),
    url(r'^(?P<building_id>[0-9]+)/rfeature/(?P<pk>[0-9]+)/$', views.rfeature, name="rfeature"),

    url(r'^(?P<building_id>[0-9]+)/failureReport/$', views.failureReport, name="failureReport"),

    url(r'^(?P<building_id>[0-9]+)/cfailureReport/$', views.CfailureReport.as_view(), name="cfailureReport"),
    url(r'^(?P<building_id>[0-9]+)/ufailureReport/(?P<pk>[0-9]+)/$', views.UfailureReport.as_view(), name="ufailureReport"),
    url(r'^(?P<building_id>[0-9]+)/dfailureReport/(?P<pk>[0-9]+)/$', views.dfailureReport, name="dfailureReport"),
    url(r'^(?P<building_id>[0-9]+)/rfailureReport/(?P<pk>[0-9]+)/$', views.rfailureReport, name="rfailureReport"),
    url(r'^(?P<building_id>[0-9]+)/rfailureReportm/(?P<pk>[0-9]+)/$', views.rfailureReportm, name="rfailureReportm"),#todo age beshe ba balayi yeki shan


    url(r'^(?P<building_id>[0-9]+)/poll/$', views.poll, name="poll"),

    url(r'^(?P<building_id>[0-9]+)/cpoll/$', views.Cpoll.as_view(), name="cpoll"),
    url(r'^(?P<building_id>[0-9]+)/upoll/(?P<pk>[0-9]+)/$', views.Upoll.as_view(), name="upoll"),
    url(r'^(?P<building_id>[0-9]+)/dpoll/(?P<pk>[0-9]+)/$', views.dpoll, name="dpoll"),
    url(r'^(?P<building_id>[0-9]+)/rpoll/(?P<pk>[0-9]+)/$', views.rpoll, name="rpoll"),
    url(r'^(?P<building_id>[0-9]+)/rpollm/(?P<pk>[0-9]+)/$', views.rpollm, name="rpollm"),


]
