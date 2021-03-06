from utility import *
from RC4 import *

ENCRYPT=1
DECRYPT=0

ROUNDS=16

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25    
]



KeyParityDrop=[
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4    
]

KeyPermute =[
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32    
]

ExpansionBox=[
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

PBox=[
    16,  7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11, 4,  25
]

Sboxes = [
    
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
        ],

        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],

        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],

        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],  

        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ], 

        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ], 

        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],
        
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]
]

KeyShifts=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

class DES:
    
    '''
    # Original DES Key algorithm
    @staticmethod
    def genKeys(key):
        key=str2bin(key[:8],8)
        #drop parity
        reducedKey="".join([key[x-1] for x in KeyParityDrop])
        keys=[]
        for shift in KeyShifts:
            left,right=reducedKey[:28],reducedKey[28:]
            
            #shifting
            left = left[shift:] + left[:shift]
            right = right[shift:] + right[:shift]
            
            reducedKey=left+right
            keyTemp = "".join([reducedKey[ x-1 ] for x in KeyPermute])
            keys.append(keyTemp)
        return keys
    '''     
    @staticmethod
    def rc4Key(key):
        finalkeys=[]
        for rnd in range(16):
            key=RC4.genKey(key,6)
            key=str2bin(key,8)
            finalkeys.append(key)        
        return finalkeys
            
    @staticmethod
    def getTextBlocks(text,split=64):
        #split-Size of each block in bytes
        text=str2bin(text,8)
        results=[text[i:i+split] for i in range(0,len(text),split)]
        res=[]
        for result in results:
            if len(result)<split:
                result = result +  "0"*(split-len(result))
            res.append(result)
        return res
    
    @staticmethod
    def initalPermute(text):
        return "".join([str(text[x-1]) for x in IP ])

    @staticmethod
    def finalPermute(text):
        return "".join([str(text[x-1]) for x in FP ])
    
    @staticmethod
    def swap(text):
        return text[32:]+text[:32]
    
    @staticmethod
    def expansion(text):
        return "".join([ str( text[x-1] ) for x in ExpansionBox ])
    
    @staticmethod
    def xor(left,right):
        return "".join([ str( int(left[i]) ^ int(right[i])  ) for i in range(len(left)) ])
    
    @staticmethod
    def sbox(text):
        #divide 48 bits to 8 bit block each
        sblock = [ text[i:i+6] for i in range(0,len(text),6) ]
        res=""
        for i in range(len(sblock)):
            box=Sboxes[i]
            block=sblock[i]
            row=int(block[0]+block[5],2)
            col=int(block[1:5],2)
            cell=box[row][col]
            res+=bin(cell)[2:].zfill(4)
        return res
            
        

    @staticmethod
    def pbox(text):
        return "".join([ str(text[x-1]) for x in PBox  ])
    
    @staticmethod
    def fFunction(right,key):
        expand=DES.expansion(right)
        xor = DES.xor(expand,key)
        sbox= DES.sbox(xor)
        pbox = DES.pbox(sbox)
        return pbox       
        
    
    @staticmethod
    def fiestalFunction(text,key):
        left,right=text[:32],text[32:]
        left= DES.xor( DES.fFunction(right,key) , left  ) 
        return left+right      
                
    
    @staticmethod
    def des(block,keys):
        init=DES.initalPermute(block)
        for round in range(ROUNDS):
            init=DES.fiestalFunction(init,keys[round])
            init=DES.swap(init)
        init=DES.swap(init)                                            
        final=DES.finalPermute(init)
        return final

    @staticmethod
    def applyDES(text,keys,mode=ENCRYPT):
        if mode == DECRYPT:
            keys=keys[::-1]
        #text processing
        blocks=DES.getTextBlocks(text)
        res=""
        for block in blocks:
            res+=(DES.des(block,keys))
        return res
                            
        
    @staticmethod
    def encrypt(text,key):
        return bin2str(DES.applyDES(text,key,True))

    @staticmethod
    def decrypt(text,key):
        return bin2str(DES.applyDES(text,key,False))

    
        
        
          