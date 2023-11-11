class Celcius:
    def __init__(self, temperature) -> None:
        self.temperature = temperature

    def to_farahnheit(self):
        return (self._temperature * 1.8) + 32
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, new_temp):
        if new_temp < -273.15:
            raise ValueError("Harorat -273.15 dan past bo'lmasligi kerak")
        self._temperature = new_temp

       
    
temp1 = Celcius(310)

print(temp1.temperature, temp1.to_farahnheit())
temp1.temperature = -800















# def get_temperature(self):
#         return self._temperature
    
#     def set_temperature(self, new_temp):
#         if new_temp < -273.15:
#             raise ValueError("Harorat -273.15 dan past bo'lmasligi kerak")
#         self._temperature = new_temp