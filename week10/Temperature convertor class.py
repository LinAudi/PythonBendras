class Temperature:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return round(kelvin-272.15, 1)

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return round((kelvin -272.15) * (9/5) +32, 1)

    def __str__(self):
        celcius = Temperature.kelvin_to_celsius(self.kelvin)
        ferenheit = Temperature.kelvin_to_fahrenheit(self.kelvin)
        return f"Temperature: {self.kelvin}K, {celcius}°C, {ferenheit}°F"



temp = Temperature(300)
print(temp)

print(Temperature.kelvin_to_celsius(300),"°C")
print(Temperature.kelvin_to_fahrenheit(300),"°F")