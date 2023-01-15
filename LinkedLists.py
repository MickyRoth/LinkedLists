# Linked Lists (LL) for Python by Micky Roth 2023

class Node:
    '''
    Class for the list elements (Nodes)
    '''
    def __init__(self, daten):
        self.daten = daten     # Node mit Daten füllen
        self.nachfolger = None # Nachfolger ist (erstmal) keiner da

class LinkedList:
    ''' Class for the linked list (LL) 
        node = data element in the LL
        head = first node in the LL
        nachfolger = successor - next element in the LL
    '''

    def __init__(self):
        ''' Initialisation of the LL '''
        self.head = None # Liste ist noch leer, deshalb gibt es noch keinen Head (ersten Node)

    def __repr__(self):  # Diese Standardmethode liefert eine Repräsentation z.B. für print() zurück
        ''' Generation of the print-output (representation) of the LL'''
        darstellung = [] # Temp-Variable für die Repräsentation (Darstellung) der VL
        aktuell = self.head # Ersten Node zum aktuellen machen
        if self.head!=None: # Falls mindestens ein Node existiert...
            darstellung.append(aktuell.daten) # ...Daten aus erstem Node anhängen
        while aktuell.nachfolger != None: # Solange ein Nachfolger vom aktuellen Node existiert
            aktuell = aktuell.nachfolger  # Den Nachfolger zwischenspeichern
            darstellung.append(aktuell.daten) # Daten aus Nachfolger an Repräsentation anhängen
        return str(darstellung)

    def append(self, daten):      # Iteriert durch die VL, falls nötig und hängt einen neuen Node an
        '''Appends a data element at the end of the LL'''
        neuer_Node = Node(daten)  # Neuen Node anlegen, Daten dort speichern
        if self.head == None:      # Wenn die VL noch leer ist
            self.head = neuer_Node # Dann ist der neue Node der Head!
            return                 # und der append ist fertig!
        aktuell = self.head        # aktuellen Head zwischenspeichern
        while aktuell.nachfolger != None: # Solange ein Nachfolger vom aktuellen Node existiert
            aktuell = aktuell.nachfolger  # Den Nachfolger zwischenspeichern
        aktuell.nachfolger = neuer_Node   # An den letzten Node den neuen anhängen
        return

    def set(self, index, daten):
        ''' changes the content of a data-element at the specified index position'''
        aktuell = self.head # Ersten Node zum aktuellen machen
        i = 0 # Start beim ersten Index
        while aktuell.nachfolger != None and i<index: # Solange ein Nachfolger vom aktuellen Node existiert...
            vorgänger = aktuell                       # Vorgänger merken
            aktuell = aktuell.nachfolger              # ...den Nachfolger zwischenspeichern
            i+=1                                      # Indexvariable erhöhen
        if index>i: raise IndexError('linked-list-index out of range') # Wenn der Index zu groß war, Error ausgeben
        aktuell.daten = daten

    def get(self, index):   # Liefert die Daten des Nodes mit dem Index zurück
        ''' Returns the element with the specified index'''
        if self.head == None:      # Wenn die VL noch leer ist
            raise IndexError('linked-list-index out of range')
        aktuell = self.head # Ersten Node zum aktuellen machen
        i = 0 # Start beim ersten Index
        while aktuell.nachfolger != None and i<index: # Solange ein Nachfolger vom aktuellen Node existiert...
            aktuell = aktuell.nachfolger              # ...den Nachfolger zwischenspeichern
            i+=1                                      # Indexvariable erhöhen
        if index>i: raise IndexError('linked-list-index out of range') # Wenn der Index zu groß war, Error ausgeben
        return aktuell.daten # Daten des aktuellen Nodes zurückgeben

    def delete(self, index):
        ''' Deletes the element with the specified index'''
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
        ''' Inserts a data-element at the specified index position'''
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


    def len(self):
        ''' Returns the number of nodes of the LL'''
        if self.head == None: return 0     # Wenn die VL noch leer ist
        aktuell = self.head # Ersten Node zum aktuellen machen
        i = 0 # Start beim ersten Index
        while aktuell.nachfolger != None:                       # Solange ein Nachfolger vom aktuellen Node existiert...
            aktuell = aktuell.nachfolger                        # ...den Nachfolger zwischenspeichern
            i+=1                                                # Indexvariable erhöhen
        return i+1                                              # Daten des Indexzählers zurückgeben

if __name__ == "__main__":   # Verhindert, dass bei einem Import dieses Skriptes das Hauptprogramm ausgeführt wird
    # Demonstration aller wichtiger Methoden

    mylliste = LinkedList() # Neue VL erzeugen
    for i in range(8): mylliste.append(i+100)

    print(mylliste)          # Greift auf die Methode __repr__() zu, um die komplette VL zu printen
    print("get Index 3:",mylliste.get(6))   # Greift auf .get() zurück, um einen bestimmten Node auszulesen

    mylliste.delete(1)
    print("Lösche (.delete) Index 1:", mylliste)

    mylliste.insert(1, "Neues Element eingefügt!")
    print(mylliste)

    print("Ändere Element 1:")
    mylliste.set(1, "Geändert")
    print(mylliste)

    print("Länge der Liste:", mylliste.len(), "Elemente")
