class Insumos():
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso
        self.custo_grama = preco/peso
        
    def __str__(self):
        return f'Insumo: {self.nome}'
    
    