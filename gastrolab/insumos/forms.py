from django.forms import models
from .models import Insumo

class InsumoForm(models.ModelForm):
    class Meta:
        model = Insumo
        fields = [  'nome',
                    'quantidade_embalagem',
                    'preco_custo',
                    'unidade_medida'
                ]

    def clean_preco_custo(self):
        preco = self.cleaned_data.get('preco_custo')
        print(preco)
        if preco == 0:
            self.add_error('preco_custo', 'O Valor deve ser maior que 0 (Zero)')
        return preco