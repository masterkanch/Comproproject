def begin():
    global option
    print("Welcome to Game")
    option = input("Login or Register or LeaderBoard(login,reg,score): ")
    if(option!="login" and option != "reg" and option != "score"):
        begin()

def login(name,password):
    success = False
    file = open("user.txt","r")
    for i in file:
        a,b = i.split(",")
        a = a.strip()
        b = b.strip()
        if(a==name and b==password): 
            success=True
            break     
    file.close()
    if(success):
        print("Login Successful!!!")
        import ComPro_Project_Keng
    else:
        print("wrong username or password")

def register(name,password):
    file = open('user.txt','a')
    file.write(f'{name},{password}\n')
    file.close
    import ComPro_Project_Keng

def begin():
    global option
    print("Welcome to Game")
    option = input("Login or Register or LeaderBoard(login,reg,score): ")
    if(option!="login" and option != "reg" and option != "score"):
        begin()

def access(option):
    global name
    if(option=="login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name,password)
    elif option == "reg":
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)
    elif option == "score":
        LeaderBoard()

def LeaderBoard():
    print("=======================LeaderBoard====================")
    print("Username                           Totalscore         ")
    file = open("score.txt","r")
    for i in file:
        Username,chompoo,namkhing,totalscore = i.split(",")
        Username = Username.strip()
        totalscore = totalscore.strip()
        print(f"{Username}                                {totalscore}")
    file.close()
begin()
access(option)




