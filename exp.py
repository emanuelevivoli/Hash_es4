from test import *
import matplotlib.pyplot as plt

input = [1000,[10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 87, 89, 90,
91, 92, 93, 94, 95, 95, 97, 98, 99, 100]]
pickle.dump(input, open("input.p", "wb"))

test_ = test()
test_.start()

output = pickle.load(open("output.p", "rb"))

# creazione dell'oggetto plot

plt.switch_backend('TkAgg')

# subplot Collisioni in Indirizzamento Aperto
plt.subplot(221)
plt.plot(output[0], output[1][0])
plt.plot(output[0], output[1][1])
plt.plot(output[0], output[1][2])
plt.xlabel("Percentuali")
plt.ylabel("Collisioni")
plt.title("Collisioni in Indirizzamento Aperto")
plt.legend(["Min", "Med", "Max"])

# subplot Sequenze di Ispezione in Indirizzamento Aperto
plt.subplot(222)
plt.plot(output[0], output[2][0])
plt.plot(output[0], output[2][1])
plt.plot(output[0], output[2][2])
plt.xlabel("Percentuali")
plt.ylabel("Sequenza Ispezione")
plt.title("Sequenze di Ispezione in Indirizzamento Aperto")
plt.legend(["Min", "Med", "Max"])

# subplot Collisioni in Concatenamento
plt.subplot(212)
plt.plot(output[0], output[3][0])
plt.plot(output[0], output[3][1])
plt.plot(output[0], output[3][2])
plt.xlabel("Percentuali")
plt.ylabel("Collisioni")
plt.title("Collisioni in Concatenamento")
plt.legend(["Min", "Med", "Max"])

# imposto grandezza finestra plot Maximized
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')

plt.show()

