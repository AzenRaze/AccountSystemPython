Thing = input("Press 1 to make an account,Press 2 to login:")

if Thing == "1":
    name = input("Name:")
    psw = input("Password:")

    with open('Accounts.txt', 'r') as f:
        accounts = f.readlines()
        for acc in accounts:
            name_txt = acc.split(',')[0]
        with open("Accounts.txt","a") as f:

            if name == name_txt:
                print("Name Taken")
            else:
                f.write(f"{name},{psw}\n")
                print("Account Added")
if Thing == "2":
    name = input("Name:")
    psw = input("Password:")
    
    with open("accounts.txt","r") as f:
       accounts = f.readlines()
       
    for acc in accounts:
        name_txt = acc.split(",")[0]
        
        
        
    for acc in accounts:
        name_txt = acc.split(",")[0]
        psw_txt = acc.split(",")[1]
        
        psw_txt = psw.replace("\n", "")

    if name_txt == name  and psw_txt == psw:
        print("Logged In")
    else:
        print("Wrong")
        
quit()
