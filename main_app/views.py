import csv, io
import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Bubble
from rest_framework import viewsets
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'index.html')

# def get_bubbles(request, stop_id):
#     stop = Bubble.objects.all().values('stop_id')
#     stop_list = list(stops)
#     for i in range(len(stop_list)):
#         if stop_id == stop_list[i]:
#             return JsonResponse('stop_id', safe=False)

@permission_required('admin.can_add_log_entry')
def data_upload(request):
    template = 'data_upload.html'
    prompt = {
        'order': 'stop_id,boardings,alightings,location'

    }
    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'File must be in .csv format.')

    # data_set = csv_file.read().decode('UTF-8')
    # io_string = io.StringIO(data_set)
    # next(io_string)
    data_set = pd.read_csv(csv_file)
    # location_set = data_set['location']
    # print(location_set)

    for row in data_set:
        _, created = Bubble.objects.update_or_create(
            stop_id=data_set['stop_id'],
            boardings=data_set['boardings'],
            alightings=data_set['alightings'],
            location=data_set['location']
        )
    # for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #     _, created = Bubble.objects.update_or_create(
    #         stop_id=column[0],
    #         boardings=column[1],
    #         alightings=column[2],
    #         location=column[3],
    #         )
    context = {}
    return render(request, template, context)
