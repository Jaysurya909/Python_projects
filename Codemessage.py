import random
import string

num_chars = 3
code=input("Enter the codeword")

#ENCODING
if len(code)>=3:
    code1=code[0]
    #code2=code.replace(code[0],"") its also removing the same characters if it appears first
    code2=code[1:]
    code3=code2+code1
    random_chars = ''.join(random.choices(string.ascii_letters , k=num_chars))
    code3=random_chars+code3
    random_chars = ''.join(random.choices(string.ascii_letters , k=num_chars))
    code3=code3+random_chars
    code=code3
    print("Your encoded message is :- ",code)
else:
    code1=code[0]
    code1=code[1]+code1
    code=code1
    print("Your encoded message is :- ",code)

#DECODING
if len(code)>=3:
    code1=code[3:]
    code2=code1[0:-3]# also can use len(code1)-3
    code3=code2[-1]
    #code=code2.replace(code2[-1],"") 
    code=code2[0:-1]
    code=code3+code
    print("Your decoded message is :- ",code)    
else:
    code1=code[0]
    code1=code[1]+code1
    code=code1
    print("Your decoded message is:- ",code)
