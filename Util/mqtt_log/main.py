from paho.mqtt import client as mqtt_client
from threading import Thread
import json, datetime

# Configuracoes de conexao ao broker:
broker = '192.168.0.66'
port = 1883

#Callback - mensagem recebida do broker

def registrar_SLD(msg):
    arquivo = open(f'./logs/resgistro.log','a')
    hora = str(datetime.datetime.now())
    cor = str(msg)
    arquivo.write('\n/nfc/SLD:\n')
    arquivo.write(hora[:19] + "\n" + cor +"\n")
    arquivo.close()

    arquivo = open(f'./logs/resgistro_SLD.log','a')
    hora = str(datetime.datetime.now())
    cor = str(msg)
    arquivo.write('\n/nfc/SLD:\n')
    arquivo.write(hora[:19] + "\n" + cor +"\n")
    arquivo.close()

    

def on_message_SLD(client, userdata, msg):
    MensagemRecebida = str(msg.payload.decode())
    registrar_SLD(MensagemRecebida)
    print("[MSG RECEBIDA] Topico: "+msg.topic)

def on_connect_SLD(client, userdata, flags, rc):
    print("conectado ao broke: /nfc/SLD")

    #faz subscribe automatico no topico
    client.subscribe('/nfc/SLD')
 

client_SLD = mqtt_client.Client()
client_SLD.on_connect = on_connect_SLD
client_SLD.on_message = on_message_SLD
client_SLD.connect(broker, port)
th01 = Thread(target=client_SLD.loop_forever)
th01.start()



def registrar_MPO(msg):
    arquivo = open(f'./logs/resgistro.log','a')
    hora = str(datetime.datetime.now())
    cor = str(msg)
    arquivo.write('\n/nfc/MPO:\n')
    arquivo.write(hora[:19] + "\n" + cor +"\n")
    arquivo.close()
    
    arquivo = open(f'./logs/resgistro_MPO.log','a')
    hora = str(datetime.datetime.now())
    cor = str(msg)
    arquivo.write('\n/nfc/MPO:\n')
    arquivo.write(hora[:19] + "\n" + cor +"\n")
    arquivo.close()

def on_message_MPO(client, userdata, msg):
    MensagemRecebida = str(msg.payload.decode())
    registrar_MPO(MensagemRecebida)
    print("[MSG RECEBIDA] Topico: "+msg.topic)

def on_connect_MPO(client, userdata, flags, rc):
    print("conectado ao broke: /nfc/MPO")

    #faz subscribe automatico no topico
    client.subscribe('/nfc/MPO')
 
client_MPO = mqtt_client.Client()
client_MPO.on_connect = on_connect_MPO
client_MPO.on_message = on_message_MPO
client_MPO.connect(broker, port)
th02 = Thread(target=client_MPO.loop_forever)
th02.start()

##################  HBW ######################

def registrar_HBW(msg):
    arquivo = open(f'./logs/resgistro.log','a')
    hora = str(datetime.datetime.now())
    cor = str(msg)
    arquivo.write('\n/nfc/HBW:\n')
    arquivo.write(hora[:19] + "\n" + cor +"\n")
    arquivo.close()

    arquivo = open(f'./logs/resgistro_HBW.log','a')
    hora = str(datetime.datetime.now())
    cor = str(msg)
    arquivo.write('\n/nfc/HBW:\n')
    arquivo.write(hora[:19] + "\n" + cor +"\n")
    arquivo.close()

def on_message_HBW(client, userdata, msg):
    MensagemRecebida = str(msg.payload.decode())
    registrar_HBW(MensagemRecebida)
    print("[MSG RECEBIDA] Topico: "+msg.topic)

def on_connect_HBW(client, userdata, flags, rc):
    print("conectado ao broke: /nfc/HBW")

    #faz subscribe automatico no topico
    client.subscribe('/nfc/HBW')

client_HBW = mqtt_client.Client()
client_HBW.on_connect = on_connect_HBW
client_HBW.on_message = on_message_HBW
client_HBW.connect(broker, port)
th03 = Thread(target=client_HBW.loop_forever)
th03.start()
