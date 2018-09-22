from django.contrib import admin

from conteudo.models import Categoria, Video


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome', )}
admin.site.register(Categoria, CategoriaAdmin)

class VideoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
admin.site.register(Video, VideoAdmin)
