import random
from paho.mqtt import client as mqtt_client
from datetime import time
from time import sleep


# Configuracao Broker:
broker = '127.0.0.1'
port = 1883
 
client_id = f'python-mqtt-mock'
id_sld = 'mock_interface_sensor-SLD'
id_mpo = 'mock_interface_sensor-MPO'
id_hbw = 'mock_interface_sensor-HBW'
id_vgr = 'mock_interface_sensor-VGR'

# Topicos MQTT:
topic_sld = '/nfc/SLD'
topic_mpo = '/nfc/MPO'
topic_hbw = '/nfc/HBW'
topic_vgr = '/nfc/VGR'

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

# Funcao de publicacao SLD:
def publish_sld(client: mqtt_client, msg):
    client.publish(topic_sld, msg)
    print('Msg enviada!')

# Gera hora randomicamente
def time_random(tempo_atual: str, segundos_adicionais = random.randrange(30, 350)):
    hh = int(tempo_atual[0:2])
    mm = int(tempo_atual[3:5])
    ss = int(tempo_atual[6:])

    ss += segundos_adicionais
    
    if ss >= 60:
        aux_ss = ss/60
        ss = int(60 * (aux_ss - int(aux_ss)))
        mm += int(aux_ss)

    if mm >= 60:
        aux_mm = mm/60
        mm = int(60 * (aux_mm - int(aux_mm)))
        hh += int(aux_mm)

    if hh >= 24:
        aux_hh = mm/24
        hh = int(24 * (aux_hh - int(aux_hh)))


    print(time(hh, mm, ss))
    #return [hh, mm, ss]
    return str(time(hh, mm, ss))


# loop
def loop_time(tempo = "00:00:00"):
    while True:
        tempo = time_random(tempo)
        sleep(0.1)




# Prenchimento auto do SLD
def run(cliente):
    
    status = ['"OUT"', '"IN"']
    st = 0
    
    id_01 = 0
    id_02 = 0
    tempo = "00:00:00"
    while True:

        msg = '{ "Status": ' + status[st] + ', "UID": '+ f'[4, 192, 168, 66, 239, {id_01}, {id_02}] ' +', "Time_stamp": ' + f'"{tempo}"'
        if st == 0:
            st = 1
            # Procentagem de erro
            if random.randint(0, 100) >= 10:
                msg += ', "RESULT": "OK" }'
            else:
                msg += ', "RESULT": "NOK" }'
            id_02 += 1
            if id_02 >= 255:
                id_01 += 1
                id_02 = 0
        else:
            st = 0
            msg += ' }'
    
        publish_sld(client_sld, msg)
        tempo = time_random(tempo)
        print(msg)
        sleep(1)



if __name__ == '__main__':
    client_sld = connect_mqtt(id_sld)
    run(client_sld)
    #loop_time()
