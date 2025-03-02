from flaskLearn import app, db
from flask import render_template, url_for, request

from flaskLearn.models import Contato

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/nova/')
def novapag():
    user = "heloísa"
    namorado = "kauã"

    context = {
        'user': user,
        'namorado': namorado
    }
    return render_template('amor.html', context=context)

@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET:', pesquisa)
        context.update({'pesquisa': pesquisa})

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        db.session.add(contato)
        db.session.commit()

    return render_template('contato.html', context=context)