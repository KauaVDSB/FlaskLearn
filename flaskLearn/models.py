from flaskLearn import db, login_manager
from datetime import datetime
from flask_login import UserMixin, login_user, logout_user, current_user 



@login_manager.user_loader # Retorna sessao do usuario no controle de login
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    nome = db.Column(db.String, nullable=True)
    sobrenome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    senha = db.Column(db.String, nullable=True)
    data_cadastro = db.Column(db.DateTime, default=datetime.now())
    posts = db.relationship('Post', backref='user', lazy=True) #É a tabela referenciada. (um usuario pode ter varios posts)
    post_comentarios = db.relationship('PostComentarios', backref='user', lazy=True) #É a tabela referenciada. (um usuario pode ter varios posts)

    def alt_nome(self, alt_user, novo_nome):
        alt_user.nome = novo_nome

        db.session.commit()

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


# Testando relação entre tabelas:

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.now())
    titulo = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) #Tabela que referencia a tabela usuário
    comentarios = db.relationship('PostComentarios', backref='post', lazy=True) #É a tabela referenciada. (um usuario pode ter varios posts)



    def msg_resumo(self):
        len_msg = len(self.mensagem)
        if len_msg > 10:
            return f"{self.mensagem[:10]} ..."
        else:
            return self.mensagem
        
    def data_resumo(self):
        return str(self.data_criacao)[:16]


class PostComentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.now())
    comentario = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=True)
    
    def data_resumo(self):
        return str(self.data_criacao)[:10]