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
    url(r'^(?P<building_id>[0-9]+)/cfeature/$', views.Cfeature.as_view(), name="cfeature"),

    url(r'^(?P<building_id>[0-9]+)/failureReport/$', views.failureReport, name="failureReport"),
    url(r'^(?P<building_id>[0-9]+)/cufailureReport/$', views.cufailureReport, name="cufailureReport"),

    url(r'^(?P<building_id>[0-9]+)/poll/$', views.poll, name="poll"),
    url(r'^(?P<building_id>[0-9]+)/cupoll/$', views.cupoll, name="cupoll"),


]
