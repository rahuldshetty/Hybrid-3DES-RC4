def printUni(a,sep=" "):
        # this function is used to print the unicode string in the conosles 
        print(sep.join([str(x.encode("ascii",'ignore')) for x in a]))