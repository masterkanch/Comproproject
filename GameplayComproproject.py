

def Setting():
    global total_score
    total_score = 0
        
    

def rungame():
    global total_score
    times = 12
    run = 0
    score = 0

    print("You're in embarassment: Please Type Run %i times" %times)
    while run < times:

        x = input(" ")
        x = x.lower()

        if x == "run":
            run +=1
            score += 1

        else:
            print("You tripped! Hurry up! Run!")

    total_score += score
    
    


def contact():
    global total_score
    print("Warning! you are in love.")
    print("To contact her")
    x = input("Please type IDLINE FACEBOOK INSTAGRAM " ).split()
    y = input("Please type idline facebook Instagram " ).split()

    score = 0

    if x == "IDLINE FACEBOOK INSTAGRAM":
        score += 5 
    else: 
        score -= 3
    
    if y == "idline facebook Instagram":
        score += 5
    else:
        score -= 3

    total_score += score
    

    


def secret():
    global total_score
    score = 0
    print("Warning secret of your 2 crushes will be reveal. Tough Though Through Thorough Thought ")

    tough = input("")
    though = input("")
    through = input("")
    thorough = input("")
    thought = input("")

    if tough == "Tough":
        score += 2
    else:
        score -= 1
    
    if though == "Though":
        score += 2
    else:
        score -= 1

    if through == "Through":
        score += 2
    else:
        score -= 1

    if thorough == "Thorough":
        score += 2
    else:
        score -= 1

    if thought == "Thought":
        score += 2
    else:
        score -= 1

    total_score += score


def chooserandom():
    print("Your first date")
    print("1.Who are your true love? Chompoo or NamKing")
    print("2.Who are your true love? Chompoo or NamKing")
    print("3.Who are your true love? Chompoo or NamKing")
    choice = int(input(" "))