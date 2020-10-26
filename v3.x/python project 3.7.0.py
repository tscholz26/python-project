from tkinter import *
import time
import math

master = Tk()


mx = 400
my = 325

gold = ((math.sqrt(5)-1)/2)
facelist = list()

checkedges = IntVar()
checkfaces = IntVar()
checkiko = IntVar()
checkkep = IntVar()
checkdod = IntVar()
checkrep = IntVar()
checkdeg = IntVar()
checkrad = IntVar()
    
class object3d:
    name = 'Ikosaeder'
    xyz = []
    xy = []
    sl = 2.5
    ek = IntVar() #anzahl der ecken pro seitenfläche
    a = IntVar()
    xspeed = IntVar()
    yspeed = IntVar()
    zspeed = IntVar()

obj = object3d()


def ikosaeder():
    canvas1.delete(ALL)
    obj.name = 'Ikosaeder'
    obj.a = 200
    phi = (gold*obj.a)
    obj.xyz = [0,-obj.a,phi, 0,-obj.a,-phi, 0,obj.a,phi, 0,obj.a,-phi, phi,0,obj.a, phi,0,-obj.a, -phi,0,obj.a, -phi,0,-obj.a, obj.a,-phi,0, obj.a,phi,0, -obj.a,-phi,0, 0-obj.a,phi,0]
    obj.sl = 2*phi
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D')
    #in startposition drehen für bessere optik
    rotx(1)
    rotx(1)
    resetspeeds()
    zeichnen()
    
def keplerstern():
    canvas1.delete(ALL)
    obj.name = 'Keplerstern'
    obj.a = 150
    obj.xyz = [obj.a,0,0, 0,obj.a,0, 0,0,obj.a, 0-obj.a,0,0, 0,0-obj.a,0, 0,0,-obj.a,
               obj.a,0-obj.a,-obj.a, 0-obj.a,obj.a,-obj.a, 0-obj.a,0-obj.a,obj.a, 0-obj.a,obj.a,obj.a, obj.a,0-obj.a,obj.a, obj.a,obj.a,-obj.a, 0-obj.a,0-obj.a,-obj.a, obj.a,obj.a,obj.a]
    obj.sl = obj.a * math.sqrt(2)
    #obj.sl = obj.a * 3
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D')
    #in startposition drehen für bessere optik
    rotx(40)
    roty(30)
    rotz(30)
    resetspeeds()
    zeichnen()
    
def dodekaeder():
    canvas1.delete(ALL)
    obj.name = 'Dodekaeder'
    obj.a = 130
    phi = (gold*obj.a)
    phim = obj.a/gold
    obj.xyz = [obj.a,obj.a,obj.a, 0-obj.a,obj.a,obj.a, obj.a,0-obj.a,obj.a, obj.a,obj.a,-obj.a, obj.a,0-obj.a,-obj.a, 0-obj.a,obj.a,-obj.a, 0-obj.a,0-obj.a,obj.a, 0-obj.a,0-obj.a,-obj.a, phim,phi,0, 0-phim,phi,0, 0-phim,0-phi,0, phim,0-phi,0, 0,phim,phi, 0,phim,-phi, 0,0-phim,-phi, 0,0-phim,phi, phi,0,phim, phi,0,-phim, 0-phi,0,phim, 0-phi,0,-phim]
    obj.sl = 2*phi
    obj.ek = 5
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D')
    #in startposition drehen für bessere optik
    rotx(1)
    rotx(1)
    roty(-1)
    resetspeeds()
    zeichnen()
    
master.title('Darstellung eines ' + obj.name + 's in 3D')
    
def conv32():
    obj.xy = []
    for i in range (0,len(obj.xyz)//3):
        distance = 3000
        #strahlensatz
        obj.xy.append(mx + (obj.xyz[3*i] * distance)/(obj.xyz[3*i+2] + distance))
        obj.xy.append(my + (obj.xyz[3*i+1] * distance)/(obj.xyz[3*i+2] + distance))
    return obj.xy




def getdeg():
    if editdeg.get() != '':
        deg = float(editdeg.get())
    else:
        deg = 10
    if checkdeg.get() == 1:
        deg = deg / 180 * math.pi
    return(deg)

def rotx(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    c = math.cos(deg)
    s = math.sin(deg)
    for p in range(0,len(obj.xyz)//3):
        yalt = obj.xyz[3*p+1]
        zalt = obj.xyz[3*p+2]
        obj.xyz[3*p+1] = ((yalt) * c - (zalt) * s)
        obj.xyz[3*p+2] = ((yalt) * s + (zalt) * c)
    obj.xy = conv32()
    zeichnen()    
    return(obj.xyz)

def roty(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    c = math.cos(deg)
    s = math.sin(deg)
    for p in range(0,len(obj.xyz)//3):
        xalt = obj.xyz[3*p]
        zalt = obj.xyz[3*p+2]
        obj.xyz[3*p] = ((xalt) * c - (zalt) * s)
        obj.xyz[3*p+2] = ((xalt) * s + (zalt) * c)
    obj.xy = conv32()
    zeichnen()
    return(obj.xyz)

def rotz(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    c = math.cos(deg)
    s = math.sin(deg)
    for p in range(0,len(obj.xyz)//3):
        xalt = obj.xyz[3*p]
        yalt = obj.xyz[3*p+1]
        obj.xyz[3*p] = ((xalt) * c - (yalt) * s)
        obj.xyz[3*p+1] = ((xalt) * s + (yalt) * c)
    obj.xy = conv32()
    zeichnen()
    return(obj.xyz)



def resetspeeds():
    obj.xspeed = 0
    obj.yspeed = 0
    obj.zspeed = 0

def setspeeds(char,speed):
    resetspeeds()
    if checkrep.get() == 1:
        if char == 'x':
            obj.xspeed = speed
        if char == 'y':
            obj.yspeed = speed
        if char == 'z':
            obj.zspeed = speed

def infiniterep():
    master.after(100, lambda:(rotx(obj.xspeed), roty(obj.yspeed), rotz(obj.zspeed), infiniterep()))

                 


#sortieren nach z
def zsort():
    for m in range(0,len(obj.xyz)//3):
        for n in range (0, len(obj.xyz)//3):
            if ((obj.xyz[3*m+2] < obj.xyz[3*n+2]) and (m>n)):
                obj.xyz[3*m],obj.xyz[3*n] = obj.xyz[3*n],obj.xyz[3*m]
                obj.xyz[3*m+1],obj.xyz[3*n+1] = obj.xyz[3*n+1],obj.xyz[3*m+1]
                obj.xyz[3*m+2],obj.xyz[3*n+2] = obj.xyz[3*n+2],obj.xyz[3*m+2]
    #print('obj.xyz sortiert: ' + str(obj.xyz))
    return(obj.xyz)

def getcolor(string):
    if string == 'fc':
        color = editfc.get()
    if string == 'oc':
        color = editoc.get()
    if color[0] == 'r' and not color == 'red':
            color = color[color.find('(')+1:color.find(')')]
            rstring = color[:color.find(',')]
            colorrest = color[color.find(',')+1:]
            gstring = colorrest[:colorrest.find(',')]
            bstring = colorrest[colorrest.find(',')+1:]
            rhex = hex(int(rstring))[2:]
            ghex = hex(int(gstring))[2:]
            bhex = hex(int(bstring))[2:]
            if len(rhex) == 1:
                rhex = '0' + rhex
            if len(ghex) == 1:
                ghex = '0' + ghex
            if len(bhex) == 1:
                bhex = '0' + bhex
            color = '#'+rhex+ghex+bhex
    return(color)

def drawedges():
    canvas1.delete(ALL)
    obj.xy = conv32()
    #print('obj.xyz: ' + str(obj.xyz))
    #print('obj.xy: ' + str(obj.xy))
    for k in range (0,len(obj.xyz)//3):
        for m in range (0,len(obj.xyz)//3):
            abstand = (round(math.sqrt((obj.xyz[3*k]-obj.xyz[3*m])**2+(obj.xyz[3*k+1]-obj.xyz[3*m+1])**2+(obj.xyz[3*k+2]-obj.xyz[3*m+2])**2)))
            #print(abstand)
            if (abs(abstand-obj.sl) < 5):
                canvas1.create_line(obj.xy[2*k],obj.xy[2*k+1],obj.xy[2*m],obj.xy[2*m+1], fill = getcolor('oc'))
                
def drawfaces():
    facelist.clear()
    #sortieren nach z
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
                        if (abs(qr-obj.sl) < 10) or ((obj.ek == 5) and (abs(qr-(2*obj.sl*math.sin(54/180*math.pi))) < 10)):
                            if obj.ek > 3:
                                for s in range (0,len(obj.xyz)//3):
                                    qs = math.sqrt((obj.xyz[3*q]-obj.xyz[3*s])**2+(obj.xyz[3*q+1]-obj.xyz[3*s+1])**2+(obj.xyz[3*q+2]-obj.xyz[3*s+2])**2)
                                    if (abs(qs-obj.sl) < 10):
                                        for t in range (0,len(obj.xyz)//3):
                                            st = math.sqrt((obj.xyz[3*s]-obj.xyz[3*t])**2+(obj.xyz[3*s+1]-obj.xyz[3*t+1])**2+(obj.xyz[3*s+2]-obj.xyz[3*t+2])**2)
                                            if (abs(st-obj.sl) < 10):
                                                rt = math.sqrt((obj.xyz[3*r]-obj.xyz[3*t])**2+(obj.xyz[3*r+1]-obj.xyz[3*t+1])**2+(obj.xyz[3*r+2]-obj.xyz[3*t+2])**2)
                                                if (abs(rt-obj.sl) < 10):
                                                    obj.xy = conv32()
                                                    provebvb()
                                                    canvas1.create_polygon(obj.xy[2*p],obj.xy[2*p+1], obj.xy[2*q],obj.xy[2*q+1], obj.xy[2*s],obj.xy[2*s+1],obj.xy[2*t],obj.xy[2*t+1], obj.xy[2*r],obj.xy[2*r+1], fill = getcolor('fc'), outline = getcolor('oc'))
                                                
                            else:
                                #p,q,r sortieren
                                abc = [p,q,r]
                                for f in range(0,obj.ek):
                                    for g in range(0,obj.ek):
                                        if (abc[f] > abc[g]) and (f < g):
                                            abc[f],abc[g] = abc[g],abc[f]
                                if len(facelist) == 0:
                                    for i in range(0,obj.ek):
                                        facelist.append(abc[i])
                                else:
                                    #prüfen ob p,q,r in liste enthalten ist
                                    add = 1
                                    for i in range(0,len(facelist)//3):
                                        if (facelist[3*i] == abc[0]) and (facelist[3*i+1] == abc[1]) and (facelist[3*i+2] == abc[2]):
                                            add = 0
                                    if add == 1:
                                        #ggf. hinzufügen
                                        for j in range(0,obj.ek):
                                            facelist.append(abc[j])
    if obj.ek == 3:
        #nach mzpolygon sortieren
        for m in range(0,len(facelist)//3):
            for n in range(0,len(facelist)//3):
                mzpolygonm = (obj.xyz[3*facelist[3*m]+2] + obj.xyz[3*facelist[3*m+1]+2] + obj.xyz[3*facelist[3*m+2]+2])/3
                mzpolygonn = (obj.xyz[3*facelist[3*n]+2] + obj.xyz[3*facelist[3*n+1]+2] + obj.xyz[3*facelist[3*n+2]+2])/3
                if (mzpolygonm > mzpolygonn) and (m > n):
                    facelist[3*m],facelist[3*n] = facelist[3*n],facelist[3*m]
                    facelist[3*m+1],facelist[3*n+1] = facelist[3*n+1],facelist[3*m+1]
                    facelist[3*m+2],facelist[3*n+2] = facelist[3*n+2],facelist[3*m+2]
                    
        #finales zeichnen
        obj.xy = conv32()
        for i in range(0,len(facelist)//3):
            p = facelist[3*i]
            q = facelist[3*i+1]
            r = facelist[3*i+2]
            provebvb()
            canvas1.create_polygon(obj.xy[2*p],obj.xy[2*p+1], obj.xy[2*q],obj.xy[2*q+1], obj.xy[2*r],obj.xy[2*r+1], fill = getcolor('fc'), outline = getcolor('oc')) 
    
                   
def zeichnen():
    if checkedges.get() == 1:
        drawedges()
    if checkfaces.get() == 1:
        drawfaces()



        
def provebvb():
    black = 0
    yellow = 0
    if editfc.get() == 'black':
        black = 1
    if editfc.get() == 'yellow':
        yellow = 1
    if editoc.get() == 'black':
        black = 1
    if editoc.get() == 'yellow':
        yellow = 1
    if black + yellow == 2:
        avoidbvb()
            
def avoidbvb():
    popup('bvb')
    editoc.delete(0,'end')
    editoc.insert(10,'rgb(255,0,0)')
    editfc.delete(0,'end')
    editfc.insert(10,'#b0daf0')   




def popup(string):
    if string == 'tip':
        msg = 'Es gibt vier Wege der Farbeingabe: \n    (1) Anklicken des Buttons mit der gewünschten Farbe \n    (2) Eingeben von Standardfarben von Python (Bsp: red, yellow, ...) \n    (3) Eingeben von Hexadezimalwerten (Bsp: #ab42cd) \n    (4) Eingeben von RGB-Tripeln (Bsp: rgb(42,69,255) )'
    if string == 'bvb':
        msg = 'Die Farbkombination schwarz-gelb ist dank \nFabien Streuber und Tristan Scholz verboten \nworden, um den Nutzer zu schützen. Die Farben \nwerden zu einer besseren Kombination geändert.'
    masterpopup = Tk()
    masterpopup.title('Hinweis')
    labelmsg = Label(masterpopup, text = msg, justify = 'left', font = '15')
    labelmsg.pack(padx = 10, pady = 10)




def deselectall():
    cbiko.deselect()
    cbkep.deselect()
    cbdod.deselect()

            

def colormode(colorname):
    color = colorname
    master['bg'] = color
    canvas1['bg'] = color
    labelname['bg'] = color
    labeloc['bg'] = color
    labelfc['bg'] = color
    cbedges['bg'] = color
    cbfaces['bg'] = color
    labeldeg['bg'] = color
    cbdeg['bg'] = color
    cbreprot['bg'] = color
    cbiko['bg'] = color
    cbkep['bg'] = color
    cbdod['bg'] = color

#canvas1 = Canvas(master, width = 800, height = 600, bg = 'white')
canvas1 = Canvas(master, width = 800, height = 600, highlightthickness = 0)
canvas1.grid(row = 0, column = 0, rowspan = 15, columnspan = 17)

labelname = Label(master, text = (obj.name + 'darstellung'), font = 'Verdana 25' )
labelname.grid(row = 0, column = 0, rowspan = 3, columnspan = 10, sticky = NW, padx = 15, pady = 15)

buttonblackoc = Button(master, text = 'XX', bg = 'black', fg = 'black', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'black'), zeichnen()))
buttonblackoc.grid(row = 15, column = 2, pady = 10)

buttonblueoc = Button(master, text = 'XX', bg = 'blue', fg = 'blue', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'blue'), zeichnen()))
buttonblueoc.grid(row = 15, column = 3, pady = 10)

buttonredoc = Button(master, text = 'XX', bg = 'red', fg = 'red', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'red'), zeichnen()))
buttonredoc.grid(row = 15, column = 4, pady = 10)

buttongreenoc = Button(master, text = 'XX', bg = 'green', fg = 'green', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'green'), zeichnen()))
buttongreenoc.grid(row = 15, column = 5, pady = 10)

buttonyellowoc = Button(master, text = 'XX', bg = 'yellow', fg = 'yellow', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'yellow'), zeichnen()))
buttonyellowoc.grid(row = 15, column = 6, pady = 10)

buttonblackfc = Button(master, text = 'XX', bg = 'black', fg = 'black', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'black'), zeichnen()))
buttonblackfc.grid(row = 15, column = 9, pady = 10)

buttonbluefc = Button(master, text = 'XX', bg = 'blue', fg = 'blue', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'blue'), zeichnen()))
buttonbluefc.grid(row = 15, column = 10, pady = 10)

buttonredfc = Button(master, text = 'XX', bg = 'red', fg = 'red', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'red'), zeichnen()))
buttonredfc.grid(row = 15, column = 11, pady = 10)

buttongreenfc = Button(master, text = 'XX', bg = 'green', fg = 'green', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'green'), zeichnen()))
buttongreenfc.grid(row = 15, column = 12, pady = 10)

buttonyellowoc = Button(master, text = 'XX', bg = 'yellow', fg = 'yellow', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'yellow'), zeichnen()))
buttonyellowoc.grid(row = 15, column = 13, pady = 10)

labeloc = Label(master, text = 'Randfarbe: ', font = '14')
labeloc.grid(row = 16, column = 2, columnspan = 2, pady = 10)

editoc = Entry(master, font = '14', width = 15)
editoc.grid(row = 16, column = 4, columnspan = 3, pady = 10)
editoc.insert(10,'rgb(255,0,0)')

labelfc = Label(master, text = 'Füllfarbe: ', font = '14')
labelfc.grid(row = 16, column = 9, columnspan = 2, pady = 10)

editfc = Entry(master, font = '14', width = 15)
editfc.grid(row = 16, column = 11, columnspan = 3, pady = 10)
editfc.insert(10,'#b0daf0')

cbedges = Checkbutton(master, text = 'Kanten zeichnen', var = checkedges, command = lambda:(cbfaces.deselect(), cbedges.select(), zeichnen()))
cbedges.grid(row = 0, column = 16, columnspan = 2, padx = 15, pady = 5)

cbfaces = Checkbutton(master, text = 'Flächen zeichnen', var = checkfaces, command = lambda:(cbedges.deselect(), cbfaces.select(), zeichnen()))
cbfaces.grid(row = 1, column = 16, columnspan = 2, padx = 15, pady = 5)

labeldeg = Label(master, text = 'Drehungswinkel:')
labeldeg.grid(row = 3, column = 16, columnspan = 2)

cbdeg = Checkbutton(master, text = 'deg', var = checkdeg)
cbdeg.grid(row = 4, column = 17)
cbdeg.select()

editdeg = Entry(master, width = 8)
editdeg.grid(row = 4, column = 16, columnspan = 1, padx = 15, pady = 5)
editdeg.insert(10,'10')

buttonx = Button(master, text = 'rot x', command = lambda:(rotx(1), setspeeds('x',1)))
buttonx.grid(row = 6, column = 16, padx = 10, pady = 5)

buttony = Button(master, text = 'rot y', command = lambda:(roty(1), setspeeds('y',1)))
buttony.grid(row = 7, column = 16, padx = 10,  pady = 5)

buttonz = Button(master, text = 'rot z', command = lambda:(rotz(1), setspeeds('z',1)))
buttonz.grid(row = 8, column = 16, padx = 10,  pady = 5)

buttonmx = Button(master, text = 'rot -x', command = lambda:(rotx(-1), setspeeds('x',-1)))
buttonmx.grid(row = 6, column = 17, padx = 10,  pady = 5)

buttonmy = Button(master, text = 'rot -y', command = lambda:(roty(-1), setspeeds('y',-1)))
buttonmy.grid(row = 7, column = 17, padx = 10,  pady = 5)

buttonmz = Button(master, text = 'rot -z', command = lambda:(rotz(-1), setspeeds('z',-1)))
buttonmz.grid(row = 8, column = 17, padx = 10,   pady = 5)

cbreprot = Checkbutton(master, text = 'weiterdrehen', var = checkrep, command = resetspeeds)
cbreprot.grid(row = 9, column = 16, columnspan = 2, padx = 15, pady = 5)

cbiko = Checkbutton(master, text = 'Ikosaeder zeichnen', justify = 'left', var = checkiko, command = lambda:(deselectall(), cbiko.select(), ikosaeder()))
cbiko.grid(row = 11, column = 16, columnspan = 2, pady = 5)

cbkep = Checkbutton(master, text = 'Keplerstern zeichnen', justify = 'left', var = checkkep, command = lambda:(deselectall(), cbkep.select(), keplerstern()))
cbkep.grid(row = 12, column = 16, columnspan = 2, pady = 5)

cbdod = Checkbutton(master, text = 'Dodekaeder zeichnen', justify = 'left', var = checkdod, command = lambda:(deselectall(), cbdod.select(), dodekaeder()))
cbdod.grid(row = 13, column = 16, columnspan = 2, pady = 5)

buttontip = Button(master, text = 'Hinweis zu Farbeingabe', command = lambda:popup('tip'))
buttontip.grid(row = 15, rowspan = 1, column = 16, columnspan = 2)

buttonrefresh = Button(master, text = 'Farben aktualisieren', command = zeichnen)
buttonrefresh.grid(row = 16, column = 16, columnspan = 2, padx = 15, pady = 5)

colormode('#fafafa')

cbfaces.select()
cbiko.select()
ikosaeder()

infiniterep()
