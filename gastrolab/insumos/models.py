from django.db import models
from django.utils import timezone


class Insumo(models.Model):
    UNIDADE = "unidade"
    GRAMA = "g"
    UNIDADE_CHOICES = [(UNIDADE, "Unidade"), (GRAMA, "Grama")]

    nome = models.CharField(max_length=255)
    quantidade_embalagem = models.DecimalField(max_digits=10, decimal_places=3)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.CharField(max_length=10, choices=UNIDADE_CHOICES)
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=5, editable=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        is_new = not self.pk  # Se pk = True então é uma atualizacao se não é uma criacao
        
        if not is_new:
            original = Insumo.objects.get(pk=self.pk)
            InsumoHistorico.objects.create(
                insumo=original,
                quantidade_embalagem=original.quantidade_embalagem,
                preco_custo=original.preco_custo,
                unidade_medida=original.unidade_medida,
                custo_unitario=original.custo_unitario,
                tipo=InsumoHistorico.ALTERACAO,
            )

        if self.quantidade_embalagem:
            self.custo_unitario = self.preco_custo / self.quantidade_embalagem

        super().save(*args, **kwargs)

        if is_new:
            InsumoHistorico.objects.create(
                insumo=self,
                quantidade_embalagem=self.quantidade_embalagem,
                preco_custo=self.preco_custo,
                unidade_medida=self.unidade_medida,
                custo_unitario=self.custo_unitario,
                tipo=InsumoHistorico.CRIACAO,
            )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"


class InsumoHistorico(models.Model):
    CRIACAO = "criacao"
    ALTERACAO = "alteracao"
    TIPO_CHOICES = [(CRIACAO, "Criação"), (ALTERACAO, "Alteração")]

    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name="historico")
    quantidade_embalagem = models.DecimalField(max_digits=10, decimal_places=3)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.CharField(max_length=10)
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=5)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data_atualizacao = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ["-data_atualizacao"] # - significa ordem decrescente
        verbose_name = "Histórico de insumo"

