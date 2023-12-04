# RAA - API

Para a documentação da API, foi usado Swagger.

## Como executar o Back-End

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

## Execução local

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenpython -m venv .v.pypa.io/en/latest/).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API basta lançar o seguinte comando no terminal:

```
(env)$ flask run --host 0.0.0.0 --port 4000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 4000 --reload
```

Abra o [http://localhost:4000/#/](http://localhost:4000/#/) no navegador para verificar o status da API em execução.

