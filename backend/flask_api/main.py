from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
import random

# DataBase configs:
db_adress = 'sensor_db'
db_port = '3306'
db_user = 'foxconn'
db_passwd = 'foxconn'
db_name = 'sensor4.0'


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_passwd}@{db_adress}/{db_name}'
db = SQLAlchemy(app)



# Mapping das Tabelas:
class SLD(db.Model):
    __tablename__ = 'sld'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean, default=True)
    uid = db.Column(db.BigInteger)
    baia = db.Column(db.Integer)
    time = db.Column(db.String(length=10))
    result = db.Column(db.Boolean)
    def to_json(self):
        return {
            "id": self.id,
            "status": self.status,
            "uid": self.uid,
            "baia": self.baia,
            "time": self.time,
            "result": self.result
            }

class MPO(db.Model):
    __tablename__ = 'mpo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean, default=True)
    uid = db.Column(db.BigInteger)
    time = db.Column(db.String(length=10))
    result = db.Column(db.Boolean, default=True)
    def to_json(self):
        return {
            "id": self.id,
            "status": self.status,
            "uid": self.uid,
            "time": self.time,
            "result": self.result
            }


class VGR(db.Model):
    __tablename__ = 'vgr'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean, default=True)
    uid = db.Column(db.BigInteger)
    time = db.Column(db.String(length=10))
    def to_json(self):
        return {
            "id": self.id,
            "status": self.status,
            "uid": self.uid,
            "time": self.time
            }

class HBW(db.Model):
    __tablename__ = 'hbw'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=True)
    uid = db.Column(db.BigInteger)
    baia = db.Column(db.Integer)
    local = db.Column(db.String(length=20))
    destino = db.Column(db.String(length=20))
    time = db.Column(db.String(length=10))
    result = db.Column(db.String(length=20))
    def to_json(self):
        return {
            "id": self.id,
            "status": self.status,
            "uid": self.uid,
            "baia": self.baia,
            "time": self.time,
            "local": self.local,
            "destino": self.destino,
            "result": self.result
            }
# ----------------------------------------------------------------------------------------------------------------------------------------- #


# Criar as tabelas no banco de dados
@app.route("/", methods=["GET"])
def cria_tabelas():
    with app.app_context():
        db.create_all()
    return '<h1>Tabelas criadas com sucesso!!! </h1>'

# Selecionar Tudo
@app.route("/sld", methods=["GET"])
def seleciona_sld():

    sld_objetos = SLD.query.all()
    sld_json = [sld.to_json() for sld in sld_objetos]

    return gera_response(200, "sld", sld_json)
    

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo
    headers = {"Access-Control-Allow-Origin": "*"}

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), headers=headers, status=status, mimetype="application/json")

@app.route("/teste", methods=["GET"])
def teste():
    a = random.randint(0, 100)
    #b = random.randint(0, 100)
    #c = random.randint(0, 100)
    #d = random.randint(0, 100)
    
    return gera_response(200, "teste", a)

if __name__ == "__main__":
    app.run(host='0.0.0.0')