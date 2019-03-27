import math

initPBox = [
			58,50,42,34,26,18,10,2,
			60,52,44,36,28,20,12,4,
			62,54,46,38,30,22,14,6,
			64,56,48,40,32,24,16,8,
			57,49,41,33,25,17,9,1,
			59,51,43,35,27,19,11,3,
			61,53,45,37,29,21,13,5,
			63,55,47,39,31,23,15,7
			]

inversePBox = [
			40,8,48,16,56,24,64,32,
			39,7,47,15,55,23,63,31,
			38,6,46,14,54,22,62,30,
			37,5,45,13,53,21,61,29,
			36,4,44,12,52,20,60,28,
			35,3,43,11,51,19,59,27,
			34,2,42,10,50,18,58,26,
			33,1,41,9,49,17,57,25	
]

exansionPBox=[
	32,1,2,3,4,5,
	4,5,6,7,8,9,
	8,9,10,11,12,13,
	12,13,14,15,16,17,
	16,17,18,19,20,21,
	20,21,22,23,24,25,
	24,25,26,27,28,29,
	28,29,30,31,32,1
]

straightPBox =[
	16,7,20,21,29,12,28,17,
	1,15,23,26,5,18,31,10,
	2,8,24,14,32,27,3,9,
	19,13,30,6,22,11,4,25
]

SBOX = [
	[ "0010","1100","0100","0001","0111","1010","1011","0110","1000","0101","0011","1111","1101","0000","1110","1001"],
	[ "1110","1011","0010","1100","0100","0111","1101","0001","0101","0000","1111","1010","0011","1001","1000","0110"],
	[ "0100","0010","0001","1011","1010","1101","0111","1000","1111","1001","1100","0101","0110","0011","0000","1110"],
	[ "1011","1000","1100","0111","0001","1110","0010","1101","0110","1111","0000","1001","1010","0100","0101","0011"]
]

class DES:

    ENCRYPT = 1
    DECRYPT = 0

    def __init__(self):
        self.keys = []
        self.text = None

    def tobin(self, text):
        # String to binary List
        text = list(map(ord, text))
        binVal = []
        for i in text:
            f = [int(x) for x in "{0:b}".format(i)]
            if len(f) < 8:
                f = f[::-1]
                while len(f) != 8:
                    f.append(0)
                f = f[::-1]
            binVal += f
        return binVal

    def binToInt(self,bin):
    	bin=bin[::-1]
    	i=1
    	num=0
    	ptr=0
    	while ptr<len(bin):
    		num+= i*int(bin[ptr])
    		i=i*2
    		ptr+=1
    	return num





    def toString(self, binVal):
        # binary List to String
        text = ""
        for i in range(0, len(binVal), 8):
            g = binVal[i:i+8]
            jnd = "".join([str(x) for x in g])
            val = int(jnd, 2)
            text += chr(val)
        return (text.encode("utf-8").decode("utf-8"))

    def genKeys(self, key, rounds=16):
        # 1.Removing Parity bits
        temp = []
        for i, c in enumerate(key):
            if i % 8 != 0:
                temp.append(c)

        oneBitShiftRounds = [1, 2, 9, 16]

        PBox = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
                23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

        leftHalf, rightHalf = temp[0:28], temp[28:]
        # each round repeat
        for rnd in range(rounds):
            # get no. of shifts to perform
            no_shift = 2 if rnd+1 not in oneBitShiftRounds else 1

            # left shifting
            leftHalf = leftHalf[no_shift:] + leftHalf[:no_shift]
            rightHalf = rightHalf[no_shift:] + rightHalf[:no_shift]

            result = leftHalf + rightHalf

            # compression P-Box
            finalKey = []
            for i, num in enumerate(PBox):
                finalKey.append(result[num-1])
            self.keys.append(finalKey)
        # resultant key added to self.keys list


    def permute(self,lists,box):
    	if len(lists)!=len(box):
    		raise Exception("Invalid permutation objects")
    	newList=[0]*len(lists)
    	for i,pos in enumerate(box):
    		newList[i]=lists[pos-1]
    	return newList




    def applyDES(self, key, text, type=1):
        if len(key) < 8:
            raise Exception("Key should be 8 bytes long.")
        else:
            key = self.tobin(key[:8])
            self.genKeys(key)

        if type==self.DECRYPT:
        	self.keys=self.keys[::-1]

        binText = self.tobin(text)
        blocks=[binText[i:i+64] for i in range(0,len(binText),64)]
        result=[]
        for i in range(len(blocks)):
        	blocks[i]+=[0]*(64-len(blocks[i]))

        for i,block in enumerate(blocks):
        	#init permutation
        	initList = self.permute(block,initPBox)
        	data = initList
        	leftData,rightData=data[:32],data[32:]
        	
        	
        	for j in range(16):
        		temp=rightData
        		# Feistal Round function
        		
        		#exampnsionPBox
        		newTemp=[]
        		for pos in (exansionPBox):
        			newTemp.append(temp[pos-1])

        		#xor with key
        		for k in range(len(newTemp)):
        			newTemp[k]^=self.keys[j][k]

        		#sbox grouping
        		sblockData=[]
        		for k in range(0,len(newTemp),6):
        			sblock=(newTemp[k:k+6])
        			row=str(sblock[0])+str(sblock[5])
        			col="".join([str(x) for x in sblock[2:5] ])
        			row=self.binToInt(row)
        			col=self.binToInt(col)
        			cell=SBOX[row][col]
        			sblockData+=list(cell)

        		tempS=[]
        		#straight PBOX
        		for k,pos in enumerate(straightPBox):
        			tempS.append(int(sblockData[pos-1]))

        		#xor with left half
        		for i in range(len(tempS)):
        			rightData[i]=(tempS[i]^leftData[i])

        		if j!=15:
        			leftData,rightData=rightData,leftData

        	resultData=leftData+rightData

        	#inverse permutation
        	finalList = self.permute(resultData,inversePBox)
        	result.append(self.toString(finalList))

        self.result=result

        return "".join(result)

      






if __name__ == "__main__":
    d = DES()
    f = d.applyDES(key="helloworld", text="WorldPeace")


def is_pow_of(n):
    i = n
    while(i/2 > 2):
        i = i / 2
    return i == 2


is_pow_of(2)
