from setuptools import setup, find_packages

VERSION = '0.1.1'
DESCRIPTION = 'Projeto final da disciplina de Programação Orientada a Objetos II'
LONG_DESCRIPTION = """# Descrição
A `SearchForThis` é uma biblioteca que efetua pesquisas em motores de busca na web.

# Funcionalidades
* Realizar buscas por conteúdos desejados
* Acessar links retornados

# Biblioteca
### Instalação
```python
pip install searchft
```
### Importação
```python
import searchft
```
### Formas de utilização
```python
search = searchft.Searchft
```
`Ou`
```python
from searchft import Searchft
``` 

### Acessando métodos
Uma das formas de acessar os métodos da classe, é a seguinte:
```python
Searchft.method()
```
Onde `method`, é o nome método que você deseja utilizar.
### Realizando buscas:
Use o método `buscar` da classe, da seguinte forma:
```python
resultado = Search.buscar(conteúdo_da_busca, size)
```
A variável size, armazena a quantidade de links que você deseja buscar. O conteúdo da busca deve ser uma string.

### Visitando links
Use o método `visitarLink`, da seguinte forma:
```python
Searchft.visitarLink(link)
```
O link deve ser uma string.
"""
setup(
    name = 'SearchForThis',
    version = VERSION,
    author = 'liedson',
    author_email = 'fabricoliedson@gamil.com',
    description = DESCRIPTION,
    Long_description = LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    packages = ['SearchForThis'],
    python_requires = '>=3.6',
    install_requires = ['googlesearch-python==1.2.3', 'webbrowser'],

    keywords = ['python', 'web', 'search'],
    classifiers = [
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
 
)

# pypi-AgEIcHlwaS5vcmcCJGM1MjY4MWQyLWFhYmEtNDA5ZS05ZDNjLTQxNWY0Mzc3OTM1NwACKlszLCIxZWNkZDA1Yi0zM2VlLTQ4ZDAtOWIxZS05ZjM0NjRkYjFmYjEiXQAABiBCi99wIevAE2UyLF9i1S1QmY3bIn_V4lJyh5XJnnXwvQ