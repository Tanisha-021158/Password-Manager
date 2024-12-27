from cryptography.fernet import Fernet

#key+password+text to encrypt= random text
#random text+key+password=text to encrypt

def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key

master_p=input("Enter your masterpassword:")
key=load_key()+master_p.encode()
fer=Fernet(key)
print("View/Add")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            line=line.rstrip()
            user,passw=line.split("  ",1)
            print("User:",user,"Password:",fer.decrypt(passw.encode()).decode())

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
            f.write(name+"  "+fer.encrypt(p.encode()).decode()+"\n")

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
        