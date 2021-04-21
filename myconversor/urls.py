from django.urls import path

from myconversor import views

urlpatterns = [
    path('home', views.ytb_down),
    path('download', views.yt_download),

]
