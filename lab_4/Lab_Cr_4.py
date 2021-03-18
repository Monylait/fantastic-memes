import bitarray
from bitstring import BitArray


def L(mes):
    A="8e20faa72ba0b470 47107ddd9b505a38 ad08b0e0c3282d1c d8045870ef14980e 6c022c38f90a4c07 3601161cf205268d 1b8e0b0e798c13c8 83478b07b2468764 a011d380818e8f40 5086e740ce47c920 2843fd2067adea10 14aff010bdd87508 0ad97808d06cb404 05e23c0468365a02 8c711e02341b2d01 46b60f011a83988e 90dab52a387ae76f 486dd4151c3dfdb9 24b86a840e90f0d2 125c354207487869 092e94218d243cba 8a174a9ec8121e5d 4585254f64090fa0 accc9ca9328a8950 9d4df05d5f661451 c0a878a0a1330aa6 60543c50de970553 302a1e286fc58ca7 18150f14b9ec46dd 0c84890ad27623e0 0642ca05693b9f70 0321658cba93c138 86275df09ce8aaa8 439da0784e745554 afc0503c273aa42a d960281e9d1d5215 e230140fc0802984 71180a8960409a42 b60c05ca30204d21 5b068c651810a89e 456c34887a3805b9 ac361a443d1c8cd2 561b0d22900e4669 2b838811480723ba 9bcf4486248d9f5d c3e9224312c8c1a0 effa11af0964ee50 f97d86d98a327728 e4fa2054a80b329c 727d102a548b194e 39b008152acb8227 9258048415eb419d 492c024284fbaec0 aa16012142f35760 550b8e9e21f7a530 a48b474f9ef5dc18 70a6a56e2440598e 3853dc371220a247 1ca76e95091051ad 0edd37c48a08a6d8 07e095624504536c 8d70c431ac02a736 c83862965601dd1b 641c314b2b8ee083"
    A=A.split()
    block=""
    mes_8=list()
    j=0
    result=list()
    for i in mes:
        if j!=8:
            block=block+str(i)
            j+=1
        else:
            j=0
            mes_8.append(block)
    for i in mes_8:
        res=0
        c = BitArray(hex=i)
        c.bin[2:]
        A_index=0
        for z in c:
            if int(z)==0:
                result.append("00000000")
            elif int(z)==1:
                result.append(A[A_index])
            A_index+=1
        for j in range(0,64):
            res=res^result[j]





def P(mes):
    tabl= (0, 8, 16, 24, 32, 40, 48, 56, 1, 9, 17, 25, 33, 41, 49, 57, 2, 10, 18, 26, 34, 42, 50, 58, 3, 11, 19, 27, 35, 43, 51, 59, 4, 12, 20, 28, 36, 44, 52, 60, 5, 13, 21, 29, 37, 45, 53, 61, 6, 14, 22, 30, 38, 46, 54, 62, 7, 15, 23, 31, 39, 47, 55, 63)
    for i in range(0,64):
        [i] = a[tabl[i]]
    return mes


def S(mes):
    pi= (252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166, 116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182)
    for i in range(0,64):
       mes[i] = pi[mes[i]];
    return mes


def start_settings()->list:
    i=True
    list_variables=list()
    while i:
        try:
            task_1=int(input("Enter 512\\256\n"))
            if task_1==512:
                list_variables.append(512)
                i=False
            elif task_1==256:
                list_variables.append(256)
                i=False
        except Exception:
            print("\nTry more. Error. \n")
    i=True
    while i:
        try:
            task_1=input("Enter message\n")
            if len(task_1)!=0:
                list_variables.append(task_1)
                i=False
            else:
               raise Exception
        except Exception:
            print("\nTry more. Error. \n")
    return list_variables


def bitstring(str_text: str):
    res = ''.join(format(ord(i), 'b').zfill(8) for i in str_text)
    return res


def gnhm(h,m):
    pass


def LPS(mes):
    return L(P(S(mes)))


list_variables=start_settings()
M=bitstring(list_variables[1])

IV="0"*list_variables[0]
h=IV
N="0"*512
E="0"*512

if len(M)<512:
    print("lel >> 3 step")
else:
    len_m=len(M)-512
    m=M[len_m:]
    M_shtrix=M[0:len_m]
    block=""
    j=0
    byte_m=list()
    for i in m:
        if j==7:
            byte_m.append(block)
            block=""
            j=0
        else:
            block=block+i
            j+=1    
    #h=gn(h,m)



