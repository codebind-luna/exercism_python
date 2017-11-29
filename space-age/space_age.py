class SpaceAge(object):

    EARTH_YEAR_SECONDS = 31557600
    YEAR_MULT = {'Mercury': 0.2408467,
                 'Venus': 0.61519726,
                 'Earth': 1,
                 'Mars': 1.8808158,
                 'Jupiter': 11.862615,
                 'Saturn': 29.447498,
                 'Uranus': 84.016846,
                 'Neptune': 164.79132}

    def __init__(self, seconds):
        self.seconds = seconds


    def on_planet(self, planet):
        return round(self.seconds / (SpaceAge.EARTH_YEAR_SECONDS * SpaceAge.YEAR_MULT[planet]), 2)

    def on_mercury(self):
        return self.on_planet('Mercury')

    def on_venus(self):
        return self.on_planet('Venus')

    def on_earth(self):
        return self.on_planet('Earth')

    def on_mars(self):
        return self.on_planet('Mars')

    def on_mercury(self):
        return self.on_planet('Mercury')

    def on_jupiter(self):
        return self.on_planet('Jupiter')

    def on_saturn(self):
        return self.on_planet('Saturn')

    def on_uranus(self):
        return self.on_planet('Uranus')

    def on_neptune(self):
        return self.on_planet('Neptune')
