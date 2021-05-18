import RSA
import Lab_7
import random
import SHA

def gener_k(B):
    k=random.randbytes(256)
    with open("Seanse_Key.txt","w") as txt:
        txt.write(str(k))

    with open("private.txt", "r") as pub_k:
        d = float(pub_k.readline())
    with open("publick.txt", "r") as pub_k:
        e = int(pub_k.readline())
        n = int(pub_k.readline())
    cp=Lab_7(SHA.sha512(B+" "+str(k)),d, e, n)
    Ekb=RSA.Encription(str(k)+" "+str(cp))
    check_B(Ekb)


def check_B(Ekb):
    Ekb=RSA.Decription(Ekb)

Id_A="0001"
Id_B="0002"


