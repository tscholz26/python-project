from tkinter import *
import math

master = Tk()

gold = ((math.sqrt(5)-1)/2)

mx = 300
my = 300
mz = 0
a = 200
phi = round(gold*a)
xyz = []
# Würfel:
#xyz = [mx,my,mz, mx+a,my,mz, mx,my+a,mz, mx,my,mz+a, mx+a,my+a,mz, mx+a,my,mz+a, mx,my+a,mz+a, mx+a,my+a,mz+a]

# Ikosaeder:
xyz = [mx,my-a,mz+phi, mx,my-a,mz-phi, mx,my+a,mz+phi, mx,my+a,mz-phi, mx+phi,my,mz+a, mx+phi,my,mz-a, mx-phi,my,mz+a, mx-phi,my,mz-a, mx+a,my-phi,mz, mx+a,my+phi,mz, mx-a,my-phi,mz, mx-a,my+phi,mz]

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
    #xyz = [mx,my,mz, mx+a,my,mz, mx,my+a,mz, mx,my,mz+a, mx+a,my+a,mz, mx+a,my,mz+a, mx,my+a,mz+a, mx+a,my+a,mz+a]
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

def rotx(deg):
    canvas1.delete(ALL)
    rad = deg/180*math.pi
    c = math.cos(rad)
    s = math.sin(rad)
    for p in range(0,len(xyz)//3):
        y = xyz[3*p+1]
        z = xyz[3*p+2]
        #translate to origin
        y = y - my
        z = z - mz
        #rotate
        yneu = y * c - z * s
        zneu = y * s + z * c
        #translate back to origin
        y = yneu + my
        z = zneu+ mz
        xyz[3*p+1] = y
        xyz[3*p+2] = z
    xy = conv32()
    for k in range (0,len(xyz)//3):
        for m in range (0,len(xyz)//3):
            abstand = (round(math.sqrt((xyz[3*k]-xyz[3*m])**2+(xyz[3*k+1]-xyz[3*m+1])**2+(xyz[3*k+2]-xyz[3*m+2])**2)))
            #print(abstand)
            if (abs(abstand-2*phi) < 5):
                canvas1.create_line(xy[2*k],xy[2*k+1],xy[2*m],xy[2*m+1], fill = 'green')
    return(xyz)

def roty(deg):
    canvas1.delete(ALL)
    rad = deg/180*math.pi
    c = math.cos(rad)
    s = math.sin(rad)
    for p in range(0,len(xyz)//3):
        x = xyz[3*p]
        z = xyz[3*p+2]
        #translate to origin
        x = x - mx
        z = z - mz
        #rotate
        xneu = x * c - z * s
        zneu = x * s + z * c
        #translate back to origin
        x = xneu + mx
        z = zneu+ mz
        xyz[3*p] = x
        xyz[3*p+2] = z
    xy = conv32()
    for k in range (0,len(xyz)//3):
        for m in range (0,len(xyz)//3):
            abstand = (round(math.sqrt((xyz[3*k]-xyz[3*m])**2+(xyz[3*k+1]-xyz[3*m+1])**2+(xyz[3*k+2]-xyz[3*m+2])**2)))
            #print(abstand)
            if (abs(abstand-2*phi) < 5):
                canvas1.create_line(xy[2*k],xy[2*k+1],xy[2*m],xy[2*m+1], fill = 'green')
    return(xyz)

def rotz(deg):
    canvas1.delete(ALL)
    rad = deg/180*math.pi
    c = math.cos(rad)
    s = math.sin(rad)
    for p in range(0,len(xyz)//3):
        x = xyz[3*p]
        y = xyz[3*p+1]
        #translate to origin
        x = x - mx
        y = y - my
        #rotate
        xneu = x * c - y * s
        yneu = x * s + y * c
        #translate back to origin
        x = xneu + mx
        y = yneu+ my
        xyz[3*p] = x
        xyz[3*p+1] = y
    xy = conv32()
    for k in range (0,len(xyz)//3):
        for m in range (0,len(xyz)//3):
            abstand = (round(math.sqrt((xyz[3*k]-xyz[3*m])**2+(xyz[3*k+1]-xyz[3*m+1])**2+(xyz[3*k+2]-xyz[3*m+2])**2)))
            #print(abstand)
            if (abs(abstand-2*phi) < 5):
                canvas1.create_line(xy[2*k],xy[2*k+1],xy[2*m],xy[2*m+1], fill = 'green')
    return(xyz)


canvas1 = Canvas(master, width = 800, height = 600)
canvas1.pack()

button1 = Button(master, text = 'zeichnen', command = draw())
button1.pack()

#buttonx = Button(master, text = 'rot x', command = rotx(10))
#buttonx.pack()

#buttony = Button(master, text = 'rot y', command = roty(10))
#buttony.pack()

#buttonz = Button(master, text = 'rot z', command = rotz(10))
#buttonz.pack()

