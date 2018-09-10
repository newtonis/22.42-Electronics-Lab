import visa
import time
import gen
import osc
import bode

m = 10**6

gen1 = gen.Gen()
gen1.connect()
osc1 = osc.Oscilloscope()
osc1.connect()

bode1 = bode.Bode(osc1, gen1)

bode1.start(100, 1*m, 100, 2)
end = 0
while not end:
    end = bode1.update()

gen1.close()
osc1.close()