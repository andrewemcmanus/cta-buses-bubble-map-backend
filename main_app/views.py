from django.shortcuts import render
from .models import Bubble
from rest_framework import viewsets
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'index.html')

def get_bubbles(request, stop_id):
    stop = Bubble.objects.all().values('stop_id')
    stop_list = list(stops)
    for i in range(len(stop_list)):
        if stop_id == stop_list[i]:
            return JsonResponse('stop_id', safe=False)
