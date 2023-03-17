from flask import Flask, request, jsonify
from pymongo import MongoClient
from mongopass import mongopass

app = Flask(__name__)
app.config["DEBUG"] = True

# conexão com o banco de dados
client = MongoClient(mongopass)
db = client.crud   # nome do banco
minhacolecao = db.myCol   # nome da coleção


# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    livros = db.minhacolecao.find()

    return jsonify([livro for livro in livros])


# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    livro = db.minhacolecao.find_one({"_id": id})

    return livro


# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    liv_alt = request.get_json()
    livro_alterado = db.minhacolecao.find_one_and_update(
        {'_id': id},
        {'$set': {'titulo': liv_alt['titulo']}}
        )

    return livro_alterado


# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    db.minhacolecao.insert_one(novo_livro)

    return jsonify(message="adicionado com sucesso")


# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    db.minhacolecao.delete_one({'_id': id})

    return jsonify(message="removido com sucesso")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
