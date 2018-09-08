import visa
rm = visa.ResourceManager()
print(rm.list_resources())

inst = rm.open_resource('USB0::0x0957::0x1724::MY45002351::INSTR')

inst.write(":MEASURE:SOURCE CHANNEL1")

v = inst.query(":MEASure:VAMPlitude?")



print(v)

inst.close()