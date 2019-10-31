def lees_inhoud(bestandnaam):
    """ input: bestandnaam

output: kolomAB
"""
    #zet het bestand in een list
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

def gemiddeldeberekenen(kolomAB):
    """
input: kolomAB
output: totaal aantal en gemiddelde

"""
    totaalaantal = 0
    for i in range(len(kolomAB)):
        totaalaantal += kolomAB[i][1]
    gemiddelde = totaalaantal/len(kolomAB)
    print(totaalaantal)
    print(gemiddelde)

def groterdan50(kolomAB):
    """
input: kolomAB
output: groterlijst

"""
    groterlijst = []
    for i in range(len(kolomAB)):
        if kolomAB[i][1] >= 50:
            groterlijst.append(kolomAB[i][0])
    return groterlijst
    

def main():
    bestandnaam = "SC_expression.csv"
    kolomAB = lees_inhoud(bestandnaam)
    gemiddeldeberekenen(kolomAB)
    groterlijst = groterdan50(kolomAB)
    print(groterlijst[0:10])
main()
