from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework import routers
router = routers.DefaultRouter()

urlpatterns = [

path('', views.index, name="index"),
path('api/', include(router.urls))

]
