from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form2/', views.form2, name='index'),

]