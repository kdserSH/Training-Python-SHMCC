from django.shortcuts import render

# Create your views here.
from .models import Trade
from django.http import HttpResponseRedirect
import pymysql.cursors



def getList(request):
    trades = Trade.objects.filter()
    print(trades.__len__())
    return render(request,'list.html',{
    "trades":trades
    })