from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from myconversor.forms import LinkForm
from siteconversor.models import link   
from django.contrib import messages
from pytube import YouTube
import time




def ytb_down(request):
    return render(request, 'html/ytb_main.html')


def yt_download(request):
    if request.method == "GET":
        url = request.GET.get('url')
        obj = YouTube(url)
        h = "Título:"
        #resolucao = []
        thumbnail = obj.thumbnail_url
        titulo = obj.title
        strm_all = obj.streams.filter()
        video_id = url
        time.sleep(3)
        aviso = "Download começou!"
        down = strm_all.first().download(r'C:\Users\willyam cutrim/Downloads')

        
#down': down,
        
        """for i in strm_all:
            resolucao.append(i.resolution)
            
        resolucao = list(dict.fromkeys(resolucao))
        resolucao.remove(None)
        ordem = resolucao.sort(reverse=True)"""

        return render(request, 'html/yt_download.html', {'thumbnail': thumbnail, 'titulo': titulo, 'strm_all': strm_all, 'h': h, 'down': down, 'aviso': aviso})


