from django.urls import path
from conteudo import views

app_name = 'conteudo'

urlpatterns = [
    path('', views.exibir_catalogo, name='catalogo'),
    path('cadastro_video/', views.cadastro_video, name='cadastro_video'),
    path('editar_video/<int:id>/', views.editar_video, name='editar_video'),
    path('<int:id>/', views.exibir_video, name='exibir_video'),

    path('categoria/', views.lista_categoria, name='listar_todas_categorias'),
    path('categoria/<int:id>/', views.lista_categoria, name='lista_categoria'),
]