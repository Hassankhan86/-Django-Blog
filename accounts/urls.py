from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [

    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name='logout'),
    #    path('Cancel',views.Cancel_view,name='Cancel'),
]
