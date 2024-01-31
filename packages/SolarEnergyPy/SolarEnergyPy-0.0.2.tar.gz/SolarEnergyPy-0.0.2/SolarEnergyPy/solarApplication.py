import numpy as np
import pendulum as pd
import SolarEnergyPy.solarPosFunc as sp
from VisualShape3D.geometry import *
from VisualShape3D.models import *
from VisualShape3D.plotable import Plotable

class Scene(Plotable):
### Init
    def __init__(self, title="untitled", site = (117, 31), 
                       tz='Asia/Shanghai', 
                       style={'alpha':0.5}, ax=None, *args, **kwargs):
        super().__init__()
        if self.get_ax() is not None:
            self.clear_ax()

        if ax is None :
            # it is the very first plot of the application
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            
        self.set_ax(ax)

        self.project = title
        self.longitude = site[0]   
        self.latitude  = site[1]
        self.tz = tz
        self.layouts = {}
        self.style = style

        circle = Shape(shape="regularPolygon",**{'R':1,'n':48,'P0':(0,0,0)})
        self.ground = circle.move(by=(0,90))
        self.add_plot(self.ground, style = style)

    def __str__(self):
        ret =  f" Project : {self.project} at {self.longitude,self.latitude}\n"
        ret += f"Timezone : {self.tz}"
        return ret

### Visibility
    def get_object(self): return self

    def get_domain(self):
        """
        :return   ndarray([min], [max])
        """
        if self.building is not None : 
            buidling_domain = self.building.get_domain()
        else:
            buidling_domain = np.ones((0, 3))

        points = np.vstack(( buidling_domain,self.ground.vertices))
        domain = np.array([points.min(axis=0), points.max(axis=0)])
        
        # bound  = np.max(domain[1]-domain[0])
        # print(f" bound = {bound}")
        # print(f" domain[0] = {domain[0]}")
        return domain

    def iplot(self, style , ax,**kwargs):
        
        facecolor = style['facecolor']  if 'facecolor' in style else self.facecolor
        edgecolor = style['edgecolor']  if 'edgecolor' in style else self.edgecolor  
        marker = style['marker']     if 'marker'       in style else self.marker  
        alpha  = style['alpha']      if 'alpha'        in style else self.alpha 
        label  = style['label']      if 'label'        in style else self.label  

        if self.plot_style == None :  # the first time
            if facecolor == 'default': facecolor = 't'
            if facecolor == 't':       facecolor = 'xkcd:beige'
            if edgecolor == 'default': edgecolor = 'olive'
            if alpha  == 'default':    alpha = 0.5

        else :
            if facecolor == 'default': facecolor = 't'
            if facecolor == 't':       facecolor = self.plot_style['facecolor']
            if edgecolor == 'default': edgecolor = self.plot_style['edgecolor']
            if alpha      == 'default':    alpha = self.plot_style['alpha']

        self.plot_style = {'facecolor':facecolor, 'edgecolor':edgecolor, 'alpha':alpha}

        self.ground.iplot( style= self.plot_style, ax=ax,**kwargs)

        if self.building is not None : 
            self.building.iplot(style=( facecolor, edgecolor, alpha), ax=ax,**kwargs)

### Functions
    def reference(self, longitude=117, latitude=31, tz='Asia/Shanghai' ):
        self.longitude = longitude
        self.latitude  = latitude
        self.tz = tz

    def add_building(self,title = "building"):
        self.layouts[title] = Building(title)
        return self.layouts[title]

    def add_panels(self, panels, title = "panels"):
        self.layouts[title] = panels
        return self.layouts[title]

    def period(self,start = sp.local_time(1,1,0,0), 
                      end = sp.local_time(12,31,23,59)):
        self.start = start
        self.end = end
        delta = self.end - self.start
        return delta.hours

    def render(self):
        self.show(elev= 20.0, azim = -70.0, hideAxes=True, origin = True)

    def solarPosition(self, time) :
        pass

### Demos
def plotPoints():
    P = Point(0.5,0.5,0.5)
    P.plot(style={'facecolor':'r','alpha':0.5})
    P1 = Point(0.5,0.7,0.5)
    P.add_plot(P1)
    P.show()

def plotLine():
    P1 = Point(0.2,0.1,0.1)
    P2 = Point(0.8,0.5,0.8)
    L  = Segment(P1,P2)
    L.plot()
    L.show()

def plotPolygon():
    x = [0.5,0.3,0.6,0.9,0.1]
    y = [0.1,0.9,0.3,0.4,0.8]
    z = [0.7,0.3,0.1,0.9,0.6]
    points = list(zip(x,y,z))
    poly = Polygon(points)
    poly.plot()
    poly.show()

def plotScene():
    se = Scene(title='new',site=(117,31))
    se.plot()
    print(se)
    se.render()    

def main():
    # plotPoints()
    # plotPolygon()
    # plotLine()
    plotScene()

if __name__ == '__main__':
    main()
