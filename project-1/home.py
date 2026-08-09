#database ["user@ducat.com,"12345"]
# = , == 
# & , | ,

# login : email : password


email=input("enter your email: ")
password=input("enter your password: ")

if email=="" and password=="":
    print("please enter your email and password")
elif email=="":
    res="please enter your email"
elif password=="":
     res="please enter your password"
    
else:
    res="wellcome"    
    print(res)

