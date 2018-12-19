"""siteadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from pst.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
  # path('api/', include('mynewapp.urls')),
  re_path('home/', TemplateView.as_view(template_name='index.html')),
  path('print_tweets/', print_tweets),
  path('fetch_tweets/', fetch_tweets),
  path('fetch_sexist_words/', fetch_sexist_words),
  path('stream_tweets/', streaming)
#   re_path('.*', TemplateView.as_view(template_name='index.html')),
#   url(r'^', TemplateView.as_view(template_name='index.html')),

]
