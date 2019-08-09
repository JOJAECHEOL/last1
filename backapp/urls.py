"""backproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
import backapp.views
# from django.conf.urls import include
# from django.views.generic.base import TemplateView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', backapp.views.index, name='index'),
    path('choose/', backapp.views.choose, name='choose'),
    path('buy1/', backapp.views.buy1, name='buy1'),
    path('buy2/', backapp.views.buy2, name='buy2'),
    # path('login/', include('django.contrib.auth.urls')),
    # path('login/', include('loginapp.urls')),
]


