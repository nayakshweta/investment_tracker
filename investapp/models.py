# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Scheme(models.Model):
    amc = models.CharField(max_length=200)
    scheme_name = models.CharField(max_length=200)
    scheme_code = models.IntegerField()

    def __str__(self):
        return str(self.scheme_code) + " "  + self.scheme_name

    class Meta:
        ordering = ['scheme_name']

class DailyNAV(models.Model):
    scheme = models.ForeignKey(to=Scheme)
    asset_value = models.DecimalField(max_digits=25, decimal_places=5)
    date = models.DateField()

class TotalInvestment(models.Model):
    scheme = models.ForeignKey(to=Scheme)
    total_amount = models.DecimalField(max_digits=50, decimal_places=2)
    #latest_val = models.DecimalField(max_digits=50, decimal_places=2)

class HoldingInvestment(models.Model):
    scheme = models.ForeignKey(to=Scheme)
    purchase_date = models.DateField()
    purchase_NAV = models.DecimalField(max_digits=25, decimal_places=5)
    number_of_units = models.DecimalField(max_digits=25, decimal_places=5)

    def __str__(self):
        return str(self.scheme.scheme_name)

class SoldInvestment(models.Model):
    scheme = models.ForeignKey(to=Scheme)
    sell_date = models.DateField()
    purchase_NAV = models.DecimalField(max_digits=25, decimal_places=5)
    number_of_units = models.DecimalField(max_digits=25, decimal_places=5)
