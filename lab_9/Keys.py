import random
import SHA
from Crypto.Util import number

def Evklid(x,y):
        a2 = 1
        a1 = 0
        b2 = 0
        b1 = 1
        while y != 0:
            q = int(x / y)
            r = (x - q * y)
            a = a2 - q * a1
            b = b2 - q * b1
            x = y
            y = r
            a2 = a1
            a1 = a
            b2 = b1
            b1 = b
        d = x
        a = a2
        b = b2
        if d==1:
            return a
        else: return False


def phi(n: int) -> int:
    result = n
    i = 2
    while i**2 < n:
        while n % i == 0:
            n /= i
            result -= result / i
        i += 1
    if n > 1:
        result -= result / n
    return result


def gen_start_param():
    result=list()
    p=3618006199
    q=60427
    a=int()
    e=int()
    print("1")
    #while True:   #это правильно, просто долго считает и я записал вычисленные значения
    #    p=(number.getPrime(32, randfunc=None))
    #    q=(number.getPrime(16, randfunc=None))
    #
    #    if ((p-1)%q)==0:
    #        print(p)
    #        print(q)
    #        if q>=547 and q<=((p-1)/2):
    #            break
    print("2")
    while True:
        a=random.randint(0,100000)
        if Evklid(a,q)==1:
            break
    print(a)
    print("3")
    k=(number.getPrime(64, randfunc=None))
    z=(number.getPrime(64, randfunc=None))
    print(k)
    print(z)
    Pj=pow(a,k,p)
    L=pow(a,z,p)
    #fin=int(phi((p-1)*(q-1))) #а вот тут уже хуйня
    fin=218621642520348
    print("4")
    #while True: #а вот тут уже хуйня
    #    e=random.randint(2,fin-1,)
    #    check=Evklid(e,fin)
    #    if check==1:
    #        break
    e=361800619
    print("5")
    d = pow(int(e),int(-1),int(fin))
    with open("Lead.txt","w") as txt:
        txt.write(str(L)+"\n"+str(d))    
    with open("Open_Key.txt","w") as txt:
        txt.write(str(Pj)+"\n"+str(d)+"\n"+str(p*q)+"\n"+str(p)+"\n"+str(q)+"\n"+str(e)+"\n"+str(a))
    with open("Private.txt","w") as txt:
        txt.write(str(k)+"\n"+str(z))
    
#d = 516879114930275
#n = 5675883232155861034610532046308411920318640800383419639841397798324649865976160650588663060523766623141640147956008326095962026060117847564320631841855689
#p = 2504422769
#q = 56569
#e = 141085775941355
