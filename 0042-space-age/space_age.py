class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_sec_per_y = 31557600

    def get_years(self, ratio=1):
        answer = (self.seconds / self.earth_sec_per_y) / ratio
        return round(answer, 2)

    def on_earth(self):
        return self.get_years()

    def on_mercury(self):
        return self.get_years(0.2408467)

    def on_venus(self):
        return self.get_years(0.61519726)

    def on_mars(self):
        return self.get_years(1.8808158)

    def on_jupiter(self):
        return self.get_years(11.862615)

    def on_saturn(self):
        return self.get_years(29.447498)

    def on_uranus(self):
        return self.get_years(84.016846)

    def on_neptune(self):
        return self.get_years(164.79132)


"""

Given an age in seconds, calculate how old someone would be on:

Mercury: orbital period 0.2408467 Earth years
Venus: orbital period 0.61519726 Earth years
Earth: orbital period 1.0 Earth years, 365.25 Earth days, or 31557600 seconds
Mars: orbital period 1.8808158 Earth years
Jupiter: orbital period 11.862615 Earth years
Saturn: orbital period 29.447498 Earth years
Uranus: orbital period 84.016846 Earth years
Neptune: orbital period 164.79132 Earth years
"""


if __name__ == "__main__":
    print(SpaceAge(1000000000).on_earth(), 31.69)

    print(SpaceAge(2134835688).on_mercury(), 280.88)

    print(SpaceAge(189839836).on_venus(), 9.78)

    print(SpaceAge(2129871239).on_mars(), 35.88)

    print(SpaceAge(901876382).on_jupiter(), 2.41)

    print(SpaceAge(2000000000).on_saturn(), 2.15)

    print(SpaceAge(1210123456).on_uranus(), 0.46)

    print(SpaceAge(1821023456).on_neptune(), 0.35)
