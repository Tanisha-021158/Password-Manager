master_p=input("Enter your masterpassword:")
print("View/Add")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("  ")
            print("User:",user,"Password:",passw)

def existing_user(name):
    with open ('password.txt','r') as f:
        for line in f.readlines():
            user,passw=line.rstrip().split("  ")
            if user==name:
                print("User already exists")
                return True
    return False
    

def add():
    name=input("Enter your name:")
    check=existing_user(name)
    if check==False:
        p=input("Enter your password:")
        with open('password.txt','a') as f:
            f.write(name+"  "+p+"\n")

while True:
    ch=input("Enter your choice(Enter q to quit):").lower()
    if ch=='q':
        break
    if ch=="view":
        view()
    elif ch=="add":
        add()
    else:
        continue
        