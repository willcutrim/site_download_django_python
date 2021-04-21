from django.urls import path

from myconversor import views

urlpatterns = [
    path('', views.ytb_down),
    path('download', views.yt_download),

]
