from Lab_Tools.ParadigmStrings import BinStr
import secret

def feistel(block,keys):
    halflen=int(len(block)/2)
    l0=block[:halflen]
    r0=block[halflen:]
    for k in keys:
        r1=l0^(r0^k)
        l1=r0
        r0=r1
        l0=l1
        #Every key is insecure... because of me! Every print statement must die
        print(BinStr("".join([r0.ascii(),l0.ascii()])))
    return BinStr("".join([r0.ascii(),l0.ascii()]))

keys=[]
for i in range(0,len(secret.flag)-5,5):
    keys.append(BinStr(secret.flag[i:i+5]))

feistel(secret.code,keys)
