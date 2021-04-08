import random
import SHA
import Stribog


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

def gen_keys():
    easy_numbers = list()
    flag=True
    while flag:
        leng=input("Choose leng \n256 - 1\n512 - 2\n> ")
        if leng=="1":
            leng=256
            flag=False
        elif leng=="2":
            leng=512
            flag = False
        else:
            print("Bad input\n")
    with open("result.txt", "r") as pq:
        for i in pq:
            easy_numbers.append(int(i))
    p = 0
    q = 0
    while p == q:
        p = random.randrange(0, len(easy_numbers), 1)
        q = random.randrange(0, len(easy_numbers), 1)
    p = easy_numbers[p]
    q = easy_numbers[q]
    n = p * q
    Ai=list()
    Bi=list()
    print(n)
    for i in range (0,leng,1):
        ai=random.randint(0,10000)
        #q=Evklid(ai,n)
        #if q==False:
          #  print("False")
         #   continue
        #print("ai = "+str(ai)+"\nq = "+str(q))
        q=pow(ai,-1,n)
        bi=int((q*q)%n)
        Ai.append(ai)
        Bi.append(bi)
    with open("publick.txt","w") as pub:
        strin=""
        for elem in Bi:
            strin=strin+str(elem)+" "
        strin = strin + "\n"+str(n)
        pub.write(strin)
    with open("privat.txt","w") as priv:
        strin = ""
        for elem in Ai:
            strin = strin + str(elem) + " "
        strin = strin + "\n"+str(p)+"\n"+str(q)
        priv.write(strin)
    return leng



