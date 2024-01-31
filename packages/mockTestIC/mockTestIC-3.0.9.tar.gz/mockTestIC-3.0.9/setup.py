from setuptools import setup

with open('README.md', 'r') as arq:
    readme = arq.read()

setup(
    name='mockTestIC',
    version='3.0.9',
    license='MIT License',
    author='Victor Augusto do Carmo',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='Victoraugustodocarmo32@gmail.com',
    keywords=['mockTest', 'dados falsos', 'insert de dados falsos', 'dados ficticios', 'SQL', 'gerador de dados', 'false data', 'fictitious data', 'data', 'dados', 'data generator'],
    description='O código utiliza a biblioteca Faker para gerar dados fictícios com base em um mapeamento pré-definido. A função fakeJson recebe um dicionário representando dados em formato JSON e substitui os valores associados às chaves de acordo com o mapeamento fornecido. Cada chave do JSON é mapeada para uma função correspondente da biblioteca Faker, gerando assim dados fictícios variados, como nomes, endereços, datas e números. Se uma chave não estiver no mapeamento, a função levanta uma exceção de valor inválido.',
    packages=['mockTestIC'],
    install_requires=[
        'pydantic',
        'faker',
        'typing',
        'setuptools',
    ],
)
