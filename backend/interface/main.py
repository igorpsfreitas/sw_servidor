from paho.mqtt import client as mqtt_client
from threading import Thread
from sqlalchemy.ext.declarative import declarative_base
import json 
import sqlalchemy as db
from log import registrar

# Configuracoes de conexao ao broker:
broker = 'sensor_broker'
port = 1883
id_sld = 'interface_sensor-SLD'
id_mpo = 'interface_sensor-MPO'
id_hbw = 'interface_sensor-HBW'
id_vgr = 'interface_sensor-VGR'

# Configuracoes de conexao ao Banco de dados:
db_adress = 'sensor_db'
db_port = '3306'
db_user = 'root'
db_passwd = '15031989'
db_name = 'sensor4.0'

engine = db.create_engine(f'mysql+pymysql://{db_user}:{db_passwd}@{db_adress}/{db_name}')
base = declarative_base()

# DataBase session configs:
Session = db.orm.sessionmaker()
Session.configure(bind=engine)
Session = Session()


# Mapping das Tabelas:
class SLD(base):
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

class MPO(base):
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

class HBW(base):
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

class VGR(base):
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

# --------------------------------------------------------------------------------------------------------------------------------------- #

# Funcao de conexao ao broker:
def connect_mqtt(client_id):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f'Conexao "{client_id}": OK!')
        else:
            print(f'Conexao "{client_id}": FAIL!')

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Funcao de subscriçao SLD:
def subscribe_sld(client: mqtt_client, topic: str()):
    def on_message(client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            registrar(data)
            #print(data)
            
            # Tratamento dos dados MQTT:
            if (data['Status'] == "OUT"):
                data['Status'] = False
            else:
                data['Status'] = True

            try:            
                str_aux = ''
                for i in data['UID']:
                    str_aux += str(i)
                data['UID'] = int(str_aux)
            except:
                data['UID'] = 404
            if 'RESULT' in data:
                if (data['RESULT'] == "NOK"):
                    data['RESULT'] = False
                elif (data['RESULT'] == "OK"):
                    data['RESULT'] = True
                
            #print(data)

            # Insercao ao Banco de dados:
            try:
                engine.execute('ALTER TABLE `sld` AUTO_INCREMENT = 0')
                if 'RESULT' in data:
                    newProduto = SLD(
                    status=data['Status'],
                    uid=data['UID'],
                    time=data['Time_stamp'],
                    result=data['RESULT']
                    )
                else:
                    newProduto = SLD(
                    status=data['Status'],
                    uid=data['UID'],
                    time=data['Time_stamp']
                    )
                Session.add(newProduto)
                print('Dado registrado no banco!')
                print(data)
                Session.commit()
            
            except:
                print(f'Erro na adição ao Banco de Dados')


        except:
            print(f'Erro no JSON recebido no topico: "SLD"\n Mensagem: {msg.payload.decode()}')

    client.subscribe(topic)
    client.on_message = on_message


# Funcao de subscricao MPO:
def subscribe_mpo(client: mqtt_client, topic: str()):
    def on_message(client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            print(data)
            # Incersao no banco:

            # Falta implementar

        except:
            print(f'Erro no JSON recebido no topico: "MPO"\n Mensagem: {msg.payload.decode()}')

    client.subscribe(topic)
    client.on_message = on_message

# Funcao de subscricao HBW:
def subscribe_hbw(client: mqtt_client, topic: str()):
    def on_message(client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            print(data)
            # Incersao no banco:

            # Falta implementar

        except:
            print(f'Erro no JSON recebido no topico: "HBW"\n Mensagem: {msg.payload.decode()}')

    client.subscribe(topic)
    client.on_message = on_message

# Funcao de subscricao VGR:
def subscribe_vgr(client: mqtt_client, topic: str()):
    def on_message(client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            print(data)
            # Incersao no banco:

            # Falta implementar

        except:
            print(f'Erro no JSON recebido no topico: "vgr"\n Mensagem: {msg.payload.decode()}')

    client.subscribe(topic)
    client.on_message = on_message




# Ativacao:

# SLD:
cliente_SLD = connect_mqtt(id_sld)
subscribe_sld(cliente_SLD, '/nfc/SLD')
th_sld = Thread(target=cliente_SLD.loop_forever)
th_sld.start()
# MPO:
cliente_MPO = connect_mqtt(id_mpo)
subscribe_mpo(cliente_MPO, '/nfc/MPO')
th_MPO = Thread(target=cliente_MPO.loop_forever)
th_MPO.start()
# HBW:
cliente_HBW = connect_mqtt(id_hbw)
subscribe_hbw(cliente_HBW, '/nfc/HBW')
th_HBW = Thread(target=cliente_HBW.loop_forever)
th_HBW.start()
# VGR:
cliente_VGR = connect_mqtt(id_vgr)
subscribe_vgr(cliente_VGR, '/nfc/VGR')
th_vgr = Thread(target=cliente_VGR.loop_forever)
th_vgr.start()