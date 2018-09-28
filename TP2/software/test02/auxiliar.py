from math import *


def get_rel_pos(rel, arr):
    if rel == 1:
        return arr[-1]
    return arr[int(rel*len(arr))]


def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)


def convert_seconds(value):
    value = round_sig(value, 1)
    if value < 0.1:
        return "%3d ms" % (value*1000)
    else:
        return "%.2f s" % value


def convert_voltage(value):
    value = round_sig(value, 2)
    return str(value) + " v"


def convert_freq(value):
    value = round_sig(value,1)
    if value < 1000:
        return "%3d Hz" % value
    if value < 1000 * (10**3):
        return "%.1f KHz" % (value/1000.0)
    return "%.1f MHz" % (value/float(10**6))


def convert_res(value):
    if value == -1:
        return "No R"
    value = round_sig(value,2)
    if value < 10**3:
        return str(value) + " ohm"
    elif value < (10**6):
        return str(value/(10**3)) + "K"
    else:
        return str(value/(10**6)) + "M"
