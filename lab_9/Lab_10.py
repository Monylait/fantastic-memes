import random
import SHA
import Keys


def convert_base(num, to_base, from_base):
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n,m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


def Pim(ai,si,n,g):
    pim=1
    for i in range (0,g):
        aisi=pow(int(ai[i]),int(si[i]),int(n))
        pim=pim*aisi
    return pim


def LEAD_1():
    with open("Message.txt","r") as txt:
        M=txt.read()
    with open("Open_Key.txt","r") as txt:
        x=txt.read().split("\n")
        P=int(x[0])
        d=int(x[1])
        n=int(x[2])
        p=int(x[3])
        q=int(x[4])
        e=int(x[5])
        a=int(x[6])
    H=SHA.sha512(M)
    Lambda=pow(int(convert_base(H+str(P),10,16)),d,n)
    U=pow(int(P),Lambda,p)
    with open("1_res.txt","w") as txt:
        txt.write(str(U)+"\n"+str(Lambda))
    return Lead_to_U_2(q,p,a)


    #with open("Lead.txt","r") as txt:
    #        x=txt.read().split("\n")
    #        d=int(x[1])
    #        L=int(x[0])   
#2
def Lead_to_U_2(q,p,a):
    t=random.randint(2,q-1)
    R=pow(a,t,p)
    return Lead_3(R,t)


#3
def Lead_3(R,t):
    with open("Message.txt","r") as txt:
        M=txt.read()
    with open("1_res.txt","r") as txt:
        x=txt.read().split("\n")
    with open("Private.txt","r") as txt:
        k=txt.read().split("\n")[0]
    with open("Open_Key.txt","r") as txt:
        x=txt.read().split("\n")
        P=int(x[0])
        d=int(x[1])
        n=int(x[2])
        p=int(x[3])
        q=int(x[4])
        e=int(x[5])
        a=int(x[6])
    T=random.randint(2,q-1)
    Rshtix=pow(a,T,p)
    R=(Rshtix*R)%p
    E=SHA.sha512(M+str(R)+str(x[0]))
    return U_4(E,x[1],k,q,t,T)


#4
def U_4(E,Lambda,k,q,t,T):
    Si=(t+int(k)*int(Lambda)*int(convert_base(E, 10, 16)))%q
    return  LEAD_5(Si,Lambda,E,T)


#5
def LEAD_5(Si,Lambda,E,T):
    with open("Private.txt","r") as txt:
        z=txt.read().split("\n")[1]
    with open("Open_Key.txt","r") as txt:
        x=txt.read().split("\n")
        P=int(x[0])
        d=int(x[1])
        n=int(x[2])
        p=int(x[3])
        q=int(x[4])
        e=int(x[5])
        a=int(x[6])
    stepen=(-1)*int(Lambda)*int(convert_base(E, 10, 16))
    Ri=pow(P,stepen,p)
    Ssht=(int(T)+int(z)*int(convert_base(E, 10, 16)))%q
    S=(Ssht+Si)%q
    with open("1_res.txt","r") as txt:
        U=txt.read().split("\n")[0]
    with open("Sign.txt","w") as txt:
        txt.write(str(U)+"\n"+str(E)+"\n"+str(S)+"\n")

print("Start gen")
Keys.gen_start_param()
print("End gen")

LEAD_1()


print("Check CP")
with open("Message.txt","r") as txt:
        M=txt.read()
with open("1_res.txt","r") as txt:
        x=txt.read().split("\n")
        U=int(x[0])
        Lambda=int(x[1])
with open("Open_Key.txt","r") as txt:
        x=txt.read().split("\n")
        P=int(x[0])
        d=int(x[1])
        n=int(x[2])
        p=int(x[3])
        q=int(x[4])
        e=int(x[5])
        a=int(x[6])
with open("Sign.txt","r") as txt:
    S=txt.read().split("\n")[2]
H=SHA.sha512(M)
UL=U*Lambda
UL_L=pow(UL,0-Lambda)
a=pow(a,int(S))
R=pow(int(UL_L*a),1,int(p))
E=SHA.sha512(M+str(R)+str(U))

with open("Sign.txt","r") as txt:
    Ec=txt.read().split("\n")[1]
    if E==Ec:
        print(True)
    else:
        print("E      = "+str(E))
        print("E sign = "+str(Ec))


