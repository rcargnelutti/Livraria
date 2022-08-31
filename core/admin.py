from django.contrib import admin

from core.models import Categoria, Editora, Autor, Livro

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Livro)
class CoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'ISBN', 'quantidade', 'preco', 'editora', 'categoria']
    list_display_links = ['id', 'titulo', 'ISBN']


admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
# admin.site.register(Livro)
