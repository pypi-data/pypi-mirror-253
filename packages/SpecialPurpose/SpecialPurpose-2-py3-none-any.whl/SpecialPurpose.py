import string 
from Crypto.Util import number
import random
import math
import pyfiglet
import matplotlib.pyplot as plt
from getpass import getpass


# Generals : 
def welcome():
    """
    Displays a simple welcome banner
    """
    welcome_mess = pyfiglet.figlet_format("Welcome to MonieCrypt",font="slant")
    print(welcome_mess)


# String preping 
def clean(x:str):
    """
    Clears the given string argument from punctuation and newlines
    returns the cleaned string
    """
    result=[]
    for i in list(x) :
        if i not in string.punctuation and not i in string.digits:
            result.append(i)
    return "".join(result)


# File handeling :
def readFile():
    """
    Gets the filename and opens it.
    Keeps taking input until a correct filename is entered.
    Returns the filename
    """
    while True:
        try:
            infile = input("Enter the input filename : ")
            file = open(infile,"r")
            break
        except:
            print(f"{infile} doesnt exist in this directory ! ")
    return file.read()


def writeFile(text:str):
    """
    Gets the output filename , creates it and writes into it the given string argument.
    Returns the output filename
    """
    outFile = input("Enter output filename : ")
    file = open(outFile,"w")
    print(text,file=file)
    return outFile




#Key handeling:
def getKey():
    """
    Prompts the user to input the key
    clears it and turns it into lowercase string
    """
    key = getpass("Enter Key : ")
    key = clean(key).lower()
    return key



def genkey(k:str):
    """
    Takes a given key and generated the key sequence.
    return the generated sequence.
    """
    k1=k.lower()
    k=""
    for i in k1:
        if i not in k:
            k+=i
    l=string.ascii_lowercase
    for i in l:
        if i not in k:
            k+=i
    return k


# Encryption and Decryption functions : 
def oldEnc(k,m:str):
    """
    Encrypts given a key and a message using the classic monoalphabet cipher.
    """
    k=genkey(k)
    k=list(k)
    m = clean(m).lower()
    c=""
    for i in m:
        if i in string.punctuation or i=='\n' or i==" ":
            c+=i
        else:
            c+= k[ord(i)%97]
    return c

def oldDec(k,c):
    """
    Decrypts given a key and a ciphered text using the classic monoalphabet cipher.
    """
    k=genkey(k)
    dic={}
    char=97
    c = clean(c)
    m=""
    for i in k:
        dic[i]=chr(char)
        char+=1

    for i in c:
        if i ==' ' or i=='\n':
            m+=i
        else:
            m+=dic[i]
    return m



# Frequency Attack 
def Unigram_frequencyAnalysis(c):
    """
    Does a character-based frequency analysis 
    return a dictionary of the results 
    """
    c = c.replace(" ",'')
    c = c.replace("\n",'')
    dic={}
    c=list(c)
    for i in c:
        if i in dic:
            dic[i]+=1
        else :
            dic[i]=1

    return dic


def Bigram_frequencyAnalysis(c):
    c = c.replace(" ","")
    c = c.replace("\n","")
    diction = {}
    for i in range(1, len(c),2):
            bigram = c[i-1:i+1]
            if bigram in diction:
                diction[bigram] += 1
            else:
                diction[bigram] = 1 

    return diction


def Trigram_frequencyAnalysis(c):
    c = c.replace(" ","")
    c = c.replace("\n","")
    diction = {}
    for i in range(1,len(c)-1,3):
            tri = c[i-1:i+2]
            if tri in diction:
                diction[tri]+=1 
            else:
                diction[tri]=1 

    return diction



def Attack(S):
    freq = Unigram_frequencyAnalysis(S)
    sorted_freq = sorted([(value,key) for (key, value) in freq.items()],reverse=True)
    English_Letters =  "etaoinshrdlcumwfgypbvkjxqz"
    plainText = [""]*25

    for i in range(25):
        shift = ord(English_Letters[i])-ord(sorted_freq[i%len(sorted_freq)][1])
        p = ""
        for j in S:
        
            if j==" ":
                p+=" "
                continue
            else:
                y = ord(j)-97
                y +=shift

                if y<0:
                    y+=25
                if y>25:
                    y-=26

                p+=chr(y+97)
            plainText[i]=p
        
        print(plainText[i])

def plot_analysis(dic):
    """
    Generates a bar chart of the frequency analysis.
    both on screen and png saved
    """
    letters = list(dic.keys())
    freq = list(dic.values())
    plt.title('Frequency analysis')
    plt.bar(range(len(dic)), freq, tick_label=letters)
    plt.rcParams.update({
        "font.family": "monospace",
        "font.monospace": ["monospace"],  
    })

    plt.savefig("Analysis.png")
    plt.show()
    print(">>The output has been saved in Analysis.png")


def table_analysis(dic):
    total =  sum(dic.values())

    print("\n{:<10} {:<10} {:<10}".format('GRAM', 'FREQUENCY', 'PERCENTAGE'))
    for key,value in dic.items():
        print("{:<10} {:<10} {:<10.2f}".format(key,value, value/total))
        


def new_mono_enc(k,m):
    p=number.getPrime(1024)
    q=number.getPrime(1024)    
    n=q*p
    tot=(p-1)*(q-1)
    e = random.randrange(1, tot)
    while math.gcd(e, tot) != 1:
        e = random.randrange(1, tot)
    d=pow(e,-1,tot)

    m=oldEnc(k,m)
    m = m.encode('utf-8')  
    c = pow(int.from_bytes(m, 'big'), e, n)
    return c,d,n



def new_mono_dec(k,c,d,n):
    m = pow(c, d, n)
    m = m.to_bytes((m.bit_length() + 7) // 8, 'big')
    m = m.decode('utf-8')    
    m=oldDec(k,m)
    return m


def int_to_string(integer):
    return ''.join([chr((integer >> j) & 0xff) for j in reversed(range(0, 64, 8))])





















































