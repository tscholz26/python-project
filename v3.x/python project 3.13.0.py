"""@package docstring
Documentation for this module.

More details.
"""

from tkinter import *
import math, time

master = Tk()

#nötige Variablen
versionshinweis =  '(Version 3.13.0)'
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
checkgradient = IntVar()
checkrewriteedit = IntVar()
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
xspeed = int
yspeed = int
zspeed = int
global scalervar
global mousespeed
global mousedown
scalevar = float()
mousespeed = float
mousedown = 0
#scalevar = 50
global gradientcolor
global direction
global colors





class Object3d(object):
    def __init__(self, name = str, xyz = [], xy = [], sl = float, ek = int, a = int):
        self.__name = name
        self.__xyz = xyz
        self.__xy = xy
        self.__sl = sl
        self.__ek = ek
        self.__a = a

    def name(self):
        return(self.__name)

    def conv32(self):
        self.__xy = []
        for i in range (0,len(self.__xyz)//3):
            distance = 3000
            #strahlensatz
            self.__xy.append(mx + (self.__xyz[3*i] * distance)/(self.__xyz[3*i+2] + distance))
            self.__xy.append(my + (self.__xyz[3*i+1] * distance)/(self.__xyz[3*i+2] + distance))
        return self.__xy

    def initkep(self):
        self.__name = 'Keplerstern'
        self.__a = 150
        self.__xyz = [self.__a,0,0, 0,self.__a,0, 0,0,self.__a, -self.__a,0,0, 0,-self.__a,0, 0,0,-self.__a,
                   self.__a,-self.__a,-self.__a, -self.__a,self.__a,-self.__a, -self.__a,-self.__a,self.__a, -self.__a,self.__a,self.__a, self.__a,-self.__a,self.__a, self.__a,self.__a,-self.__a, -self.__a,-self.__a,-self.__a, self.__a,self.__a,self.__a]
        self.__sl = self.__a * math.sqrt(2)
        self.__ek = 3
        obj.rotx(2)
        obj.roty(2)

    def initiko(self):
        self.__name = 'Ikosaeder'
        self.__a = 200
        phi = gold * self.__a
        self.__xyz = [0,-self.__a,phi, 0,-self.__a,-phi, 0,self.__a,phi, 0,self.__a,-phi, phi,0,self.__a, phi,0,-self.__a, -phi,0,self.__a, -phi,0,-self.__a, self.__a,-phi,0, self.__a,phi,0, -self.__a,-phi,0, -self.__a,phi,0]
        self.__sl = 2 * phi
        self.__ek = 3
        obj.rotx(2)

    def initdod(self):
        self.__name = 'Dodekaeder'
        self.__a = 130
        phi = (gold*self.__a)
        phim = self.__a/gold
        self.__xyz = [self.__a,self.__a,self.__a, -self.__a,self.__a,self.__a, self.__a,-self.__a,self.__a, self.__a,self.__a,-self.__a, self.__a,-self.__a,-self.__a, -self.__a,self.__a,-self.__a, -self.__a,-self.__a,self.__a, -self.__a,-self.__a,-self.__a, phim,phi,0, -phim,phi,0, -phim,-phi,0, phim,-phi,0, 0,phim,phi, 0,phim,-phi, 0,-phim,-phi, 0,-phim,phi, phi,0,phim, phi,0,-phim, -phi,0,phim, -phi,0,-phim]
        self.__sl = 2*phi
        self.__ek = 5
        obj.rotx(2)
        obj.roty(-1)

    def getcolor(self, string):
        global gradientcolor
        if checkgradient.get() == 0:
            if string == 'fc':
                color = editfc.get()
            if string == 'oc':
                color = editoc.get()
            if color[0] == 'r' and not color == 'red':
                    color = rgbtohex(color)
        else:
            if string == 'oc':
                color = 'black'
                if checkrewriteedit.get() == 1:
                    editoc.delete(0,'end')
                    editoc.insert(10,'#000000')
            else:
                color = gradientcolor
                if checkrewriteedit.get() == 1:
                    editfc.delete(0,'end')
                    editfc.insert(10,color)
        return(color)

    def initgradient(self):
        global direction
        global colors
    
        direction = [0,0,0]
        colors = [255,0,0]

        direction[0] = -1
        direction[1] = 1
        direction[2] = 0
        
    def inffuncgradient(self):
        time.sleep(0.001)
        if checkgradient.get() == 1:
            master.after(50, lambda:(obj.gradientgetcolor(), obj.zeichnen(), obj.inffuncgradient()))

    def gradientgetcolor(self):
        global starttime
        global speed
        global direction
        global colors
        global gradientcolor

        speed = scalegradient.get() / 100
        #speed = 1
    
        for i in range(0,3):
            #print('Speed: ' + str(scalevar))
            colors[i] = round( colors[i] + direction[i] * speed)
            tolerance = speed
            if colors[i] > 255 - tolerance:
                direction[i] = -1
                direction[(i+1)%3] = 1
                direction[(i+2)%3] = 0

            if colors[0] > 255 - tolerance:
                colors[0] = round(255 - tolerance)
                colors[1] = 0
                colors[2] = 0
        # 0: rot, 1: grün, 2: blau, Reihenfolge beeinflusst Abfolge des Farbverlaufes
        colorrgb = 'rgb(' + str(colors[1]) + ',' + str(colors[2]) + ',' + str(colors[0]) + ')'
        gradientcolor = rgbtohex(colorrgb)


    def zsort(self):
        for m in range(0,len(self.__xyz)//3):
            for n in range (0, len(self.__xyz)//3):
                if ((self.__xyz[3*m+2] < self.__xyz[3*n+2]) and (m>n)):
                    self.__xyz[3*m],self.__xyz[3*n] = self.__xyz[3*n],self.__xyz[3*m]
                    self.__xyz[3*m+1],self.__xyz[3*n+1] = self.__xyz[3*n+1],self.__xyz[3*m+1]
                    self.__xyz[3*m+2],self.__xyz[3*n+2] = self.__xyz[3*n+2],self.__xyz[3*m+2]
        #print('self.__xyz sortiert: ' + str(self.__xyz))
        return(self.__xyz)

    def resetspeeds(self):
        global xspeed
        global yspeed
        global zspeed
        xspeed = 0
        yspeed = 0
        zspeed = 0

    def drawedges(self):
        canvas1.delete(ALL)
        self.__xy = obj.conv32()
        for k in range (0,len(self.__xyz)//3):
            for m in range (0,len(self.__xyz)//3):
                abstand = (math.sqrt((self.__xyz[3*k]-self.__xyz[3*m])**2+(self.__xyz[3*k+1]-self.__xyz[3*m+1])**2+(self.__xyz[3*k+2]-self.__xyz[3*m+2])**2))
                #print(abstand)
                if (abs(abstand-self.__sl) < 5):
                    canvas1.create_line(self.__xy[2*k],self.__xy[2*k+1],self.__xy[2*m],self.__xy[2*m+1], fill = obj.getcolor('oc'))

    def getdeg(self):
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

    def setspeeds(self, char, speed):
        obj.resetspeeds()
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

    def infiniterep(self):
        master.after(100, lambda:(obj.rotall(), obj.infiniterep()))

    def rotall(self):
        """Diese Funktion führt letztendlich die Drehung für die weiterdrehen-Option aus,
        indem sie mithilfe der rotx()-, roty()- und rotz()-Funktion den Körper je nach
        jeweiliger Geschwindigkeit um die jeweiligen Achsen dreht.
        """
        global xspeed
        global yspeed
        global zspeed
        if xspeed != 0:
            obj.rotx(xspeed)
        if yspeed != 0:
            obj.roty(yspeed)
        if zspeed != 0:
            obj.rotz(zspeed)
        
    def rotx(self, sgndeg):
        canvas1.delete(ALL)
        deg = obj.getdeg()*sgndeg
        c = math.cos(deg)
        s = math.sin(deg)
        for p in range(0,len(self.__xyz)//3):
            yalt = self.__xyz[3*p+1]
            zalt = self.__xyz[3*p+2]
            self.__xyz[3*p+1] = ((yalt) * c - (zalt) * s)
            self.__xyz[3*p+2] = ((yalt) * s + (zalt) * c)
        self.__xy = obj.conv32()
        obj.zeichnen()    
        return(self.__xyz)

    def roty(self, sgndeg):
        canvas1.delete(ALL)
        deg = obj.getdeg()*sgndeg
        c = math.cos(deg)
        s = math.sin(deg)
        for p in range(0,len(self.__xyz)//3):
            xalt = self.__xyz[3*p]
            zalt = self.__xyz[3*p+2]
            self.__xyz[3*p] = ((xalt) * c - (zalt) * s)
            self.__xyz[3*p+2] = ((xalt) * s + (zalt) * c)
        self.__xy = obj.conv32()
        obj.zeichnen()    
        return(self.__xyz)
    
    def rotz(self, sgndeg):
        canvas1.delete(ALL)
        deg = obj.getdeg()*sgndeg
        c = math.cos(deg)
        s = math.sin(deg)
        for p in range(0,len(self.__xyz)//3):
            xalt = self.__xyz[3*p]
            yalt = self.__xyz[3*p+1]
            self.__xyz[3*p] = ((xalt) * c - (yalt) * s)
            self.__xyz[3*p+1] = ((xalt) * s + (yalt) * c)
        self.__xy = obj.conv32()
        obj.zeichnen()    
        return(self.__xyz)

    def avoidbvb(self):
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
            popup('bvb')
            editoc.delete(0,'end')
            editoc.insert(10,'rgb(255,0,0)')
            editfc.delete(0,'end')
            editfc.insert(10,'#b0daf0')
            
                        
    def drawfaces(self):
        canvas1.delete(ALL)
        facelist.clear()
        fccolor = obj.getcolor('fc')
        occolor = obj.getcolor('oc')
        #sortieren nach z
        self.__xyz = obj.zsort()
        #zeichnen
        for p in range (0,len(self.__xyz)//3):
            for q in range (0,len(self.__xyz)//3):
                pq = math.sqrt((self.__xyz[3*p]-self.__xyz[3*q])**2+(self.__xyz[3*p+1]-self.__xyz[3*q+1])**2+(self.__xyz[3*p+2]-self.__xyz[3*q+2])**2)
                if (abs(pq-self.__sl) < 10):
                    for r in range (0,len(self.__xyz)//3):
                        pr = math.sqrt((self.__xyz[3*p]-self.__xyz[3*r])**2+(self.__xyz[3*p+1]-self.__xyz[3*r+1])**2+(self.__xyz[3*p+2]-self.__xyz[3*r+2])**2)
                        if (abs(pr-self.__sl) < 10):
                            qr = math.sqrt((self.__xyz[3*q]-self.__xyz[3*r])**2+(self.__xyz[3*q+1]-self.__xyz[3*r+1])**2+(self.__xyz[3*q+2]-self.__xyz[3*r+2])**2)
                            if (abs(qr-self.__sl) < 10) or ((self.__ek == 5) and (abs(qr-(2*self.__sl*math.sin(54/180*math.pi))) < 10)):
                                if self.__ek > 3:
                                    for s in range (0,len(self.__xyz)//3):
                                        qs = math.sqrt((self.__xyz[3*q]-self.__xyz[3*s])**2+(self.__xyz[3*q+1]-self.__xyz[3*s+1])**2+(self.__xyz[3*q+2]-self.__xyz[3*s+2])**2)
                                        if (abs(qs-self.__sl) < 10):
                                            for t in range (0,len(self.__xyz)//3):
                                                st = math.sqrt((self.__xyz[3*s]-self.__xyz[3*t])**2+(self.__xyz[3*s+1]-self.__xyz[3*t+1])**2+(self.__xyz[3*s+2]-self.__xyz[3*t+2])**2)
                                                if (abs(st-self.__sl) < 10):
                                                    rt = math.sqrt((self.__xyz[3*r]-self.__xyz[3*t])**2+(self.__xyz[3*r+1]-self.__xyz[3*t+1])**2+(self.__xyz[3*r+2]-self.__xyz[3*t+2])**2)
                                                    if (abs(rt-self.__sl) < 10):
                                                        self.__xy = obj.conv32()
                                                        canvas1.create_polygon(self.__xy[2*p],self.__xy[2*p+1], self.__xy[2*q],self.__xy[2*q+1], self.__xy[2*s],self.__xy[2*s+1],self.__xy[2*t],self.__xy[2*t+1], self.__xy[2*r],self.__xy[2*r+1], fill = fccolor, outline = occolor)
                                                
                                else:
                                    #p,q,r sortieren
                                    abc = [p,q,r]
                                    for f in range(0,self.__ek):
                                        for g in range(0,self.__ek):
                                            if (abc[f] > abc[g]) and (f < g):
                                                abc[f],abc[g] = abc[g],abc[f]
                                    if len(facelist) == 0:
                                        for i in range(0,self.__ek):
                                            facelist.append(abc[i])
                                    else:
                                        #prüfen ob p,q,r in liste enthalten ist
                                        add = 1
                                        for i in range(0,len(facelist)//3):
                                            if (facelist[3*i] == abc[0]) and (facelist[3*i+1] == abc[1]) and (facelist[3*i+2] == abc[2]):
                                                add = 0
                                        if add == 1:
                                            #ggf. hinzufügen
                                            for j in range(0,self.__ek):
                                                facelist.append(abc[j])
        if self.__ek == 3:
            #nach mzpolygon sortieren
            for m in range(0,len(facelist)//3):
                for n in range(0,len(facelist)//3):
                    mzpolygonm = (self.__xyz[3*facelist[3*m]+2] + self.__xyz[3*facelist[3*m+1]+2] + self.__xyz[3*facelist[3*m+2]+2])/3
                    mzpolygonn = (self.__xyz[3*facelist[3*n]+2] + self.__xyz[3*facelist[3*n+1]+2] + self.__xyz[3*facelist[3*n+2]+2])/3
                    if (mzpolygonm > mzpolygonn) and (m < n):
                        facelist[3*m],facelist[3*n] = facelist[3*n],facelist[3*m]
                        facelist[3*m+1],facelist[3*n+1] = facelist[3*n+1],facelist[3*m+1]
                        facelist[3*m+2],facelist[3*n+2] = facelist[3*n+2],facelist[3*m+2]
                    
            #finales zeichnen
            self.__xy = obj.conv32()
            for i in range(0,len(facelist)//3):
                p = facelist[3*i]
                q = facelist[3*i+1]
                r = facelist[3*i+2]
                canvas1.create_polygon(self.__xy[2*p],self.__xy[2*p+1], self.__xy[2*q],self.__xy[2*q+1], self.__xy[2*r],self.__xy[2*r+1], fill = fccolor, outline = occolor)

    def zeichnen(self):
        obj.avoidbvb()
        if checkedges.get() == 1:
            obj.drawedges()
        if checkfaces.get() == 1:
            obj.drawfaces()






obj = Object3d("Koerper", [100,100,100,200,200,200,300,300,300], [], 10.5, 3, 200)




def setobject(name):
    canvas1.delete(ALL)
    if name == 'iko':
        obj.initiko()
    if name == 'kep':
        obj.initkep()
    if name == 'dod':
        obj.initdod()
    print(obj.name() +' wird geladen')
    labelname.config(text = (obj.name() + 'darstellung'))
    master.title('Darstellung eines ' + obj.name() + 's in 3D ' + versionshinweis)

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
    obj.resetspeeds()
    #drehen ausführen
    if scalevar >= 85:        
        print('tempo zu hoch, zurücksetzen auf standard')
        scalevar = 100
        scalespeed.set(50)
    else:
        scalevar = scalespeed.get()
    mousespeed = 85 - scalevar
    obj.roty(xdiff/mousespeed)
    obj.rotx(ydiff/mousespeed)

def release(eventrelease):
    """Diese Funktion setzt die Variable mousedown, die anzeigt, ob die Maus gerade
    geklickt wird, auf 0 zurück.
    """
    global mousedown
    mousedown = 0

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
    if int(rstring) > 255 or int(gstring) > 255 or int(bstring) > 255:
        print('farben ungültig')
        colorhex = '#0000ff'
    return(colorhex)

def popup(type):
    """Diese Funktion öffnet ein neues Fenster, in dem je nach type ein Hinweis/eine Warnung ausgegeben wird.
    Args:
        type: string
    """
    if type == 'tip':
        msg = 'Es gibt vier Wege der Farbeingabe: \n    (1) Anklicken des Buttons mit der gewünschten Farbe \n    (2) Eingeben von Standardfarben von Python (Bsp: red, yellow, ...) \n    (3) Eingeben von Hexadezimalwerten (Bsp: #ab42cd) \n    (4) Eingeben von RGB-Tripeln (Bsp: rgb(42,69,255) )'
    if type == 'bvb':
        msg = 'Die Farbkombination schwarz-gelb ist dank \nFabien Streuber und Tristan Scholz verboten \nworden, um den Nutzer zu schützen. Die Farben \nwerden zu einer besseren Kombination geändert.'
    masterpopup = Tk()
    masterpopup.title('Hinweis')
    labelmsg = Label(masterpopup, text = msg, justify = 'left', font = '15')
    labelmsg.pack(padx = 10, pady = 10)

def colormode(colorname):
    """Diese Funktion stellt Farben der Widgets ein, da das Standardgrau einfach grauenvoll aussieht.
    Args:
        color: string
    """
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
    cbgradient['bg'] = color
    cbrewriteedit['bg'] = color
    scalespeed['bg'] = color
    scalespeed['activebackground'] = color
    scalespeed['highlightcolor'] = color
    scalegradient['bg'] = color
    scalegradient['activebackground'] = color
    scalegradient['highlightcolor'] = color


def initprogram():
    """Diese Funktion ruft Funktionen auf, die beim Öffnen sinnvoll/wichtig sind,
    wie z.B das Zeichnen eines ersten Körpers
    """
    setobject('kep')
    #obj.drawfaces()
    cbfaces.select()
    cbkep.select()
    obj.inffuncgradient()
    obj.initgradient()
    obj.infiniterep()
    master.title('Darstellung eines ' + obj.name() + 's in 3D')
    canvas1.bind("<Button-1>", click)
    canvas1.bind("<Button1-Motion>", currentpos)
    canvas1.bind("<ButtonRelease-1>", release)
    colormode('#fafafa')
    obj.zeichnen()
    


       
canvas1 = Canvas(master, width = 800, height = 600, highlightthickness = 0)
canvas1.grid(row = 0, column = 0, rowspan = 16, columnspan = 17)

labelname = Label(master, text = (obj.name() + 'darstellung'), font = 'Verdana 25' )
labelname.grid(row = 0, column = 0, rowspan = 3, columnspan = 10, sticky = NW, padx = 15, pady = 15)

buttonblackoc = Button(master, text = 'XX', bg = 'black', fg = 'black', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'black'), obj.zeichnen()))
buttonblackoc.grid(row = 16, column = 2, pady = 10)

buttonblueoc = Button(master, text = 'XX', bg = 'blue', fg = 'blue', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'blue'), obj.zeichnen()))
buttonblueoc.grid(row = 16, column = 3, pady = 10)

buttonredoc = Button(master, text = 'XX', bg = 'red', fg = 'red', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'red'), obj.zeichnen()))
buttonredoc.grid(row = 16, column = 4, pady = 10)

buttongreenoc = Button(master, text = 'XX', bg = 'green', fg = 'green', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'green'), obj.zeichnen()))
buttongreenoc.grid(row = 16, column = 5, pady = 10)

buttonyellowoc = Button(master, text = 'XX', bg = 'yellow', fg = 'yellow', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'yellow'), obj.zeichnen()))
buttonyellowoc.grid(row = 16, column = 6, pady = 10)

buttonblackfc = Button(master, text = 'XX', bg = 'black', fg = 'black', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'black'), obj.zeichnen()))
buttonblackfc.grid(row = 16, column = 9, pady = 10)

buttonbluefc = Button(master, text = 'XX', bg = 'blue', fg = 'blue', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'blue'), obj.zeichnen()))
buttonbluefc.grid(row = 16, column = 10, pady = 10)

buttonredfc = Button(master, text = 'XX', bg = 'red', fg = 'red', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'red'), obj.zeichnen()))
buttonredfc.grid(row = 16, column = 11, pady = 10)

buttongreenfc = Button(master, text = 'XX', bg = 'green', fg = 'green', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'green'), obj.zeichnen()))
buttongreenfc.grid(row = 16, column = 12, pady = 10)

buttonyellowoc = Button(master, text = 'XX', bg = 'yellow', fg = 'yellow', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'yellow'), obj.zeichnen()))
buttonyellowoc.grid(row = 16, column = 13, pady = 10)

labeloc = Label(master, text = 'Kantenfarbe: ', font = '14')
labeloc.grid(row = 17, column = 2, columnspan = 2, pady = 10)

editoc = Entry(master, font = '14', width = 15)
editoc.grid(row = 17, column = 4, columnspan = 3, pady = 10)
editoc.insert(10,'rgb(255,0,0)')

labelfc = Label(master, text = 'Füllfarbe: ', font = '14')
labelfc.grid(row = 17, column = 9, columnspan = 2, pady = 10)

editfc = Entry(master, font = '14', width = 15)
editfc.grid(row = 17, column = 11, columnspan = 3, pady = 10)
editfc.insert(10,'#b0daf0')

cbedges = Checkbutton(master, text = 'Kanten zeichnen', var = checkedges, command = lambda:(cbfaces.deselect(), cbedges.select(), zeichnen()))
cbedges.grid(row = 0, column = 16, columnspan = 2, padx = 15, pady = 5)

cbfaces = Checkbutton(master, text = 'Flächen zeichnen', var = checkfaces, command = lambda:(cbedges.deselect(), cbfaces.select(), zeichnen()))
cbfaces.grid(row = 1, column = 16, columnspan = 2, padx = 15, pady = 5)

labeldeg = Label(master, text = 'Drehungswinkel:')
labeldeg.grid(row = 2, column = 16, columnspan = 2)

cbdeg = Checkbutton(master, text = 'deg', var = checkdeg)
cbdeg.grid(row = 3, column = 17)
cbdeg.select()

editdeg = Entry(master, width = 8)
editdeg.grid(row = 3, column = 16, columnspan = 1, padx = 15, pady = 5)
editdeg.insert(10,'10')

buttonx = Button(master, text = 'rot x', command = lambda:(obj.rotx(1), obj.setspeeds('x',1)))
buttonx.grid(row = 5, column = 16, padx = 10, pady = 5)

buttony = Button(master, text = 'rot y', command = lambda:(obj.roty(1), obj.setspeeds('y',1)))
buttony.grid(row = 6, column = 16, padx = 10,  pady = 5)

buttonz = Button(master, text = 'rot z', command = lambda:(obj.rotz(1), obj.setspeeds('z',1)))
buttonz.grid(row = 7, column = 16, padx = 10,  pady = 5)

buttonmx = Button(master, text = 'rot -x', command = lambda:(obj.rotx(-1), obj.setspeeds('x',-1)))
buttonmx.grid(row = 5, column = 17, padx = 10,  pady = 5)

buttonmy = Button(master, text = 'rot -y', command = lambda:(obj.roty(-1), obj.setspeeds('y',-1)))
buttonmy.grid(row = 6, column = 17, padx = 10,  pady = 5)

buttonmz = Button(master, text = 'rot -z', command = lambda:(obj.rotz(-1), obj.setspeeds('z',-1)))
buttonmz.grid(row = 7, column = 17, padx = 10,   pady = 5)

cbreprot = Checkbutton(master, text = 'weiterdrehen', var = checkrep, command = obj.resetspeeds())
cbreprot.grid(row = 8, column = 16, columnspan = 2, padx = 15, pady = 5)

scalespeed = Scale(master, var = scalevar, orient = 'horizontal', highlightthickness = 0, label = 'Mausempfindlichkeit:', from_ = -4, to = 84, showvalue = 0, length = 130)
scalespeed.grid(row = 9, column = 16, columnspan = 3, padx = 15, pady = 5)
scalespeed.set(40)

cbkep = Checkbutton(master, text = 'Keplerstern zeichnen', justify = 'left', var = checkkep, command = lambda:(cbkep.select(), cbiko.deselect(), cbdod.deselect(), setobject('kep')))
cbkep.grid(row = 10, column = 16, columnspan = 2, pady = 5)

cbiko = Checkbutton(master, text = 'Ikosaeder zeichnen', justify = 'left', var = checkiko, command = lambda:(cbkep.deselect(), cbiko.select(), cbdod.deselect(), setobject('iko')))
cbiko.grid(row = 11, column = 16, columnspan = 2, pady = 5)

cbdod = Checkbutton(master, text = 'Dodekaeder zeichnen', justify = 'left', var = checkdod, command = lambda:(cbkep.deselect(), cbiko.deselect(), cbdod.select(), setobject('dod')))
cbdod.grid(row = 12, column = 16, columnspan = 2, pady = 5)

cbgradient = Checkbutton(master, text = 'Farbverlauf aktivieren', var = checkgradient, command = lambda:(obj.inffuncgradient()))
cbgradient.grid(row = 13, column = 16, columnspan = 2)

scalegradient = Scale(master, highlightthickness = 0, from_ = 50, to = 800, orient = 'horizontal', showvalue = 0)
scalegradient.grid(row = 14, column = 16, columnspan = 2, padx = 15)
scalegradient.set(300)

cbrewriteedit = Checkbutton(master, text = 'In Entry übernehmen', var = checkrewriteedit)
cbrewriteedit.grid(row = 15, column = 16, columnspan = 2, padx = 5)
cbrewriteedit.select()

buttontip = Button(master, text = 'Hinweis zu Farbeingabe', command = lambda:popup('tip'))
buttontip.grid(row = 16, rowspan = 1, column = 16, columnspan = 2)

buttonrefresh = Button(master, text = 'Farben aktualisieren', command = obj.zeichnen)
buttonrefresh.grid(row = 17, column = 16, columnspan = 2, padx = 15, pady = 5)


initprogram()


