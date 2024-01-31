import pandas as pd
import datetime

def read_head( filename ):
    f = open(filename,'r')
    firstline = f.readline()
    f.close()
    return firstline

def read_data(filename):
    data = pd.read_csv(filename, header=1)
    return data

def read_tmy3(filename):
    head_line = read_head( filename )
    data_body = read_data(filename)
    return data_body, head_line

def conversion(x):
    y = x.split(' ')
    z = y[1].split(':')
    w = '{} {:0>2d}:{}'.format(y[0],int(z[0])-1,z[1])
    return datetime.datetime.strptime(w,"%m/%d/%Y %H:%M")

class tmy3_reader():
    def __init__(self, filename):
        self.data, self.head = read_tmy3(filename)
    
    def __str__(self):
        return 'Please get head and data by calling\n get_head()/get_data().'
    
    def get_head(self):
        return self.head
    
    def get_data(self):
        return self.data
    
    def get_headline(self):
        data_head = ['USAF', 'Name', 'State', 'TZ', 'latitude', 'longitude', 'altitude']
        return dict( zip(data_head, firstline.rstrip('\n').split(",")) )
    
    def get_columns(self, column_dict):
        keys = column_dict.keys()
        df = self.data[keys]
        df = df.rename(columns=column_dict)
        df.loc[:,'datetime'] = df['Date'] + df['Time'].apply(lambda x: f" {x}")
        df = df.drop(columns = ['Date','Time'])
        df.loc[:,'datetime'] = df['datetime'].apply(lambda x: conversion(x))
        df = df.set_index('datetime')
        return df

def test():
    filename = "dataset/Weather Data/US_WI_MADISON_DANE_CO_REGIONAL_ARPT_726410.tmy3"
    t = tmy3_reader(filename)
    titles = {"Date (MM/DD/YYYY)":"Date", "Time (HH:MM)":"Time",
                             "GHI (W/m^2)":"GHI","DNI (W/m^2)":"DNI","DHI (W/m^2)":"DHI",
                             "Dry-bulb (C)":"T","Dew-point (C)":"$T_{dew}$",
                             "RHum (%)":"RH(%)","Wspd (m/s)":"Wind","Pressure (mbar)":"P(mbar)"}
    df = t.get_columns( titles )
    print(df.head())

if __name__ == '__main__':
    test()