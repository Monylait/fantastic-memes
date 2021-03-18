from operator import xor
from hashlib import sha256
import random
mod = pow(2, 32)
L = [
0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

#для 512 K = [
#0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
#0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
#0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
#0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
#0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
#0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
#0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
#0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
#0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
#0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
#0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
#0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
#0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
#0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
#0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
#0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
#0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
#0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
#0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
#0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
#]

def bitstring(str_text: str):
    res = ''.join(format(ord(i), 'b').zfill(8) for i in str_text)
    return res

def k_to_bit(T:list):
    k = []
    for i in T:
        new = bin(i)[2:]
        while len(new)<32:
            new = '0' + new
        k.append(int(new))
    return k

#def stringbit(str_text: str):
#    res = ''
#    while len(str_text)!=0:
#        bit_str = 0
#        for i in range(0, 8):
#            if str_text[i]=='1':
#                bit_str += pow(2, 7-i)
#        res += ''.join(format(chr(int(bit_str))))
#        str_text = str_text[8:]
#    return res

def bit_i(x, y):
    mult = x&y
    return mult

def ch(x, y, z):
    return xor(bit_i(x, y), bit_i(~x, z))

def maj(x, y, z):
    xyxz = xor(bit_i(x, y), bit_i(x, z))
    return xor(xyxz, bit_i(y, z))

def E(x, cycle, cycle1, cycle2):
    onetwo = xor(x>>cycle, x>>cycle1)
    return xor(onetwo, x>>cycle2)

def sigma(x, cycle, cycle1, cycle2):
    print(x>>cycle, x>>cycle1, x>cycle2)
    one = xor(x>>cycle, x>>cycle1)
    return xor(one, x>cycle2)

def sha256(res):
    H=""
    K = []
    res = bitstring(res)
    K = k_to_bit(L)
    length = len(res)
    if length/512!=0:
        k = (448-length)%512
        res += "1"
        for i in range(k):
            res += "0"
        l = bin(length)[2:]
        while len(l)<63:
            l = "0"+l
        res += l
    N = int(len(res)/512)
    M = []
    for x in range(N):
        m0 = []
        for y in range(16):
            j = res[:32]
            res = res[32:]
            m0.append(j)
        M.append(m0)
    for i in range(1, N+1):
        W = M[i-1]
        part = []
        for t in range(16, 64):
            value = sigma(int(W[t-2]), 17, 19, 10)+int(W[t-7])+sigma(int(W[t-15]), 7, 18, 3)+int(W[t-16])
            print('s0= ', sigma(int(W[t-2]), 17, 19, 10), '\n', 's1= ', sigma(int(W[t-15]), 7, 18, 3))
            value = value%mod
            W.append(bin(value)[2:])
        print(W)
        H = [
                0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
        H = k_to_bit(H)
        a, b, c, d, e, f, g, h = (
                H[0],  H[1], H[2], H[3], 
                H[4], H[5], H[6], H[7])
        for t in range(64):
            T1 = h+E(e, 6, 11, 25)+ch(e, f, g)+int(K[t])+int(W[t])
            T1 = T1%mod
            T2 = E(a, 2, 13, 22)+maj(a, b, c)
            T2 = T2%mod
            h=g
            g=f
            f=e
            e=d+T1%mod
            d=c
            c=b
            b=a
            a=T1+T2
        H[0] = a+H[0]%mod
        H[1] = b+H[1]%mod
        H[2] = c+H[2]%mod
        H[3] = d+H[3]%mod
        H[4] = e+H[4]%mod
        H[5] = f+H[5]%mod
        H[6] = g+H[6]%mod
        H[7] = h+H[7]%mod
    G = str(H[0])+str(H[1])+str(H[2])+str(H[3])+str(H[4])+str(H[5])+str(H[6])+str(H[7])
    print(str(format(int(G),'x')))

#............................menu..............................#
def choose_text():
    flag1 = True
    while flag1:
        choose2 = int(input("Input text from - file\consol (1\\2)\n"))
        if choose2 == 1:
            fileway = choose_file()
            with open(fileway, 'r',  encoding="utf-8") as file:
                res = ''
                for line in file:
                    res += line
            return res
        elif choose2 == 2:
            res = input("Enter text \n")
            return res
        else:
            print("Error")

def choose_file():
    flag = True
    while flag:
        fileway = input("Enter way for file: \n")
        try:
            if fileway.endswith(f".txt"):
                flag = False
                return fileway
            else:
                print("Error file type")
        except Exception:
            pass


#choose = int(input("What do we do? - 256/512 (1\\2)\n"))
#res = choose_text()
##print(res, '\n')
#res1 = res
#if choose==1:
#    #print(sha256(res.encode('utf-8')).hexdigest())
#    sha256(res)
#elif choose==2:
#    sha512(res)
#

#64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c