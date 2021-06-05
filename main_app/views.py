import csv, io
from django.shortcuts import render
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

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Bubble.objects.update_or_create(
            stop_id=column[0],
            boardings=column[1],
            alightings=column[2],
            location=column[3],
            )
    context = {}
    return render(request, template, context)
