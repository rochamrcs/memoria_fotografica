from django.db import models

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.model

class Fotos(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='memorias/')
    descricao = models.TextField(blank=True)
    registrada_em = models.DateField(null=True, blank=True)
    localizacao = models.CharField(max_length=255, blank=True)
    album = models.ForeignKey(Album,on_delete=models.PROTECT, related_name='Album', blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

    def __str__(self):
        return f"Foto {self.id}"

