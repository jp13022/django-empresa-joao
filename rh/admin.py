from django.contrib import admin
from .models import Funcionarios, MensagemContato, Produto, Categoria, Cliente

@admin.register(Funcionarios)
class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'departamento', 'data_contratacao','status')
    search_fields = ("nome",)
    list_filter = ('status', 'data_contratacao')

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'lido')
    list_filter = ('lido', 'data_envio')
    search_fields = ('nome', 'email', 'assunto')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'valor')
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria',)

# Categoria e Cliente não precisam de ModelAdmin personalizado
admin.site.register(Categoria)
admin.site.register(Cliente)
