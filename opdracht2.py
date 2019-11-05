def lees_inhoud(bestandnaam):
    """opent het bestand en zet het in een list. hierna worden [i][0] en [i][1] gekozen en in een 2d lijst gezet.

    input:
    bestandnaam - string
    output:
    return kolomAB - list
    """
    #zet het bestand in een list
    try:
        bestand = open(bestandnaam)
        lijst1 = []
        for regel in bestand:
            regel = regel.rstrip().split(',')
            lijst1.append(regel)

    #kiest alleen [i][0] en i[1] en zet deze in een 2d lijst
        kolomAB = []
        for i in range(1,len(lijst1)):
            kolomAB.append([lijst1[i][0], float(lijst1[i][1])])
        print(kolomAB[0:10])
        return kolomAB

    except IOError:
        print("Dit bestand kan niet gevonden worden")
    except ValueError:
        print("Conversie van getal mislukt")

def gemiddeldeberekenen(kolomAB):
    """rekent het totaalaantal en het gemiddelde uit

    input:
    kolomAB - list
    output:
    totaalaantal, gemiddelde - float
    """

    try:
        totaalaantal = 0
        for i in range(len(kolomAB)):
            totaalaantal += kolomAB[i][1]
        gemiddelde = totaalaantal/len(kolomAB)
        print(totaalaantal)
        print(gemiddelde)

    except ValueError:
        print("Conversie van getal mislukt")

def groterdan50(kolomAB):
    """Kijkt welke stukken in kolomAB groter zijn dan 50 en zet ze in een nieuwe lijst

    input:
    kolomAB - list
    output:
    return groterlijst - list
    """
    try:
        groterlijst = []
        for i in range(len(kolomAB)):
            if kolomAB[i][1] >= 50:
                groterlijst.append(kolomAB[i][0])
        return groterlijst
    
    except ValueError:
        print("Conversie van getal mislukt")
    

def main():
    bestandnaam = "SC_expression.csv"
    kolomAB = lees_inhoud(bestandnaam)
    gemiddeldeberekenen(kolomAB)
    groterlijst = groterdan50(kolomAB)
    print(groterlijst[0:10])
main()
