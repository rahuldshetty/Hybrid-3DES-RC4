from XTDES import *

tdes=XTDES()
msg = input("Enter message:")
keys=["dsdadsas","afafsdfsdf","assdassss"]

print("Original:",msg,"\n")

enc=tdes.encrypt(msg,keys)
print('Encrypted:',enc,"\n")

dec=tdes.decrypt(enc,keys)
print('Decrypted:',dec,"\n")