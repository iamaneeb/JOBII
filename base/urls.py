from django.urls import path
from base import views

urlpatterns = [
    path("",views.Home,name="home"),
    path("jobs",views.Jobs,name="jobs")
]
