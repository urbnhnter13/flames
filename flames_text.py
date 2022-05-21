import flames_logic as flms

yname=str(input("Enter your name : "))
thname=str(input("Enter their name : "))
(msg1,nm1)=flms.printer(yname.lower(),thname.lower())
print(yname," & ",thname)
flms.messpr(nm1)
print(msg1)
print("_________________________________________")


