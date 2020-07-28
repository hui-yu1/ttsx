from django.urls import path
from apps.user import views

urlpatterns = [
    path('',views.index,name="index"),
]
