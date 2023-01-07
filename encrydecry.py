import random
import pyfiglet
app=pyfiglet.figlet_format("Caesar Cipher")
print(app)
def encrypt():
    str1=input("Enter a word or a sentence: ")
    key=int(input("Enter a key for encrypting a word or a sentence: "))
    lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x=len(str1)
    y=len(lst)
    for i in range(x):
        for j in range(y):
            if(str1[i]==lst[j]):
                z=(j+key)%26
                print(lst[z],end="")
def decrypt():
    str1=input("Enter a word or a sentence: ")
    key=int(input("Enter a key for decrypting a word or a sentence: "))
    lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x=len(str1)
    y=len(lst)
    for i in range(x):
        for j in range(y):
            if(str1[i]==lst[j]):
                z=(j-key)%26
                print(lst[z],end="")
str2=input("Enter the function you want to perform: ")
if(str2=="Encrypt" or str2=="encrypt" or str2=="ENCRYPT"):
    encrypt()
elif(str2=="Decrypt" or str2=="decrypt" or str2=="DECRYPT"):
    decrypt()
while(True):
    str3=input("\nDo you want to run the application do you want to exit the appliction: ")
    if(str3=="Yes" or str3=="yes" or str3=="YES"):
        str4=input("Enter the function you want to perform: ")
        if(str4=="Encrypt" or str4=="encrypt" or str4=="ENCRYPT"):
            encrypt()
        elif(str4=="Decrypt" or str4=="decrypt" or str4=="DECRYPT"):
            decrypt()
    elif(str3=="No" or str3=="no" or str3=="NO"):
        print("Thank you for using our application.")
        break