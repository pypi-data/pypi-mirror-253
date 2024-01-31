import pendulum as pd
# from datetime import datetime, date, time, timezone
import numpy as np

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def sind( angle ):
    return np.sin( np.radians(angle))
def cosd( angle ):
    return np.cos( np.radians(angle))
def acosd( value):
    return np.degrees(np.arccos(value))

def sort_numpy(array, col=0, undo=False):
    """
    Sorts the columns for an arrray.
    It returns a sorted_array or a list of[sorted_array, undo_index].
    Thta is, sorted_array[undo_index] == array
    
    Input :
             array: a ndarray to sort
              col : indicating which  column to sort, int
        undo_index: If True, it also returns the index for undo purpose
    
    """
    x = array[:,col]
    sorted_index = np.argsort(x, kind = 'quicksort')
    sorted_array = array[sorted_index]
    
    if not undo:
        return sorted_array
    else:
        n_points = sorted_index.shape[0]
        undo_index = np.empty(n_points, dtype=int)
        undo_index[sorted_index] = np.arange(n_points)
        return [sorted_array, undo_index]

def arange_col(n, dtype=int):
    """
    It creates a column of size n
    Input:
       n : length of the array.
    Output
       an array in a column form.
    """
    return np.reshape(np.arange(n, dtype = dtype), (n, 1))

def bool2index(bool_):
    """
    Returns a numpy array with indices of Trues in bool_.

    Input
       bool_: bool array to extract True positions.

    """
    return np.arange(bool_.shape[0])[bool_]

def index2bool(index, length=None):
    """
    Returns a numpy boolean array with Trues at index 
    .
    Input:
         index:   index array with the Trues positions.
    """
    if index.shape[0] == 0 and length is None:
        return np.arange(0, dtype = bool)
    if length is None: length = index.max()+1
        
    sol = np.zeros(length, dtype=bool)
    sol[index] = True
    return sol

#  loca time
def local_time(month=1,day=1,hour=1,second=1,tz = 'Asia/Shanghai'):
    dt_now = pd.now(tz=tz)
    return pd.datetime(dt_now.year,month,day,hour,second,tz=tz)

def time_normalized(hour, minute, second):        
    second = int(second%60)
    minute = int((minute + int(second/60))%60)
    hour   = int((hour   + int(minute/60))%60)
    hour   = hour%24
    return hour,minute,second

def longitude_to_time(dL):
    minutes = dL*4
    hour = int(minutes/60)
    minute = int(minutes%60)
    second = int( ( minutes%60 - minute )*60 )
    return f"{hour:02d}:{minute:02d}:{second:02d}"

### Solar Time
def solar_time( clock_time = local_time(), longitude=117):
    ## datetime version
    # utc_time = datetime.now(timezone.utc)
    # delta_time = clock_time - utc_time
    # longit = float(longitude) - delta_time.seconds/3600 * 15.0

    # pendulum version
    ct = clock_time
    longit = float(longitude) - ct.offset_hours * 15.0   
    
    gamma = 2 * np.pi / 365 * (ct.day_of_year - 1 + float(ct.hour - 12) / 24)
    eqtime = 229.18 * (0.000075 + 0.001868 * cos(gamma) - 0.032077 * sin(gamma) \
             - 0.014615 * cos(2 * gamma) - 0.040849 * sin(2 * gamma))
    decl = 0.006918 - 0.399912 * cos(gamma) + 0.070257 * sin(gamma) \
           - 0.006758 * cos(2 * gamma) + 0.000907 * sin(2 * gamma) \
           - 0.002697 * cos(3 * gamma) + 0.00148 * sin(3 * gamma)
    time_offset = eqtime + 4 * longit
    
    #tst = delta_time.seconds/60 + time_offset
    # ha = datetime.combine(dt.date(), time(0)) + timedelta(minutes=tst)
    
    tst = ct.hour * 60 + ct.minute + ct.second / 60 + time_offset
    
    stime =  tst/60.0
    return stime

def equation_of_time(n):
    B = (n-1) * 360/365
    E = 229.2*(0.000075+0.001868*cosd(B)-0.0320775*sind(B)
        -0.014615*cosd(2*B)-0.04089*sind(2*B))
    return E

def declination(n, simple_mode=None):
    if simple_mode :
        ret  = 23.45*sind(( 284 + n  )* 360/365 )

    else :
        B = (n-1) * 360/365
        ret = np.degrees(0.006918-0.3999912*cosd(B) + 0.070257*sind(B)
                        -0.006758*cosd(2*B) + 0.000907*sind(2*B)
                        -0.002697*cosd(3*B) + 0.00148*sind(3*B))
    return ret

def hour_angle(Ts):
    return ( Ts - 12 )* 15

def day_number(month, day, leap=None):
    monthly_days = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
    if leap :
        monthly_days = np.array([31,29,31,30,31,30,31,31,30,31,30,31])

    d = int(day)
    m = int(month)
    
    if not(0< m and m<= 12) :
        return " Wrong month number !!!"
        
    if not(d <= monthly_days[m-1]):
        return " Wrong day number !!!"
    
    n = d
    for i in range(m-1):
        n += monthly_days[i]          
    
    return n

# Solar Position
def solarZenith(latitude, n, Ts):
    Phi       = latitude 
    w         = hour_angle( Ts ) 
    Delta     = declination( n )
    cosThetaz = cosd( Phi)* cosd( Delta )* cosd ( w ) + sind( Phi )* sind( Delta )
    thetaz    = acosd( cosThetaz )
    return thetaz

def solarAzimuth(latitude, n, Ts):
    Ze    = solarZenith( latitude, n, Ts ) 
    Phi   = latitude 
    w     = hour_angle( Ts )
    Delta = declination( n )
    x     = cosd(Ze) * sind(Phi) - sind(Delta)
    x     = x / ( sind( Ze )*cosd( Phi ) )
    az    = np.sign(w) * abs( acosd(x))
    return az

def solarLatitude(latitude, n, Ts):
    zenith = solarZenith( latitude, n, Ts) 
    latitude = 90 - zenith
    return latitude

def solarAngles(latitude, n, Ts):
    Azimuth = solarAzimuth( latitude, n, Ts )
    Zenith  = solarZenith ( latitude, n, Ts )
    return Azimuth, Zenith

def solarVector( latitude, n, Ts ):
    """
     For a solar day-time, it gives the solar direction
     as a vector in the local ( S,E,Z ) coodinate system.
     Usage: 
             s,e,u = solarVector( latitude, n, Ts )
     Example:
             s,e,u = solarVector( 30,100,10) 
    """    

    theta = ( Ts - 6.0 ) * 15;
    phi   = ( 90.0 - latitude );    
    delta = declination( n )   # declination
    s = sind(theta)*cosd(phi)*cosd(delta)-sind(phi)*sind(delta) 
    e = cosd(theta)*cosd(delta)*sind(phi);
    u = sind(theta)*sind(phi)*cosd(delta)+cosd(phi)*sind(delta) 
    return s,e,u

def panelVector( gamma, beta ):
    s = cosd(beta)*cosd(gamma)
    e = -cosd(beta)*sind(gamma)
    u = sind(beta)
    return s,e,u

def main():
    Ts = 10
    n = 100
    latitude = 117
    solar = solarVector(latitude,n,Ts)
    print(solar)
    panel = panelVector( 15, 30 )
    print(panel)

    solar = np.array(solar)
    panel = np.array(panel)
    print(solar.dot(panel))
    print((solar*panel).sum())

    print(declination(n))

if __name__ == '__main__':
    main()