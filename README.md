# Hash
A short description of the Hashmap, and little bit of collision resolution theory (in Italian)

L'esercizio proposto è quello di vedere il comportamento delle tabelle hash al crescere del
fattore di carico $alpha = n / m$.
Si implementano le tabelle hash con il metodo di risoluzione delle collisioni a "concatenamento"
e "indirizzamento aperto" (ispezione lineare):
- la funzione hash è calcolata con il metodo di divisione;
- m = dimensione tabella, se m inserito non è primo se ne sceglie
  il numero primo >=m più vicino nel caso di indirizzamento aperto,
  mentre <=m per concatenamento;
In ingresso si prende un array pickle del tipo [200, [10, 50, 80]] che indica:
- tabella con 200 elementi (m=200)
- testare le percentuali 10, 50, 80 (n=10% of m, ecc..)
I risultati vengono raccolti e mostrati con più grafici.

(esercizio x04 el corso Algoritmi e Strutture dati, Unifi)
