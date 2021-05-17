from django.shortcuts import redirect, render
from django.http import HttpResponse
from myconversor.forms import LinkForm  
from pytube import YouTube
from pathlib import Path
import os
from .forms import LinkForm, ImagemForm
from PIL import Image
import requests



def ytb_down(request):
    form = LinkForm(request.GET)
    return render(request, 'html/ytb_main.html', {'form': form})



   
def yt_download(request):
    validation = request.get('link')
    if validation.status_code == requests.codes.OK:
        erro = 'algo deu errado!'
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
        alert = request.GET.get('Exibir Alert')
    
        for res in strm_all: #filtrando as resoluções
            resolucao.append(res.resolution)
        resolucao = list(dict.fromkeys(resolucao))
        resolucao.remove(None)
        
        if formatRadio == "720p":
            if "720p" in resolucao:
                print(strm_all)
                down = strm_all.get_by_itag(247).download(paht_video)
                print("Baixando 720")
            else: 
                return HttpResponse('/{}'.format(erro))

        elif formatRadio == "360p":
            if '360p' in resolucao:
                print(strm_all)
                down = strm_all.get_by_resolution("360p").download(paht_video)
                print("baixando 360")
            else:
                down = strm_all.first().download(paht_video)
                print('baixando a primerria resolucao')

        elif formatRadio == "audio":
            down = strm_all.filter().last().download(paht_video)

        else:
            down = strm_all.first().download(paht_video)
            print("Baixando a primeira qualidade")

        return render(request, 'html/yt_download.html', {'thumbnail': thumbnail, 'titulo': titulo, 'h': h, 'strm_all': strm_all, 'alerta': alerta, 'erro': erro})
