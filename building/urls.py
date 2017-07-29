from django.conf.urls import url
from . import views
# building/
app_name = 'building'
urlpatterns = [
    url(r'^$', views.building, name="building"),

    url(r'^(?P<building_id>[0-9]+)/$', views.showdash, name="showdash"),

    url(r'^create/$', views.CreateBuildingFormView.as_view(), name="createBuilding"),
    url(r'^(?P<building_id>[0-9]+)/update/$', views.UpdateBuildingFormView.as_view(), name="updateBuilding"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeleteBuilding.as_view(), name="deleteBuilding"),

    url(r'^activities/$', views.activities, name="activities"),
    url(r'^inbox/$', views.inbox, name="inbox"),
    url(r'^updateProfile/$', views.UpdateUserProfileFormView.as_view(), name="updateUserProfile"),
    url(r'^changePassword/$', views.ChangePasswordFormView.as_view(), name="changePassword"),


    url(r'^(?P<building_id>[0-9]+)/unit/$', views.unit, name="unit"),
    url(r'^(?P<building_id>[0-9]+)/unit/create/$', views.CreateUnitFormView.as_view(), name="createUnit"),

    url(r'^(?P<building_id>[0-9]+)/neighbor/$', views.neighbor, name="neighbor"),
    url(r'^(?P<building_id>[0-9]+)/neighbor/create/$', views.CreateNeighborFormView.as_view(), name="createNeighbor"),


    url(r'^(?P<building_id>[0-9]+)/transaction/$', views.transaction, name="transaction"),
]

