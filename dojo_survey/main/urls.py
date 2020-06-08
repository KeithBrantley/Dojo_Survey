from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('results', views.results),
    path('go_back', views.direct_to_index),
]
