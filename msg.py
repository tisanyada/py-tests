from cryptography.fernet import Fernet

def genewrite_key():
    key= Fernet.generate_key()
    with open("pass.key","wb") as key_file:
        key_file.write(key)

def get_key():
    key= open("pass.key","rb").read()
    return key

 
genewrite_key()
msg=input("Enter the message you want to ENCRYPT : ")
key= get_key()
text=msg.encode()
a= Fernet(key)
encrypted_msg= a.encrypt(text)
print(encrypted_msg,)
