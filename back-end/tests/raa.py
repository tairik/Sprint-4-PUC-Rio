import warnings
warnings.filterwarnings("ignore")
import unittest
import pandas as pd
from pickle import load
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

class Testing(unittest.TestCase):
    def test_raa(self):
        # Parâmetros
        url_dados = "../database/raa.csv"
        atributos = ['raca', 'idade', 'sexo', 'dieta', 'cocou']

        # Carga dos dados
        dataset = pd.read_csv(url_dados, delimiter=',')

        # Separando em dados de entrada e saída
        X = dataset.iloc[:, 0:-1]
        Y = dataset.iloc[:, -1]

        model_path = '../model.pkl'
        loaded_model = load(open(model_path, 'rb'))

        predicoes = loaded_model.predict(X)
        acuracia_svm, recall_svm, precisao_svm, f1_svm = (accuracy_score(Y, predicoes),
                                                          recall_score(Y, predicoes),
                                                          precision_score(Y, predicoes),
                                                          f1_score(Y, predicoes))

        assert acuracia_svm >= 0.45
        assert recall_svm >= 0.35
        assert precisao_svm >= 0.45
        assert f1_svm >= 0.4

if __name__ == '__main__':
    unittest.main()