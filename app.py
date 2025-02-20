from flask import Flask,render_template,request,redirect
from tinydb import TinyDB

db=TinyDB('cartoes.json')
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html', titulo="Escolha uma opção")

@app.route('/cadastro')
def Cadastrar():
    return render_template('Cadastro.html', titulo="Cadastre um Cartão")

@app.route('/exibir')
def Exibir():
    valores = []
    for dado in db:
        registro = dict(dado)  # Cria um novo dicionario
        registro["doc_id"] = dado.doc_id  # Adiciona o campo "adoc-id no registro"
        valores.append(registro)  # Cria a lista com todos os dicionarios com o id agora

    return render_template('Exibir.html', titulo="Cartões Cadastrados", dados=valores)

@app.route('/criar', methods=['POST'])
def Criar():

    nome = request.form['nome']
    nmr = request.form['nmr']
    data = request.form['data']
    cvv= request.form['cvv']

    dado = {"Nome":nome,"Nmr":nmr,"Data":data,"cvv":cvv}
    db.insert(dado)

    return redirect('/exibir')

@app.route('/excluir/<id>')
def Excluir(id):
    db.remove(doc_ids=[int(id)])
    return redirect('/exibir')

@app.route('/editar/<id>')
def Editar(id):
    dado = db.get(doc_ids=[int(id)])
    return render_template("editar.html", titulo = 'Editar', id=id, dado = dado[0])
 # 0 para pegar somente o dicionario da lista

@app.route('/alterar/<id>', methods=['POST'])
def Alterar(id):
    nome = request.form['Nome']
    nmr = request.form['nmr']
    data = request.form['data']
    cvv = request.form['cvv']
    db.update({"Nome": nome, "Nmr": nmr, "Data": data,"cvv":cvv}, doc_ids=[int(id)])

    return redirect('/exibir')


if __name__ == '__main__':
    app.run()
