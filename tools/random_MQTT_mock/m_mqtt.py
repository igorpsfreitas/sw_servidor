from paho.mqtt import client as mqtt_client

# Configuracao Broker:
broker = '127.0.0.1'
port = 1883
 
client_id = f'python-mqtt-mock'
id = 'mock_interface_sensor'


# Topicos MQTT:
sld = '/nfc/SLD'
mpo = '/nfc/MPO'
hbw = '/nfc/HBW'

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

# Funcao de publicação:
def publish(client: mqtt_client, topic, msg):
    client.publish(topic, msg)
    print('Msg enviada!')


# Teste:
if __name__ == "__main__":
    user = connect_mqtt(id)
    publish(user, hbw, ' Teste - 0')
    publish(user, sld, ' Teste - 1')
    publish(user, mpo, ' Teste - 3')