def math():
    import random
    A = random.randint(0, 500)
    B = random.randint(501, 1000)
    User_answer = int(input("What is %i + %i" %(A,B)))
    if User_answer == A+B:
        print("Correct")
    else:
        print("Wrong")
        
math()