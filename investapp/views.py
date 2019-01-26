# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Scheme, TotalInvestment, HoldingInvestment, DailyNAV
from django.db.models import Sum

# Create your views here.

def total_investment(request):
    total_investment = TotalInvestment.objects.all().order_by('scheme__scheme_name')
    t1 = TotalInvestment.objects.values('scheme__scheme_name').annotate(Sum('total_amount'))


    return render(request, 'investapp/total_investment.html', {'t1': t1})
