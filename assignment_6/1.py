class Password_manager:
    def __init__(self, usr_id, name):
        self.old_passwords=[]
        self.name=name
        self.usr_id=usr_id
    def get_password(self):
        if self.old_passwords==[]:
            return "no passwords are set"
        else:
            return self.old_passwords[-1]
        
    def set_password(self, new_password):
        if new_password in self.old_passwords:
            print("new password cannot be one of old passwords")
            return 1
        else:
            self.old_passwords.append(new_password)
            return 0
    def is_correct(self,password):
        if password == self.old_passwords[-1]:
            return True
        else:
            return False
users={}
curr_usr=''
def add_usr():
    global users
    u_id=input("Enter User Id:\t")
    u_name=("Enter User Name:\t")
    if u_id not in users.keys():
        users[u_id]=Password_manager(u_id,u_name)
def change_usr():
    global curr_usr
    global users
    u_id=input("Enter User Id:\t")
    if(u_id in users.keys()):
        curr_usr=u_id
    else:
        print("User not added. please add user first")
while True:
    if users=={}:
        print("No users added. please add a user")
        add_usr()
        continue
    if curr_usr=='':
        print("No users are selected. Select current user")
        curr_usr=input("Enter User Id:\t")
        continue
    print("""
____________________________PasswordManager____________________________

0. Add User
1. Set User
2. Set Password
3. Get Password
4. Check Password
5. Change User
6. Exit
_______________________________________________________________________
          """)
    
    choice=int(input("Enter Choice:\t"))
    if choice==0:
        add_usr
    elif choice==1:
        curr_usr=input("Enter User Id:\t")
        if curr_usr not in users.keys():
            print("User not added")
    elif choice==2:
        password=input("Enter Password:\t")
        users[curr_usr].set_password(password)
    elif choice==3:
        print(users[curr_usr].get_password())
    elif choice==4:
        password=input("Enter Password:\t")
        print(users[curr_usr].is_correct(password))
    elif choice==5:
        change_usr()
    elif choice ==6:
        break
