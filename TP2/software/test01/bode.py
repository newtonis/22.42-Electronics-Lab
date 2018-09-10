import numpy as np


class Bode:
    points = []
    current = 0
    amp = 2
    data = dict()
    status = 0

    def __init__(self, osc, gen):
        self.osc = osc
        self.gen = gen

    def start(self, start_freq, end_freq, points , amp):
        self.points = np.logspace(np.log10(start_freq), np.log10(end_freq), points)
        self.current = 0
        self.amp = amp
        self.status = 1
        self.get_to_freq(self.points[self.current], self.amp)

    def update(self):
        if self.status:
            if self.osc.update():
                print("Taking point ", self.current)

                self.data[str(self.points[self.current])] = dict()

                self.data[str(self.points[self.current])]["vin"] = self.amp
                self.data[str(self.points[self.current])]["amp"] = self.osc.ratio2to1()
                self.data[str(self.points[self.current])]["pha"] = self.osc.phase2to1()

                print(self.data[str(self.points[self.current])])

                self.current += 1
                if self.current == len(self.points):
                    print("Bode finished")
                    print(self.data)
                    self.status = 0
                    return 1
                self.get_to_freq(self.points[self.current], self.amp)
        return 0

    def get_to_freq(self, freq, amp):
        self.osc.set_scale_X(1.0 / freq * 3)
        self.gen.set_sine(freq, amp)