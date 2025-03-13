from flaskLearn import app, db
from flask import render_template, url_for, request, redirect
from flask_login import login_user, logout_user, current_user, login_required

from flaskLearn.models import Contato, Postagem, Post, User
from flaskLearn.forms import UserForm, AlterUserForm, AdminForm, LoginForm, ContatoForm, PostagemForm, PostForm, PostComentariosForm


# Rota para homepage
@app.route('/')
def homepage():
    dados = Postagem.query.order_by('id')

    context = {'dados': dados.all()}

    return render_template('index.html', context=context)


# Dashboard usuario
@app.route('/dashboard/', methods=['GET', 'POST'])
@login_required                 # Exige login do usuário.
def dashboard():
    lenPosts = len(current_user.posts)
    obj = User.query.get(current_user.id)
    form = AlterUserForm()
    admform = AdminForm()
    context = {
        'lenPosts': lenPosts
    }
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('dashboard'))
    if admform.validate_on_submit():
        admform.save()
        return redirect(url_for('dashboard'))
    return render_template('login/dashboard.html', obj=obj, context=context, form=form, admform=admform)


# Rota para cadastro de usuario
@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
    form = UserForm()
    context = {}
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    print(form.errors) #aponta erro caso não seja validado

    return render_template('login/cadastro.html', context=context, form=form)


# Rota para login do usuário
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    print(form.errors) #aponta erro caso não seja validado
    return render_template('login/login.html', form=form)


# Rota para logout
@app.route('/sair/')
@login_required                 # Exige login do usuário.
def logout():
    logout_user()
    return redirect(url_for('homepage'))


# Rota para Post Novo
@app.route('/post/novo/', methods=['GET', 'POST'])
@login_required                 # Exige login do usuário.
def postNovo():
    form = PostForm()
    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('postLista'))
    return render_template('posts/post_novo.html', form=form)


@app.route('/post/lista/')
def postLista():
    posts = Post.query.all()
    return render_template('posts/post_lista.html', posts=posts)


@app.route('/post/<int:id>/', methods=['GET', 'POST'])
@login_required                 # Exige login do usuário.
def postDetail(id):
    obj = Post.query.get(id)
    lenComentarios = len(obj.comentarios)
    form = PostComentariosForm()
    context = {
        'lenComentarios': lenComentarios
    }
    if form.validate_on_submit():
        form.save(current_user.id, id)
        return redirect(url_for('postDetail', id=id))

    return render_template('posts/post_detail.html', obj=obj, form=form, context=context)




# Rota para o editor do blog
@app.route('/blog/editor/', methods=['GET', 'POST'])
@login_required                 # Exige login do usuário.
def editorBlog():
    if current_user.admin == False:
        return redirect(url_for('homepage'))
    form = PostagemForm()
    context = {}    
    if form.validate_on_submit():
        form.salvar()
        print("oi")
        return redirect(url_for('homepage'))
    print(form.errors) #aponta erro caso não seja validado

    return render_template('blog/editor-blog.html', context=context, form=form)


# Rota para postagem específica
@app.route('/blog/postagem/<int:id>/')
@login_required                 # Exige login do usuário.
def detailBlog(id):
    obj = Postagem.query.get(id)

    return render_template('blog/detail-blog.html', obj=obj)





# Rota para contato do usuario
@app.route('/contato/', methods=['GET', 'POST'])
@login_required                 # Exige login do usuário.
def contato():
    form = ContatoForm()
    context = {}    
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('contatoLista'))
    print(form.errors) #aponta erro caso não seja validado

    return render_template('contato/contato.html', context=context, form=form)


# Rota para lista de contatos dos usuarios
@app.route('/contato/lista/')
@login_required                 # Exige login do usuário.
def contatoLista():

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '') #Caso nao ache informacao correspondente, retorna nulo.

    dados = Contato.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa) #Filtra a coluna nome para receber nomes iguais a pesquisa.

    context = {'dados': dados.all()}

    return render_template('contato/contato_lista.html', context=context)


# Rota para informacoes de um contato especifico de usuario
@app.route('/contato/<int:id>/')
@login_required                 # Exige login do usuário.
def contatoDetail(id):
    obj = Contato.query.get(id)
    
    return render_template('contato/contato_detail.html', obj=obj)



#------------------------------------------------------------

@app.route('/amor/')
@login_required                 # Exige login do usuário.
def amor():
    user = "heloísa"
    namorado = "kauã"

    context = {
        'user': user,
        'namorado': namorado
    }
    return render_template('misc/amor.html', context=context)


# Formato não recomendado
@app.route('/contato_old/', methods=['GET', 'POST'])
@login_required                 # Exige login do usuário.
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

    return render_template('misc/contato_old.html', context=context)