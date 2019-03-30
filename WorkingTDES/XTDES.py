from DES import *
from utility import *
from TDES import *
from RC4 import *

class XTDES:
    @staticmethod
    def apply(text,keys,mode=ENCRYPT):
        rc4 = RC4()
        tdes = TDES()
        keys = [ rc4.genKey(x,8) for x in keys ]
        res=""
        if mode==ENCRYPT:
            res=tdes.encrypt(text,keys)
        else:
            res=tdes.decrypt(text,keys)
        return res
    
    @staticmethod
    def encrypt(text,keys):
        return XTDES.apply(text,keys,ENCRYPT)
    
    @staticmethod
    def decrypt(text,keys):
        return XTDES.apply(text,keys,DECRYPT)     
        
        
        
        
    