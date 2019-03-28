from src.DES import *
from src.utility import * 

class TDES:

    ENCRYPT = 1
    DECRYPT = 0  

    def __init__(self):
        pass
    
    def applyTDES(self,text,keys,type=1):
        no_keys = len(keys)
        if type==0:keys=keys[::-1]
        des = DES()
        temp=text
        intermediate=[]
        for key in keys:
            temp = des.applyDES(text=temp,key=key,type=type)
            intermediate.append(temp)
            type^=1
        self.result=temp
        self.interm=intermediate
        return temp

    def encrypt(self,text,keys):
        return self.applyTDES(text,keys,1)
    def decrypt(self,text,keys):
        return self.applyTDES(text,keys,0)
        

