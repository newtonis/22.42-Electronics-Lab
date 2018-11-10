
data = dict()

data["freq"] = []
data["dbm"] = []

M = 1e6


def addToData(freq, dbm):
    data["freq"].append(freq)
    data["dbm"].append(dbm)


addToData(freq=1.8*M, dbm=-11.4)
addToData(freq=5.2*M, dbm=-21.4)
addToData(freq=8.6*M, dbm=-26.6)



#15, 22, 25 Y 29 orales
# 22 parcial
# repasar PLL

