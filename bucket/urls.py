from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='bucket-home'),
    path('bucketSet/', views.bucketSet, name='bucket-settings'),

]