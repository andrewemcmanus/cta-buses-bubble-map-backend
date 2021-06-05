from django.shortcuts import render
from .models import Bubble
from rest_framework import viewsets
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'index.html')
