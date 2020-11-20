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

color = '#f0f0f0'
print(hextorgb(color))
