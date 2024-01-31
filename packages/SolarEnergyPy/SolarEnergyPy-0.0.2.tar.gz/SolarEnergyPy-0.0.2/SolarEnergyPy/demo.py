from datetime import datetime
import pendulum
from SolarEnergyPy.solarPosition import solarPosition as sp
from SolarEnergyPy.solarRadiation import solarRadiation as sr

def solar_system_demo(longitude, latitude, dt):

    solar_position = sp(longitude, latitude)
    solar_radiation = sr()
    solar_position.clocktime = dt
    solar_radiation.clocktime = dt

    print(f"Solar Position:{sp.site}")
    print(f"Date-Time: {solar_position._datetime}")
    print(f"Latitude: {solar_position.latitude}")
    print(f"Longitude: {solar_position.longitude}")
    print(f"Declination: {solar_position.declination}")
    print(f"Solar Azimuth: {solar_position.solar_azimuth}")
    print(f"Solar Zenith: {solar_position.zenith}")

    print("\nSolar Radiation:")
    beam, diffuse = solar_radiation.solar_radiation_at()
    print(f"Beam Radiation: {beam} W/m^2")
    print(f"Diffuse Radiation: {diffuse} W/m^2")

if __name__ == '__main__':

    longitude = 112
    latitude = 31
    dt = pendulum.now('Asia/Shanghai')
    solar_system_demo(longitude, latitude, dt)
