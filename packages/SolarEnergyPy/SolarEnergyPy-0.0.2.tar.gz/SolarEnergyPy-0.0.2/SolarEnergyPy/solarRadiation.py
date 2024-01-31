__author__ = ' He Liqun '
import pendulum
import math
import numpy
from fractions import Fraction
from SolarEnergyPy.solarPosition import *

class solarRadiation(solarPosition):
    solar_constant = 1367  # W/m^2
    Gsc = solar_constant

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.constant:0.1f} W/m^2'

    @property
    def constant(self):
        return self.solar_constant

    def Gon_generator(self, n):
        if isinstance(n, (list, tuple, range)):
            m = n
        else:
            m = range(n)
        for i in m:
            yield self.Gon(i)

    def Gon(self, n=None, precise=None):
        m = n if n is not None else self._datetime.day_of_year
        G = self.Gsc * self.simple_equation(m)
        if not precise is None:
            G = self.Gsc * self.Spencer_equation(m)
        return G

    def simple_equation(self, n=1):
        B = 360 * n / super().days_of_one_year
        var = 1 + 0.033 * cosd(B)
        return var

    def Spencer_equation(self, n=1):
        B = 360 * (n - 1) / super().days_of_one_year
        var = 1.00011 + 0.034221 * cosd(B) + 0.001280 * sind(B) + 0.000719 * cosd(2 * B) * 0.000077 * sind(2 * B)
        return var

    def solar_radiation_at(self, at=None, n=None):
        if at is not None:
            old = self.clocktime
            self.clocktime = pendulum.instance(at)

        seconds = self._datetime.second
        m = n if n is not None else self._datetime.day_of_year

        Ts = self.clocktime.hour + self.clocktime.minute / 60 + self.clocktime.second / 3600
        solar_hour_angle = (Ts - 12) * 15

        print(f'Ts: {Ts}, solar_hour_angle: {solar_hour_angle}')  # 添加的打印语句

        A = (284 + m) * 360. / self.days_of_one_year
        solar_declination = 23.45 * sind(A)

        Phi = self.latitude
        w = solar_hour_angle
        Delta = solar_declination

        cosThetaz = cosd(Phi) * cosd(Delta) * cosd(w) + sind(Phi) * sind(Delta)

        if cosThetaz > cosd(90):
            tb = self.a0 + self.a1 * math.exp(-self.k / cosThetaz)
            td = 0.271 - 0.294 * tb
        else:
            tb, td = 0, 0

        if at is not None:
            self.clocktime = old
        return self.Gon(m) * tb, self.Gon(m) * td

    def solar_radiation_during(self,
                                dt1=pendulum.datetime(datetime.now().year, 1, 1, 0, 0),
                                dt2=pendulum.datetime(datetime.now().year, 12, 31, 23, 59)):
        start = dt1
        end = dt2
        current_time = start
        beams = []
        diffuses = []

        restore = self.clocktime
        while current_time <= end:
            self.clocktime = current_time
            beam, diffuse = self.solar_radiation_at()
            beams.append(beam)
            diffuses.append(diffuse)
            current_time = current_time.add(hours=1)

        self.clocktime = restore
        return beams, diffuses

import matplotlib.pyplot as plt

def demo():
    dt = pendulum.now()
    sr = solarRadiation(longitude=110, latitude=30, dt=dt)
    print(f'当前时间：{dt}')
    print(f'直射、散射：{sr.solar_radiation_at()}')

if __name__ == '__main__':
    demo()
