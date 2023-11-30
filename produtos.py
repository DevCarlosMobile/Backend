from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {
        'id': 1,
        'titulo': "Nutri Whey Protein",
        'marca': "Whey",
        'preco': 50
        
    },
    {
        'id': 2,
        'titulo': "Creatina Pura",
        'marca': "Creatina",
        'preco': 60
        
    },
    {
        'id': 3,
        'titulo': "Pré-treino Diabo Verde",
        'marca': "Diabo verde",
        'preco': 80
        
    },
]


@app.route('/produtos')
def obter_produtos():
    return jsonify(produtos)

app.run(port=500,host='localhost',debug=True)

