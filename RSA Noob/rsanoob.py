import binascii 

N = 0x272a2e453c69586f0350db30e52c44e10b715dda610b79b29b
c = 0x61626374667b6233747465725f75705f793075725f657d
e = 0x1
print ('c = ',(c))
print ('e = ', (e))
print ('N = ', (N))
res = (c ** e) % N
print('(c ^ e) % N = ', (res))
print("FLAG :")
print (binascii.unhexlify(format(res,'x')))