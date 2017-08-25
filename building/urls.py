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
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteBuilding.as_view(), name="deleteBuilding"),

    url(r'^activities/$', views.activities, name="activities"),
    url(r'^inbox/$', views.inbox, name="inbox"),
    url(r'^sendmessage/$', views.Sendmessage.as_view(), name="sendmessage"),
    url(r'^deletemessage/(?P<pk>[0-9]+)/$', views.dmessage, name="dmessage"),
    url(r'^retrivemessage/(?P<pk>[0-9]+)/$', views.rmessage, name="rmessage"),
    url(r'^support/$', views.Support.as_view(), name="support"),
    url(r'^updateProfile/$', views.UpdateUserProfileFormView.as_view(), name="updateUserProfile"),
    url(r'^changePassword/$', views.ChangePasswordFormView.as_view(), name="changePassword"),


    url(r'^(?P<building_id>[0-9]+)/unit/$', views.unit, name="unit"),
    url(r'^(?P<building_id>[0-9]+)/unit/create/$', views.CreateUnitFormView.as_view(), name="createUnit"),

    url(r'^(?P<building_id>[0-9]+)/neighbor/$', views.neighbor, name="neighbor"),
    url(r'^(?P<building_id>[0-9]+)/neighbor/create/$', views.CreateNeighborFormView.as_view(), name="createNeighbor"),


    url(r'^(?P<building_id>[0-9]+)/transaction/$', views.transaction, name="transaction"),
    url(r'^(?P<building_id>[0-9]+)/cudebt/$', views.cudebt, name="cudebt"),

    url(r'^(?P<building_id>[0-9]+)/news/$', views.news, name="news"),
    url(r'^(?P<building_id>[0-9]+)/cunews/$', views.cunews, name="cunews"),

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
    url(r'^(?P<building_id>[0-9]+)/cupoll/$', views.cupoll, name="cupoll"),


]
