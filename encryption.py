import os

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a',
'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P',
'D':'Q', 'E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F','T':'G','U':'H', 'V':'I','W':'J','X':'K','Y':'L','Z':'M'} 
def ENCODER():
  global password
  password = input("\n enter the password to be encoded or decoded\n")
  global pssd 
  pssd =[]
  print("the encoded phrase is ")
  for i in password:
    if i.isalpha():

        encodeed = key[i]
        pssd.append(encodeed)
        print(key[i], end="",)
    else:
      print(i,end="")
    
ENCODER()
ptr=open('password.txt','a')
ptr.write(password+"--")
for i in pssd:
 ptr.write(i)
ptr.close()
print('\nFile Created in /home Directory')




