

from __future__ import unicode_literals

from django.views.generic.edit import CreateView
from reporter.models import Galleta
from django.views.generic.list import ListView




class GalletaCreate (CreateView):
    model =Galleta
    fields = '__all__'
    sucess_url = "/"   #=reverse_lazy('galleta_list') 
    

class GalletaListView(ListView):
    model= Galleta
    fields = '__all__'
    