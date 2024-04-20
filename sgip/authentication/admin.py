from django.contrib import admin
from .models import Produto
from .forms import ProdutoForm

class ProdutoAdmin(admin.ModelAdmin):
    form = ProdutoForm

admin.site.register(Produto, ProdutoAdmin)