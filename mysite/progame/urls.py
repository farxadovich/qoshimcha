from django.urls import path
from . import views


urlpatterns = [
    path('hello/', name='hello'),
    path('', views.index, name='index'),

]
