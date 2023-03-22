from paho.mqtt import client as mqtt_client
from sqlalchemy.ext.declarative import declarative_base
import json 
import sqlalchemy as db

# Configuracoes de conexao ao broker:
#broker = '127.0.0.1'
broker = 'sensor_broker'
port = 1883
topics = [
    ('/nfc/SLD', 0),
    ('/nfc/MPO', 0),
    ('/nfc/HBW', 0)
    ]

# Configuracoes de conexao ao Banco de dados:
#db_adress = '127.0.0.1'
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

# adicionais:
lista_in_sld = []

# Mapping das Tabelas:
class MPO(base):
    __tablename__ = 'mpo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(length=10))
    uid = db.Column(db.BigInteger)
    result = db.Column(db.String(length=5))
    time = db.Column(db.String(length=10))
    
class SLD(base):
    __tablename__ = 'sld'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(length=10))
    uid = db.Column(db.BigInteger)
    baia = db.Column(db.Integer)
    time = db.Column(db.String(length=10))
    result = db.Column(db.String(length=5))
    
class HBW(base):
    __tablename__ = 'hbw'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(length=10))
    uid = db.Column(db.BigInteger)
    local = db.Column(db.String(length=20))
    baia = db.Column(db.Integer)
    destino = db.Column(db.String(length=20))
    result = db.Column(db.String(length=5))
    time = db.Column(db.String(length=10))
    
# --------------------------------------------------------------------------------------------------------------------------------------- #

# Funcao de conexao ao broker:
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f'Conexao: OK!')
        else:
            print(f'Conexao: FAIL!')

    client = mqtt_client.Client('interface_sensor')
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Funcao de subscriçao SLD:
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            # Decoder UID list to int:
            str_aux = ''
            for i in data['UID']:
                str_aux += str(i)
            data['UID'] = int(str_aux)
            
            # Recebe os dados para o banco:
            match msg.topic:
                
                case '/nfc/MPO':
                    try:
                        engine.execute('ALTER TABLE `mpo` AUTO_INCREMENT = 0')
                        if 'RESULT' in data:
                            newProduto = MPO(
                            status=data['Status'],
                            uid=data['UID'],
                            result=data['RESULT'],
                            time=data['Time_stamp']
                            )
                        else:
                            newProduto = MPO(
                            status=data['Status'],
                            uid=data['UID'],
                            time=data['Time_stamp']
                            )
                        Session.add(newProduto)
                        print(data)
                        Session.commit()
                        print('Dado registrado no banco!')
                    
                    except:
                        print(f'Erro na adição ao Banco de Dados')
                
                case '/nfc/SLD':
                    # Corrigi o erro de nao receber baia na hora da saida:
                    if (data['UID'] in lista_in_sld) and (data['Status'] == 'OUT'):
                        data['baia'] = lista_in_sld[lista_in_sld.index(data['UID']) + 1]
                        del lista_in_sld[lista_in_sld.index(data['UID']) + 1]
                        lista_in_sld.remove(data['UID'])
                    else:
                        lista_in_sld.append(data['UID'])
                        lista_in_sld.append(data['baia'])
                    try:
                        engine.execute('ALTER TABLE `sld` AUTO_INCREMENT = 0')
                        if 'RESULT' in data:
                            newProduto = SLD(
                            status=data['Status'],
                            uid=data['UID'],
                            baia=data['baia'],
                            result=data['RESULT'],
                            time=data['Time_stamp']
                            )
                        else:
                            newProduto = SLD(
                            status=data['Status'],
                            uid=data['UID'],
                            baia=data['baia'],
                            time=data['Time_stamp']
                            )
                        Session.add(newProduto)
                        print(data)
                        Session.commit()
                        print('Dado registrado no banco!')
                    
                    except:
                        print(f'Erro na adição ao Banco de Dados')
                
                case '/nfc/HBW':
                    try:
                        engine.execute('ALTER TABLE `hbw` AUTO_INCREMENT = 0')
                        if data['Local'] == 'Debug_ICT':
                            if 'Result' in data:
                                newProduto = HBW(
                                status=data['Status'],
                                uid=data['UID'],
                                local=data['Local'],
                                baia=data['Baia'],
                                result=data['Result'],
                                destino=data['Destino'],
                                time=data['Time_stamp']
                                )
                            else:
                                newProduto = HBW(
                                status=data['Status'],
                                uid=data['UID'],
                                local=data['Local'],
                                baia=data['Baia'],
                                time=data['Time_stamp']
                                )

                        else:
                            if 'Result' in data:
                                # Corrigi o erro de padronis:
                                if data['Next'] == 'Final':
                                    data['Next'] = 'Saida'
                            
                                newProduto = HBW(
                                status=data['Status'],
                                uid=data['UID'],
                                local=data['Local'],
                                baia=data['Baia'],
                                result=data['Result'],
                                destino=data['Next'],
                                time=data['Time_stamp']
                                )
                            else:
                                newProduto = HBW(
                                status=data['Status'],
                                uid=data['UID'],
                                local=data['Local'],
                                baia=data['Baia'],
                                time=data['Time_stamp']
                                )
                        
                        
                        Session.add(newProduto)
                        print(data)
                        Session.commit()
                        print('Dado registrado no banco!')
                    
                    except:
                        print(f'Erro na adição ao Banco de Dados')
        except:
            print(f'Erro no JSON recebido no topico: {msg.topic}\n Mensagem: {msg.payload.decode()}')
    client.subscribe(topics)
    client.on_message = on_message


# Ativacao:
cliente = connect_mqtt()
subscribe(cliente)
cliente.loop_forever()