#Examen de evaluación 2D, Andrei Enrique Carvajal Brito, 14/12/2020
#No. control: 1839022
#importa libreria
import matplotlib.pyplot as plt 
import numpy as np 

#poner margen
plt.axis([0,300,0,300])
plt.axis('on')
plt.grid(True)

#centro del círculo y radio
xc=200
yc=150
r=40

#plotear circulo
p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color=(0,2/10,2/10))
    xlast=xp
    ylast=yp


#segundo rectángulo con esquina en el circulo
x=np.array([xc,xc,xc-2.5*r,xc-2.5*r,xc])
y=np.array([yc,yc-2.5*r,yc-2.5*r,yc,yc])
plt.plot(x,y, color=(0,2/10,2/10))

#primer rectángulo, encerrando el círculo y con esquina en el centro del segundo rectángulo
xc=xc*1.25
yc=yc*(200/150)

x=np.array([xc,xc,xc-2.5*r,xc-2.5*r,xc])
y=np.array([yc,yc-2.5*r,yc-2.5*r,yc,yc])
plt.plot(x,y, color=(0,2/10,2/10))

plt.axes().set_aspect('equal')
plt.show()