from django.contrib import admin
from galeria.models import Fotos, Album


class FotosAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'registrada_em', 'localizacao', 'upload_at')
    search_fields = ('descricao','localizacao')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name',)
    search_fields = ('album_name',)

admin.site.register(Fotos, FotosAdmin)
admin.site.register(Album, AlbumAdmin)