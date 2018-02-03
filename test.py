import  pickle
from hash import *
import random

#Oggetto collisione, memorizza min, med, max per percentuale
class Coll:
    min_ = None
    med_ = None
    max_ = None

    def __init__(self, mini, med, maxi):
        self.min_ = mini
        self.med_ = med
        self.max_ = maxi

#Oggetto sequenza di ispezione, memorizza min, med, max per percentuale
class Len_Ispection:
    min_ = None
    med_ = None
    max_ = None

    def __init__(self, mini, med, maxi):
        self.min_ = mini
        self.med_ = med
        self.max_ = maxi

class test:

    #COSTRUTTORE
    def __init__(self):
        my_test = pickle.load(open("input.p", "rb"))
        self.m = my_test[0]
        self._test = my_test[1]
        self._col_IA = [Coll]*len(self._test)
        self._len_IA = [Len_Ispection]*len(self._test)
        self._col_C = [Coll]*len(self._test)

    #METODO CHE ESEGUE IL TEST
    def start(self):

        # ciclo sulle percentuali
        for perc in range(0, len(self._test)):
            self._len_IA[perc] = Len_Ispection(float("inf"),0.0,0)
            self._col_IA[perc] = Coll(float("inf"),0 ,0)

            self._col_C[perc] = Coll(float("inf"), 0, 0)

            # 20 test per ogni percentuale
            for it_1 in range(0, 20):
                A = Hash_IA(self.m)
                coll_A = 0

                B = Hash_C(self.m)
                coll_B = 0

                # ciclo di inserimento di m*(val%) oggetti nelle hash
                for it_2 in range(0, A.length*(self._test[perc])/100):
                    a = Node(int(random.uniform(0, 100*self.m)), (str)(chr(int(random.uniform(97,122)))))
                    A.insert(a)
                    if it_2 < B.length*(self._test[perc])/100:
                        B.insert(a)

                    coll_A += (1 if A.coll > 0 else 0)

                    # Indirizamento Aperto: aggiorno la lunghezza delle sequenze di ispezione min, med, max
                    if A.coll > self._len_IA[perc].max_:
                        self._len_IA[perc].max_ = A.coll
                    elif A.coll < self._len_IA[perc].min_:
                        self._len_IA[perc].min_ = A.coll
                    self._len_IA[perc].med_ = (self._len_IA[perc].med_ * it_2 + A.coll) / (it_2+1)

                # Indirizzamento Aperto: aggiorno valori di collisione min, med, max
                if coll_A < self._col_IA[perc].min_:
                    self._col_IA[perc].min_ = coll_A
                elif self._col_IA[perc].max_ < coll_A:
                    self._col_IA[perc].max_ = coll_A
                self._col_IA[perc].med_ = round(float((self._col_IA[perc].med_ * it_1 + coll_A) /(it_1+1)), 6)

                # Concatenamento: aggiorno valori di collisione min, med, max
                if B.coll < self._col_C[perc].min_:
                    self._col_C[perc].min_ = B.coll
                elif self._col_C[perc].max_ < B.coll:
                    self._col_C[perc].max_ = B.coll
                self._col_C[perc].med_ = round(float((self._col_C[perc].med_ * it_1 + B.coll)/(it_1+1)), 6)

        # Indirizzamento Aperto: liste con valori min, med, max (collisioni)
        IA_coll_min = []
        IA_coll_med = []
        IA_coll_max = []

        # Indirizzamento Aperto: liste con valori min, med, max (lunghezza sequenza ispezione)
        IA_len_min = []
        IA_len_med = []
        IA_len_max = []

        # Concatenamento: liste con valori min, med, max (collisioni)
        C_coll_min = []
        C_coll_med = []
        C_coll_max = []

        for i in range(0, len(self._test)):
            IA_coll_min.append(self._col_IA[i].min_)
            IA_coll_med.append(self._col_IA[i].med_)
            IA_coll_max.append(self._col_IA[i].max_)
            IA_len_min.append(self._len_IA[i].min_)
            IA_len_med.append(self._len_IA[i].med_)
            IA_len_max.append(self._len_IA[i].max_)
            C_coll_min.append(self._col_C[i].min_)
            C_coll_med.append(self._col_C[i].med_)
            C_coll_max.append(self._col_C[i].max_)

        # creo la lista risultato
        result =   [ self._test ,
                   [IA_coll_min, IA_coll_med, IA_coll_max] ,
                   [IA_len_min, IA_len_med, IA_len_max] ,
                   [C_coll_min, C_coll_med, C_coll_max] ]

        # creo il file pickle risultato
        pickle.dump(result, open("output.p", "wb"))