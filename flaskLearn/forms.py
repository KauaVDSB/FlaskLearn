from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

# Para validar email, baixar biblioteca email_validator
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


from flaskLearn import db, bcrypt
from flaskLearn.models import User, Contato


# Cadastro de usuario
class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmar senha', validators=[DataRequired, EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    # def com validate propria para verificar se email e unico. 
    def validate_email(self, email): # Ao dar submit, ele procura todas as def que comecam com 'validate_'.
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