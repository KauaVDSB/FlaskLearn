from flaskLearn import app
from flask import render_template, url_for, request

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

@app.route('/contato/')
def contato():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa': pesquisa})
    return render_template('contato.html', context=context)