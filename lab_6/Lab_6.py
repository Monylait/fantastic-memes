import Stribog as STR
import SHA 
import os
from random import randint
from bitstring import BitArray

def Key():
    notsecret=os.urandom(randint(5,6415))
    #notsecret = BitArray(hex=notsecret)
    #notsecret=notsecret.bin[2:]
    with open("NotKey.jspy","w",encoding="UTF-8") as notkeyfile:
        notkeyfile.write(str(notsecret))
    return notsecret


def SiSo(K0,ipad,ipod):
    siso=list()
    r=[x^y for x,y in zip(K0,ipad)]
    siso.append(r)
    r=[x^y for x,y in zip(K0,ipod)]
    siso.append(r)
    return  siso


def mes_b(mes,b):
    M = []
    for x in range(b):
        m0 = []
        for y in range(16):
            j = res[:64]
            res = res[64:]
            m0.append(j)
        M.append(m0)
  

def mes_ord(mes):
    m=[0]*len(mes)
    for i in range(0, len(mes)):
        m[i] = ord(mes[i])
    return m
        
def HMAC(SISO,M, type):
    Si=SISO[0]  # K0^ipad
    So=SISO[1]  # K0^opad
    Si=''.join(reversed([('%0.2X' % a) for a in Si]))
    So=''.join(reversed([('%0.2X' % a) for a in So]))
    x=Si+M
    if type[0]==1:
        y=STR.Stribog(x,type[1]) 
        y=''.join(reversed([('%0.2X' % a) for a in y]))
        z=STR.Stribog(So+y,type[1])
        z=''.join(reversed([('%0.2X' % a) for a in z]))
    elif type[0]==0:
        if type[1]==256:
            y=SHA.sha256(M)
            z=SHA.sha256(So+M)
        elif type[1]==512:
            y=SHA.sha512(M)
            z=SHA.sha512(So+M)
    return z



flag = True
mes=""
H=""
while flag:


    b=64
    ipad=(0x36,0x36,0x36,0x36,0x36,0x36,0x36,0x36)
    opad=(0x5c,0x5c,0x5c,0x5c,0x5c,0x5c,0x5c,0x5c)
    K=Key()
    K0=""
    if len(K)==b:
        K0=K
    elif len(K)>b:
        K0=STR.Stribog(K0, 256)
        i=len(K0)
        while len(K0)!=b:
            K0.append(0)
    elif len(K)<b:
        K0=K
        while len(K)!=b:
            K0=K0+b"0x00"
    SISO=SiSo(K0,ipad,opad)



    point = str(input("Step 1\n>> Give message - 1\n>> Go to step 2 - 2\n>> Exit - 4\n>>> "))
    if point == "1":
        flag_4=True
        while flag_4:
            choose=str(input(">> From file - 1\n>> From console - 2\n"))
            if choose=="1":
                while True:
                    way = input("Enter file path\n(end on .txt)\n")
                    if os.path.isfile(way) and way[-4:] == ".txt":
                        with open(way,'r') as file:
                            mes = file.read()
                        flag_4=False
                        break
                    else:
                        print("Error - incorrect path\n")
            elif choose=="2":
                mes=str(input(">> Enter text: "))
                flag_4=False
                break

    elif point=="2" and mes!="":
        
        flag_2=True
        #M=mes_b(mes,b)
        M=mes_ord(mes)

        while flag_2:
            hesh = str(input("Step 2\n>> SHA - 1\n>> Stribog - 2\n>> Exit    - 3\n>>> "))
            if hesh == "1":
                flag_3=True
                while flag_3:
                    type = str(input("Step 2.1\n>> SHA 256 - 1\n>> SHA 512 - 2\n>> Exit    - 3\n>>> "))
                    if type=="1":
                        H=("Result >> " + HMAC(SISO,mes,(0,256)) + "\n")
                        print(H)
                    elif type=="2":
                        H=("Result >> " + HMAC(SISO,mes,(0,512)) + "\n")
                        print(H)
                    elif type=="3":
                        flag_3 = False
                    else:
                        print("Error - incorrect choose\n")
            elif hesh=="2":
                flag_3=True
                while flag_3:
                    type = str(input("Step 2.1\n>>Stribog 256 - 1\n>>Stribog 512 - 2\n>> Exit    - 3\n>>> "))
                    if type=="1":
                        bit = int(256)
                        H=("Result >> " + HMAC(SISO,mes,(1,bit)) + "\n")
                        print(H)
                    elif type=="2":
                        bit = int(512)
                        H=("ВResult >> " + HMAC(SISO,mes,(1,bit)) + "\n")
                        print(H)
                    elif type=="3":
                        flag_3 = False
                    else:
                        print("Error - incorrect choose\n")
            elif hesh=="3":
                flag_2=False
            else:
                print("Error - incorrect choose\n")
    elif point == "3":
        flag = False
        break
    else:
        print("Error - incorrect choose\n")