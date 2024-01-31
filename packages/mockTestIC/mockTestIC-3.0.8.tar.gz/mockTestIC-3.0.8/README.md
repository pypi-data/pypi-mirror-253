
# mockTestIC
Este script Python utiliza a biblioteca Faker para gerar dados ficticios de acordo com as chaves especificadas em um dicionario de entrada. A funcao principal é fakeJson, que recebe um dicionario json_data contendo chaves que representam tipos de dados desejados e valores associados a esses tipos.



## Dicionario
``` 
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
        "cartaoVencimento":fakecredit_card_expire, 
 ```
# Como usar

Para utilizar a biblioteca mockTestIC, primeiro e necessario instala-la. Voce pode fazer isso executando o seguinte comando no terminal: 

``` 
    pip install mockTestIC
```

Apos a instalacao, importe a biblioteca ou a funcao que deseja no seu codigo da seguinte maneira:

``` 
    from mockTestIC import fakeJson, fakeJsonFor, fakeSQL
```

Agora, abaixo, voce encontra um exemplo de como implementar a funcao fakeJson:

## fakeJson

```
    from mockTestIC import fakeJson  

dados_json = {
    "primeiro nome": "primeiroNome",
    "sobrenome": "sobreNome",
    "nome completo": "nomeCompleto",
    "nome user": "nomeUser",
    "prefixo": "prefixo",
    "suffix": "suffix",
}

dados_gerados = fakeJson(dados_json)

print(dados_gerados)

```
## fakeJsonFor

Agora, abaixo, voce encontra um exemplo de como implementar a funcao fakeJsonFor ele funciona na mesma maneira unica diferenca que ele aceita ser implementado com FOR no seu codigo:

```
    from mockTestIC import fakeJsonFor  

dados_json = {
    "primeiro nome": "primeiroNome",
    "sobrenome": "sobreNome",
    "nome completo": "nomeCompleto",
    "nome user": "nomeUser",
    "prefixo": "prefixo",
    "suffix": "suffix",
}

dados_gerados = fakeJson(dados_json)

print(dados_gerados)

```
## fakeSQL
Agora, abaixo, voce encontra um exemplo de como implementar a funcao fakeSQL, voce atribui um valor a uma:

```
from mockTestIC import fakeSQL  

sql_string = "INSERT INTO usuarios (id, nome, idade, cidade);"


dados_gerados = fakeSQL(sql_string)


print("Dados gerados:", dados_gerados)


sql_com_dados = sql_string.format(**dados_gerados)
print("SQL com dados fictícios:", sql_com_dados)
```
Lembrando que existe um dicionario de palavras reservadas para gerar esses dados que vai esta abaixo tambem vale lembrar que qualquer texto que passar e estiver uma palavra especifica que esta na biblioteca ele ira gerar esse dado.


Lembre-se de que o nome do campo no dicionario dados_json pode ser qualquer um; apenas o valor associado a cada chave deve seguir a formatacao especificada.

Abaixo esta a lista dos tipos de dados suportados pela biblioteca, que podem ser utilizados como valores no dicionario dados_json

## Dicionario fakeJson e fakeJsonFor
```
    {
    "primeiroNome": "primeiroNome",
    "sobreNome": "sobreNome",
    "nomeCompleto": "nomeCompleto",
    "nomeUser": "nomeUser",
    "prefixo": "prefixo",
    "suffix": "suffix",
    "endereco": "endereco",
    "cidade": "cidade",
    "estado": "estado",
    "pais": "pais",
    "codigoPostal": "codigoPostal",
    "enderecoRua": "enderecoRua",
    "latitude": "latitude",
    "longitude": "longitude",
    "numeroTelefone": "numeroTelefone",
    "email": "email",
    "emailSeguro": "emailSeguro",
    "dataNasc": "dataNasc",
    "dataSec": "dataSec",
    "dataDec": "dataDec",
    "horario": "horario",
    "dataHora": "dataHora",
    "horaISO": "horaISO",
    "frase": "frase",
    "paragrafo": "paragrafo",
    "texto": "texto",
    "empresa": "empresa",
    "cargo": "cargo",
    "segurancaSocial": "segurancaSocial",
    "numeroInteiro": "numeroInteiro",
    "elemento": "elemento",
    "amostra": "amostra",
    "numeroFlutuante": "numeroFlutuante",
    "url": "url",
    "ipv4": "ipv4",
    "ipv6": "ipv6",
    "numeroCartao": "numeroCartao",
    "cartaoVencimento": "cartaoVencimento"
}
```

## Dicionario fakeSQL

```
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
        "credito": fake.credit_card_number()
        "cpf": fake.random_int(min=11111111111, max=99999999999),
        "rg": fake.random_int(min=111111111, max=999999999),
        "estoque": fake.random_int(min=0, max=99999),
        "texto": fake.text(),
        "salario": fake.random_int(min=100, max=99999),
        "ativo": fake.boolean()
    }
```


# Contato

Email: Victoraugustodocarmo32@gmail.com<br> 
Linkedin: [Victor Augusto](https://www.linkedin.com/in/victor-augusto-2b01a71a6/)<br>
Github: [@Augustoo22](https://github.com/Augustoo22)<br>
