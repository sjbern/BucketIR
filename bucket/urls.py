from django.urls import path
from . import views
from .views import (
                    ZoneCreateView,
                   )


urlpatterns = [
    path('', views.home, name='bucket-home'),
    path('bucketSet/', views.bucketSet, name='bucket-settings'),
    path('bucket/new/', ZoneCreateView.as_view(), name='zone-create'),

]
