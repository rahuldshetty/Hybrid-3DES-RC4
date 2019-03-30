class RC4:
    @staticmethod
    def KSA(key):
        key_len = len(key)
        S = []
        for i in range(256):
            S.append(i)
        j = 0
        for i in range(256):
            j = (j+ S[i] +key[i % key_len]) % 256
            S[i], S[j] = S[j] , S[i]
        return(S)
    
    @staticmethod
    def con_to_ascii(key_string):
        key = [ord(x) for x in key_string]
        return key
    
    @staticmethod
    def PRGA(S):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i],S[j] = S[j],S[i]
            k = S[(S[i] + S[j]) % 256]
            yield k
            
    @staticmethod
    def genKey(text,length=10):
        key = RC4.con_to_ascii(text)
        S = RC4.KSA(key)
        key_stream = RC4.PRGA(S)
        cipher_key=[]
        for i in range(length):
            cipher_key.append(next(key_stream))
        return "".join([chr(x) for x in cipher_key])
