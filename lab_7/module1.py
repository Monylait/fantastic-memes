import random
import time
import timeit
from Crypto.Util import number

def exponentiating(a,n):
    x = 1
    b = to_bin(n)
    for i in range(len(b)):
        x = x * (a**(int(b[i])*(2**(i))))
    return x


def to_bin(n):
    n = bin(n)
    n = str(n)
    b = []
    for i in range(len(n)):
        b.append(n[i])
    b.reverse()
    b.pop()
    b.pop()
    return b


def Test_M_R(n):
    w=n-1
    s=0
    q=1
    while w!=1:
        if w%2==0:
            w=w/2
            s=s+1
        else:
            q=int(w)
            break
    a=random.randint(1,n-1)
    if exponentiating(a,q)==1:
        return True
    for i in range(0,s,1):
        check=exponentiating(a,exponentiating(2,i)*q) 
        if check==1:
            return True
    return False


def rmspp(number, attempts=28):
    """
    rmspp(n, attempts=28) -> True if n appears to be primary, else False
    rmspp: Rabin-Miller Strong Pseudoprime Test
    http://mathworld.wolfram.com/Rabin-MillerStrongPseudoprimeTest.html
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    # Given an odd integer n, let n = 2**r*s+1, with s odd... 
    s = number - 1
    r = 0
    while s % 2 == 0:
        r += 1
        s /= 2
    while attempts:
        # ... choose a random integer a with 1 ≤ a ≤ n-1
        a = random.randint(1, number-1)
        # Unless a**s % n ≠ 1 ...
        if mod_exp(a, s, number) != 1:
            # ... and a**((2**j)*s) % n ≠ -1 for some 0 ≤ j ≤ r-1 
            for j in range(0, r):
                if mod_exp(a, (2**j)*s, number) == number-1:
                    break
            else:
                return False
        attempts -= 1
        continue
    # A prime will pass the test for all a.
    return True


def mod_exp(base, exponent, modulus):
    """
    mod_exp(b, e, m) -> value of b**e % m
    Calculate modular exponentation using right-to-left binary method.
    http://en.wikipedia.org/wiki/Modular_exponentiation#Right-to-left_binary_method
    """
    result = 1
    exponent=int(exponent)
    while exponent > 0:
        if (exponent & 1) == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result


def convert_base(num, to_base=10, from_base=2):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def mr(n,k):
    t=n-1
    s=0
    while t%2==0:
        t=int(t/2)
        s+=1
    for i in range (0,k):
        check=0
        a=random.randint(2,n-2)
        x=pow(a,t,n)
        print("Алгоритм считал:", str(z), "секунд\n")
        return 0
        if x==1 or x==n-1:
            pass
        else:
            while check < s-1:
                check+=1
                x=pow(x,2,n)
                if x==1:
                    return False
                elif x==n-1:
                    break
            if check==s-1:
                return False
    return True


def Gen_Easy_Num(k,t):
    flag=True
    while flag:
        j=k-1
        mass_p=list()
        mass_p.append(1)
        while j>1:
            x=random.randint(0,1)
            mass_p.append(x)
            j-=1
        mass_p.append(1)
        string=''
        for item in mass_p:
            string+=str(item)
        p=convert_base(string, 10, 2)
        x=mr(int(p),int(t))
        if x:
            print("Lol")
            with open("result_Easy_numbers.txt", "a") as REN:
                REN.write(str(p)+"\n")
            flag=False
for i in range(0,10):
    z=(number.getPrime(512, randfunc=None))
    with open("result.txt", "a") as REN:
                REN.write(str(z)+"\n")

