from django.db import models

# Create your models here.
class Insumo(models.Model):
    PESO = 'P'
    UNIDADE = 'U'
    
    TIPO_MEDIDA_CHOICE = [(PESO, 'Peso (gramas)'), (UNIDADE, 'Unidade')]
    
    nome = models.CharField(
        max_length=120,
        unique=True
    )
    
    tipo_medida = models.CharField(
        max_length=1,
        choices=TIPO_MEDIDA_CHOICE
    )
    
    quantidade_base = models.DecimalField(
        max_digits=10,
        decimal_places=3, 
        help_text='Quantidade descrita na embalagem (g ou und)'
        )
    
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Valor do produto'
    )
    
    custo_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        editable=False
    )
    
    ativo = models.BooleanField(
        default=True
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True
    )
    
    data_atualizacao = models.DateTimeField(
        auto_now_add=True
    )
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'
        
    def save(self, *args, **kwargs):
        # Ao salvar os dados calcula o custo unitario internamente
        if self.quantidade_base and self.valor:
            self.custo_unitario = self.valor / self.quantidade_base
        super().save(*args, **kwargs)
        
class HistoricoInsumo(models.Model):
    insumo = models.ForeignKey(
        'Insumo',
        on_delete=models.CASCADE,
        related_name='historicos'
    )

    # Dados financeiros no momento do registro
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Valor pago pelo insumo na data'
    )

    quantidade_base = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        help_text='Quantidade base do insumo (ex: gramas ou unidades)'
    )

    custo_unitario = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        help_text='Custo por grama ou por unidade'
    )

    data_referencia = models.DateTimeField(
        auto_now_add=True
    )

    motivo = models.CharField(
        max_length=100,
        blank=True,
        help_text='Ex: reajuste fornecedor, troca de marca, correção'
    )

    observacao = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = 'Histórico de Insumo'
        verbose_name_plural = 'Histórico de Insumos'
        ordering = ['-data_referencia']
        indexes = [
            models.Index(fields=['insumo', 'data_referencia']),
        ]

    def __str__(self):
        return f'{self.insumo.nome} - {self.data_referencia:%d/%m/%Y}'