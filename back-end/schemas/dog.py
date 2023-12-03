from pydantic import BaseModel

class RaaSchema(BaseModel):
    """ Define como uma previsão para diagnóstico de RAA será apresentada
    """
    raa: int = 1

class RaaPostSchema(BaseModel):
    """ Define como os parâmetros devem ser passados para o modelo de ML
    """
    raca: int = 1
    idade: int = 3
    sexo: int = 0
    dieta: int = 1
    cocou: int = 1

