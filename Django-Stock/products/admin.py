from django.contrib import admin
from products.models import Tipo, Articulo

class TipoAdmin(admin.ModelAdmin):
    pass

class ArticuloAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tipo, TipoAdmin)
admin.site.register(Articulo, ArticuloAdmin)