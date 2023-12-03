# Pets API

Este pequeno projeto faz parte do MVP do curso de Pós-Gradução em **Engenharia de Software** 

O crescimento do número de cães e gatos em estado de sobrepeso e obesos tem sido uma grande preocupação para Médicos Veterinários especializados em Nutrição e Nutrologia Veterinária que usam tabelas de determinação de Escore de Condição Corporal (ECC).

O produto desenvolvido tem como objetivo prever se o animal terá Reação Alérgica ao Alimento em função da dieta, idade, raça, sexo e análise clínica do cão.

Por fim, para a documentação da API, foi usado Swagger.
---
## Link para Colab: https://colab.research.google.com/drive/1AjynX5aR-y6LMosfu25qL7g4I4IGAuXC#scrollTo=RCn8CH4M7wF-

## Como executar 

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

