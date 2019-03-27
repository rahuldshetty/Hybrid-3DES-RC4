from DES import *

d = DES()
f = d.applyDES(key="hellworl", text="0123456789ABCDEF")

print('Encrypt',f)

f = d.applyDES(key="hellworl", text=f)

print('Decrypt',f)
