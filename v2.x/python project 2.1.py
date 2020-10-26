from tkinter import *
import math

master = Tk()

gold = ((math.sqrt(5)-1)/2)

px = 300
py = 300
pz = 0
a = 200
phi = round(gold*a)
xyz = []
# Würfel:
#xyz = [px,py,pz, px+a,py,pz, px,py+a,pz, px,py,pz+a, px+a,py+a,pz, px+a,py,pz+a, px,py+a,pz+a, px+a,py+a,pz+a]

# Ikosaeder:
xyz = [px,py-a,pz+phi, px,py-a,pz-phi, px,py+a,pz+phi, px,py+a,pz-phi, px+phi,py,pz+a, px+phi,py,pz-a, px-phi,py,pz+a, px-phi,py,pz-a, px+a,py-phi,pz, px+a,py+phi,pz, px-a,py-phi,pz, px-a,py+phi,pz]

def conv32():
    xy = []
    for i in range (0,len(xyz)//3):
        xy.append(xyz[3*i]+round(xyz[3*i+2]/2/math.sqrt(2)))
        xy.append(xyz[3*i+1]-round(xyz[3*i+2]/2/math.sqrt(2)))
        #xyz[3*i] = xyz[3*i] + round(xyz[3*i+2]/2/math.sqrt(2))
        #xyz[3*i+1] = xyz[3*i+1] - round(xyz[3*i+2]/2/math.sqrt(2))        
    return xy

def draw():
    #xy = []
    #xyz = [px,py,pz, px+a,py,pz, px,py+a,pz, px,py,pz+a, px+a,py+a,pz, px+a,py,pz+a, px,py+a,pz+a, px+a,py+a,pz+a]
    xy = conv32()
    print('xyz: ' + str(xyz))
    print('xy: ' + str(xy))
    for k in range (0,len(xyz)//3):
        for m in range (0,len(xyz)//3):
            abstand = (round(math.sqrt((xyz[3*k]-xyz[3*m])**2+(xyz[3*k+1]-xyz[3*m+1])**2+(xyz[3*k+2]-xyz[3*m+2])**2)))
            #print(abstand)
            if (abs(abstand-2*phi) < 5):
                canvas1.create_line(xy[2*k],xy[2*k+1],xy[2*m],xy[2*m+1], fill = 'blue')
            ##canvas1.create_line(xyz[3*k],xyz[3*k+1],xyz[3*m],xyz[3*m+1])

def rotx(rx):        
    return(xyz)

def roty(ry):
    return(xyz)

def rotz(rz):
    az = rz/180*math.pi
    for p in range(0,len(xyz)//3):
        x = (xyz[3*p] - px)
        print('x = ' + str(x))
        y = (xyz[3*p+1] - py)
        print('y = ' + str(y))
        z = math.sqrt((xyz[3*p]-px)**2+(xyz[3*p+1]-py)**2)  #z dimension außer acht lassen
        print('Abstand z = ' + str(z))
        d = math.asin(x/z)
        print('d mit p = ' + str(p) + ': ' + str(d))
        xn = math.sin(az+d) * z
        print('xn = ' + str(x))
        yn = math.cos(az+d) * z
        print('yn = ' + str(y))
        xyz[3*p] = round(xyz[3*p] - x + xn)
        xyz[3*p+1] = round(xyz[3*p] - y + yn)
        print('Xneu = ' + str(xyz[3*p]))
        print('Yneu = ' + str(xyz[3*p+1]))
    #draw()
    xy = conv32()
    for k in range (0,len(xyz)//3):
        for m in range (0,len(xyz)//3):
            canvas1.create_line(xy[2*k],xy[2*k+1],xy[2*m],xy[2*m+1], fill = 'green')
    return(xyz)


canvas1 = Canvas(master, width = 800, height = 600)
canvas1.pack()

button1 = Button(master, text = 'zeichnen', command = draw())
button1.pack()


