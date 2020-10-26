from tkinter import *
import time
import math

master = Tk()

mx = 400
my = 300
mz = 0
a = 200
gold = ((math.sqrt(5)-1)/2)
phi = (gold*a)
phim = a/gold

check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
check4 = IntVar()
check5 = IntVar()
check6 = IntVar()

class object3d:
    name = 'Ikosaeder'
    xyz = [mx,my-a,mz+phi, mx,my-a,mz-phi, mx,my+a,mz+phi, mx,my+a,mz-phi, mx+phi,my,mz+a, mx+phi,my,mz-a, mx-phi,my,mz+a, mx-phi,my,mz-a, mx+a,my-phi,mz, mx+a,my+phi,mz, mx-a,my-phi,mz, mx-a,my+phi,mz]
    xy = []
    sl = 2 * phi
    ek = 3 #anzahl der ecken pro seitenfläche
    
obj = object3d()


def keplerstern():
    a = 150
    canvas1.delete(ALL)
    obj.name = 'Keplerstern'
    obj.xyz = [mx+a,my,mz, mx,my+a,mz, mx,my,mz+a, mx-a,my,mz, mx,my-a,mz, mx,my,mz-a,  mx+a,my-a,mz-a, mx-a,my+a,mz-a, mx-a,my-a,mz+a, mx-a,my+a,mz+a, mx+a,my-a,mz+a, mx+a,my+a,mz-a, mx-a,my-a,mz-a, mx+a,my+a,mz+a]
    obj.sl = b * math.sqrt(2)
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    zeichnen()

def oktaeder():
    a = 200
    canvas1.delete(ALL)
    obj.name = 'Oktaeder'
    obj.xyz = [mx+a,my,mz, mx,my+a,mz, mx,my,mz+a, mx-a,my,mz, mx,my-a,mz, mx,my,mz-a]
    obj.sl = math.sqrt(2)*a
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    zeichnen()
    
def ikosaeder():
    a = 200
    canvas1.delete(ALL)
    obj.name = 'Ikosaeder'
    obj.xyz = [mx,my-a,mz+phi, mx,my-a,mz-phi, mx,my+a,mz+phi, mx,my+a,mz-phi, mx+phi,my,mz+a, mx+phi,my,mz-a, mx-phi,my,mz+a, mx-phi,my,mz-a, mx+a,my-phi,mz, mx+a,my+phi,mz, mx-a,my-phi,mz, mx-a,my+phi,mz]
    obj.sl = 2*phi
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    zeichnen()

def dodekaeder():
    a = 150
    phi = (gold*a)
    phim = a/gold
    canvas1.delete(ALL)
    obj.name = 'Dodekaeder'
    obj.xyz = [mx+a,my+a,mz+a, mx-a,my+a,mz+a, mx+a,my-a,mz+a, mx+a,my+a,mz-a, mx+a,my-a,mz-a, mx-a,my+a,mz-a, mx-a,my-a,mz+a, mx-a,my-a,mz-a, mx+phim,my+phi,mz, mx-phim,my+phi,mz, mx-phim,my-phi,mz, mx+phim,my-phi,mz, mx,my+phim,mz+phi, mx,my+phim,mz-phi, mx,my-phim,mz-phi, mx,my-phim,mz+phi, mx+phi,my,mz+phim, mx+phi,my,mz-phim, mx-phi,my,mz+phim, mx-phi,my,mz-phim]
    obj.sl = 2*phi
    obj.ek = 5
    print(str(obj.name) +' wird geladen')
    zeichnen()
    
def conv32():
    obj.xy = []
    for i in range (0,len(obj.xyz)//3):
        obj.xy.append(obj.xyz[3*i]+obj.xyz[3*i+2]/2/math.sqrt(2))
        obj.xy.append(obj.xyz[3*i+1]-obj.xyz[3*i+2]/2/math.sqrt(2))    
    return obj.xy

def drawedges():
    canvas1.delete(ALL)
    obj.xy = conv32()
    print('obj.xyz: ' + str(obj.xyz))
    print('obj.xy: ' + str(obj.xy))
    for k in range (0,len(obj.xyz)//3):
        for m in range (0,len(obj.xyz)//3):
            abstand = (round(math.sqrt((obj.xyz[3*k]-obj.xyz[3*m])**2+(obj.xyz[3*k+1]-obj.xyz[3*m+1])**2+(obj.xyz[3*k+2]-obj.xyz[3*m+2])**2)))
            #print(abstand)
            if (abs(abstand-obj.sl) < 5):
                canvas1.create_line(obj.xy[2*k],obj.xy[2*k+1],obj.xy[2*m],obj.xy[2*m+1], fill = 'blue')

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
    for p in range(0,len(obj.xyz)//3):
        yalt = obj.xyz[3*p+1]
        zalt = obj.xyz[3*p+2]
        obj.xyz[3*p+1] = ((yalt - my) * c - (zalt - mz) * s) + my
        obj.xyz[3*p+2] = ((yalt - my) * s + (zalt - mz) * c) + mz
    obj.xy = conv32()
    zeichnen()
    print('Drehungswinkel: ' + str(deg))
    return(obj.xyz)

def roty(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    rad = deg/180*math.pi
    c = math.cos(rad)
    s = math.sin(rad)
    for p in range(0,len(obj.xyz)//3):
        xalt = obj.xyz[3*p]
        zalt = obj.xyz[3*p+2]
        obj.xyz[3*p] = ((xalt - mx) * c - (zalt - mz) * s) + mx
        obj.xyz[3*p+2] = ((xalt - mx) * s + (zalt - mz) * c) + mz
    obj.xy = conv32()
    zeichnen()
    print('Drehungswinkel: ' + str(deg))
    return(obj.xyz)

def rotz(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    rad = deg/180*math.pi
    c = math.cos(rad)
    s = math.sin(rad)
    for p in range(0,len(obj.xyz)//3):
        xalt = obj.xyz[3*p]
        yalt = obj.xyz[3*p+1]
        obj.xyz[3*p] = ((xalt - mx) * c - (yalt - my) * s) + mx
        obj.xyz[3*p+1] = ((xalt - mx) * s + (yalt - my) * c) + my
    obj.xy = conv32()
    zeichnen()
    print('Drehungswinkel: ' + str(deg))
    return(obj.xyz)




#sortieren nach kleinstem x abstand zu mx
def xsort():
    for m in range(0,len(obj.xyz)//3):
        for n in range (0, len(obj.xyz)//3):
            if ((abs(obj.xyz[3*m]-mx) > abs(obj.xyz[3*n]-mx)) and (m<n)):
                obj.xyz[3*m],obj.xyz[3*n] = obj.xyz[3*n],obj.xyz[3*m]
                obj.xyz[3*m+1],obj.xyz[3*n+1] = obj.xyz[3*n+1],obj.xyz[3*m+1]
                obj.xyz[3*m+2],obj.xyz[3*n+2] = obj.xyz[3*n+2],obj.xyz[3*m+2]
    print('obj.xyz sortiert: ' + str(obj.xyz))
    return(obj.xyz)   
    

#sortieren nach kleinstem y abstand zu my
def ysort():
    for m in range(0,len(obj.xyz)//3):
        for n in range (0, len(obj.xyz)//3):
            if ((abs(obj.xyz[3*m+1]-my) > abs(obj.xyz[3*n+1]-my)) and (m<n)):
                obj.xyz[3*m],obj.xyz[3*n] = obj.xyz[3*n],obj.xyz[3*m]
                obj.xyz[3*m+1],obj.xyz[3*n+1] = obj.xyz[3*n+1],obj.xyz[3*m+1]
                obj.xyz[3*m+2],obj.xyz[3*n+2] = obj.xyz[3*n+2],obj.xyz[3*m+2]
    print('obj.xyz sortiert: ' + str(obj.xyz))
    return(obj.xyz)



#sortieren nach z
def zsort():
    for m in range(0,len(obj.xyz)//3):
        for n in range (0, len(obj.xyz)//3):
            if check4.get() == 0:
                if ((obj.xyz[3*m+2] < obj.xyz[3*n+2]) and (m>n)):
                    obj.xyz[3*m],obj.xyz[3*n] = obj.xyz[3*n],obj.xyz[3*m]
                    obj.xyz[3*m+1],obj.xyz[3*n+1] = obj.xyz[3*n+1],obj.xyz[3*m+1]
                    obj.xyz[3*m+2],obj.xyz[3*n+2] = obj.xyz[3*n+2],obj.xyz[3*m+2]
            else:
                if ((obj.xyz[3*m+2] > obj.xyz[3*n+2]) and (m>n)):
                    obj.xyz[3*m],obj.xyz[3*n] = obj.xyz[3*n],obj.xyz[3*m]
                    obj.xyz[3*m+1],obj.xyz[3*n+1] = obj.xyz[3*n+1],obj.xyz[3*m+1]
                    obj.xyz[3*m+2],obj.xyz[3*n+2] = obj.xyz[3*n+2],obj.xyz[3*m+2]
    print('obj.xyz sortiert: ' + str(obj.xyz))
    return(obj.xyz)

def drawfaces():
    #punkte sortieren
    obj.xyz = xsort()
    obj.xyz = ysort()
    obj.xyz = zsort()
    #zeichnen
    for p in range (0,len(obj.xyz)//3):
        for q in range (0,len(obj.xyz)//3):
            pq = math.sqrt((obj.xyz[3*p]-obj.xyz[3*q])**2+(obj.xyz[3*p+1]-obj.xyz[3*q+1])**2+(obj.xyz[3*p+2]-obj.xyz[3*q+2])**2)
            if (abs(pq-obj.sl) < 10):
                for r in range (0,len(obj.xyz)//3):
                    pr = math.sqrt((obj.xyz[3*p]-obj.xyz[3*r])**2+(obj.xyz[3*p+1]-obj.xyz[3*r+1])**2+(obj.xyz[3*p+2]-obj.xyz[3*r+2])**2)
                    if (abs(pr-obj.sl) < 10):
                        qr = math.sqrt((obj.xyz[3*q]-obj.xyz[3*r])**2+(obj.xyz[3*q+1]-obj.xyz[3*r+1])**2+(obj.xyz[3*q+2]-obj.xyz[3*r+2])**2)
                        if (abs(qr-obj.sl) < 10):
                            #umwandeln in 2d
                            obj.xy = conv32()
                            canvas1.create_polygon(obj.xy[2*p],obj.xy[2*p+1],obj.xy[2*q],obj.xy[2*q+1],obj.xy[2*r],obj.xy[2*r+1], fill = 'yellow', outline = 'blue')
    

def zeichnen():
    if check1.get() == 1:
        drawedges()
    if check2.get() == 1:
        drawfaces()    
    
canvas1 = Canvas(master, width = 800, height = 600)
canvas1.grid(row = 0,column = 0, rowspan = 11, columnspan = 1, padx = 15, pady = 15)

editdeg = Entry(master)
editdeg.grid(row = 2,column = 1, columnspan = 3, padx = 15, pady = 15)
editdeg.insert(10,'10')

cbedges = Checkbutton(master, text = 'Kanten zeichnen', var = check1, command = lambda:(cbfaces.deselect(), cbedges.select(), zeichnen()))
cbedges.grid(row = 0, column = 1, columnspan = 3, padx = 15, pady = 15)

cbfaces = Checkbutton(master, text = 'Flächen zeichnen', var = check2, command = lambda:(cbedges.deselect(), cbfaces.select(), zeichnen()))
cbfaces.grid(row = 1, column = 1, columnspan = 3, padx = 15, pady = 15)
cbfaces.select()
zeichnen()

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

buttonkep = Button(master, text = 'kep', command = keplerstern)
buttonkep.grid(row = 5, column = 3, columnspan = 1,pady = 15, padx = 15)

cbiko = Checkbutton(master, text = 'Ikosaeder zeichnen', var = check3, command = lambda:(cbiko.select(), cbokt.deselect(), cbkep.deselect(), cbdod.deselect(), ikosaeder()))
cbiko.grid(row = 6, column = 1, columnspan = 2, pady = 15)
cbiko.select()

cbokt = Checkbutton(master, text = 'Oktaeder zeichnen', var = check4, command = lambda:(cbokt.select(), cbiko.deselect(), cbkep.deselect(), cbdod.deselect(), oktaeder()))
cbokt.grid(row = 7, column = 1, columnspan = 2, pady = 15)

cbkep = Checkbutton(master, text = 'Keplerstern zeichnen', var = check5, command = lambda:(cbkep.select(), cbiko.deselect(), cbokt.deselect(), cbdod.deselect(), keplerstern()))
cbkep.grid(row = 8, column = 1, columnspan = 2, pady = 15)

cbdod = Checkbutton(master, text = 'Dodekaeder zeichnen', var = check6, command = lambda:(cbdod.select(), cbiko.deselect(), cbokt.deselect(), cbkep.deselect(), dodekaeder()))
cbdod.grid(row = 9, column = 1, columnspan = 2, pady = 15)

buttonclose = Button(master, text = 'close', command = quit)
buttonclose.grid(row = 10, column = 1, columnspan = 3,padx = 15, pady = 15)




