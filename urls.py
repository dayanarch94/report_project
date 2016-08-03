'''
Created on Aug 1, 2016

@author: dayana
'''
from __future__ import unicode_literals
from django.conf.urls import url
from reporter.generic import GalletaCreate
from reporter.generic import GalletaListView

urlpatterns = [
               url("create$", GalletaCreate.as_view(), name= "galleta_create")
                
                ]

urlpatterns = [
    url("listview$", GalletaListView.as_view(), name="galleta_list"),
]