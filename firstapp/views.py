from django.shortcuts import render

from django.views import generic

from firstapp.models import Data


class DataListView(generic.ListView):
    model = Data
    template_name = 'firstapp/index.html'


class DataDetailView(generic.DetailView):
    model = Data
    template_name = 'firstapp/detail.html'
