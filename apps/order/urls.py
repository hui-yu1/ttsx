from django.urls import path
from apps.order import views

urlpatterns = [
    path('',views.index,name="index"),
]
