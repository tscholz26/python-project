"""@package docstring
Documentation for this module.

More details.
"""

from tkinter import *
import time
import math

master = Tk()

versionshinweis =  '(Version 3.11.3)'

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

global clickx
global clicky
global currentx
global currenty
global releasex
global releasey
global posx
global posy
posx = 100
posy = 100

global xspeed
global yspeed
global zspeed
xspeed = IntVar()
yspeed = IntVar()
zspeed = IntVar()

global scalervar
global mousespeed
global mousedown
scalevar = float()
mousespeed = float()
mousedown = 0
#scalevar = 50


class object3d:
    """
    das ist meine klasse
    sie ist sehr schön
    """
    name = 'Ikosaeder'
    xyz = []
    xy = []
    sl = 2.5
    ek = 3 #anzahl der ecken pro seitenfläche
    a = 200

obj = object3d()


def ikosaeder():
    """
    Diese Funktion modifiziert die Member-Variablen der object3d Klasse so
    dass ein Ikosaeder gezeichnet werden kann, gibt über die Überschrift aus,
    welcher Körper gezeichnet wird, und dreht ihn in eine optisch ansprechende
    Startposition.
    """
    canvas1.delete(ALL)
    obj.name = 'Ikosaeder'
    obj.a = 200
    phi = (gold*obj.a)
    obj.xyz = [0,-obj.a,phi, 0,-obj.a,-phi, 0,obj.a,phi, 0,obj.a,-phi, phi,0,obj.a, phi,0,-obj.a, -phi,0,obj.a, -phi,0,-obj.a, obj.a,-phi,0, obj.a,phi,0, -obj.a,-phi,0, -obj.a,phi,0]
    obj.sl = 2*phi
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D ' + versionshinweis)
    #in startposition drehen für bessere optik
    rotx(1)
    rotx(1)
    resetspeeds()
    zeichnen()
    
def keplerstern():
    """
    Diese Funktion modifiziert die Member-Variablen der object3d Klasse so
    dass ein Keplerstern gezeichnet werden kann, gibt über die Überschrift aus,
    welcher Körper gezeichnet wird, und dreht ihn in eine optisch ansprechende
    Startposition.
    """
    canvas1.delete(ALL)
    obj.name = 'Keplerstern'
    obj.a = 150
    obj.xyz = [obj.a,0,0, 0,obj.a,0, 0,0,obj.a, -obj.a,0,0, 0,-obj.a,0, 0,0,-obj.a,
               obj.a,-obj.a,-obj.a, -obj.a,obj.a,-obj.a, -obj.a,-obj.a,obj.a, -obj.a,obj.a,obj.a, obj.a,-obj.a,obj.a, obj.a,obj.a,-obj.a, -obj.a,-obj.a,-obj.a, obj.a,obj.a,obj.a]
    obj.sl = obj.a * math.sqrt(2)
    #obj.sl = obj.a * 3
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D ' + versionshinweis)
    #in startposition drehen für bessere optik
    rotx(2)
    roty(2)
    resetspeeds()
    zeichnen()
    
def dodekaeder():
    """
    Diese Funktion modifiziert die Member-Variablen der object3d Klasse so
    dass ein Dodekaeder gezeichnet werden kann, gibt über die Überschrift aus,
    welcher Körper gezeichnet wird, und dreht ihn in eine optisch ansprechende
    Startposition.
    """
    canvas1.delete(ALL)
    obj.name = 'Dodekaeder'
    obj.a = 130
    phi = (gold*obj.a)
    phim = obj.a/gold
    obj.xyz = [obj.a,obj.a,obj.a, -obj.a,obj.a,obj.a, obj.a,-obj.a,obj.a, obj.a,obj.a,-obj.a, obj.a,-obj.a,-obj.a, -obj.a,obj.a,-obj.a, -obj.a,-obj.a,obj.a, -obj.a,-obj.a,-obj.a, phim,phi,0, -phim,phi,0, -phim,-phi,0, phim,-phi,0, 0,phim,phi, 0,phim,-phi, 0,-phim,-phi, 0,-phim,phi, phi,0,phim, phi,0,-phim, -phi,0,phim, -phi,0,-phim]
    obj.sl = 2*phi
    obj.ek = 5
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D ' + versionshinweis)
    #in startposition drehen für bessere optik
    rotx(1)
    rotx(1)
    roty(-1)
    resetspeeds()
    zeichnen()
    
master.title('Darstellung eines ' + obj.name + 's in 3D')



def conv32():
    """Diese Funktion wandelt die dreidimensionalen Koordinaten aller Punkte in
    2D-Koordinaten um, die gezeichnet werden können. An den 3D-Koordinaten werden
    keine Änderungen vorgenommen, da 2D- und 3D-Koordinaten in verschiedenen Arrays
    enthalten sind.
    
    Args:
        keine: none
    
    returns:
        xy: list    
    """
    pass
    obj.xy = []
    for i in range (0,len(obj.xyz)//3):
        distance = 3000
        #strahlensatz
        obj.xy.append(mx + (obj.xyz[3*i] * distance)/(obj.xyz[3*i+2] + distance))
        obj.xy.append(my + (obj.xyz[3*i+1] * distance)/(obj.xyz[3*i+2] + distance))
    return obj.xy



def getdeg():
    """Diese Funktion fragt den Inhalt des Entrys ab, welches den Drehungswinkel enthält.
    wenn das Entry nichts oder nur ein Komma enthält, wird der Drehungswinkel automatisch
    auf 0 gesetzt. Je nach Zustand der Checkbox für Bogen-/Gradmaß kann der Winkel zwischen
    ebengenannten umgewandelt werden. Wenn gerade mit der Maus der Körper bewegt
    wird, wird der Winkel auf 10° gesetzt, da in diesem Fall die Geschwindigkeit
    über die Scale Mausempfindlichkeit geregelt wird.
    """
    if mousedown == 1:
        deg = 10/180*math.pi
    else:
        if editdeg.get() != '':
            if editdeg.get() == '.':
                deg = 0
            else:
                deg = float(editdeg.get())
        else:
            deg = 0
        if checkdeg.get() == 1:
            deg = deg / 180 * math.pi
    return(deg)

def rotx(sgndeg):
    """Diese Funktion berechnet aus Winkel getdeg() und Vorzeichen sgndeg einen
    Drehungswinkel, rotiert alle Punkte um diesen Winkel um die x-Achse und zeichnet
    am Ende den Körper neu.
    """
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
    """Diese Funktion berechnet aus Winkel getdeg() und Vorzeichen sgndeg einen
    Drehungswinkel, rotiert alle Punkte um diesen Winkel um die y-Achse und zeichnet
    am Ende den Körper neu.
    """
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
    """Diese Funktion berechnet aus Winkel getdeg() und Vorzeichen sgndeg einen
    Drehungswinkel, rotiert alle Punkte um diesen Winkel um die z-Achse und zeichnet
    am Ende den Körper neu.
    """
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
    """Diese Funktion setzt die Drehgeschwindigkeiten in alle Dimensionen (x,y,z) auf 0.
    Das bewirkt, dass sich der Körper wenn die weiterdrehen-Option ausgewählt ist immer
    nur in eine Richtung dreht und nicht in mehrere gleichzeitig, da man sonst sehr
    schnell Epilepsie bekommen kann
    
    Args:
        xspeed: integer
        yspeed: integer
        zspeed: integer

    returns:
        nichts, ändert lediglich die Werte globaler Variablen
    """
    
    global xspeed
    global yspeed
    global zspeed
    xspeed = 0
    yspeed = 0
    zspeed = 0

def setspeeds(char,speed):
    """Diese Funnktion ruft erst die resetspeeds() Funktion auf, und je nachdem ob der
    String char x,y oder z enthält, wird die Drehgeschwindigkeitum die jeweilige Achse
    auf die Variable speed gesetzt. Diese enthält normalerweise -1 oder 1.

    Args:
        char: string
        speed: integer
    """
    resetspeeds()
    global xspeed
    global yspeed
    global zspeed
    if checkrep.get() == 1:
        if char == 'x':
            xspeed = speed
        if char == 'y':
            yspeed = speed
        if char == 'z':
            zspeed = speed

def infiniterep():
    """Diese Funktion ruft sich aller 100ms selbst auf und dreht den Körper mithilfe der
    rotall()-Funktion
    """
    master.after(100, lambda:(rotall(), infiniterep()))

def rotall():
    """Diese Funktion führt letztendlich die Drehung für die weiterdrehen-Option aus,
    indem sie mithilfe der rotx()-, roty()- und rotz()-Funktion den Körper je nach
    jeweiliger Geschwindigkeit um die jeweiligen Achsen dreht.
    """
    global xspeed
    global yspeed
    global zspeed
    if xspeed != 0:
        rotx(xspeed)
    if yspeed != 0:
        roty(yspeed)
    if zspeed != 0:
        rotz(zspeed)



def click(eventclick):
    """Diese Funktion setzt die Variable mousedown, die zeigt, ob die Maus gerade
    gehalten wird, auf 1 und ändert currentx und currenty auf die Koordinaten des
    Punktes, der angeklickt wurde.

    Args:
        eventlick: vom System angelegt, enthält u.A. x/y Koordinaten des Punkts
    """
    global clickx
    global clicky
    global currentx
    global currenty
    global mousedown

    mousedown = 1
    
    clickx = eventclick.x
    clicky = eventclick.y
    currentx = clickx
    currenty = clicky

def currentpos(eventcurrent):
    """Diese Funktion fragt die aktuellen Koordinaten des Mauszeigers ab und berechnet
    die Entfernung zur vorherigen Position. SIe berechnet je nach Mausempfindlichkeit
    (einstellbar mit Scale) die Mausgeschwindigkeit und dreht mit rotx() und roty()
    den Körper.

    Args:
        eventcurrent: vom System angelegt, enthält u.A. x/y Koordinaten des Punkts
    """
    global clickx
    global clicky
    global currentx
    global currenty
    global posx
    global posy
    global currentx
    global currenty
    global scalevar
    global mousespeed
    
    #alte pos speichern
    currentxalt = currentx
    currentyalt = currenty
    #neue pos
    currentx = eventcurrent.x
    currenty = eventcurrent.y
    #differenz = drehungbetrag
    xdiff = currentxalt - currentx
    ydiff = currentyalt - currenty
    #weiterdrehen deaktivieren
    cbreprot.deselect()
    resetspeeds()
    #drehen ausführen
    if scalevar >= 85:        
        print('tempo zu hoch, zurücksetzen auf standard')
        scalevar = 100
        scalespeed.set(50)
    else:
        scalevar = scalespeed.get()
    mousespeed = 85 - scalevar
    roty(xdiff/mousespeed)
    rotx(ydiff/mousespeed)

def release(eventrelease):
    """Diese Funktion setzt die Variable mousedown, die anzeigt, ob die Maus gerade
    geklickt wird, auf 0 zurück.
    """
    global mousedown
    mousedown = 0    


#sortieren nach z
def zsort():
    """Diese Funktion sortiert das Array obj.xyz welches 3D-Koordinaten enthält nach
    höchstem z-Wert. Punkte die also "weiter hinten" sind, werden dann zuerst gezeichnet
    und z.T. übermalt. Dadurch werden verdeckte Kanten unsichtbar.

    returns:
        obj.xyz: Array mit 3D-Koordinaten
    """
    for m in range(0,len(obj.xyz)//3):
        for n in range (0, len(obj.xyz)//3):
            if ((obj.xyz[3*m+2] < obj.xyz[3*n+2]) and (m>n)):
                obj.xyz[3*m],obj.xyz[3*n] = obj.xyz[3*n],obj.xyz[3*m]
                obj.xyz[3*m+1],obj.xyz[3*n+1] = obj.xyz[3*n+1],obj.xyz[3*m+1]
                obj.xyz[3*m+2],obj.xyz[3*n+2] = obj.xyz[3*n+2],obj.xyz[3*m+2]
    #print('obj.xyz sortiert: ' + str(obj.xyz))
    return(obj.xyz)

def rgbtohex(color):
    """Diese Funktion wandelt rgb-Farben in hex-Farben um, die Python leicht
    darstellen kann.

    args:
        color: String mit rgb-farbe

    returns:
        colorhex: String mit hex-Farbe
    """
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
    colorhex = '#'+rhex+ghex+bhex
    return(colorhex)
    

def getcolor(string):
    """Diese Funktion fragt je nachdem ob der String fc (face color) oder oc (Outline
    Color) enthält den Inhalt des zugehörigen Entrys ab. Wenn dort ein rgb-Wert steht,
    wird dieser mit der rgbtohex() Funktion in hex umgewandelt. Zum Schluss wird die
    Zeichenfarbe für das jeweilige Element (face/outline) zurückgegeben.

    args:
        string: string, der 'fc' oder 'oc' enthält

    returns:
        color: string, der Farbe enthält
    """
    if string == 'fc':
        color = editfc.get()
    if string == 'oc':
        color = editoc.get()
    if color[0] == 'r' and not color == 'red':
            color = rgbtohex(color)
    return(color)

def drawedges():
    """Diese Funktion leert zuerst vollständig die Zeichenfläche. Danach erzeugt sie mit
    der conv32() Funktion die 2D-Koordinaten des "Körpers" und kombiniert nun immer 2
    Punkte, solange bis alle Kombinationen probiert sind. Wenn der Abstand der zwei
    Punkte der Seitenlänge obj.sl (mit einer Toleranz von 5) entspricht, werden mit der
    getcolor() Funktion die gewünschte Linienfarbe errechnet und die Punkte verbunden.
    """
    canvas1.delete(ALL)
    obj.xy = conv32()
    #print('obj.xyz: ' + str(obj.xyz))
    #print('obj.xy: ' + str(obj.xy))
    for k in range (0,len(obj.xyz)//3):
        for m in range (0,len(obj.xyz)//3):
            abstand = (math.sqrt((obj.xyz[3*k]-obj.xyz[3*m])**2+(obj.xyz[3*k+1]-obj.xyz[3*m+1])**2+(obj.xyz[3*k+2]-obj.xyz[3*m+2])**2))
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
                if (mzpolygonm > mzpolygonn) and (m < n):
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
    scalespeed['bg'] = color
    scalespeed['activebackground'] = color
    scalespeed['highlightcolor'] = color    
    

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

scalespeed = Scale(master, var = scalevar, orient = 'horizontal', highlightthickness = 0, label = 'Mausempfindlichkeit:', from_ = -4, to = 84, showvalue = 0, length = 130)
scalespeed.grid(row = 10, column = 16, columnspan = 3, padx = 15, pady = 5)
scalespeed.set(40)

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

canvas1.bind("<Button-1>", click)
canvas1.bind("<Button1-Motion>", currentpos)
canvas1.bind("<ButtonRelease-1>", release)
