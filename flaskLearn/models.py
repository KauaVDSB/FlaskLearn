from flaskLearn import db, login_manager
from datetime import datetime
from flask_login import UserMixin, login_user, logout_user, current_user 



@login_manager.user_loader # Retorna sessao do usuario no controle de login
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    sobrenome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    senha = db.Column(db.String, nullable=True)
    data_cadastro = db.Column(db.DateTime, default=datetime.now())


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.now())
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    assunto = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    respondido = db.Column(db.Integer, default=0)

    
class Postagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.now())
    autor = db.Column(db.String, nullable=True)
    titulo = db.Column(db.String, nullable=True)
    conteudo = db.Column(db.String, nullable=True)