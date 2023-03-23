from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
import random

# DataBase configs:
db_adress = '127.0.0.1'  # Desenvolvimento
#db_adress = 'sensor_db' # Produção
db_port = '3306'
db_user = 'foxconn'
db_passwd = 'foxconn'
db_name = 'sensor4.0'


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_passwd}@{db_adress}/{db_name}'
db = SQLAlchemy(app)


# Mapping das Tabelas:
class MPO(db.Model):
    __tablename__ = 'mpo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(length=10))
    uid = db.Column(db.BigInteger)
    result = db.Column(db.String(length=5))
    time = db.Column(db.String(length=10))
    def to_json(self):
        return {
            "id": self.id,
            "Status": self.status,
            "UID": self.uid,
            "RESULT": self.result,
            "Time_stamp": self.time
            }
    
class SLD(db.Model):
    __tablename__ = 'sld'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(length=10))
    uid = db.Column(db.BigInteger)
    baia = db.Column(db.Integer)
    time = db.Column(db.String(length=10))
    result = db.Column(db.String(length=5))
    def to_json(self):
        return {
            "id": self.id,
            "Status": self.status,
            "UID": self.uid,
            "baia": self.baia,
            "Time_stamp": self.time,
            "RESULT": self.result
            }

class HBW(db.Model):
    __tablename__ = 'hbw'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(length=10))
    uid = db.Column(db.BigInteger)
    local = db.Column(db.String(length=20))
    baia = db.Column(db.Integer)
    destino = db.Column(db.String(length=20))
    result = db.Column(db.String(length=5))
    time = db.Column(db.String(length=10))
    def to_json(self):
        return {
            "id": self.id,
            "Status": self.status,
            "UID": self.uid,
            "Local": self.local,
            "Baia": self.baia,
            "RESULT": self.result,
            "Destino": self.destino,
            "Time_stamp": self.time
            }
# ----------------------------------------------------------------------------------------------------------------------------------------- #
# Gera estrutura de envio das querys
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo
    headers = {"Access-Control-Allow-Origin": "*"}

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), headers=headers, status=status, mimetype="application/json")


# Endpoints:

@app.route("/MPO_0A", methods=["GET"])
def mpo_0A():
    mpo_objs_OK = MPO.query.filter_by(result='OK')
    mpo_OK = [mpo.to_json() for mpo in mpo_objs_OK]
    mpo_objs_NOK = MPO.query.filter_by(result='NOK')
    mpo_NOK = [mpo.to_json() for mpo in mpo_objs_NOK]
    
    return gera_response(200, "MPO_0A", [len(mpo_OK), len(mpo_NOK)])

@app.route("/MPO_0B", methods=["GET"])
def mpo_0B():
    def calcula_lista(lista):
        resultado = []
        for item in lista:
            hora = str(item['Time_stamp'][0:2]).zfill(2) + ':00'
            if len(resultado) == 0:
                resultado.append({
                    'x' : hora,
                    'y' : 1})
            else:
                existe_hora=0
                for item in resultado:
                    if item['x'] == hora:
                        item['y'] += 1
                        existe_hora += 1
                if existe_hora == 0:
                    resultado.append({
                    'x' : hora,
                    'y' : 1})
        return resultado
            

    mpo_objs_OK = MPO.query.filter_by(result='OK')
    mpo_OK = [mpo.to_json() for mpo in mpo_objs_OK]
    res_ok = calcula_lista(mpo_OK)

    mpo_objs_NOK = MPO.query.filter_by(result='NOK')
    mpo_NOK = [mpo.to_json() for mpo in mpo_objs_NOK]
    res_nok = calcula_lista(mpo_NOK)
    
    
       
    resposta = [{
        'name' : 'Aprovados',
        'data' : res_ok
        },{
        'name' : 'Reprovados',
        'data' : res_nok
        }]
    
    return gera_response(200, "MPO_0B", resposta)





@app.route("/teste1", methods=["GET"])
def teste():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    #c = random.randint(0, 100)
    #d = random.randint(0, 100)
    f = [a, b]
    return gera_response(200, "teste", f)






if __name__ == "__main__":
    # Criando as tabelas:
    with app.app_context():
        db.create_all()
    
    # Iniciando api
    app.run(host='0.0.0.0')
    