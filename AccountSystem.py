
Accorlog = input("Press 1 to make an account,Press 2 to login to an account: ")
lmao = 0

if Accorlog == "1":
   name = input("Name:")
   psw = input("Password:")
    
   with open("accounts.txt","a") as f:
        f.write(f"{name},\n{psw}\n\n")
        print("Account added, if login does not work it has already been taken")

if Accorlog == "2":
    
    name = input("Name:")
    psw = input("Password:")
    
    with open("accounts.txt","r") as f:
        accounts = f.readlines()
        
        
        
    for acc in accounts:
        name_txt = acc.split(",")[0]
        psw_txt = acc.split(",")[1]
        
        psw_txt = psw.replace("\n", "")

    if name_txt == name  and psw_txt == psw:
        print("logged in")
    else:
        print("nope")
        
quit()
        

