
def str2bin(string,fill=0):
    text=list(map(ord,string))
    binVal=""
    for i in text:
        f = [int(x) for x in "{0:b}".format(i)]
        f="".join([str(x) for x in f]).zfill(fill)
        binVal+=f
    return binVal
        
def bin2str(binString,read=8):
    blocks=[binString[i:i+read] for i in range(0,len(binString),read)]
    text=""
    for block in blocks:
        text+=chr(int(block,2))
    return text
        
