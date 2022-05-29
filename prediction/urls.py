from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('report/', views.Report, name='report'),
    # path('home/predict/', views.predict, name='predict'),
    path('', views.signup, name='home1')
]