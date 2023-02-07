import string, random
def gen2():
    def generate(pwd,leng):
        s=""
        for i in range(leng):
                s+= ''.join(random.choice(pwd))
        return s
    if(choi=="dlp"):
        def dlp():
          global d
          d=0
          global l
          l=0
          global p
          p=0
          while((d and l and p)==0):  
             pwd = string.ascii_letters + string.digits + string.punctuation
             global a
             a=generate(pwd,leng)      
             d=0        
             l=0         
             p=0
             for i in a:
                     if(i.isdigit()):
                             d+=1
                     if(i.isupper()):
                            l+=1
                     w=string.punctuation
                     if(i in w):
                        p+=1
        dlp()
        print(a)
       
            
    if(choi=="d"):
        pwd =string.digits
        print(generate(pwd,leng))
    if(choi=="l"):
        pwd=string.ascii_letters
        print(generate(pwd,leng))
    if(choi=="p"):
        pwd=string.punctuation
        print(generate(pwd,leng))
    if(choi=="dl"):
        def dl():
          global d
          d=0
          global l
          l=0
          while((d and l)==0):  
             pwd =string.digits+string.ascii_letters
             global a
             a=generate(pwd,leng)      
             d=0        
             l=0         
             for i in a:
                    if(i.isdigit()):
                        d+=1
                    if(i.isupper()):
                        l+=1
        dl()
        print(a)
    if(choi=="lp"):
        def lp():
          global l
          l=0
          global p
          p=0
          while((l and p)==0):  
             pwd = string.ascii_letters + string.punctuation
             global a
             a=generate(pwd,leng)          
             l=0         
             p=0
             for i in a:
                    if(i.isupper()):
                        l+=1
                    w=string.punctuation
                    if(i in w):
                        p+=1
        lp()
        print(a)
    if(choi=="dp"):
        def dp():
          global d
          d=0
          global p
          p=0
          while((d and p)==0):  
             pwd =string.digits + string.punctuation
             global a
             a=generate(pwd,leng)      
             d=0              
             p=0
             for i in a:
                    if(i.isdigit()):
                        d+=1
                    w=string.punctuation
                    if(i in w):
                        p+=1
        dp()
        print(a)
global leng
leng=int(input(" Enter the length of the password"))
print(" Enter d for digits only \n Enter l for letters only \n Enter p for punctuation only \n Enter dl for digits and letters \n Enter lp for letters and punctuation \n Enter dp for digits and punctuation \n Enter dlp for all combinations") 
global choi
choi=input()

