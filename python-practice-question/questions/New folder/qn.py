def extrabraces(eqn):
    lst=[]
    i=0
    while(i<len(eqn)):
        if eqn[i] in ['(','+','-','*','/']:
            lst.append(eqn[i])
        elif eqn[i]==')' :
            if lst[-1]=='(':
                return 1
            else:
                while( not(not(lst)) and lst[-1]!='(' ):
                    lst.pop()
                lst.pop()
        i+=1
    return 0     
     
eqn="((a+b))"     
extrabraces(eqn)             
