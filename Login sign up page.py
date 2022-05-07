import json
import os
accounts={}
user_choice=input("if you want sign up,enter 1,if you want login,press2")
if user_choice=="1":
    uname=input("enter the username to add")
    pwd=input("enter the password to add")
    # create={"account":[uname,pwd]}
    phone=input("enter your phone num")
    email=input("enter the email address")



    accounts.update({"name":uname})
    accounts.update({"password":pwd})
    accounts.update({"phone num":phone})
    accounts.update({"gmail":email})
    accounts=json.dumps(accounts)
    
    with open("accounts.json","w") as f:
        f.write(accounts)
        # json.dump(accounts,f,indent=4)
        # f.write(",\n")
    with open("accounts.json","r") as f:
        accounts=json.load(f)

elif user_choice=="2":
    pass
else:
    print("you must enter 1 or 2")