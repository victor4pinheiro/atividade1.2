from flask import Flask, request, render_template
import numpy as np
import pickle

# Criação da aplicação Flask
app = Flask(__name__)

# Carregar o modelo treinado (você precisará salvar o modelo como um arquivo .pkl)
with open('modelo_regressao.pkl', 'rb') as f:
    modelo = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obter o valor de horas de estudo do formulário
    investimento_marketing = float(request.form['investimento_marketing'])

    # Verifica se o atributo existe na requisição
    if 'investimento_marketing' not in request.form:
        return render_template('erro.html')

    # Se estiver vazio, atribua 0 como valor padrão
    if not investimento_marketing:
        investimento_marketing = 0
    
    # Transformar a entrada em um array adequado para o modelo
    investimento_marketing_array = np.array([[investimento_marketing]])
    
    # Fazer a previsão usando o modelo
    previsao_vendas = modelo.predict(investimento_marketing_array)
    
    # Retornar o resultado em HTML
    return render_template('resultado.html', investimento_marketing=investimento_marketing, vendas=previsao_vendas[0])

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=True)
