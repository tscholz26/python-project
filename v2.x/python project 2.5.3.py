from tkinter import *
import time
import math

master = Tk()

mx = 400
my = 300
mz = 0
gold = ((math.sqrt(5)-1)/2)
facelist = list()

check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
check4 = IntVar()
check5 = IntVar()
check6 = IntVar()
check7 = IntVar()
check8 = IntVar()

class object3d:
    name = 'Ikosaeder'
    xyz = []
    xy = []
    sl = 2.5
    ek = IntVar() #anzahl der ecken pro seitenfläche
    a = IntVar()

obj = object3d()

class fivevar:
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    

def keplerstern():
    canvas1.delete(ALL)
    obj.name = 'Keplerstern'
    obj.a = 150
    obj.xyz = [mx+obj.a,my,mz, mx,my+obj.a,mz, mx,my,mz+obj.a, mx-obj.a,my,mz, mx,my-obj.a,mz, mx,my,mz-obj.a,  mx+obj.a,my-obj.a,mz-obj.a, mx-obj.a,my+obj.a,mz-obj.a, mx-obj.a,my-obj.a,mz+obj.a, mx-obj.a,my+obj.a,mz+obj.a, mx+obj.a,my-obj.a,mz+obj.a, mx+obj.a,my+obj.a,mz-obj.a, mx-obj.a,my-obj.a,mz-obj.a, mx+obj.a,my+obj.a,mz+obj.a]
    obj.sl = obj.a * math.sqrt(2)
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    zeichnen()

def oktaeder():
    canvas1.delete(ALL)
    obj.name = 'Oktaeder'
    obj.a = 200
    obj.xyz = [mx+obj.a,my,mz, mx,my+obj.a,mz, mx,my,mz+obj.a, mx-obj.a,my,mz, mx,my-obj.a,mz, mx,my,mz-obj.a]
    obj.sl = math.sqrt(2)*obj.a
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    zeichnen()
    
def ikosaeder():
    canvas1.delete(ALL)
    obj.name = 'Ikosaeder'
    obj.a = 200
    phi = (gold*obj.a)
    obj.xyz = [mx,my-obj.a,mz+phi, mx,my-obj.a,mz-phi, mx,my+obj.a,mz+phi, mx,my+obj.a,mz-phi, mx+phi,my,mz+obj.a, mx+phi,my,mz-obj.a, mx-phi,my,mz+obj.a, mx-phi,my,mz-obj.a, mx+obj.a,my-phi,mz, mx+obj.a,my+phi,mz, mx-obj.a,my-phi,mz, mx-obj.a,my+phi,mz]
    obj.sl = 2*phi
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    zeichnen()

def dodekaeder():
    canvas1.delete(ALL)
    obj.name = 'Dodekaeder'
    obj.a = 150
    phi = (gold*obj.a)
    phim = obj.a/gold
    obj.xyz = [mx+obj.a,my+obj.a,mz+obj.a, mx-obj.a,my+obj.a,mz+obj.a, mx+obj.a,my-obj.a,mz+obj.a, mx+obj.a,my+obj.a,mz-obj.a, mx+obj.a,my-obj.a,mz-obj.a, mx-obj.a,my+obj.a,mz-obj.a, mx-obj.a,my-obj.a,mz+obj.a, mx-obj.a,my-obj.a,mz-obj.a, mx+phim,my+phi,mz, mx-phim,my+phi,mz, mx-phim,my-phi,mz, mx+phim,my-phi,mz, mx,my+phim,mz+phi, mx,my+phim,mz-phi, mx,my-phim,mz-phi, mx,my-phim,mz+phi, mx+phi,my,mz+phim, mx+phi,my,mz-phim, mx-phi,my,mz+phim, mx-phi,my,mz-phim]
    obj.sl = 2*phi
    obj.ek = 5
    print(str(obj.name) +' wird geladen')
    zeichnen()

def wuerfel():
    canvas1.delete(ALL)
    obj.name = 'Würfel'
    obj.a = 150
    obj.xyz = [mx-obj.a,my-obj.a,mz-obj.a, mx+obj.a,my+obj.a,mz-obj.a, mx+obj.a,my-obj.a,mz+obj.a, mx-obj.a,my+obj.a,mz+obj.a, mx+obj.a,my-obj.a,mz-obj.a, mx-obj.a,my+obj.a,mz-obj.a, mx-obj.a,my-obj.a,mz+obj.a, mx+obj.a,my+obj.a,mz+obj.a]
    obj.sl = 2*obj.a
    obj.ek = 4
    print(str(obj.name) +' wird geladen')
    zeichnen()
    
def z42():
    canvas1.delete(ALL)
    obj.name = '42'
    obj.a = 200
    obj.xyz =  []
    obj.sl = obj.a
    obj.ek = 4
    print(str(obj.name) +' wird geladen')
    zeichnen()
    
def conv32():
    obj.xy = []
    for i in range (0,len(obj.xyz)//3):
        obj.xy.append(obj.xyz[3*i]+obj.xyz[3*i+2]/2/math.sqrt(2))
        obj.xy.append(obj.xyz[3*i+1]-obj.xyz[3*i+2]/2/math.sqrt(2))
    return obj.xy

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

#bubblesort von pqr nach größtem vn
def bubblesort(a,b,c,d,e):
    #in array transferieren
    arraypqr = []
    arraypqr.append(a)
    arraypqr.append(b)
    arraypqr.append(c)
    arraypqr.append(d)
    arraypqr.append(e)
    #array sortieren
    for m in range(0,len(arraypqr)):
        for n in range(0,len(arraypqr)):
            if (arraypqr[m] > arraypqr[n]) and (m > n):
                arraypqr[m],arraypqr[n] = arraypqr[n],arraypqr[m]
    #zurück transferieren
    pqr = fivevar()
    pqr.v1 = arraypqr[0]
    pqr.v2 = arraypqr[1]
    pqr.v3 = arraypqr[2]
    pqr.v4 = arraypqr[3]
    pqr.v5 = arraypqr[4]
    return(pqr)

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
                
def drawfaces():
    facelist.clear()
    #punkte sortieren
    #obj.xyz = xsort()
    #obj.xyz = ysort()
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
                            if obj.ek > 4:
                                print('ek > 4')
                            else:
                                pqr = bubblesort(p,q,r,0,0)
                                if len(facelist) == 0:
                                    facelist.append(100)
                                    facelist.append(100)
                                    facelist.append(100)
                                    facelist.append(100)
                                    facelist.append(100)
                                draw = IntVar()
                                draw = 1
                                for c in range(0,len(facelist)//5):
                                    if (facelist[5*c] == pqr.v1) and (facelist[5*c+1] == pqr.v2) and (facelist[5*c+2] == pqr.v3) and (facelist[5*c+3] == pqr.v4) and (facelist[5*c+4] == pqr.v5):
                                        draw = 0
                                if draw == 1:
                                    facelist.append(pqr.v1)
                                    facelist.append(pqr.v2)
                                    facelist.append(pqr.v3)
                                    facelist.append(pqr.v4)
                                    facelist.append(pqr.v5)
                                    obj.xy = conv32()
                                    #finales zeichnen
                                    canvas1.create_polygon(obj.xy[2*p],obj.xy[2*p+1],obj.xy[2*q],obj.xy[2*q+1],obj.xy[2*r],obj.xy[2*r+1], fill = 'yellow', outline = 'blue')                                
                      
def zeichnen():
    if check1.get() == 1:
        drawedges()
    if check2.get() == 1:
        drawfaces()

def deselectall():
    cbiko.deselect()
    cbokt.deselect()
    cbkep.deselect()
    cbdod.deselect()
    cbwur.deselect()
    cbz42.deselect()
    
canvas1 = Canvas(master, width = 800, height = 600)
canvas1.grid(row = 0,column = 0, rowspan = 12, columnspan = 1, padx = 15, pady = 15)

editdeg = Entry(master)
editdeg.grid(row = 2,column = 1, columnspan = 3, padx = 15, pady = 15)
editdeg.insert(10,'10')

cbedges = Checkbutton(master, text = 'Kanten zeichnen', var = check1, command = lambda:(cbfaces.deselect(), cbedges.select(), zeichnen()))
cbedges.grid(row = 0, column = 1, columnspan = 3, padx = 15, pady = 15)

cbfaces = Checkbutton(master, text = 'Flächen zeichnen', var = check2, command = lambda:(cbedges.deselect(), cbfaces.select(), zeichnen()))
cbfaces.grid(row = 1, column = 1, columnspan = 3, padx = 15, pady = 15)

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

cbiko = Checkbutton(master, text = 'Ikosaeder zeichnen', var = check3, command = lambda:(deselectall(), cbiko.select(), ikosaeder()))
cbiko.grid(row = 5, column = 1, columnspan = 2, pady = 15)

cbokt = Checkbutton(master, text = 'Oktaeder zeichnen', var = check4, command = lambda:(deselectall(), cbokt.select(), oktaeder()))
cbokt.grid(row = 6, column = 1, columnspan = 2, pady = 15)

cbkep = Checkbutton(master, text = 'Keplerstern zeichnen', var = check5, command = lambda:(deselectall(), cbkep.select(), keplerstern()))
cbkep.grid(row = 7, column = 1, columnspan = 2, pady = 15)

cbdod = Checkbutton(master, text = 'Dodekaeder zeichnen', var = check6, command = lambda:(deselectall(), cbdod.select(), dodekaeder()))
cbdod.grid(row = 8, column = 1, columnspan = 2, pady = 15)

cbwur = Checkbutton(master, text = 'Würfel zeichnen', var = check7, command = lambda:(deselectall(), cbwur.select(), wuerfel()))
cbwur.grid(row = 9, column = 1, columnspan = 2, pady = 15)

cbz42 = Checkbutton(master, text = 'z42 zeichnen', var = check8, command = lambda:(deselectall(), cbz42.select(), z42()))
cbz42.grid(row = 10, column = 1, columnspan = 2, pady = 15)

buttonclose = Button(master, text = 'close', command = quit)
buttonclose.grid(row = 11, column = 1, columnspan = 3,padx = 15, pady = 15)

cbfaces.select()
cbiko.select()
ikosaeder()



