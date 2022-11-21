from django.urls import path, register_converter
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('index', index),
    path('addPunto/<str:lng>/<str:lat>/',addPunto),
    path('verPunto/<int:idP>/',verPunto),
    path('delPunto/<int:idP>/',delPunto),
]