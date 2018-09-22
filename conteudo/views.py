from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from conteudo.models import Video, Categoria

def exibir_catalogo(request):
    categorias = Categoria.objects.all()
    return render(request, 'conteudo/catalogo_videos.html', {'categorias': categorias})

def cadastro_video(request):
    return  render(request, 'conteudo/cadastro_video.html')

def editar_video(request):
    return render(request, 'conteudo/editar_video.html')

def lista_categoria(request, id=None):
    categorias = Categoria.objects.all()
    if id != None:
        videos_lista = Video.objects.all().filter(categoria_id=id)
    else:
        videos_lista = Video.objects.all()

    paginator = Paginator(videos_lista, 3)
    page = request.GET.get('page',1)

    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    return render(request, 'conteudo/lista_categoria.html', {'categorias': categorias, 'videos' : videos})

def exibir_video(request, id):
    video = get_object_or_404(Video, id= id)
    categorias = Categoria.objects.all()
    return render(request, 'conteudo/player_video.html', {'video':video, 'categorias':categorias})
