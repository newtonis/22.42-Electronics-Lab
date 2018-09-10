import osc
import gen
import np


class Bode:
    osc = None
    gen = None
    points = []
    current = 0
    status = None

    data_points = dict()

    def __init__(self,osc , gen):
        self.osc = osc
        self.gen = gen

    def begin(self, start_freq, end_freq, points):
        self.points = np.logspace(log10(start_freq), log10(end_freq), points)
        self.current = 0

    def update(self):
        if self.osc.adjust():
            print("adjusted! ")





