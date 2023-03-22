class Clock:
    def __init__(self, time) -> None:
        self.real_time = time
        
        self._hh = int(self.real_time[0:2])
        self._mm = int(self.real_time[3:5])
        self._ss = int(self.real_time[6])

    def now(self):
        print(f'{str(self._hh).zfill(2)}:{str(self._mm).zfill(2)}:{str(self._ss).zfill(2)}')
        return f'{str(self._hh).zfill(2)}:{str(self._mm).zfill(2)}:{str(self._ss).zfill(2)}'

    def add(self, segundos_adicionais):
        self._ss += segundos_adicionais
        
        if self._ss >= 60:
            aux_ss = self._ss/60
            self._ss = int(self._ss%60)
            self._mm += int(aux_ss)
            
        if self._mm >= 60:
            aux_mm = self._mm/60
            self._mm = int(self._mm%60)
            self._hh += int(aux_mm)
        
        if self._hh >= 24:
            self._hh = int(self._hh%24)
        
        return self.now()


# Testes:
if __name__ == "__main__":
    relogio = Clock('00:37:42')
    relogio.add(120)