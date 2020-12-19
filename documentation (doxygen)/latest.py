"""@package docstring
Documentation for this module.

More details.
"""

from tkinter import *
import math, time

master = Tk()

#nötige Variablen
versionshinweis =  '(Version 3.13.5)'
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
global gradientcolor
global direction
global colors



class Object3d(object):
    """
    Diese Klasse beschreibt unsere Körper, mit Name, 3D- und 2D-Koordinaten, Seitenlänge sl, Streckungsfaktor a und der Eckenzahl der Seitenflächen ek.
    """
    def __init__(self, name = str, xyz = [], xy = [], sl = float, ek = int, a = int):
        self.__name = name
        self.__xyz = xyz
        self.__xy = xy
        self.__sl = sl
        self.__ek = ek
        self.__a = a

    def name(self):
        """Diese Methode dient dazu, den Namen des Objekts zurückzugeben (benötigt
        für Aktualisierung des Programmtitels im Label"""
        return(self.__name)

    def initkep(self):
        """Diese Methode modifiziert die Member-Variablen der object3d Klasse so
        dass ein Keplerstern gezeichnet werden kann, gibt über die Überschrift aus,
        welcher Körper gezeichnet wird, und dreht ihn in eine optisch ansprechende
        Startposition.
        """
        self.__name = 'Keplerstern'
        self.__a = 150
        self.__xyz = [self.__a,0,0, 0,self.__a,0, 0,0,self.__a, -self.__a,0,0, 0,-self.__a,0, 0,0,-self.__a,
                   self.__a,-self.__a,-self.__a, -self.__a,self.__a,-self.__a, -self.__a,-self.__a,self.__a, -self.__a,self.__a,self.__a, self.__a,-self.__a,self.__a, self.__a,self.__a,-self.__a, -self.__a,-self.__a,-self.__a, self.__a,self.__a,self.__a]
        self.__sl = self.__a * math.sqrt(2)
        self.__ek = 3
        obj.rotx(2)
        obj.roty(2)

    def initiko(self):
        """Diese Methode modifiziert die Member-Variablen der object3d Klasse so
        dass ein Ikosaeder gezeichnet werden kann, gibt über die Überschrift aus,
        welcher Körper gezeichnet wird, und dreht ihn in eine optisch ansprechende
        Startposition.
        """
        self.__name = 'Ikosaeder'
        self.__a = 200
        phi = gold * self.__a
        self.__xyz = [0,-self.__a,phi, 0,-self.__a,-phi, 0,self.__a,phi, 0,self.__a,-phi, phi,0,self.__a, phi,0,-self.__a, -phi,0,self.__a, -phi,0,-self.__a, self.__a,-phi,0, self.__a,phi,0, -self.__a,-phi,0, -self.__a,phi,0]
        self.__sl = 2 * phi
        self.__ek = 3
        obj.rotx(2)

    def initdod(self):
        """Diese Methode modifiziert die Member-Variablen der object3d Klasse so
        dass ein Dodekaeder gezeichnet werden kann, gibt über die Überschrift aus,
        welcher Körper gezeichnet wird, und dreht ihn in eine optisch ansprechende
        Startposition.
        """
        self.__name = 'Dodekaeder'
        self.__a = 130
        phi = (gold*self.__a)
        phim = self.__a/gold
        self.__xyz = [self.__a,self.__a,self.__a, -self.__a,self.__a,self.__a, self.__a,-self.__a,self.__a, self.__a,self.__a,-self.__a, self.__a,-self.__a,-self.__a, -self.__a,self.__a,-self.__a, -self.__a,-self.__a,self.__a, -self.__a,-self.__a,-self.__a, phim,phi,0, -phim,phi,0, -phim,-phi,0, phim,-phi,0, 0,phim,phi, 0,phim,-phi, 0,-phim,-phi, 0,-phim,phi, phi,0,phim, phi,0,-phim, -phi,0,phim, -phi,0,-phim]
        self.__sl = 2*phi
        self.__ek = 5
        obj.rotx(2)
        obj.roty(-1)

    def conv32(self):
        """Diese Methode wandelt die dreidimensionalen Koordinaten aller Punkte in
        2D-Koordinaten um, die gezeichnet werden können. An den 3D-Koordinaten werden
        keine Änderungen vorgenommen, da 2D- und 3D-Koordinaten in verschiedenen Arrays
        enthalten sind.
    
        returns:
            xy: list    
        """
        self.__xy = []
        for i in range (0,len(self.__xyz)//3):
            distance = 3000
            #strahlensatz
            self.__xy.append(mx + (self.__xyz[3*i] * distance)/(self.__xyz[3*i+2] + distance))
            self.__xy.append(my + (self.__xyz[3*i+1] * distance)/(self.__xyz[3*i+2] + distance))
        return self.__xy

    def getcolor(self, string):
        """Diese Methode fragt je nachdem ob der String fc (face color) oder oc (Outline
        Color) enthält den Inhalt des zugehörigen Entrys ab. Wenn dort ein rgb-Wert steht,
        wird dieser mit der rgbtohex() Methode in hex umgewandelt. Zum Schluss wird die
        Zeichenfarbe für das jeweilige Element (face/outline) zurückgegeben.
    
        args:
            string: string, der 'fc' oder 'oc' enthält
    
        returns:
            color: string, der Farbe enthält
        """
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
        """Diese Methode initialisiert den Farbverlauf, indem dafür nötigen Variablen
        zum ersten Mal ein sinnvoller Wert zugewiesen wird."""
        global direction
        global colors
    
        direction = [0,0,0]
        colors = [255,0,0]

        direction[0] = -1
        direction[1] = 1
        direction[2] = 0
        
    def inffuncgradient(self):
        """Diese Methode ruft sich aller 50 ms rekursiv selbst auf. Falls mit dem
        Checkbutton ein Farbverlauf gewünscht wird, wird dieser mithilfe der Methode
        gradientgetcolor() umgesetzt
        """
        time.sleep(0.001)
        if checkgradient.get() == 1:
            master.after(50, lambda:(obj.gradientgetcolor(), obj.zeichnen(), obj.inffuncgradient()))

    def gradientgetcolor(self):
        """Diese Methode wird aller 50 ms aufgerufen und ändert die RGB-Werte jeweils,
        um die Farben kleinschrittig zu verändern. Je nach speed (abhängig von Scale)
        geschieht das z.T. auch etwas schneller/langsamer
        """
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
        """Diese Methode sortiert das Array obj.xyz welches 3D-Koordinaten enthält nach
        höchstem z-Wert. Punkte die also "weiter hinten" sind, werden dann zuerst gezeichnet
        und z.T. übermalt. Dadurch werden verdeckte Kanten unsichtbar.
    
        returns:
            obj.xyz: Array mit 3D-Koordinaten
        """        
        for m in range(0,len(self.__xyz)//3):
            for n in range(0, len(self.__xyz)//3-m-1):
                if (self.__xyz[3*n+2] > self.__xyz[3*(n+1)+2]):
                    self.__xyz[3*n],self.__xyz[3*(n+1)] = self.__xyz[3*(n+1)],self.__xyz[3*n]
                    self.__xyz[3*n+1],self.__xyz[3*(n+1)+1] = self.__xyz[3*(n+1)+1],self.__xyz[3*n+1]
                    self.__xyz[3*n+2],self.__xyz[3*(n+1)+2] = self.__xyz[3*(n+1)+2],self.__xyz[3*n+2]
        #print('self.__xyz sortiert: ' + str(self.__xyz))
        return(self.__xyz)

    def resetspeeds(self):
        """Diese Methode setzt die Drehgeschwindigkeiten in alle Dimensionen (x,y,z) auf 0.
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

    def getdeg(self):
        """Diese Methode fragt den Inhalt des Entrys ab, welches den Drehungswinkel enthält.
        wenn das Entry nichts oder nur ein Komma enthält, wird der Drehungswinkel automatisch
        auf 0 gesetzt. Je nach Zustand der Checkbox für Bogen-/Gradmaß kann der Winkel zwischen
        ebengenannten umgewandelt werden. Wenn gerade mit der Maus der Körper bewegt
        wird, wird der Winkel auf 10° gesetzt, da in diesem Fall die Geschwindigkeit
        über die Scale Mausempfindlichkeit geregelt wird.
        """
        if mousedown == 1:
            deg = 10/180*math.pi
        else:
            error = 0
            stringdeg = editdeg.get()
            if stringdeg != '':
                if stringdeg == '.':
                    deg = 0
                    print('unvollständige Eingabe (Winkel)')
                else:
                    for i in range (0, len(stringdeg)):
                        if stringdeg[i] not in ['0','1','2','3','4','5','6','7','8','9','.']:
                            error = 1
                            print('fehlerhafte Eingabe (Winkel)')
                    if error == 0:
                        deg = float(stringdeg)
                    else:
                        deg = 0
            else:
                deg = 0
            if checkdeg.get() == 1:
                deg = deg / 180 * math.pi
        return(deg)

    def setspeeds(self, char, speed):
        """Diese Funnktion ruft erst die resetspeeds() Methode auf, und je nachdem ob der
        String char x,y oder z enthält, wird die Drehgeschwindigkeitum die jeweilige Achse
        auf die Variable speed gesetzt. Diese enthält normalerweise -1 oder 1.

        Args:
            char: string
            speed: integer
        """
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
        """Diese Methode ruft sich aller 100ms selbst auf und dreht den Körper mithilfe der
        rotall()-Methode
        """
        master.after(100, lambda:(obj.rotall(), obj.infiniterep()))

    def rotall(self):
        """Diese Methode führt letztendlich die Drehung für die weiterdrehen-Option aus,
        indem sie mithilfe der rotx()-, roty()- und rotz()-Methode den Körper je nach
        jeweiliger Geschwindigkeit um die jeweiligen Achsen dreht.
        """
        global xspeed
        global yspeed
        global zspeed
        if checkrep.get() == 1:
            if xspeed != 0:
                obj.rotx(xspeed)
            if yspeed != 0:
                obj.roty(yspeed)
            if zspeed != 0:
                obj.rotz(zspeed)
        
    def rotx(self, sgndeg):
        """Diese Methode berechnet aus Winkel getdeg() und Vorzeichen sgndeg einen
        Drehungswinkel, rotiert alle Punkte um diesen Winkel um die x-Achse und zeichnet
        am Ende den Körper neu.
        """
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
        """Diese Methode berechnet aus Winkel getdeg() und Vorzeichen sgndeg einen
        Drehungswinkel, rotiert alle Punkte um diesen Winkel um die y-Achse und zeichnet
        am Ende den Körper neu.
        """
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
        """Diese Methode berechnet aus Winkel getdeg() und Vorzeichen sgndeg einen
        Drehungswinkel, rotiert alle Punkte um diesen Winkel um die z-Achse und zeichnet
        am Ende den Körper neu.
        """
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
        """Diese Methode prüft, ob der Nutzer bei der Farbauswahl aufgrund geistiger
        Umnachtung die katastrophale Farbkombination schwarz-gelb gewählt hat, und
        stellt eine angenehmere Farbkombination ein, da es sonst zu seelischen Schmerzen
        aufgrund der schwarz-gelben Farbe kommen könnte und die Versicherungen der
        Codeschreiber diese Gefahr nicht abdecken (nichtmal Fabis private Kasse).
        """
        black = 0
        yellow = 0
        """
        if editfc.get() == 'black':
            black = 1
        if editfc.get() == 'yellow':
            yellow = 1
        if editoc.get() == 'black':
            black = 1
        if editoc.get() == 'yellow':
            yellow = 1
        """
        fc = editfc.get()
        oc = editoc.get()
        black = checkcolor('black',fc) + checkcolor('black',oc)
        yellow = checkcolor('yellow',fc) + checkcolor('yellow',oc)
        if black == yellow == 1:
            popup('bvb')
            editoc.delete(0,'end')
            editoc.insert(10,'rgb(255,0,0)')
            editfc.delete(0,'end')
            editfc.insert(10,'#b0daf0')
            
    def drawedges(self):
        """Diese Methode leert zuerst vollständig die Zeichenfläche. Danach erzeugt sie mit
        der conv32() Methode die 2D-Koordinaten des "Körpers" und kombiniert nun immer 2
        Punkte, solange bis alle Kombinationen probiert sind. Wenn der Abstand der zwei
        Punkte der Seitenlänge obj.sl (mit einer Toleranz von 5) entspricht, werden mit der
        getcolor() Methode die gewünschte Linienfarbe errechnet und die Punkte verbunden.
        """
        canvas1.delete(ALL)
        self.__xy = obj.conv32()
        for k in range (0,len(self.__xyz)//3):
            for m in range (0,len(self.__xyz)//3):
                abstand = (math.sqrt((self.__xyz[3*k]-self.__xyz[3*m])**2+(self.__xyz[3*k+1]-self.__xyz[3*m+1])**2+(self.__xyz[3*k+2]-self.__xyz[3*m+2])**2))
                #print(abstand)
                if (abs(abstand-self.__sl) < 5):
                    canvas1.create_line(self.__xy[2*k],self.__xy[2*k+1],self.__xy[2*m],self.__xy[2*m+1], fill = obj.getcolor('oc'))
                        
    def drawfaces(self):
        """Diese Methode leert zuerst vollständig die Zeichenfläche. Die 3D-Koordinaten
        werden mit zsort() sortiert. Danach  werden systematisch Punkte kombiniert, und
        überprüft ob der Abstand der Punkte der Seitenlänge obj.sl entspricht (Toleranz).
        Wenn man so Dreiecke/Fünfecke findet, die zum Körper gehören, werden die Punkte
        die dazu gehören dem Array facelist hinzugefügt. Bei Dreiecken wird geprüft, ob die
        Fläche bereits enthalten ist, um Flächen nicht doppelt zu zeichnen. Bei Fünfecken
        bräuchte dies Verfahren mehr Rechenleistung als das doppelt zeichnen. Danach werden
        Flächenmittelpunkte berechnet und nach höchsten z-Koordinaten sortiert, um die
        verdeckten Flächen zum Schluss zu malen, und es werden dann die gefundenen Flächen
        in facelist gezeichnet.
        """
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
                                    start = time.time()
                                    for f in range(0,self.__ek):
                                        for g in range(0,self.__ek-f-1):
                                            if (abc[f] > abc[f+1]):
                                                abc[f],abc[f+1] = abc[f+1],abc[f]
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
                for n in range(0,len(facelist)//3-m-1):
                    mzpolygon1 = (self.__xyz[3*facelist[3*n]+2] + self.__xyz[3*facelist[3*n+1]+2] + self.__xyz[3*facelist[3*n+2]+2])/3
                    mzpolygon2 = (self.__xyz[3*facelist[3*(n+1)]+2] + self.__xyz[3*facelist[3*(n+1)+1]+2] + self.__xyz[3*facelist[3*(n+1)+2]+2])/3
                    if (mzpolygon1 > mzpolygon2):
                        facelist[3*n],facelist[3*(n+1)] = facelist[3*(n+1)],facelist[3*n]
                        facelist[3*n+1],facelist[3*(n+1)+1] = facelist[3*(n+1)+1],facelist[3*n+1]
                        facelist[3*n+2],facelist[3*(n+1)+2] = facelist[3*(n+1)+2],facelist[3*n+2]                        
                    
            #finales zeichnen
            self.__xy = obj.conv32()
            for i in range(0,len(facelist)//3):
                p = facelist[3*i]
                q = facelist[3*i+1]
                r = facelist[3*i+2]
                canvas1.create_polygon(self.__xy[2*p],self.__xy[2*p+1], self.__xy[2*q],self.__xy[2*q+1], self.__xy[2*r],self.__xy[2*r+1], fill = fccolor, outline = occolor)

    def zeichnen(self):
        """Diese Methode führt je nach Zeichenmodus (mit Checkbuttons ausgewählt) die
        Zeichnung mithilfe der obj.drawedges() oder obj.drawfaces()-Methode aus.
        """
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
    """Diese Methode setzt die Variable mousedown, die zeigt, ob die Maus gerade
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
    """Diese Methode fragt die aktuellen Koordinaten des Mauszeigers ab und berechnet
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
    """Diese Methode setzt die Variable mousedown, die anzeigt, ob die Maus gerade
    geklickt wird, auf 0 zurück.
    """
    global mousedown
    mousedown = 0

def rgbtohex(color):
    """Diese Methode wandelt rgb-Farben in hex-Farben um, die Python leicht
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

def hextorgb(color):
    """Diese Methode wandelt hex-Farben in rgb-Farben um.

    args:
        color: String mit hex-farbe

    returns:
        colorrgb: String mit rgb-Farbe
    """
    startindex = color.find('#') + 1
    r = color[startindex: startindex + 2]
    g = color[startindex + 2: startindex + 4]
    b = color[startindex + 4: startindex + 6]
    rstring = str(int(r,16))
    gstring = str(int(g,16))
    bstring = str(int(b,16))
    colorrgb = 'rgb(' + rstring + ',' + gstring + ',' + bstring + ')'
    return(colorrgb)

def checkcolor(avoidcolor, color):
    """Diese Methode prüft, ob die zu prüfenden Farbe color mit der Farbe avoidcolor auf eine bestimmte Toleranz
    genau übereinstimmt."""
    x = 0
    if (color == avoidcolor) or (avoidcolor == 'yellow' and color == 'gold') :
        x = 1
    else:
        if color[0] == '#':
            color = hextorgb(color)
        if color[0:2] == 'rg':
            tolerance = 30
            if avoidcolor == 'yellow':
                ravoid = 255
                gavoid = 255
                bavoid = 0
            if avoidcolor == 'black':
                ravoid = 0
                gavoid = 0
                bavoid = 0
            color = color[color.find('(')+1:color.find(')')]
            rcolor = int(color[:color.find(',')])
            colorrest = color[color.find(',')+1:]
            gcolor = int(colorrest[:colorrest.find(',')])
            bcolor = int(colorrest[colorrest.find(',')+1:])
            if abs(ravoid-rcolor) < tolerance:
                if abs(gavoid-gcolor) < tolerance:
                    if abs(bavoid-bcolor) < tolerance:
                        x = 1
    return(x)   
        

def popup(typ):
    """Diese Methode öffnet ein neues Fenster, in dem je nach type ein Hinweis/eine Warnung ausgegeben wird.
    Args:
        typ: string
    """
    if typ == 'tip':
        msg = 'Es gibt vier Wege der Farbeingabe: \n    (1) Anklicken des Buttons mit der gewünschten Farbe \n    (2) Eingeben von Standardfarben von Python (Bsp: red, yellow, ...) \n    (3) Eingeben von Hexadezimalwerten (Bsp: #ab42cd) \n    (4) Eingeben von RGB-Tripeln (Bsp: rgb(42,69,255) )'
    if typ == 'bvb':
        msg = 'Die Farbkombination schwarz-gelb ist dank \nFabien Streuber und Tristan Scholz verboten \nworden, um den Nutzer zu schützen. Die Farben \nwerden zu einer besseren Kombination geändert.'
    masterpopup = Tk()
    masterpopup.title('Hinweis')
    labelmsg = Label(masterpopup, text = msg, justify = 'left', font = '15')
    labelmsg.pack(padx = 10, pady = 10)

def colormode(colorname):
    """Diese Methode stellt Farben der Widgets ein, da das Standardgrau einfach grauenvoll aussieht.
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
    """Diese Methode ruft Methodeen auf, die beim Öffnen sinnvoll/wichtig sind,
    wie z.B das Zeichnen eines ersten Körpers
    """
    setobject('kep')
    #obj.drawfaces()
    cbfaces.select()
    cbkep.select()
    obj.inffuncgradient()
    obj.initgradient()
    obj.infiniterep()
    master.title('Darstellung eines ' + obj.name() + 's in 3D ' + versionshinweis)
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

cbedges = Checkbutton(master, text = 'Kanten zeichnen', var = checkedges, command = lambda:(cbfaces.deselect(), cbedges.select(), obj.zeichnen()))
cbedges.grid(row = 0, column = 16, columnspan = 2, padx = 15, pady = 5)

cbfaces = Checkbutton(master, text = 'Flächen zeichnen', var = checkfaces, command = lambda:(cbedges.deselect(), cbfaces.select(), obj.zeichnen()))
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


