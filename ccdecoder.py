import string
alpha = string.ascii_lowercase 
def decrypt(x,y): 
    decrypted = ""
    for i in x:
        if i in alpha:
            p = alpha.find(i)
            v = (p - y) % 26
            z = alpha[v]
            decrypted += z
        else:
            decrypted += i
    print(decrypted)
def userinput():
    a = "J xpoefs jg bozpof ifsf dbo efdpef uijt?".lower()
    key = 0
    while key < 26:
        decrypt(a, key)
        key += 1

userinput()    