from elasticsearch import Elasticsearch
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Configuração da conexão com Elasticsearch
es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=('elastic', os.getenv('ELASTICSEARCH_PASSWORD'))  # Substitua pelas suas credenciais
)

def create_driver_car_index():
    # Criar o índice driver_car
    index_mapping = {
        "mappings": {
            "properties": {
                "motorista_nome": {
                    "type": "text",
                    "fields": {
                        "keyword": {"type": "keyword"}
                    }
                },
                "avaliacao_media": {"type": "float"},
                "marca_carro": {
                    "type": "text",
                    "fields": {
                        "keyword": {"type": "keyword"}
                    }
                },
                "modelo_carro": {
                    "type": "text",
                    "fields": {
                        "keyword": {"type": "keyword"}
                    }
                },
                "veiculo_id": {"type": "integer"},
                "motorista_id": {"type": "integer"}
            }
        }
    }
    
    # Criar o índice (se já existir, deletar primeiro)
    if es.indices.exists(index="driver_car"):
        es.indices.delete(index="driver_car")
    
    es.indices.create(index="driver_car", body=index_mapping)
    print("Índice 'driver_car' criado com sucesso!")

def combine_driver_car_data():
    # Buscar todos os motoristas
    motoristas_query = {"query": {"match_all": {}}}
    motoristas_response = es.search(index="motoristas", body=motoristas_query, size=1000)
    
    # Buscar todos os veículos
    veiculos_query = {"query": {"match_all": {}}}
    veiculos_response = es.search(index="veiculos", body=veiculos_query, size=1000)
    
    # Criar dicionário de veículos para acesso rápido por ID
    veiculos_dict = {}
    for veiculo in veiculos_response['hits']['hits']:
        veiculo_data = veiculo['_source']
        veiculos_dict[veiculo_data['id']] = veiculo_data
    
    # Combinar dados e indexar no driver_car
    for motorista in motoristas_response['hits']['hits']:
        motorista_data = motorista['_source']
        motorista_id = motorista_data['id']
        veiculo_id = motorista_data.get('veiculo_id')
        
        # Verificar se o motorista tem veículo associado
        if veiculo_id and veiculo_id in veiculos_dict:
            veiculo_data = veiculos_dict[veiculo_id]
            
            # Criar documento combinado
            driver_car_doc = {
                "motorista_nome": motorista_data['nome'],
                "avaliacao_media": motorista_data['avaliacao_media'],
                "marca_carro": veiculo_data['marca'],
                "modelo_carro": veiculo_data['modelo'],
                "veiculo_id": veiculo_id,
                "motorista_id": motorista_id
            }
            
            # Indexar no Elasticsearch
            es.index(index="driver_car", id=motorista_id, body=driver_car_doc)
            print(f"Dados combinados indexados para motorista ID: {motorista_id}")
        else:
            print(f"Motorista ID {motorista_id} não tem veículo associado ou veículo não encontrado")

def verify_driver_car_index():
    # Verificar se os dados foram indexados corretamente
    verify_query = {"query": {"match_all": {}}}
    response = es.search(index="driver_car", body=verify_query)
    
    print("\n=== DADOS NO ÍNDICE DRIVER_CAR ===")
    for hit in response['hits']['hits']:
        doc = hit['_source']
        print(f"Motorista: {doc['motorista_nome']} | Avaliação: {doc['avaliacao_media']} | Carro: {doc['marca_carro']} {doc['modelo_carro']}")

if __name__ == "__main__":
    try:
        # Verificar conexão
        if es.ping():
            print("Conexão com Elasticsearch estabelecida!")
            
            # Criar índice
            create_driver_car_index()
            
            # Combinar dados
            combine_driver_car_data()
            
            # Verificar resultado
            verify_driver_car_index()
            
        else:
            print("Erro ao conectar com Elasticsearch")
            
    except Exception as e:
        print(f"Erro: {e}")
