from ast import Return


word ="incredible"


def stutter(str):
    word2=""
    word3=""
    for i in range(0,2):
        word2+=str[i]#we add the first two letters of str to word2 because word2 must countains the first two letters of str
   #we can also replace word2 by str[0:2]
   
    word3 = word2+"..."+word2+"..."+str+"?"#it stutters the word 
    print(word3)#it prints the word3 resulted in the screen

stutter("enthusiastic")