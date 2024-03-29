import random


def fi(n):
    f = n;
    if n%2 == 0:
        while n%2 == 0:
            n = n // 2;
        f = f // 2;
    i = 3
    while i*i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i;
            f = f // i;
            f = f * (i-1);
        i = i + 2;
    if n > 1:
        f = f // n;
        f = f * (n-1);
    return f;


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




def Evklid(x,y):
    a2=1
    a1=0
    b2=0
    b1=1
    while(y!=0):
        q=int(x/y)
        r=(x-q*y)
        a=a2-q*a1
        b=b2-q*b1
        x=y
        y=r
        a2=a1
        a1=a
        b2=b1
        b1=b
    return x


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


def generate_keys():
    easy_numbers=list()
    with open("result.txt","r") as pq:
        for i in pq:
            easy_numbers.append(int(i))
    p=0
    q=0
    while p==q:
        p=random.randrange(0,len(easy_numbers),1)
        q=random.randrange(0,len(easy_numbers),1)
    p=easy_numbers[p]
    q=easy_numbers[q]
    n=p*q
    fin=phi((p-1)*(q-1))
    while True:
        e=random.randrange(2,fin-1,1)
        check=Evklid(e,fin)
        if check==1:

            print("e, fin "+str(e)+" "+str(fin))
            break
    d = pow(int(e),int(-1),int(fin))
    test=convert_base(int(d),2,10)
    test1=len(test)
    test=convert_base(e,2,10)
    test2=len(test)
    test=convert_base(n,2,10)
    test3=len(test)
    print("\nd - "+str(test1)+"\te - "+str(test2)+"\tn - "+str(test3))
    with open("publick.txt","w") as pub:
        stre=""+str(e)+"\n"+str(n)
        test=convert_base(n,2,16)
        test=len(test)
        pub.write(stre)
    with open("private.txt","w") as pri:
        stra=""+str(d)
        pri.write(stra)

