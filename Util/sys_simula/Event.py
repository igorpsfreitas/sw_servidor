from datetime import time
import random

class Clock:
    def __init__(self, hora = '08:00:00') -> None:
        self._hora = hora

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, hora):
        self._hora = hora

    def time_random(self, segundos_adicionais = random.randrange(30, 350)):
        
        hora_atual = self.hora
        dd = 0
        hh = int(hora_atual[0:2])
        mm = int(hora_atual[3:5])
        ss = int(hora_atual[6:])

        ss += segundos_adicionais        
        if ss >= 60:
            aux_ss = ss / 60
            ss = int(ss % 60)
            mm += int(aux_ss)

        if mm >= 60:
            aux_mm = mm/60
            mm = int(mm % 60)
            hh += int(aux_mm)

        if hh >= 24:
            aux_hh = mm/24
            hh = int(hh % 24)
            dd += 1

        #print(str(time(hh, mm, ss)) + f'::{dd}')
        #return [hh, mm, ss]
        return str(time(hh, mm, ss))


class MPO:
    def __init__(self, clock: Clock) -> None:
        self.status = 0
        self.clock = clock
        self.taxa_aprovados = 75

    def resultado(self):
        if random.randrange(0,100) <= self.taxa_aprovados:
            return 'OK'
        else:
            return 'NOK'
        
    
    def in_placa(self, uid):
        if self.status == 0:
            self.status = 1
            self.placa_UID = uid
                    
            #Função de escrita MQTT
            print(f'Entrou no MPO: UID = {self.placa_UID}, -- {self.clock.hora}')
        else:
            pass

    def out_placa(self):
        if self.status == 1:
            self.status = 0
            self.clock.hora = self.clock.time_random(30)
        
            #Função de escrita MQTT
            print(f'Saiu do MPO: UID = {self.placa_UID}. Resultado = {self.resultado()} -- {self.clock.hora} ') 
        else:
            pass
def processo(placa, mpo: MPO):
    if mpo.status == 0:
        mpo.in_placa(placa)
    mpo.out_placa()
    

if __name__ == '__main__':
    clock = Clock()
    mpo = MPO(clock)
    processo(489, mpo)
    print(clock.hora)
