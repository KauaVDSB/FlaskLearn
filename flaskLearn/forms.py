from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField

# Para validar email, baixar biblioteca email_validator
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from flask_login import current_user

from flaskLearn import db, bcrypt
from flaskLearn.models import User, Contato, Postagem, Post, PostComentarios


# Cadastro de usuario
class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    # def com validate propria para verificar se email e unico. 
    def validade_email(self, email): # Ao dar submit, ele procura todas as def que comecam com 'validade_'.
        if User.query.filter(email=email.data).first():
            return ValidationError('Usuário já cadastrado com este E-mail.')


    # Cadastro no banco de dados
    def save(self):
        # gera hash para senha criptografada que permite caracteres especiais.
        senha =  bcrypt.generate_password_hash(self.senha.data.encode('utf-8')) 

        user = User(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha
        )

        # salva o usuario na sessão e passa para o banco de dados
        db.session.add(user)
        db.session.commit()
        return user


class AlterUserForm(FlaskForm):
    nome = StringField('Nome')
    sobrenome = StringField('Sobrenome')
    email = StringField('E-mail', validators=[Email()])
    senha = PasswordField('Senha')
    confirmacao_senha = PasswordField('Confirmar senha', validators=[EqualTo('senha')])
    btnSubmit = SubmitField('Salvar alterações')

    def save(self):
        alt_user = User.query.filter_by(id=current_user.id).first()
        
        if self.nome.data:
            alt_user.nome = self.nome.data
        if self.sobrenome.data:
            alt_user.sobrenome = self.sobrenome.data
        if self.email.data:
            alt_user.email = self.email.data
        if self.senha.data:
            alt_user.senha = self.senha.data
        

        db.session.commit()


# Login do usuario
class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Login')

    def login(self):
        # recuperar usuario do email
        user = User.query.filter_by(email=self.email.data).first()

        # verificar se a senha é valida
        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                # Retorna o usuario
                return user
            else:
                raise Exception('Senha incorreta.')
        else:
            raise Exception('Usuário não encontrado.')

    
# Postagem do admin
class PostagemForm(FlaskForm):
    autor = StringField('Autor', validators=[DataRequired()])
    titulo = StringField('Titulo', validators=[DataRequired()])
    conteudo = StringField('Conteudo')
    btnSubmit = SubmitField('Vai')

    def salvar(self):
        post = Postagem(
            autor = self.autor.data,
            titulo = self.titulo.data,
            conteudo = self.conteudo.data
        )

        db.session.add(post)
        db.session.commit()
        print(post)


# Contato do usuario
class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(contato)
        db.session.commit()

# Post do usuario com banco relacional
class PostForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id):
        post = Post(
            titulo=self.titulo.data,
            mensagem=self.mensagem.data,
            user_id=user_id            
        )

        db.session.add(post)
        db.session.commit()


class PostComentariosForm(FlaskForm):
    comentario = TextAreaField('Comentario', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id, post_id):
        post_comentarios = PostComentarios(
            comentario=self.comentario.data,
            user_id=user_id,
            post_id=post_id
        )

        db.session.add(post_comentarios)
        db.session.commit()
        
