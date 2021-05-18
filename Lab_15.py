import random
from Crypto.Util import number



def generate():
        return number.getPrime(16, randfunc=None)


def Evklid(x,y):
        while y != 0:
            q = int(x / y)
            r = (x - q * y)
            x = y
            y = r
        d = x
        if d==1:
            return True
        else: return False


class Fiat_Shamir():


    def __init__(self):
        self.v=0
        self.x=0
        self.n=0
        self.z=0
        self.c=0
        self.s=0


    #3
    def AtoBstep3dot1(self,n,v,s):
        self.v=v
        self.n=n
        self.s=s
        self.z=random.randrange(2,n-1)
        x=pow(self.z,2,n)
        self.BtoAstep3dot2(x)
    
    
    #3.2
    def BtoAstep3dot2(self,x):
        self.x=x
        self.AtoBstep3dot3(random.randrange(0,2))


    #3.3
    def AtoBstep3dot3(self,c):
        self.c=c
        if c==0:
            y=self.z
        elif c==1:
            y=(self.z*self.s)%n
        self.BtoAstep3dot4(y)


    #3.4
    def BtoAstep3dot4(self,y):
        yy=(y*y)%n
        vc=pow(self.v,self.c) 
        if y!=0 and yy==(self.x*vc)%self.n:
            print(True)
        else:
            print(False)
     
            

p=generate()
q=generate()
n=p*q
s=0
v=0
while True:
    s=random.randrange(1,n)
    if Evklid(s,n)==1:
        v=pow(s,2,n)
        break
obj=Fiat_Shamir()
for i in range(0,10):
    obj.AtoBstep3dot1(n,v,s)
