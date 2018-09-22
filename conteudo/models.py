from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def videosCategoria(self):
        return Video.objects.all().filter(categoria_id=self.id).order_by('-id')[:4]

class Video(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=255)
    url = models.FileField(upload_to='conteudo/videos/')
    capa = models.FileField(upload_to='conteudo/images/')
    visualizacao = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    nota = models.FloatField(max_length=20)
    sinopse = models.CharField(max_length=500)

    class Meta:
            ordering = ('nome',)
            verbose_name = 'video'
            verbose_name_plural = 'videos'

    def __str__(self):
        return self.nome