import sqlite3  
from database.connection import get_connection

def cadastrar_insumo(insumo):
    conexao = get_connection()
    cursor = conexao.cursor()
    
    cursor.execute("""
        INSERT INTO insumos (nome, preco, peso, custo_grama)
        VALUES (?, ?, ?, ?)
    """, (insumo.nome, insumo.preco, insumo.peso, insumo.custo_grama))

    conexao.commit()
    conexao.close()
    
def listar_insumo():
    conexao = get_connection()
    cursor = conexao.cursor()
    
    cursor.execute('''
        SELECT id, nome, preco, peso, custo_grama FROM insumos               
    ''')
    
    dados = cursor.fetchall()
    conexao.close()
    return dados

def remover_insumo(insumo_id):
    conexao = get_connection()
    cursor = conexao.cursor()
    
    cursor.execute('''
        DELETE FROM insumos WHERE id = ?
        ''',(insumo_id,)        
    )
    if cursor.rowcount == 0:
        print('Nenhum insumo encontrado com esse ID')
    else:
        print('Insumo removido com sucesso!')
        
    conexao.commit()
    conexao.close()
    
def atualizar_insumo(insumo_id, novo_preco, novo_peso):
    conexao = get_connection()
    cursor = conexao.cursor()
    
    custo_grama = novo_preco/novo_peso
    
    cursor.execute('''
        UPDATE insumos 
        SET preco = ?, peso = ?, custo_grama = ?
        WHERE id = ? 
        ''',(novo_preco, novo_peso, custo_grama, insumo_id)
    )
    
    if cursor.rowcount == 0:
        print('Nenhum insumo encontrado com esse ID')
    else:
        print('Insumo atualizado com sucesso')
        
    conexao.commit()
    conexao.close()
    
def buscar_por_id(insumo_id):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT id, nome, preco, peso FROM insumos WHERE id = ?',
        (insumo_id,)
    )

    row = cursor.fetchone()
    conexao.close()

    if row:
        return {'id': row[0], 'nome': row[1], 'preco': row[2], 'peso': row[3]}
    return None
