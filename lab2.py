country = "Ukraine"
class city:
    def __init__(self, name, population, coordinates):
        self.name = name
        self.population = population
        self.coordinates = coordinates

    def info(self):
        return f"В {country} є місто {self.name} з населенням {self.population} і координатами {self.coordinates}"
    
    def move(self, dlat, dlon):
        self.coordinates = (self.coordinates[0] + dlat, self.coordinates[1] + dlon)

Kiev = city("kiev", 3000000, (50.4501, 30.5234))

Lviv = city("Lviv", 3500000, (51.4501, 32.5234))

Ivano_Frankivsk = city("Ivano_Frankivsk", 4000000, (49.4501, 29.5234))

Jutomir = city("Jutomir", 2500000, (52.4501, 32.5234))

print(Kiev.info())
Kiev.move(1, 15)
print(Kiev.info())