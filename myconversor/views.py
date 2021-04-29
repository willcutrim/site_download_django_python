from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from myconversor.forms import LinkForm
from siteconversor.models import link   
from django.contrib import messages
from pytube import YouTube
import time
from pathlib import Path
from django.core.validators import URLValidator
import urllib
from .forms import LinkForm



def ytb_down(request):
    form = LinkForm(request.GET)
    if form.is_valid():
        return redirect('download')
    return render(request, 'html/ytb_main.html', {'form': form})



    
def yt_download(request):

    home = Path.home()
    paht_video = home / 'Downloads'
    url = request.GET.get('link')
    obj = YouTube(url)
    h = "Título:"
    #resolucao = []
    thumbnail = obj.thumbnail_url
    titulo = obj.title
    strm_all = obj.streams.filter()
    alerta = "Download concluído..."
    down = strm_all.first().download(paht_video)

    return render(request, 'html/yt_download.html', {'thumbnail': thumbnail, 'titulo': titulo, 'h': h, 'strm_all': strm_all, 'alerta': alerta})
    
        

