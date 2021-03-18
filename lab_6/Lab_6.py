import Stribog as STR
import SHA 
import os
from random import randint
from bitstring import BitArray

def Key():
    notsecret=os.urandom(randint(5,1000000))
    #notsecret = BitArray(hex=notsecret)
    #notsecret=notsecret.bin[2:]
    with open("NotKey.jspy","w",encoding="UTF-8") as notkeyfile:
        notkeyfile.write(str(notsecret))
    return notsecret


def SiSo(K0,ipad,ipod):
    return [K0^ipad,K0^ipod]


def mes_b(mes,b):
    M = []
    for x in range(N):
        m0 = []
        for y in range(16):
            j = res[:64]
            res = res[64:]
            m0.append(j)
        M.append(m0)
        

flag = True
mes=""
H=""
while flag:


    b=64
    ipad=b"0x36"*b
    opad=b"0x5c"*b
    K=Key()
    K0=""
    if len(K)==b:
        K0=K
    elif len(K)>b:
        K0=STR.Stribog(K0, 256)
        i=len(K0)
        while len(K0)!=b:
            K0=K0+"0"
    elif len(K)<b:
        K0=K
        while len(K)!=b:
            K0=K0+b"0x00"

    SISO=SiSo(K0,ipad,ipod)
    Si=SISO[0]
    So=SISO[1]


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

        M=mes_b(mes,b)

        while flag_2:
            hesh = str(input("Step 2\n>> SHA - 1\n>> Stribog - 2\n>> Exit    - 3\n>>> "))
            if type == "1":
                flag_3=True
                while flag_3:
                    type = str(input("Step 2.1\n>> SHA 256 - 1\n>> SHA 512 - 2\n>> Exit    - 3\n>>> "))
                    if type=="1":
                        pass
                    elif type=="2":
                        pass
                    elif type=="3":
                        flag_3 = False
                    else:
                        print("Error - incorrect choose\n")
            elif type=="2":
                flag_3=True
                while flag_3:
                    type = str(input("Step 2.1\n>>Stribog 256 - 1\n>>Stribog 512 - 2\n>> Exit    - 3\n>>> "))
                    if type=="1":
                        bit = int(256)
                        H=("Result >> " + STR.Stribog(mes, bit) + "\n")
                    elif type=="2":
                        bit = int(512)
                        H=("ВResult >> " + STR.Stribog(mes, bit) + "\n")
                    elif type=="3":
                        flag_3 = False
                    else:
                        print("Error - incorrect choose\n")
            elif type=="3":
                flag_2=False
            else:
                print("Error - incorrect choose\n")
    elif point == "3":
        flag = False
        break
    else:
        print("Error - incorrect choose\n")