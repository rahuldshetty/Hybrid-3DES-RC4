from DES import *
from utility import *

class TDES:
    
    @staticmethod
    def genModifKeys(keys):
        iv="0"*48
        ivset=[iv]*16
        keys=[DES.rc4Key(k) for k in keys]
        finalKey=[]
        for j in range(3):
            temp=[]
            for i in range(16):
                temp.append( DES.xor(ivset[i] , keys[j][i] ) )
            ivset=temp
            finalKey.append(ivset)
        return finalKey
        


    @staticmethod
    def applyTDES(text,keys,mode=ENCRYPT):
        res=text
        keys=TDES.genModifKeys(keys)
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
    
    
    