def start(self):
    # ciclo sulle percentuali
    for perc in range(0, len(self._test)):
        self._len_IA[perc] = Len_Ispection(float("inf"), 0.0, 0)
        self._col_IA[perc] = Coll(float("inf"), 0.0, 0)
        self._col_C[perc] = Coll(float("inf"), 0.0, 0)

        # 20 test per ogni percentuale
        for it_1 in range(0, 20):
            A = Hash_IA(self.m)
            coll_A = 0
            B = Hash_C(self.m)

            # ciclo di inserimento di m*(val%) oggetti nelle hash
            for it_2 in range(0, A.length * (self._test[perc]) / 100):
                a = Node(int(random.uniform(0, 100 * self.m)),
                         (str)(chr(int(random.uniform(97, 122)))))
                A.insert(a)
                if it_2 < B.length * (self._test[perc]) / 100:
                    B.insert(a)
                coll_A += (1 if A.coll > 0 else 0)

                # Indirizamento Aperto: aggiorno la lunghezza
                # delle sequenze di ispezione min, med, max
                if A.coll > self._len_IA[perc].max_:
                    self._len_IA[perc].max_ = A.coll
                elif A.coll < self._len_IA[perc].min_:
                    self._len_IA[perc].min_ = A.coll
                self._len_IA[perc].med_ = \
                    round(float((self._len_IA[perc].med_*it_2+A.coll)
                                /(it_2 + 1)), 6)

            # Indirizzamento Aperto: aggiorno valori
            # di collisione min, med, max
            if coll_A < self._col_IA[perc].min_:
                self._col_IA[perc].min_ = coll_A
            elif self._col_IA[perc].max_ < coll_A:
                self._col_IA[perc].max_ = coll_A
            self._col_IA[perc].med_ = \
                round(float((self._col_IA[perc].med_*it_1+coll_A)
                            /(it_1 + 1)), 6)



            # Concatenamento: aggiorno valori di collisione min, med, max
            if B.coll < self._col_C[perc].min_:
                self._col_C[perc].min_ = B.coll
            elif self._col_C[perc].max_ < B.coll:
                self._col_C[perc].max_ = B.coll
            self._col_C[perc].med_ = \
                round(float((self._col_C[perc].med_*it_1+B.coll)
                            /(it_1 + 1)), 6)