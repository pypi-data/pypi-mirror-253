from faker import Faker
from typing import Dict, List

# Cria uma instância da classe Faker
fake = Faker()

tipo_dados_mapper = {
    "primeiroNome": fake.first_name,
    "sobreNome": fake.last_name,
    "nomeCompleto": fake.name,
    "nomeUser": fake.user_name,
    "prefixo": fake.prefix,
    "suffix": fake.suffix,
    "endereco": fake.address,
    "cidade": fake.city,
    "estado": fake.state,
    "pais": fake.country,
    "codigoPostal": fake.zipcode,
    "enderecoRua": fake.street_address,
    "latitude": fake.latitude,
    "longitude": fake.longitude,
    "numeroTelefone": fake.phone_number,
    "email": fake.email,
    "emailSeguro": fake.safe_email,
    "dataNasc": fake.date_of_birth,
    "dataSec": fake.date_this_century,
    "dataDec": fake.date_this_decade,
    "horario": fake.time,
    "dataHora": fake.date_time,
    "horaISO": fake.iso8601,
    "frase": fake.sentence,
    "paragrafo": fake.paragraph,
    "texto": fake.text,
    "empresa": fake.company,
    "cargo": fake.job,
    "segurancaSocial": fake.ssn,
    "numeroInteiro": fake.random_int,
    "elemento": fake.random_element,
    "amostra": fake.random_sample,
    "numeroFlutuante": fake.pyfloat,
    "url": fake.url,
    "ipv4": fake.ipv4,
    "ipv6": fake.ipv6,
    "numeroCartao": fake.credit_card_number,
    "cartaoVencimento": fake.credit_card_expire,
}

def fakeJson(json_data: Dict[str, str]) -> Dict[str, str]:
    # Itera sobre as chaves e valores do dicionário de dados
    for key, value in json_data.items():
        # Verifica se o tipo de dado é suportado
        if value in tipo_dados_mapper:
            # Substitui o valor no dicionário pelo valor gerado pela função Faker correspondente
            json_data[key] = tipo_dados_mapper[value]()
        # Levanta uma exceção se o tipo de dado não for suportado    
        else:
            raise ValueError(f"Tipo de dado não suportado para a chave '{key}': {value}")
    
    return json_data


def fakeJsonFor(json_data: Dict[str, str]) -> Dict[str, str]:
    # Cria uma cópia do dicionário original para evitar alterações indesejadas
    result_data = json_data.copy()

    # Itera sobre as chaves e valores do dicionário de dados
    for key, value in json_data.items():
        # Verifica se o tipo de dado é suportado
        if key in tipo_dados_mapper:
            # Substitui o valor no dicionário pelo valor gerado pela função Faker correspondente
            result_data[key] = tipo_dados_mapper[key]()
        # Levanta uma exceção se a chave não for suportada    
        else:
            raise ValueError(f"Chave não suportada: {key}")

    return result_data  

# Função para localizar e substituir palavras-chave por dados fictícios gerados com Faker
def fakeSQL(texto):
    fake = Faker()

    # Mapeia as palavras-chave para os métodos correspondentes do Faker
    palavras_chave = {
        "id": fake.random_int(min=1, max=9999),
        "nome": fake.first_name(),
        "idade": fake.random_int(min=0, max=120),  # Gera uma idade entre 0 e 120 anos
        "cidade": fake.city(),  # Gera o nome de uma cidade fictícia
        "profissao": fake.job(),  # Gera o nome de uma profissão fictícia
        "sobrenome": fake.last_name(),
        "completo": fake.name(),
        "usuario": fake.user_name(),
        "prefixo": fake.prefix(),
        "sufixo": fake.suffix(),
        "endereco": fake.address(),
        "estado": fake.state(),
        "pais": fake.country(),
        "cep": fake.zipcode(),
        "rua": fake.street_address(),
        "latitude": fake.latitude(),
        "longitude": fake.longitude(),
        "celular": fake.phone_number(),
        "telefone": fake.phone_number(),
        "email": fake.email(),
        "nascimento": fake.date_of_birth().strftime('%Y-%m-%d'), 
        "cadastro": fake.date_time().strftime('%y-%m-%d'),
        "horario": fake.time(),
        "descricao": fake.text(),
        "empresa": fake.company(),
        "cargo": fake.job(),
        "site": fake.url(),
        "linkedin": fake.url(),
        "ipv4": fake.ipv4(),
        "ipv6": fake.ipv6(),
        "cartao": fake.credit_card_number(),
        "credito": fake.credit_card_number(),
        "cpf": fake.random_int(min=11111111111, max=99999999999),
        "rg": fake.random_int(min=111111111, max=999999999),
        "estoque": fake.random_int(min=0, max=99999),
        "texto": fake.text(),
        "salario": fake.random_int(min=100, max=99999),
        "ativo": fake.boolean()
    }

    dados_gerados = {}
    
    for palavra_chave, valor_ficticio in palavras_chave.items():
        # Localiza a posição da palavra-chave no texto
        indice_palavra_chave = texto.find(palavra_chave)

        if indice_palavra_chave != -1:
            # Substitui a palavra-chave pelo valor fictício no texto
            texto = (
                texto[:indice_palavra_chave]
                + str(valor_ficticio)  # Convertendo o valor para string
                + texto[indice_palavra_chave + len(palavra_chave):]
            )
            dados_gerados[palavra_chave] = valor_ficticio
        # else:
        #     print(f"Palavra-chave '{palavra_chave}' não encontrada no texto.")

    return dados_gerados