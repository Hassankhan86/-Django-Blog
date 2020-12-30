"""djangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from django.urls import path, include




urlpatterns = [
    url('admin/', admin.site.urls,name='admin'),
    url(r'^accounts/',include("accounts.urls")),
    url(r'^articles/', include('articles.urls')),
    url(r'^about/$', views.about,name="About"),
    url(r'^homepage/$',views.homepage ,name ="Home-Page"),
    url(r'^$', article_views.article_list,name ="Home"),
    #path('homepage',views.homepage,name='Home-Page'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
