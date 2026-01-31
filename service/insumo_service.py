# REGRAS DE NEGÓCIO/VALIDAÇÃO DE DADOS

from database import insumo_repository as repository
from models.insumos import Insumos


def cadastrar_insumo(insumo:Insumos):
    if insumo is None:
        raise ValueError('Insumo não informado')

    if not insumo.nome or not insumo.nome.strip():
        raise ValueError('Nome do insumo é obrigatório')

    if insumo.preco <= 0:
        raise ValueError('Preço deve ser maior que zero')

    if insumo.peso <= 0:
        raise ValueError('Peso deve ser maior que zero')

    if repository.buscar_por_nome(insumo.nome):
        raise ValueError('Já existe um insumo com esse nome')

    repository.cadastrar_insumo(insumo)

def listar_insumo():
    return repository.listar_insumo()

def atualizar_insumo(insumo_id, novo_preco=None, novo_peso=None):
    insumo_atual = repository.buscar_por_id(insumo_id)

    if not insumo_atual:
        raise ValueError('Insumo não encontrado')
        
    if novo_preco is None and novo_peso is None:
        raise ValueError('Informe ao menos um campo para atualização')
    
    preco = novo_preco if novo_preco is not None else insumo_atual['preco']
    peso = novo_peso if novo_peso is not None else insumo_atual['peso']

    repository.atualizar_insumo(insumo_id, preco, peso)


def remover_insumo(insumo_id):
    insumo = repository.buscar_por_id(insumo_id)
    
    if not insumo:
        raise ValueError('Insumo não encontrado')

    repository.remover_insumo(insumo_id)
