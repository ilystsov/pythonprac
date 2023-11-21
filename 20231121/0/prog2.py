import pickle 
class SerCls:
    ...

ser = SerCls()
ser.lst = [1,2,3]
ser.dct = {True: 1}
ser.num = 2
ser.st = 'idfuhn'
s = pickle.dumps(ser)
del ser 
ser1 = pickle.loads(s)
print(ser1, ser1.lst, ser1.num)