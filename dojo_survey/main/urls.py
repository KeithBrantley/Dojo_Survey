from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('results', views.results),
    path('results/<int:num_of_results>', views.number_of_results),
]
