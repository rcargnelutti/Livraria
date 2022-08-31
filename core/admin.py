from django.contrib import admin

from core.models import Categoria, Editora, Autor, Livro, Compra, ItensCompra

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Livro)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'ISBN', 'quantidade', 'preco', 'editora', 'categoria', 'get_autores']
    list_display_links = ['id', 'titulo', 'ISBN']


admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
# admin.site.register(Compra)
# admin.site.register(ItensCompra)
# admin.site.register(Livro)

class ItensInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)