import datetime

def registrar(msg):
    arquivo = open(f'./logs/resgistro.log','a')
    hora = str(datetime.datetime.now())
    cor = str(msg)
    arquivo.write(hora[:19] + "\n" + cor +"\n")
    arquivo.close()
