from datetime import time
import random

class time_now:
    def __init__(self, time: str = "08:00:00") -> None:
        self._tempo_atual = time

    def __str__(self) -> str:
        return self._tempo_atual

    @property
    def tempo_atual(self):
        return self._tempo_atual
    
    @tempo_atual.setter
    def tempo_atual(self, value):
        self._tempo_atual = value

    def time_random(self, segundos_adicionais = random.randrange(30, 350)):
        hh = int(self.tempo_atual[0:2])
        mm = int(self.tempo_atual[3:5])
        ss = int(self.tempo_atual[6:])
        dd = 0 

        ss += segundos_adicionais
    
        if ss >= 60:
            aux_ss = ss/60
            ss = int(ss%60)
            mm += int(aux_ss)

        if mm >= 60:
            aux_mm = mm/60
            mm = int(mm%60)
            hh += int(aux_mm)

        if hh >= 24:
            aux_hh = hh/24
            hh = int(hh%24)
            dd += int(aux_hh)
        
        self.tempo_atual(f'{hh}:{mm}:{ss}')

class Fila:
    def __init__(self) -> None:
        self.lista = [123123, 789789, 456456, 741741, 852852, 963963, 159159, 753753]

    def add(self, item):
        self.lista.append(item)

    def rm(self):
        return self.lista.pop(0)    

class VGR:
    def __init__(self, time: time_now, fila: Fila) -> None:
        self.status = False
        self.time = time.tempo_atual




if __name__ == "__main__":
    vgr, mpo, sld, hbw = True, True, True, True
    hora = time_now()
    hora.tempo_atual = "09:30:30"
    print(hora)
    

    