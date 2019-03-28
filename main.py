from src.TDES import *
from src.utility import *

d = TDES()
f = d.encrypt(keys=["hellworl","holaAmigo"], text="0123456789ABCDEF")

printUni(["Encrypted:",f])

f = d.decrypt(keys=["hellworl","holaAmigo"], text=f)

printUni(["Decrypted:",f])



