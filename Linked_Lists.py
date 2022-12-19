# Verkettete Liste (VL) selbst implementiert - bislang nur init, append, get und VL-Ausgabe
# Node = ein Element der VL
# head = erster Node der VL
# nachfolger = Nächstes Element der VL, steht im jeweiligen Node

class Node:
    def __init__(self, daten):
        self.daten = daten     # Node mit Daten füllen
        self.nachfolger = None # Nachfolger ist (erstmal) keiner da

class VerketteteListe:
    def __init__(self):
        self.head = None # Liste ist noch leer, deshalb gibt es noch keinen Head (ersten Node)

    def __repr__(self):  # Diese Standardmethode liefert eine Repräsentation z.B. für print() zurück
        darstellung = [] # Temp-Variable für die Repräsentation (Darstellung) der VL
        aktuell = self.head # Ersten Node zum aktuellen machen
        if self.head!=None: # Falls mindestens ein Node existiert...
            darstellung.append(aktuell.daten) # ...Daten aus erstem Node anhängen
        while aktuell.nachfolger != None: # Solange ein Nachfolger vom aktuellen Node existiert
            aktuell = aktuell.nachfolger  # Den Nachfolger zwischenspeichern
            darstellung.append(aktuell.daten) # Daten aus Nachfolger an Repräsentation anhängen
        return str(darstellung)

    def append(self, daten):      # Iteriert durch die VL, falls nötig und hängt einen neuen Node an
        neuer_Node = Node(daten)  # Neuen Node anlegen, Daten dort speichern
        if self.head == None:      # Wenn die VL noch leer ist
            self.head = neuer_Node # Dann ist der neue Node der Head!
            return                 # und der append ist fertig!
        aktuell = self.head        # aktuellen Head zwischenspeichern
        while aktuell.nachfolger != None: # Solange ein Nachfolger vom aktuellen Node existiert
            aktuell = aktuell.nachfolger  # Den Nachfolger zwischenspeichern
        aktuell.nachfolger = neuer_Node   # An den letzten Node den neuen anhängen
        return

    def get(self, index):   # Liefert die Daten des Nodes mit dem Index zurück
        aktuell = self.head # Ersten Node zum aktuellen machen
        i = 0 # Start beim ersten Index
        while aktuell.nachfolger != None and i<index: # Solange ein Nachfolger vom aktuellen Node existiert...
            aktuell = aktuell.nachfolger              # ...den Nachfolger zwischenspeichern
            i+=1                                      # Indexvariable erhöhen
        if index>i: raise IndexError('linked-list-index out of range') # Wenn der Index zu groß war, Error ausgeben
        return aktuell.daten # Daten des aktuellen Nodes zurückgeben

    def delete(self, index):
        aktuell = self.head # Ersten Node zum aktuellen machen
        i = 0 # Start beim ersten Index
        while aktuell.nachfolger != None and i<index: # Solange ein Nachfolger vom aktuellen Node existiert...
            vorgänger = aktuell                       # Vorgänger merken
            aktuell = aktuell.nachfolger              # ...den Nachfolger zwischenspeichern
            i+=1                                      # Indexvariable erhöhen
        if index>i: raise IndexError('linked-list-index out of range') # Wenn der Index zu groß war, Error ausgeben
        vorgänger.nachfolger = aktuell.nachfolger     # Dem Vorgänger den Nachfolger vom zu löschenden (aktuellen) Node zuweisen
        del aktuell                                   # Aktuellen Node löschen

    def insert(self, index, daten):
        aktuell = self.head # Ersten Node zum aktuellen machen
        i = 0 # Start beim ersten Index
        while aktuell.nachfolger != None and i<index: # Solange ein Nachfolger vom aktuellen Node existiert...
            vorgänger = aktuell                       # Vorgänger merken
            aktuell = aktuell.nachfolger              # ...den Nachfolger zwischenspeichern
            i+=1                                      # Indexvariable erhöhen
        if index>i: raise IndexError('linked-list-index out of range') # Wenn der Index zu groß war, Error ausgeben
        neuer_Node = Node(daten)                      # Neuen Node anlegen, Daten dort speichern
        neuer_Node.nachfolger = aktuell               # Aktuellen Node als Nachfolger vom neuen Node festlegen
        vorgänger.nachfolger = neuer_Node             # Neuen Node als Nachfolger des Vorgängers festlegen


if __name__ == "__main__":   # Verhindert, dass bei einem Import dieses Skriptes das Hauptprogramm ausgeführt wird

    from random import uniform # Float-Zufallszahlen, nur zum Befüllen der VL

    vkliste = VerketteteListe() # Neue VK erzeugen
    vkliste.append("Erstes")    # An die neue VL anhängen
    vkliste.append("Zweites")
    vkliste.append("Drittes")
    for i in range(3): vkliste.append(i)
    for i in range(3): vkliste.append(round(uniform(0,100),2))

    print(vkliste)          # Greift auf die Methode __repr__() zu, um die komplette VL zu printen
    print("Index 6:",vkliste.get(6))   # Greift auf .get() zurück, um einen bestimmten Node auszulesen

    vkliste.delete(1)
    print("Lösche (.delete) Index 1:",vkliste)

    vkliste.insert(1, "Neues Zweites")
    print(vkliste)