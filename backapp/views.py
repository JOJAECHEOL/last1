from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Goods

def index(request):
    goods = Goods.objects

    return render(request, 'index.html',{'goods':goods})

def choose(request):
    getitem = request.GET["goodsitem"]
    goods = Goods.objects.all().filter(item__contains=getitem)

    return render(request, 'choose.html', {'items':goods})

def buy1(request):
    return render(request, 'buy1.html')

def buy2(request):
    items = request.GET["item"]
    pricelow = request.GET["pricelow"]
    pricehigh = request.GET["pricehigh"]
    startdate = request.GET["startdate"]
    enddate = request.GET["enddate"]
    items = Goods.objects.all().filter(price__range=(pricelow, pricehigh), date__range=(startdate, enddate)).exclude(item__contains=items)
    return render(request, 'buy2.html', {'items': items})

