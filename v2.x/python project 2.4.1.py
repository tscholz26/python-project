from tkinter import *
import time
import math

master = Tk()

gold = ((math.sqrt(5)-1)/2)

mx = 400
my = 300
mz = 0
a = 200
phi = round(gold*a)
xy = []
xyz = []
sl = 0

# Würfel:
#xyz = [mx-a,my-a,mz-a, mx-a,my-a,mz+a, mx-a,my+a,mz-a, mx+a,my-a,mz-a, mx+a,my+a,mz-a, mx+a,my-a,mz+a, mx-a,my+a,mz+a, mx+a,my+a,mz+a]
#sl = 2*a
def wuerfel():
    xyz.delete
    xyz = [mx,my,mz, mx+a,my,mz, mx,my+a,mz, mx,my,mz+a, mx+a,my+a,mz, mx+a,my,mz+a, mx,my+a,mz+a, mx+a,my+a,mz+a]
    sl = 2*a
    print('Würfel wird geladen')
    draw()

# Oktaeder
#xyz = [mx+a,my,mz, mx,my+a,mz, mx,my,mz+a, mx-a,my,mz, mx,my-a,mz, mx,my,mz-a]
#sl = math.sqrt(2)*a
def oktaeder():
    xyz = [mx+a,my,mz, mx,my+a,mz, mx,my,mz+a, mx-a,my,mz, mx,my-a,mz, mx,my,mz-a]
    sl = math.sqrt(2)*a
    print('Oktaeder wird geladen')
    draw()
    
# Ikosaeder:
xyz = [mx,my-a,mz+phi, mx,my-a,mz-phi, mx,my+a,mz+phi, mx,my+a,mz-phi, mx+phi,my,mz+a, mx+phi,my,mz-a, mx-phi,my,mz+a, mx-phi,my,mz-a, mx+a,my-phi,mz, mx+a,my+phi,mz, mx-a,my-phi,mz, mx-a,my+phi,mz]
sl = 2*phi
def ikosaeder():
    xyz = [mx,my-a,mz+phi, mx,my-a,mz-phi, mx,my+a,mz+phi, mx,my+a,mz-phi, mx+phi,my,mz+a, mx+phi,my,mz-a, mx-phi,my,mz+a, mx-phi,my,mz-a, mx+a,my-phi,mz, mx+a,my+phi,mz, mx-a,my-phi,mz, mx-a,my+phi,mz]
    sl = 2*phi
    print('Ikosaeder wird geladen')
    draw()
    
def conv32():
    xy = []
    for i in range (0,len(xyz)//3):
        xy.append(xyz[3*i]+round(xyz[3*i+2]/2/math.sqrt(2)))
        xy.append(xyz[3*i+1]-round(xyz[3*i+2]/2/math.sqrt(2)))      
    return xy

def draw():
    canvas1.delete(ALL)
    xy = conv32()
    print('xyz: ' + str(xyz))
    print('xy: ' + str(xy))
    for k in range (0,len(xyz)//3):
        for m in range (0,len(xyz)//3):
            abstand = (round(math.sqrt((xyz[3*k]-xyz[3*m])**2+(xyz[3*k+1]-xyz[3*m+1])**2+(xyz[3*k+2]-xyz[3*m+2])**2)))
            #print(abstand)
            if (abs(abstand-sl) < 5):
                canvas1.create_line(xy[2*k],xy[2*k+1],xy[2*m],xy[2*m+1], fill = 'blue')

def getdeg():
    if editdeg.get() != '':
        deg = int(editdeg.get())
    else:
        deg = 10
    return(deg)

def rotx(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    rad = deg/180*math.pi
    c = math.cos(rad)
    s = math.sin(rad)
    for p in range(0,len(xyz)//3):
        yalt = xyz[3*p+1]
        zalt = xyz[3*p+2]
        xyz[3*p+1] = ((yalt - my) * c - (zalt - mz) * s) + my
        xyz[3*p+2] = ((yalt - my) * s + (zalt - mz) * c) + mz
    xy = conv32()
    drawfaces(xy,xyz)
    print('Drehungswinkel: ' + str(deg))
    return(xyz)

def roty(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    rad = deg/180*math.pi
    c = math.cos(rad)
    s = math.sin(rad)
    for p in range(0,len(xyz)//3):
        xalt = xyz[3*p]
        zalt = xyz[3*p+2]
        xyz[3*p] = ((xalt - mx) * c - (zalt - mz) * s) + mx
        xyz[3*p+2] = ((xalt - mx) * s + (zalt - mz) * c) + mz
    xy = conv32()
    drawfaces(xy,xyz)
    print('Drehungswinkel: ' + str(deg))
    return(xyz)

def rotz(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    rad = deg/180*math.pi
    c = math.cos(rad)
    s = math.sin(rad)
    for p in range(0,len(xyz)//3):
        xalt = xyz[3*p]
        yalt = xyz[3*p+1]
        xyz[3*p] = ((xalt - mx) * c - (yalt - my) * s) + mx
        xyz[3*p+1] = ((xalt - mx) * s + (yalt - my) * c) + my
    xy = conv32()
    drawfaces(xy,xyz)
    print('Drehungswinkel: ' + str(deg))
    return(xyz)




#sortieren nach kleinstem x abstand zu mx
def xsort(xyz):
    for m in range(0,len(xyz)//3):
        for n in range (0, len(xyz)//3):
            if ((abs(xyz[3*m]-mx) > abs(xyz[3*n]-mx)) and (m<n)):
                xyz[3*m],xyz[3*n] = xyz[3*n],xyz[3*m]
                xyz[3*m+1],xyz[3*n+1] = xyz[3*n+1],xyz[3*m+1]
                xyz[3*m+2],xyz[3*n+2] = xyz[3*n+2],xyz[3*m+2]
    print('xyz sortiert: ' + str(xyz))
    return(xyz)   
    

#sortieren nach kleinstem y abstand zu my
def ysort(xyz):
    for m in range(0,len(xyz)//3):
        for n in range (0, len(xyz)//3):
            if ((abs(xyz[3*m+1]-my) > abs(xyz[3*n+1]-my)) and (m<n)):
                xyz[3*m],xyz[3*n] = xyz[3*n],xyz[3*m]
                xyz[3*m+1],xyz[3*n+1] = xyz[3*n+1],xyz[3*m+1]
                xyz[3*m+2],xyz[3*n+2] = xyz[3*n+2],xyz[3*m+2]
    print('xyz sortiert: ' + str(xyz))
    return(xyz)



#sortieren nach z
def zsort(xyz):
    for m in range(0,len(xyz)//3):
        for n in range (0, len(xyz)//3):
            if ((xyz[3*m+2] > xyz[3*n+2]) and (m>n)):
                xyz[3*m],xyz[3*n] = xyz[3*n],xyz[3*m]
                xyz[3*m+1],xyz[3*n+1] = xyz[3*n+1],xyz[3*m+1]
                xyz[3*m+2],xyz[3*n+2] = xyz[3*n+2],xyz[3*m+2]
    print('xyz sortiert: ' + str(xyz))
    return(xyz)

def drawfaces(xy,xyz):
    #punkte sortieren
    xyz = xsort(xyz)
    xyz = ysort(xyz)
    xyz = zsort(xyz)
    #zeichnen
    for p in range (0,len(xyz)//3):
        for q in range (0,len(xyz)//3):
            pq = math.sqrt((xyz[3*p]-xyz[3*q])**2+(xyz[3*p+1]-xyz[3*q+1])**2+(xyz[3*p+2]-xyz[3*q+2])**2)
            if (abs(pq-sl) < 10):
                for r in range (0,len(xyz)//3):
                    pr = math.sqrt((xyz[3*p]-xyz[3*r])**2+(xyz[3*p+1]-xyz[3*r+1])**2+(xyz[3*p+2]-xyz[3*r+2])**2)
                    if (abs(pr-sl) < 10):
                        qr = math.sqrt((xyz[3*q]-xyz[3*r])**2+(xyz[3*q+1]-xyz[3*r+1])**2+(xyz[3*q+2]-xyz[3*r+2])**2)
                        if (abs(qr-sl) < 10):
                            #umwandeln in 2d
                            xy = conv32()
                            canvas1.create_polygon(xy[2*p],xy[2*p+1],xy[2*q],xy[2*q+1],xy[2*r],xy[2*r+1], fill = 'yellow', outline = 'black')
    

def alles():
    drawfaces(xy,xyz)
    
    
canvas1 = Canvas(master, width = 800, height = 600)
canvas1.grid(row = 0,column = 0, rowspan = 7, columnspan = 1, padx = 15, pady = 15)

editdeg = Entry(master)
editdeg.grid(row = 2,column = 1, columnspan = 3, padx = 15, pady = 15)
editdeg.insert(10,'10')

button1 = Button(master, text = 'Kanten zeichnen', command = draw)
button1.grid(row = 0, column = 1, columnspan = 3, padx = 15, pady = 15)

button2 = Button(master, text = 'Flächen zeichnen', command = alles)
button2.grid(row = 1, column = 1, columnspan = 3, padx = 15, pady = 15)


buttonx = Button(master, text = 'rot x', command = lambda: rotx(1))
buttonx.grid(row = 3, column = 1, padx = 15, pady = 15)

buttony = Button(master, text = 'rot y', command = lambda: roty(1))
buttony.grid(row = 3, column = 2, padx = 15,  pady = 15)

buttonz = Button(master, text = 'rot z', command = lambda: rotz(1))
buttonz.grid(row = 3, column = 3, padx = 15,  pady = 15)

buttonmx = Button(master, text = 'rot -x', command = lambda: rotx(-1))
buttonmx.grid(row = 4, column = 1, padx = 15,  pady = 15)

buttonmy = Button(master, text = 'rot -y', command = lambda: roty(-1))
buttonmy.grid(row = 4, column = 2, padx = 15,  pady = 15)

buttonmz = Button(master, text = 'rot -z', command = lambda: rotz(-1))
buttonmz.grid(row = 4, column = 3, padx = 15,   pady = 15)

buttoniko = Button(master, text = 'iko', command = ikosaeder)
buttoniko.grid(row = 5, column = 1, columnspan = 1,pady = 15, padx = 15)

buttonokt = Button(master, text = 'okt', command = oktaeder)
buttonokt.grid(row = 5, column = 2, columnspan = 1,pady = 15, padx = 15)

buttonwu = Button(master, text = 'wurf', command = wuerfel)
buttonwu.grid(row = 5, column = 3, columnspan = 1,pady = 15, padx = 15)


buttonclose = Button(master, text = 'close', command = quit)
buttonclose.grid(row = 6, column = 1, columnspan = 3,padx = 15, pady = 15)




