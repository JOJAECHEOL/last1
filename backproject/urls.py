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
from django.contrib import admin
from django.urls import path, include
import loginapp.views
import light.views
import heavy.views
from django.conf.urls import url
# import backapp.views
# from django.conf.urls import include
# from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginapp.views.main, name='main'),
    path('mypage/', light.views.mypage, name="mypage"),
    # path('', backapp.views.index, name='index'),
    # path('choose/', backapp.views.choose, name='choose'),
    # path('buy1/', backapp.views.buy1, name='buy1'),
    # path('buy2/', backapp.views.buy2, name='buy2'),
    # path('login/', include('django.contrib.auth.urls')),
    path('login/', include('loginapp.urls')),
    path('', include('backapp.urls')),

#넓은 여행 부분
    path('light/', light.views.index, name="index"),
    path('light/oneselection/', light.views.oneselection, name="oneselection"),
    path('light/twoselection/', light.views.twoselection, name="twoselection"),
    path('light/threeselection/', light.views.threeselection, name="threeselection"),
    path('light/buy/', light.views.buy, name="buy"),
 #깊은 여행 부분
    path('heavy/', heavy.views.heavymain , name="heavymain"),
    path('heavydetail/', heavy.views.heavydetail , name="heavydetail"),
    path('heavyfirst/', heavy.views.heavyfirst , name="heavyfirst"),

]


