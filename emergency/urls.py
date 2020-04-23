from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('symptoms/', views.symptoms, name="symptoms"),
    path('results/', views.results, name='results'),
]
