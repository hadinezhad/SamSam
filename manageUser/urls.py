from django.conf.urls import url
from . import views
# home/
app_name = 'manageUser'
urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.UserFormView.as_view(), name="signup"),
    url(r'^login/$', views.UserLoginFormView.as_view(), name="login"),
    url(r'^logout/$', views.UserLogoutFormView.as_view(), name="logout"),
    url(r'^guide/$', views.guide, name="guide"),
    url(r'^callus/$', views.callus, name="callus"),



]
