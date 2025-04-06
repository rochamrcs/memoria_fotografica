from django.contrib import admin
from galeria.models import Fotos


class FotosAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'registrada_em', 'localizacao', 'upload_at')
    search_filds = ('descricao',)

admin.site.register(Fotos, FotosAdmin)