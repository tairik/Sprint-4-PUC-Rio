# RAA - API / Front-End

Este pequeno projeto faz parte do MVP do curso de Pós-Gradução em **Engenharia de Software** 

Com o avanço da Medicina Veterinária e os cães se tornando cada vez mais um membro da família, há um cuidado bastante importante com a saúde dos pets. 
Dentre muitas doenças que levam a sintomas cutâneos e/ou gastrointestinais, a Reação Adversa ao Alimento (RAA) é uma delas. A RAA pode acontecer como uma reação imunológica à proteína que o cão ingere através da alimentação causando uma espécie de reação alérgica. Como descrito em literatura, não há predisposição de sexo mas racial, algumas raças tem maior predisposição que outras, e etária - acomete cães com menos de 1 ano e após 4-5 anos. 

O produto desenvolvido tem como objetivo prever se o animal terá RAA em função da dieta, idade, raça, sintoma gastrointestinal e/ou cutâneo (análise clínica do cão) sendo um ferramenta preditiva bastante importante para o início da triagem pelo médico veterinário nutrólogo. 

Por fim, para a documentação da API, foi usado Swagger.
---
## Link para Colab: https://colab.research.google.com/drive/1AjynX5aR-y6LMosfu25qL7g4I4IGAuXC#scrollTo=RCn8CH4M7wF-

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

## Como executar o Front-End

Fazer o clone do projeto localmente e abrir o arquivo index.html que se encontra dentro da pasta "front-end" no seu browser.

