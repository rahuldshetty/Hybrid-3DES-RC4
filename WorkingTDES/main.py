from XTDES import *

tdes=XTDES()
msg = input("Enter message:")

k1=input('Enter key1:')
k2=input('Enter key2:')
k3=input('Enter key3:')

keys=[k1,k2,k3]

print("Original:",msg,"\n")

enc=tdes.encrypt(msg,keys)
print('Encrypted:',enc,"\n")

dec=tdes.decrypt(enc,keys)
print('Decrypted:',dec,"\n")