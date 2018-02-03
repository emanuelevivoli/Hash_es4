debug = False

#Oggetto da inserire nelle tabelle hash
class Node:
    key = None
    val = None

    def __init__(self, key, val):
        self.key = key
        self.val = val

#HASH INDIRIZZAMENTO APERTO
class Hash_IA:
    coll = 0

    #COSTRUTTORE
    def __init__(self, m):
        self.length = self.f(m)
        self._table = [Node]*self.length

    #FUNZIONE HASH
    def h(self, key):
        return key % self.length

    #INSERIMENTO
    def insert(self, x):
        i = 0
        self.coll = 0
        pos = self.h(self.h(x.key) + i)
        while( self._table[pos].val != None if self._table[pos]!= None else False) and i<self.length:
            i+=1
            pos = self.h(self.h(x.key) + i)

        self.coll = i

        if i < self.length:
            self._table[pos] = x
            if(debug): print("OK Inse of x:" + (str)(x.key) + (str)(x.val))
            return True
        if(debug): print("NO Inse of x:" + (str)(x.key)+(str)(x.val))
        return False


    #CANCELLAZIONE
    def delete(self, x):
        i = 0
        pos = self.h(self.h(x.key) + i)
        while self._table[pos] != None and i < self.length:
            if (self._table[pos].key == x.key and self._table[pos].val == x.val):
                self._table[pos].val = None
                if(debug): print("OK Canc of x:" + (str)(x.key)+(str)(x.val))
                return True
            i += 1
            pos = self.h(self.h(x.key) + i)
        if(debug): print("NO Canc of x:" + (str)(x.key)+(str)(x.val))
        return False

    #RICERCA
    def search(self, key):
        i = 0
        pos = self.h(self.h(key) + i)
        while self._table[pos] != None and i < self.length:
            if (self._table[pos].key == key):
                if(debug): print("OK Sear of x:" + (str)(key)+(str)(self._table[pos].val)+ " pos " + (str)(pos))
                return pos
            i += 1
            pos = self.h(self.h(key) + i)
        if(debug): print("NO Sear of x:" +(str)(key))
        return False

    #FUNZIONE CALCOLA LUNGHEZZA HASH
    def f(self, m):
        for a in range(2, m):
            if m % a == 0:
                m += 1
                return self.f(m)
        else:
            return m

#HASH CON CONCATENAMENTO
class Hash_C:
    coll = 0

    #COSTRUTTORE
    def __init__(self, m):
        self.length = self.f(m)
        self._table = [None]*self.length

    #FUNZIONE HASH
    def h(self, key):
        return key % self.length

    #INSERIMENTO
    def insert(self, x):
        self.coll += 1
        pos = self.h(x.key)
        if self._table[pos] == None:
            self.coll -= 1
            self._table[pos] = []
        self._table[pos].insert(0, x)

    #CANCELLAZIONE
    def delete(self, x):
        pos = self.h(x.key)
        if self._table[pos] != None:
            for it in [0, len(self._table[pos])]:
                if self._table[pos][it].key == x.key and self._table[pos][it].val == x.val:
                    self._table[pos].remove(x)
                    if(debug): print("OK Canc of x:" + (str)(x.key) + (str)(x.val))
                    return True
        else:
            if(debug): print("NO Canc of x:" + (str)(x.key) + (str)(x.val))
            return False

    #RICERCA
    def search(self, key):
        pos = self.h(key)
        if self._table[pos] != None:
            for it in [0, len(self._table[pos])]:
                if self._table[pos][it].key == key:
                    if(debug): print("OK Sear of x:"+(str)(key)+" pos " + (str)(pos)+" "+(str)(it))
                    return True
        else:
            if(debug): print("NO Sear of x:" + (str)(key))
            return False

    #FUNZIONE CALCOLA LUNGHEZZA HASH
    def f(self, m):
        for a in range(2, m):
            if m % a == 0:
                m -= 1
                return self.f(m)
        else:
            return m