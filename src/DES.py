import math 

class DES:

    ENCRYPT=1
    DECRYPT=0

    def __init__(self):
        self.keys=[]
        self.text=None

        

    def tobin(self,text):
        #String to binary List
        text=list(map(ord,text))
        binVal=[]
        for i in text:
            f = [ int(x) for x in "{0:b}".format(i) ]
            if len(f)<8:
                f=f[::-1]
                while len(f)!=8:
                    f.append(0)
                f=f[::-1]
            binVal+=f
        return binVal

    def toString(self,binVal):
        #binary List to String
        text=""
        for i in range(0,len(binVal)-7,8):
            g=binVal[i:i+8]
            jnd="".join([str(x) for x in g])
            val=int(jnd,2)
            text+=chr(val)
        return (text.encode("utf-8").decode("utf-8") )

    def genKeys(self,key,rounds=16):
        #1.Removing Parity bits
        temp=[]
        for i,c in enumerate(key):
            if i % 8 !=0 :
                temp.append(c)

        oneBitShiftRounds=[1,2,9,16]

        PBox =[14,17,11,24,1,5,3,28,15,6,21,10,
                23,19,12,4,26,8,16,7,27,20,13,2,
                41,52,31,37,47,55,30,40,51,45,33,48,
                44,49,39,56,34,53,46,42,50,36,29,32]

        leftHalf,rightHalf = temp[0:28],temp[28:]
        # each round repeat
        for rnd in range(rounds):
            #get no. of shifts to perform
            no_shift = 2 if rnd+1 not in oneBitShiftRounds else 1
            
            #left shifting
            leftHalf = leftHalf[no_shift:] + leftHalf[:no_shift]
            rightHalf = rightHalf[no_shift:] + rightHalf[:no_shift]

            result = leftHalf + rightHalf
            
            #compression P-Box
            finalKey=[]
            for i,num in enumerate(PBox):
                finalKey.append( result[num-1]  )
            self.keys.append(finalKey)
        # resultant key added to self.keys list    



    def applyDES(self,key,text,type=ENCRYPT,padding=False):
        if len(key) < 8 :
            raise Exception("Key should be 8 bytes long.")
        else:
            key=self.tobin(key[:8])
            self.genKeys(key)
        
        
