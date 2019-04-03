from DES import *
from utility import *

class TDES:
    
    @staticmethod
    def applyTDES(text,keys,mode=ENCRYPT):
        res=text
        if mode==DECRYPT:keys=keys[::-1]
        for key in keys:
            if mode==ENCRYPT:
                res = DES.encrypt(res,key)
            else:
                res=DES.decrypt(res,key)
            mode^=1
        return res
                

    @staticmethod
    def encrypt(text,keys):
        return TDES.applyTDES(text,keys,ENCRYPT)
    
    @staticmethod
    def decrypt(text,keys):
        return TDES.applyTDES(text,keys,DECRYPT)
    
    
    