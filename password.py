import string
import random

N=4

def shuffle(string):
   blist=list(string)
   random.shuffle(blist)   
   return ' '.join(blist) 


uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))
uppercaseLetter4=chr(random.randint(65,90))


number1=str(int(random.randint(0,9)))
number2=str(int(random.randint(0,9)))

puncSign1=(string.punctuation)
puncSign2=(string.punctuation)

password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + number1 + number2 + puncSign1 + puncSign2

print (password)
