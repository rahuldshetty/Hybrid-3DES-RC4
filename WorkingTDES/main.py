from DES import *
from utility import *
from TDES import *


tdes=TDES()
msg = "holaamigo"
keys=["dsdadsas","afafsdfsdf","assdassss"]

print("Original:",msg,"\n")


enc=tdes.encrypt(msg,keys)
print('Encrypted:',enc,"\n")

dec=tdes.decrypt(enc,keys)
print('Decrypted:',dec,"\n")