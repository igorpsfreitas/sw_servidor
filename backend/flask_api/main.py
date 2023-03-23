from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
import json


# DataBase configs:
#db_adress = '127.0.0.1'  # Desenvolvimento
db_adress = 'sensor_db' # Produção
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

#------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------------
@app.route("/SLD_0B", methods=["GET"])
def sld_0B():
    p1_ok = 0
    p2_ok = 0
    p3_ok = 0
    p1_nok = 0
    p2_nok = 0
    p3_nok = 0

    for i in range(3):
        p1b1_ok = SLD.query.filter_by(result='OK', baia = i)
        p1_ok += len([sld.to_json() for sld in p1b1_ok])

    for i in range(3):
        p2b1_ok = SLD.query.filter_by(result='OK', baia = i + 3)
        p2_ok += len([sld.to_json() for sld in p2b1_ok])
        
        
    for i in range(3):
        p3b1_ok = SLD.query.filter_by(result='OK', baia = i + 6)
        p3_ok += len([sld.to_json() for sld in p3b1_ok])


    for i in range(3):
        p1b1_nok = SLD.query.filter_by(result='NOK', baia = i)
        p1_nok += len([sld.to_json() for sld in p1b1_nok])

    for i in range(3):
        p2b1_nok = SLD.query.filter_by(result='NOK', baia = i + 3)
        p2_nok += len([sld.to_json() for sld in p2b1_nok])
        
    for i in range(3):
        p3b1_nok = SLD.query.filter_by(result='NOK', baia = i + 6)
        p3_nok += len([sld.to_json() for sld in p3b1_nok])

    resposta = [{
        'name' : 'Aprovados',
        'data' : [{
            "x" : "Posto-01",
            "y" : p1_ok
        },{
            "x" : "Posto-02",
            "y" : p2_ok
        },{
            "x" : "Posto-03",
            "y" : p3_ok
        },]
        },{
        'name' : 'Reprovados',
        'data' : [{
            "x" : "Posto-01",
            "y" : p1_nok
        },{
            "x" : "Posto-02",
            "y" : p2_nok
        },{
            "x" : "Posto-03",
            "y" : p3_nok
        },]
        }]
    
    return gera_response(200, "SLD_0B", resposta)

#---------------------------------------
@app.route("/SLD_0C", methods=["GET"])
def sdl_0C():
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
            

    sld_objs_OK = SLD.query.filter_by(result='OK')
    sld_OK = [sld.to_json() for sld in sld_objs_OK]
    res_ok = calcula_lista(sld_OK)

    sld_objs_NOK = SLD.query.filter_by(result='NOK')
    sld_NOK = [sld.to_json() for sld in sld_objs_NOK]
    res_nok = calcula_lista(sld_NOK)
           
    resposta = [{
        'name' : 'Aprovados',
        'data' : res_ok
        },{
        'name' : 'Reprovados',
        'data' : res_nok
        }]
    
    return gera_response(200, "SLD_0C", resposta)
#-----------------------------------------------------------------------

@app.route("/SLD_DEBUG", methods=["GET"])
def sdl_debug():
    sld_deb_objs_OK = HBW.query.filter_by(result='OK', local='Debug_FT')
    sld_deb_OK = [sld_deb.to_json() for sld_deb in sld_deb_objs_OK]
    
    sld_deb_objs_NOK = HBW.query.filter_by(result='NOK', local='Debug_FT')
    sld_deb_NOK = [sld_deb.to_json() for sld_deb in sld_deb_objs_NOK]
    
    return gera_response(200, "SLD_DEBUG", [len(sld_deb_OK), len(sld_deb_NOK)])
# -------------------------------------------------------------------------------------

@app.route("/SLD_DEBUG_2", methods=["GET"])
def sdl_debug_2():
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
            
    debug_ok = []
    for i in range(3):
        debug_obj = HBW.query.filter_by(result='OK', local='Debug_FT', baia = i)
        debug_ok += [hbw.to_json() for hbw in debug_obj]
    res_ok = calcula_lista(debug_ok)
        
    debug_nok = []
    for i in range(3):
        debug_obj = HBW.query.filter_by(result='NOK', local='Debug_FT', baia = i)
        debug_nok += [hbw.to_json() for hbw in debug_obj]
    res_nok = calcula_lista(debug_nok)
      
    resposta = [{
        'name' : 'Aprovados',
        'data' : res_ok
        },{
        'name' : 'Scrap',
        'data' : res_nok
        }]
    
    return gera_response(200, "SLD_DEBUG_2", resposta)

# ---------------------------------------------------------------------------------------
@app.route("/MPO_DEBUG", methods=["GET"])
def mpo_debug():
    mpo_deb_objs_OK = HBW.query.filter_by(result='OK', local='Debug_ICT')
    mpo_deb_OK = [mpo_deb.to_json() for mpo_deb in mpo_deb_objs_OK]
    
    mpo_deb_objs_NOK = HBW.query.filter_by(result='NOK', local='Debug_ICT')
    mpo_deb_NOK = [mpo_deb.to_json() for mpo_deb in mpo_deb_objs_NOK]
    
    return gera_response(200, "MPO_DEBUG", [len(mpo_deb_OK), len(mpo_deb_NOK)])

#------------------------------------------------------------------------------------------
@app.route("/MPO_DEBUG_2", methods=["GET"])
def mpo_debug_2():
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
            
    debug_ok = []
    for i in range(3):
        debug_obj = HBW.query.filter_by(result='OK', local='Debug_ICT', baia = i)
        debug_ok += [hbw.to_json() for hbw in debug_obj]
    res_ok = calcula_lista(debug_ok)
        
    debug_nok = []
    for i in range(3):
        debug_obj = HBW.query.filter_by(result='NOK', local='Debug_ICT', baia = i)
        debug_nok += [hbw.to_json() for hbw in debug_obj]
    res_nok = calcula_lista(debug_nok)
      
    resposta = [{
        'name' : 'Aprovados',
        'data' : res_ok
        },{
        'name' : 'Scrap',
        'data' : res_nok
        }]
    
    return gera_response(200, "MPO_DEBUG_2", resposta)

# ----------------------------------------------------------------------------------------

@app.route("/MPO_0C", methods=["GET"])
def mpo_0c():
    def convert_sec(time):
        hora = int(time[0:2])
        minuto = int(time[3:5])
        sec = int(time[6:])
        return sec + minuto * 60 + hora * 3600

    def diferenca(a, b):
        if a >= b:
            return a - b
        else:
            return b - a

    def cal(a, b):
        horaA = convert_sec(a)
        horaB = convert_sec(b)
        return diferenca(horaA, horaB)
    
    def ocupacao(lista):
        resultado = []
        for item in lista:
            y = []
            if item['Status'] == 'IN':
                a = item['Time_stamp']
            else:
                b = item['Time_stamp']
                hora = b[:2] + ':00'
                
                if len(resultado) == 0:
                    ca = cal(a,b)
                    y.append(ca)
                    resultado.append({
                        'x' : hora,
                        'y' : y
                        })
                else:
                    existe_hora=0
                    for item in resultado:
                        if item['x'] == hora:
                            item['y'].append(cal(a, b))
                            existe_hora += 1
                    if existe_hora == 0:
                        resultado.append({
                        'x' : hora,
                        'y' : [cal(a,b)]})

        for lis in resultado:
            value = sum(lis['y']) / len(lis['y'])
            lis['y'] = float(f'{value:.1f}')
        
        return resultado
    
    def espera(lista):
        resultado = []
        a = 0
        for item in lista:
            y = []
            if item['Status'] == 'OUT':
                a = item['Time_stamp']
            elif a != 0 and item['Time_stamp'][:2] == a[:2]:
                b = item['Time_stamp']
                hora = b[:2] + ':00'
                
                if len(resultado) == 0:
                    ca = cal(a,b)
                    y.append(ca)
                    resultado.append({
                        'x' : hora,
                        'y' : y
                        })
                else:
                    existe_hora=0
                    for item in resultado:
                        if item['x'] == hora:
                            item['y'].append(cal(a, b))
                            existe_hora += 1
                    if existe_hora == 0:
                        resultado.append({
                        'x' : hora,
                        'y' : [cal(a,b)]})

        for lis in resultado:
            value = sum(lis['y']) / len(lis['y'])
            lis['y'] = float(f'{value:.2f}')
        
        return resultado
     
    mpo_obj = MPO.query.all()
    mpo_list = [mpo.to_json() for mpo in mpo_obj]

    mpo_ocupacao = ocupacao(mpo_list)
    mpo_espera = espera(mpo_list)

    resposta = [{
        'name' : 'Ocupado',
        'data' : mpo_ocupacao},
        {
        'name' : 'Espera',
        'data' : mpo_espera}]

    return gera_response(200, "MPO_0C", resposta)
#------------------------------------------------------------------------

@app.route("/SLD_0D_1", methods=["GET"])
def sld_0d_1():
    def convert_sec(time):
        hora = int(time[0:2])
        minuto = int(time[3:5])
        sec = int(time[6:])
        return sec + minuto * 60 + hora * 3600

    def diferenca(a, b):
        if a >= b:
            return a - b
        else:
            return b - a

    def cal(a, b):
        horaA = convert_sec(a)
        horaB = convert_sec(b)
        return diferenca(horaA, horaB)
    
    def ocupacao(lista):
        resultado = []
        for item in lista:
            y = []
            if item['Status'] == 'IN':
                a = item['Time_stamp']
            else:
                b = item['Time_stamp']
                hora = b[:2] + ':00'
                
                if len(resultado) == 0:
                    ca = cal(a,b)
                    y.append(ca)
                    resultado.append({
                        'x' : hora,
                        'y' : y
                        })
                else:
                    existe_hora=0
                    for item in resultado:
                        if item['x'] == hora:
                            item['y'].append(cal(a, b))
                            existe_hora += 1
                    if existe_hora == 0:
                        resultado.append({
                        'x' : hora,
                        'y' : [cal(a,b)]})

        for lis in resultado:
            value = sum(lis['y']) / len(lis['y'])
            lis['y'] = float(f'{value:.1f}')
        
        return resultado
    
    def espera(lista):
        resultado = []
        a = 0
        for item in lista:
            y = []
            if item['Status'] == 'OUT':
                a = item['Time_stamp']
            elif a != 0 and item['Time_stamp'][:2] == a[:2]:
                b = item['Time_stamp']
                hora = b[:2] + ':00'
                
                if len(resultado) == 0:
                    ca = cal(a,b)
                    y.append(ca)
                    resultado.append({
                        'x' : hora,
                        'y' : y
                        })
                else:
                    existe_hora=0
                    for item in resultado:
                        if item['x'] == hora:
                            item['y'].append(cal(a, b))
                            existe_hora += 1
                    if existe_hora == 0:
                        resultado.append({
                        'x' : hora,
                        'y' : [cal(a,b)]})

        for lis in resultado:
            value = sum(lis['y']) / len(lis['y'])
            lis['y'] = float(f'{value:.2f}')
        
        return resultado
    
    p1 = []
    for i in range(3):
        p1_dd = SLD.query.filter_by(baia = i)
        p1 += [sld.to_json() for sld in p1_dd]
    

    sld_p1_ocupacao = ocupacao(p1)
    sld_p1_espera = espera(p1)


    resposta = [{
        'name' : 'Ocupado',
        'data' : sld_p1_ocupacao},
        {
        'name' : 'Espera',
        'data' : sld_p1_espera}]

    return gera_response(200, "SLD_0D_1", resposta)
#------------------------------------------------------------------------

@app.route("/SLD_0D_2", methods=["GET"])
def sld_0d_2():
    def convert_sec(time):
        hora = int(time[0:2])
        minuto = int(time[3:5])
        sec = int(time[6:])
        return sec + minuto * 60 + hora * 3600

    def diferenca(a, b):
        if a >= b:
            return a - b
        else:
            return b - a

    def cal(a, b):
        horaA = convert_sec(a)
        horaB = convert_sec(b)
        return diferenca(horaA, horaB)
    
    def ocupacao(lista):
        resultado = []
        for item in lista:
            y = []
            if item['Status'] == 'IN':
                a = item['Time_stamp']
            else:
                b = item['Time_stamp']
                hora = b[:2] + ':00'
                
                if len(resultado) == 0:
                    ca = cal(a,b)
                    y.append(ca)
                    resultado.append({
                        'x' : hora,
                        'y' : y
                        })
                else:
                    existe_hora=0
                    for item in resultado:
                        if item['x'] == hora:
                            item['y'].append(cal(a, b))
                            existe_hora += 1
                    if existe_hora == 0:
                        resultado.append({
                        'x' : hora,
                        'y' : [cal(a,b)]})

        for lis in resultado:
            value = sum(lis['y']) / len(lis['y'])
            lis['y'] = float(f'{value:.1f}')
        
        return resultado
    
    def espera(lista):
        resultado = []
        a = 0
        for item in lista:
            y = []
            if item['Status'] == 'OUT':
                a = item['Time_stamp']
            elif a != 0 and item['Time_stamp'][:2] == a[:2]:
                b = item['Time_stamp']
                hora = b[:2] + ':00'
                
                if len(resultado) == 0:
                    ca = cal(a,b)
                    y.append(ca)
                    resultado.append({
                        'x' : hora,
                        'y' : y
                        })
                else:
                    existe_hora=0
                    for item in resultado:
                        if item['x'] == hora:
                            item['y'].append(cal(a, b))
                            existe_hora += 1
                    if existe_hora == 0:
                        resultado.append({
                        'x' : hora,
                        'y' : [cal(a,b)]})

        for lis in resultado:
            value = sum(lis['y']) / len(lis['y'])
            lis['y'] = float(f'{value:.2f}')
        
        return resultado
    
    p2 = []
    for i in range(3):
        p2_dd = SLD.query.filter_by(baia = i + 3)
        p2 += [sld.to_json() for sld in p2_dd]
    

    sld_p2_ocupacao = ocupacao(p2)
    sld_p2_espera = espera(p2)


    resposta = [{
        'name' : 'Ocupado',
        'data' : sld_p2_ocupacao},
        {
        'name' : 'Espera',
        'data' : sld_p2_espera}]

    return gera_response(200, "SLD_0D_2", resposta)
#------------------------------------------------------------------------

@app.route("/SLD_0D_3", methods=["GET"])
def sld_0d_3():
    def convert_sec(time):
        hora = int(time[0:2])
        minuto = int(time[3:5])
        sec = int(time[6:])
        return sec + minuto * 60 + hora * 3600

    def diferenca(a, b):
        if a >= b:
            return a - b
        else:
            return b - a

    def cal(a, b):
        horaA = convert_sec(a)
        horaB = convert_sec(b)
        return diferenca(horaA, horaB)
    
    def ocupacao(lista):
        resultado = []
        for item in lista:
            y = []
            if item['Status'] == 'IN':
                a = item['Time_stamp']
            else:
                b = item['Time_stamp']
                hora = b[:2] + ':00'
                
                if len(resultado) == 0:
                    ca = cal(a,b)
                    y.append(ca)
                    resultado.append({
                        'x' : hora,
                        'y' : y
                        })
                else:
                    existe_hora=0
                    for item in resultado:
                        if item['x'] == hora:
                            item['y'].append(cal(a, b))
                            existe_hora += 1
                    if existe_hora == 0:
                        resultado.append({
                        'x' : hora,
                        'y' : [cal(a,b)]})

        for lis in resultado:
            value = sum(lis['y']) / len(lis['y'])
            lis['y'] = float(f'{value:.1f}')
        
        return resultado
    
    def espera(lista):
        resultado = []
        a = 0
        for item in lista:
            y = []
            if item['Status'] == 'OUT':
                a = item['Time_stamp']
            elif a != 0 and item['Time_stamp'][:2] == a[:2]:
                b = item['Time_stamp']
                hora = b[:2] + ':00'
                
                if len(resultado) == 0:
                    ca = cal(a,b)
                    y.append(ca)
                    resultado.append({
                        'x' : hora,
                        'y' : y
                        })
                else:
                    existe_hora=0
                    for item in resultado:
                        if item['x'] == hora:
                            item['y'].append(cal(a, b))
                            existe_hora += 1
                    if existe_hora == 0:
                        resultado.append({
                        'x' : hora,
                        'y' : [cal(a,b)]})

        for lis in resultado:
            value = sum(lis['y']) / len(lis['y'])
            lis['y'] = float(f'{value:.2f}')
        
        return resultado
    
    p3 = []
    for i in range(3):
        p3_dd = SLD.query.filter_by(baia = i + 6)
        p3 += [sld.to_json() for sld in p3_dd]
    

    sld_p3_ocupacao = ocupacao(p3)
    sld_p3_espera = espera(p3)


    resposta = [{
        'name' : 'Ocupado',
        'data' : sld_p3_ocupacao},
        {
        'name' : 'Espera',
        'data' : sld_p3_espera}]

    return gera_response(200, "SLD_0D_3", resposta)

if __name__ == "__main__":
    # Criando as tabelas:
    with app.app_context():
        db.create_all()
    
    # Iniciando api
    app.run(host='0.0.0.0')
    