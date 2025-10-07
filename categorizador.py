from openai import OpenAI
from dotenv import load_dotenv 
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
prompt_sistema="""
    Você é um categorizador de produtos.
    Você deve assumir as categorias presentes na lista abaixo.
    
    # Lista de Categorias Válidas
    - Moda Sustentável
    - Produtos para o Lar
    - Beleza Natural
    - Eletrônicos Verdes
    
    # Formato de Saída
    Produto: Nome do Produto
    Categoria: apresente a categoria do produto
    
    # Exemplo de Saída
    Produto: Escova elétrica com recarga solar
    Categoria: Eletrônicos Verdes
"""

prompt_usuario = input("Apresente o nome de um produto: ")

resposta = cliente.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role":"system",
            "content": prompt_sistema
        },
        {
            "role":"user",
            "content":prompt_usuario
        }
    ],
)

print(resposta.choices[0].message.content)
