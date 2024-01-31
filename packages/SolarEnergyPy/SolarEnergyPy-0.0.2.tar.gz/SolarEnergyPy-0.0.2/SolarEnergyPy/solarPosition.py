__author__ = ' He Liqun '
""" Notes about prime meridian
                https://sciencing.com/location-earth-new-day-begin-midnight-6455.html
"""
from datetime import datetime
import pendulum
import numpy as np
from fractions import Fraction

def sin(v):
    return  np.sin(v) 

def cos(v):
    return np.cos(v)

def sind(d):
    return sin(np.radians(d)) 
    
def cosd(d):
    return cos(np.radians(d)) 

def acosd(value):
    return np.arccos(value)

def tand(d):
    return np.tan(np.radians(d))

def sign(value):
    ret = 0
    if value > 0 :
        ret = 1
    if value <0 :
        ret = -1       
    return ret

class site(object):
    r0 = (0.95,0.97,0.99,1.03)
    r1 = (0.98,0.99,0.99,1.01)
    r2 = (1.02,1.02,1.01,1.0)
    @staticmethod
    def adjust(val):
        x = val
        if val <= -180 :
            x = 360 + val
        if val > 180 :
            x = val - 360
        return x

    def __init__(self,longitude,latitude, altitude=0,climate=1):
        """
            climate           type       ( Hottel 1976, P69 )
                 0       Tropical 
                 1       Midlatitude summer   
                 2       Subarctic summer
                 3       Midlatitude winter 
        """

        self.moveto(longitude,latitude)
        self._altitude = altitude  # kilometer
        self.set_climate_type(climate)
         
    def moveto(self, longitude,latitude):
        self._longitude = self.adjust( longitude )
        self._latitude = latitude 
        return  '( {:0.2f},{:0.2f} )'.format(self.longitude,self.latitude)

    def set_climate_type(self,climate):
    
        A = self._altitude  
        a0 = 0.4237 - 0.00821*(6 - A)**2
        a1 = 0.5055 + 0.00595*(6.5 - A)**2
        k  = 0.2711 + 0.01858*(2.5 - A)**2
        
        i = climate
        self.a0 = a0*self.r0[i]
        self.a1 = a1*self.r1[i]
        self.k  = k *self.r2[i]
        self._climate_type = i

    def __str__(self):
        return '( {:0.2f},{:0.2f} )'.format(self.longitude,self.latitude) 

    @property
    def site(self):
        return '( {:0.2f},{:0.2f} )'.format(self._longitude,self._latitude)
    
    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def altitude(self):
        return self._altitude  

    @property
    def climate_type(self):
        return self._climate_type
    
    @longitude.setter
    def longitude(self,L):
        self._longitude = L

    @latitude.setter
    def latitude(self,L):
        self._latitude = L

    @site.setter
    def site(self,x,y):
        self._longitude = x
        self._latitude  = y

    @climate_type.setter 
    def climate_type(self, i):
        self.set_climate_type(i)

    @altitude.setter
    def set_altitude(self,x):
        self._altitude = x
        
class solarTime(site):
    def __init__(self, *args, **kwargs):
        dt = kwargs.get('dt', None)
        longitude = kwargs.get('longitude', 112)
        latitude = kwargs.get('latitude', 31)
        hour = kwargs.get('hour', 0)
        minute = kwargs.get('minute', 0)
        second = kwargs.get('second', 0)
        tz = kwargs.get('tz', 'Asia/Shanghai')

        super().__init__(longitude, latitude)
        self._tz = tz

        if dt is not None:
            self.clocktime = pendulum.instance(dt)
        else:
            self.clocktime = pendulum.now(self.tz)  # 初始化为当前时间

        self.clock_moveto(hour, minute, second)

    def update_solartime(self):
        if self._datetime is not None:
            dt = self._datetime.in_timezone('UTC')
            time_difference_in_minutes = self.time_correction()
            self._solar_datetime = dt.add(minutes=time_difference_in_minutes)
            return self._solar_datetime

    def __str__(self):
        return '{}'.format(self._solar_datetime.strftime("%H:%M:%S"))
 
    @property
    def clocktime(self):
        return self._datetime

    @clocktime.setter
    def clocktime(self, value):
        self._datetime = value
        self.update_solartime()

    @property
    def seconds(self):
        return self.duration.seconds 

    @property
    def tz(self):
        return self._tz

    @tz.setter
    def tz(self, value):
        self._tz = value 
        self._datetime = self._datetime.in_timezone(self._tz)
        self.update_solartime()
        
    @property
    def day_of_year(self):
        return self._datetime.day_of_year

    @property
    def duration(self):
        dt1 = self._solar_datetime
        dt2 = dt1.replace(hour=0,minute=0,second=0)
        delta = dt1 - dt2
        return delta
        
    @property
    def days_of_one_year(self):
        d = 365
        if self.is_leap_year:
            d = 366
        return d
    
    @property
    def when(self):
        return self._datetime.strftime("%H:%M:%S")

    @property
    def date(self):
        return self._datetime.strftime("%Y-%m-%d")

    @property
    def is_leap_year(self):
        return self._datetime.is_leap_year()

    @property
    def solartime(self):
        return self._solar_datetime

    # Functions for Single Datetime
    def update_solartime(self):
        dt = self._datetime.in_timezone('UTC')
        time_difference_in_minutes = self.time_correction()
        self._solar_datetime = dt.add( minutes = time_difference_in_minutes )
        # str = self._solar_datetime.strftime("%H:%M:%S")
        return self._solar_datetime

    def E(self,n):
        B = (n-1)*360/self.days_of_one_year
        return 229.2*(0.000075+0.001868*cosd(B)-0.0320775*sind(B)-0.014615*cosd(2*B)-0.04089*sind(2*B))

    def time_correction(self):
        n = self._datetime.day_of_year
        t_correcttion = super().longitude * 4 + self.E(n)  # in minutes
        return t_correcttion 

    def clock_moveto(self,h,m,s):
        self._datetime = self._datetime.replace(hour=h,minute=m,second=s)
        str =  self.update_solartime()
        return str
    
    def clock_moveto_now(self):
        self._datetime = pendulum.now(self.tz)
        str = self.update_solartime()
        return str

    def on(self,y,m,d):
        self._datetime.replace(year=y,month=m,day=d)
        self.update_solartime()
        return self

    def at(self,h,m,s):
        self.clock_moveto(h,m,s)
        return self

    def site_moveto(self,longi,lati):
        longi = self.adjust(longi)
        super().moveto(longi,lati)
        self.update_solartime()
        return self

    def next_day(self):
        dt =self._datetime.add(days=1)
        self._datetime = dt
        return self._datetime.strftime("%Y-%m-%d")
        
    def next_hour(self):
        dt=self._datetime.add(hours=1)
        self._datetime = dt
        return self._datetime.strftime("%H:%M:%S")

    def next_second(self):
        dt=self._datetime.add(minutes=1)
        self._datetime = dt
        return self._datetime.strftime("%H:%M:%S")

    # Functions for a time period
    def solar_time_during(self, 
                dt1 = datetime(datetime.now().year,1,1,0,0),\
                dt2 = datetime(datetime.now().year,12,31,23,59)):
        start  = pendulum.instance(dt1)
        end    = pendulum.instance(dt2)
        # 初始化当前时间为起始时间
        current_time = start
        
        # 循环计算每个时刻的太阳时
        solar_time_list = []
        restore = self.clocktime
        while current_time <= end:
            # 设置当前时间,更新当前时刻的太阳时
            self.clocktime = current_time

            # 累计
            solar_time_list.append(solar_time)

            # 当前时间增加1小时
            current_time = current_time.add(hours=1)

        self.clocktime = restore
        return solar_time_list
    
class solarPosition(solarTime):
    solar_distance = 1.495E11  # m

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        # super().site_moveto(longitude,latitude)
        self.get_solar_location_angles()
        self.get_solar_vector()
    
    def __str__(self):
        return 'When {}, the solar location is {} at {}.'.format(
                self.when, self.solar_location, super().site)

    @property
    def solar_location(self):
        return self.get_solar_location_angles()

    @property
    def solar_vector(self):
        return self.get_solar_vector()
   
    @property
    def hour_angle(self):
        Ts = super().seconds / 3600
        ha = ( Ts - 12 )*15
        return ha

    @property
    def declination(self):
        n  = super().day_of_year
        A  = ( 284 + n  )* 360./super().days_of_one_year
        DE = 23.45*sind(A)
        return DE

    @property
    def solar_latitude(self):
        return 90-self.zenith
        
    def set_zenith(self):
        Phi = self.latitude
        w   = self.hour_angle
        Delta =self.declination
        cosThetaz = cosd( Phi) * cosd( Delta ) * cosd ( w ) + sind( Phi ) * sind( Delta )
        ze = acosd( cosThetaz )
        self._zenit  = ze * 180 / np.pi
    
    @property
    def zenith(self):
        self.set_zenith()
        return self._zenit

    def set_azimuth(self):
        Ze    = self.zenith
        Phi   = self.latitude
        w     = self.hour_angle
        Delta = self.declination
        x     = cosd(Ze) * sind(Phi) - sind(Delta)
        x     = x / ( sind( Ze ) * cosd( Phi ) )
        az    = sign(w) * abs( acosd(x) )
        self._azimuth = az * 180 / np.pi

    # 180 ~ -180 for tropical latitudes
    #  90 ~ -90  for latitudes  23.5 - 66.45  
    # >90 or <-90 early and late in the day for > 66.45

    @property
    def solar_azimuth(self):
        self.set_azimuth()
        return self._azimuth
           
    @property
    def hourangle_for_sunrise_sunset(self):
        Phi   = self.latitude
        Delta = self.declination 
        ws    = acosd(-tand(Phi)*tand(Delta))
        return ws
 
    @property
    def day_length(self):
         pass
        #n = 2/15 * self.sun_set_hour_angle
        #return n
    
    def get_solar_location_angles(self):
        self.set_azimuth()
        self.set_zenith()
        self._angles = '( {:0.2f},{:0.2f} )'.format(self.solar_azimuth,
                         self.solar_latitude )
        return self._angles

    # theta - it starts from 6 AM where the hour angle starts from 12 AM.
    def get_solar_vector(self):
        Ts    = super().seconds / 3600
        theta = ( Ts   - 6.0 )/12.0 * 180
        phi   = ( 90.0 - self.latitude )
        delta = self.declination
        s     = sind(theta)*cosd(phi)*cosd(delta)-sind(phi)*sind(delta)
        e     = cosd(theta)*cosd(delta)*sind(phi)
        u     = sind(theta)*sind(phi)*cosd(delta)+cosd(phi)*sind(delta)
        self._vector = '( {:0.2f},{:0.2f},{:0.2f} )'.format(s,e,u)
        return self._vector
        
    def solar_noon(self):
        return 90-abs(self.latitude - self.declination)

    def solar_position_during(self, \
        dt1 = datetime(datetime.now().year,1,1,0,0),\
        dt2 = datetime(datetime.now().year,12,31,23,59)):
        start  = pendulum.instance(dt1)
        end    = pendulum.instance(dt2)
        # 初始化当前时间为起始时间
        current_time = start
        
        # 循环计算每个时刻的太阳时
        solar_locations = []
        solar_vectors  = []

        restore = self.clocktime
        while current_time <= end:
            # 设置当前时间
            self.clocktime = current_time
            
            # 计算当前时刻的太阳位置
            solar_locations.append(self.solar_location)
            solar_vectors.append(self.solar_vector)

            # 当前时间增加1小时
            current_time = current_time.add(hours=1)

        self.clocktime  = restore
        return solar_locations,solar_vectors


def demo():
    sp = solarPosition(110,30,11,12,23)
    print(sp)
    print(' solar time = {}'.format(sp.solartime))
    str = " site = {}".format(sp.site)
    print(str)
    print('date-time is {}'.format(sp._datetime))
    print(sp.is_leap_year)

    sp.clock_moveto(16,30,30)
    print('solar vector = {}'.format(sp.solar_vector))
    print('solar angles = {}'.format(sp.solar_location))
    print('solar-earch distance = {} Mm '.format(sp.solar_distance/1000000))

    dt = pendulum.from_timestamp(0, 'Asia/Shanghai').offset_hours
    print(dt)

if __name__ =='__main__':
    demo()

