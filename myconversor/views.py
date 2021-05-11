from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from myconversor.forms import LinkForm  
from django.contrib import messages
from pytube import YouTube
from pathlib import Path
import urllib
import os
from .forms import LinkForm, ImagemForm
from PIL import Image



def ytb_down(request):
    form = LinkForm(request.GET)
    return render(request, 'html/ytb_main.html', {'form': form})



   
def yt_download(request):
    formatRadio = request.GET.get('qualityRadio')
    h = "Título:"
    alerta = "Download concluído..."
    home = Path.home()
    paht_video = home / 'Downloads'
    url = request.GET.get('link')
    obj = YouTube(url)
    resolucao = []
    thumbnail = obj.thumbnail_url
    titulo = obj.title
    strm_all = obj.streams
    
    for res in strm_all: #filtrando as resoluções
        resolucao.append(res.resolution)
    resolucao = list(dict.fromkeys(resolucao))
   
    if formatRadio == "1080p":
        if '1080p' in resolucao:
            down = strm_all.get_by_itag(137).download(paht_video)
            print("baixando 1080p")
        elif "720p" in resolucao:
            down = strm_all.get_by_itag(22).download(paht_video)
            print("o video tinha resolução 1080p, mas baixou o 720p HD")
        else: 
            down = strm_all.first().download(paht_video)
            print('baixando a primeira resolucao da porra do video')

    elif formatRadio == "720p":
        if "720p" in resolucao:
            down = strm_all.get_by_itag(22).download(paht_video)
            print("Baixando 720")
        else: 
            down = strm_all.first().download(paht_video)
            print('baixando a primeira resolucao da porra do video')

    elif formatRadio == "360p":
        if '360p' in resolucao:
            down = strm_all.get_by_itag(18).download(paht_video)
            print("baixando 360")
        else:
            down = strm_all.first().download(paht_video)
            print('baixando a primerria resolucao')
    elif formatRadio == "audio":
        down = strm_all.filter().last().download(paht_video)
    else:
        down = strm_all.first().download(paht_video)
        print("Baixando a primeira qualidade")

    return render(request, 'html/yt_download.html', {'thumbnail': thumbnail, 'titulo': titulo, 'h': h, 'strm_all': strm_all, 'alerta': alerta})
