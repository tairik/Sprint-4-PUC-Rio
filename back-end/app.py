from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from schemas import *
from flask_cors import CORS
import pandas as pd
from pickle import load

info = Info(title="PetDiet Pets API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
dog_tag = Tag(name="Dog", description="Prever RAA")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

## Sistema PetDiet
##Rotas para os Dogs
@app.post('/raa', tags=[dog_tag],
             responses={"200": RaaSchema, "404": ErrorSchema})
def get_raa(form: RaaPostSchema):

        raca = form.raca
        idade = form.idade
        sexo = form.sexo
        dieta = form.dieta
        cocou = form.cocou

        """Faz a previão para diagnóstico de RAA

        Retorna 1/0 para diagnóstico positivo ou negativo.
        """
        filename = 'model.pkl'
        loaded_model = load(open(filename, 'rb'))

        # Construindo o array
        data = {'raca': [raca],
                'idade': [idade],
                'sexo': [sexo],
                'dieta': [dieta],
                'cocou': [cocou],
                }

        atributos = ['raca', 'idade', 'sexo', 'dieta', 'cocou']
        entrada = pd.DataFrame(data, columns=atributos)

        array_entrada = entrada.values
        X_entrada = array_entrada[:, 0:5].astype(float)

        prediction = loaded_model.predict(X_entrada)  # Passing in variables for prediction
        return {"raa": int(prediction[0])}