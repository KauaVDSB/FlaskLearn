from flaskLearn import app, db
from flask import render_template, url_for, request, redirect

from flaskLearn.models import Contato
from flaskLearn.forms import ContatoForm

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
    form = ContatoForm()
    context = {}    
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    print(form.errors) #aponta erro caso não seja validado

    return render_template('contato.html', context=context, form=form)



# Formato não recomendado
@app.route('/contato_old/', methods=['GET', 'POST'])
def contato_old():
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

    return render_template('contato_old.html', context=context)