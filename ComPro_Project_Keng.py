import GameplayComproproject

def start():
    global Username
    global scoreNK
    global scoreCH
    print("This is getting to the main game")
    Username = input("What you want to be called? ")
    scoreCH = 0
    scoreNK = 0



def event1():
    #เหตุ 1

    print()
    print("Event 1")
    print("เวลาเช้า // %s ตื่นนอนเวลา 6.00 น.  และเตรียมตัวไปโรงเรียน" %Username)
    print("ว๊า เช้าแล้วหรอเนี่ย วันนี้อากาศดีจัง อยากไปโรงเรียนจะแย่แล้ว")
    print("วันนี้จะเป็นวันที่ดีรึเปล่านะวันเกิดเราเองก็ต้องดีสิแต่จะมีใครจำวันเกิดเราได้รึเปล่านะ ")
    print()
    print("At the morning time 07.00")
    print(" %s ช้านี้ก็ต้องเดินไปโรงเรียนคนเดียวอีกแล้วสินะ" %Username)
    print(" สวัสดี %s ตื่นเช้าจังนะวันนี้" %Username)
    print(" %s  ฉันอยากจะลองตื่นเช้าเพื่ออากาศดีๆ สักวันน่ะ " %Username)
    print(" ปกติ %s ไม่ค่อยตื่นเช้านี่วันนี้เป็นวันพิเศษรึเปล่าน๊า" %Username)
    print()
    #ตอนนี้กำลังอยู่ในตัวเลือกที่ 1 แล้ว
    while True:
        print("Please choose")
        print("1 %s ฉันแค่อยากตื่นเช้าน่ะ" %Username)
        print("2 %s เปล่าเลยก็แค่วันธรรมดา" %Username)
        choice = int(input(" "))
        if choice == 1:
            print("(น้ำขิง) ไม่ใช้วันนี้เป็นวันพิเศษหรอกหรอ")
            print("1. ก็ไม่ได้พิเศษอะไรมากขนากนั้นหรอกนะ ")
            print("2. ใช่แล้วล่ะวันนี้วันพิเศษของฉันนะ ")
            print("3. ทำไมเธอถึงคิดว่าวันนี้ของฉันเป็นวันพิเศษของฉันล่ะ ")
            print("1. 2. 3.")
            subchoice = int(input(" ")) 
            #เสร็จตัวเลือก 1 
            print("(น้ำขิง) แต่วันนี้เป็นวันเกิด %s นี่มันก็ต้องพิเศษสิดูสิฉันมีอะไรจะให้ด้วยนะ " %Username)
            print(" %s เอ่อ...อออ อื้ม......" %Username)
            break
        elif choice == 2:
            print("(น้ำขิง) ไม่ใช่ว่าวันนี้มันเป็นวันสำคัญสำหรับเธอหรอ ")
            print("1. วันนี้อากาศดีก็เลยอยากจะตื่นเช้า")
            print("2. วันนี้ก็เป็นวันสำคัญของฉันจริงๆนั่นแหละ")
            print("3. ทำไมเธอถึงคิดว่าวันนี้ของฉันเป็นวันสำคัญของฉัน")
            print("1. 2. 3.")
            subchoice = int(input(" "))
            #เสร็จตัวเลือก 2 
            print("(น้ำขิง) ก็วันนี้เป็นวันเกิดของ %s ฉันเลยตื่นเช้ามาเพื่อเอาสิ่งนี้มาให้เลยนะ" %Username)
            print(" %s เอ่อ...อออ อื้ม......" %Username)
            break
        else:
            print("Error try again")
            continue

def event2():
    #เหตุ 2
    global scoreCH
    global scoreNK
    print("Event 2")
    print("เวลาสาย // %s เข้าเรียนแล้วเวลา 09.00 – 12.00 น." %Username)
    print("ได้เวลาเรียนคาบแรกแล้ว เสียงประกาศจากประชาสัมพันธ์")
    print("ณ หน้าชั้นเรียนวิชาแรก เวลา 09.00 น. ")
    print(" %s ฉันไม่น่าวิ่งหนีออกมาเลยวันนี้วันเกิดของฉันแท้ๆ " %Username)
    print("(ชมพู่) เอ๊ะ  %s ทำไมดูเหนื่อยๆนะเป็นอะไรรึเปล่า" %Username)
    print(" %s เปล่าหรอกไม่มีอะไร ฉันแค่วิ่งออกกำลังกายตอนเช้ามา" %Username)
    print("(ชมพู่) แต่ปกติ %s มาสายนะ อ้อ....ฉันจำได้แล้ววันนี้วันเกิดของนายนี่นา"  %Username)
    #ตอนนี้กำลังอยู่ในตัวเลือกที่ 2 แล้ว

    while True:
        print("Please choose")
        print(" 1 %s เปล่า....เธอจำของใครมารึเปล่า " %Username)
        print("2 %s เธอจำวันเกิดฉันได้หรอ " %(Username))
        choice = int(input(" "))
        if choice == 1:
            print("(ชมพู่) ก็วันนี้วันเกิดของนายนี่ฉันจำได้แม่นเลยล่ะ")
            print("1. เธอนี่น่ารักนะจำวันเดินฉันได้ด้วย ")
            print("2. ทำไมถึงได้จำแม่นขนาดนี้ล่ะ ใส่ใจฉันรึเปล่านะ ")
            print("3. ฉันรีมมาเพื่อที่จะได้เจอเธอและให้วันนี้เป็นวันที่พิเศษยิ่งกว่าไง ")
            print("1. 2. 3.")

            subchoice = int(input(" "))
            if subchoice == 2:
                scoreCH += 5
                return scoreCH
            elif subchoice == 1 or subchoice == 3:
                scoreCH += 4
                return scoreCH



            print("(ชมพู่) ปากหวานเชียว จีบฉันในวันเกิดตัวเองปะเนี่ย ")
            print(" %s ก็นิดนึงอะมีใจไหมล่ะ " %Username)
            break

        elif choice == 2:
            print("(ชมพู่) ก็ใช่น่ะสิไม่ใช่วันเกิดนายแล้วจะเป็นใครได้อีกล่ะ")
            print("1. ขอบใจนะที่จำได้ แบบนี้เรียกใส่ใจรึเปล่านะ ")
            print("2. อยากให้เป็นวันที่ดีกว่าเดิม เลยมาเช้าเพื่อเจอเธอ ")
            print("3. มีสิ่งสำคัญกว่าวันเกิดน่ะเลยมาเช้า รู้ไหมสิ่งสำคัญนั่นก็คือเธอไง ")
            print("1. 2. 3.")

            subchoice = int(input(" "))


            if subchoice == 1:
                scoreCH += 5
                return scoreCH
            elif subchoice == 2 or subchoice == 3:
                scoreCH += 4
                return scoreCH




            #เสร็จตัวเลือก 2
            print("(ชมพู่) จะจีบก็เบาๆหน่อย รู้แล้วว่าชอบ")
            print(" %s ชอบแล้วมีใจให้ไหมล่ะ" %Username)
            break
        else:
            print("Error try again")
            continue

def event3():
    global scoreCH
    global scoreNK
    #เหตุ 3
    print("Event 3")
    print("เวลาเที่ยง // %s เรียนภาคเช้าเสร็จและกำลังจะไปหาอะไรทานที่โรงอาหาร เวลา 12.00 – 13.00 น." %Username)
    print(" %s เรียนเหนื่อยจังนะ และก็หิวด้วยไปหาอไรกินที่โรงอาหารดีกว่า" %Username)
    print("(น้ำขิง) เอ๊ะ นั่น  %s นี่ฉันยังไม่ได้เอาของขวัญไปให้เลย " %Username)
    print("(น้ำขิง) ชวนไปกินข้าวเที่ยงด้วยกันจะดีไหมนะ")
    print(" %s อ้าวเจอกันพอดีเลย (น้ำขิง) ทานข้าวที่โรงอาหารด้วยกันไหม ขอโทษที่เมื่อเช้าฉันวิ่งหนีมานะ" %Username)
    print("(น้ำขิง) ไปสิ ไม่เป็นไรหรอกไปกินข้าวเที่ยงกันกันเถอะ ถ้าไม่รังเกียจช่วยรับของขวัญที่ฉันอุส่าทำมาให้ด้วยนะ")
    print(" %s เธอตั้งใจทำมาให้ฉันเลยหรอ " %Username)
    print("(น้ำขิง) ใช่ฉันคิดว่านายจะชอบมันนะ ")
    #ตอนนี้กำลังอยู่ในตัวเลือกที่ 3 แล้ว
    while True:
        print("Please choose 1 %s ขอบคุณสำหรับของขวัญนะ" %(Username))
        print("2 %s ของขวัญก็ชอบแล้วก็ชอบเธอด้วย" %Username)
        choice = int(input(" "))
        if choice == 1:
            print("(น้ำขิง) คือว่า......ฉันขอ IG ได้ไหมหรืออะไรก็ได้ที่เธอจะให้แต่ถ้าไม่ให้ก็ไม่เป็นไรนะ")
            print("1. ได้สิเธอตั้งใจทำของขวัญเพื่อฉันขนาดนี้ ")
            print("2. ได้สิว่าแต่นี่เธอแอบชอบฉันรึเปล่า ")
            print("3. ทำไมเธอถึงตั้งใจทำของขวัญเพื่อฉันขนาดนี้ล่ะ ")
            print("4. ได้สิฉันให้เธออยู่แล้ว ")
            print("1. 2. 3. 4.")
            subchoice = int(input(" "))

            if subchoice == 1:
                scoreCH += 5
                return scoreCH
            elif subchoice == 2 or subchoice == 3 or subchoice == 4:
                scoreCH += 4
                return scoreCH



            #เสร็จตัวเลือก 1
            print("(น้ำขิง) ขอบคุณนะ เอ่อคือ....จะเป็นอะไรไหม....")
            print("(ชมพู่) หวัดดี นี่พวกเธอทำอะไรกันอยู่หรอ นั่นกล่องอะไรอะ")
            break
        elif choice == 2:
            print("(น้ำขิง) เอ๊ะ ฉันก็เขินนะ.....ชอบแล้วขอ IG ได้ไหมล่ะ")
            print("1. ได้สิใครจะกล้าปฏิเสธคนที่อุส่าอาของขวัญมาให้ล่ะ ")
            print("2. ให้ทั้ง IG ทั้ง Me ไปเลยอะ ")
            print("3. เอาไปทั้งตัวและหัวใจเราเลย ")
            print("4. เอาโทรศัพท์เธอมาสิฉันจะพิมพ์ให้ ")
            print("1. 2. 3. 4.")
            subchoice = int(input(" "))

            if subchoice == 1:
                scoreCH += 5
                return scoreCH
            elif subchoice == 2 or subchoice == 3 or subchoice == 4:
                scoreCH += 4
                return scoreCH


            #เสร็จตัวเลือก 2
            print("(น้ำขิง) ขอบคุณนะ เอ่อคือ....จะเป็นอะไรไหม....")
            print("(ชมพู่) หวัดดี เจอพอดีเลยไปทานข้าวด้วยกันไหม เอ๊ะ นั่นกล่องอะไรอะ")
            break
        else:
            print("Error try again")
            continue


def event4(): 
    global scoreNK
    global scoreCH
    #เหตุ 4
    print("Event 4")
    print("เวลาบ่าย // หลังจากที่ทานอาหารเที่ยงเสร็จก็กลับไปเรียนวิชาภาคบ่าย")
    print("ณ เวลา 13.00 – 15 . 00 น. คาบว่าง")
    print(" %s เกือบไปแล้วไหมล่ะ " %Username)
    print("(น้ำขิง) นี่บ่ายแล้วนะนายไม่เรียนวิชิภาคบ่ายหรอ ")
    print(" %s พอดีว่าอาจารย์สั่งงานไว้น่ะ" %Username)
    print("(น้ำขิง) เปิดดูรึยังล่ะของขวัญ")
    print(" %s มันน่ารักมากเลยน่ะ ขอบคุณอีกครั้งที่ทำมาให้ " %Username)
    print("(น้ำขิง) ฉันดีใจที่นายชอบมันนะ คือว่ามันก็ยากที่จะพูดนะ แต่ฉันรู้สึกดีกับนายนะแล้วจะเป็นอะไรไหมถ้าเรา...")
    #ตอนนี้กำลังอยู่ในตัวเลือกที่ 4 แล้ว
    while True:
        print("Please choose 1 %s นี่เธอย่าบอกนะว่าเธอชอบฉัน " %Username )
        print("2 %s เธอหมายถึงอะไรหรอถ้าเรา...." %Username)
        choice = int(input(" "))
        if choice == 1:
            print("(น้ำขิง) ฉันชอบนายมาสักพักใหญ่แล้วล่ะ ฉันอยากจะคบหาดูใจกับนายนะ")
            print("1. ให้เวลาฉันสักหน่อยได้ไหม เธอก็มี IG ฉันแล้วนี่ ")
            print("2. ฉันก็ต้องการใครสักคนนะ ใครคนนั้นที่เป็นเธอ ")
            print("3. จริงหรอ...งั้นเย็นนี้เราไปหาอะไรกินร้านที่เธอชอบและคุยกันนะ ")
            print("4. มันเร็วไปไหมที่ฉันจะให้คำตอบตอนนี้ไว้เน็นนี้เราก็ออกไปหาอะไรกินแล้วคุยกันจะดีกว่าไหม ")
            print("1. 2. 3. 4.")
            subchoice = int(input(" "))
            if subchoice == 3:
                scoreCH += 5
                return scoreCH
            elif subchoice == 2  or subchoice == 4:
                scoreCH += 4
                return scoreCH
            elif subchoice == 1:
                scoreCH += 3
                return scoreCH


            #เสร็จตัวเลือก 1
            print("(น้ำขิง) ถ้างั้นเย็นนี้ฉันจะรอคำตอบนะ ")
            break
        elif choice == 2:
            print("(น้ำขิง) ถ้าฉันอยากจะขอคบหาดูใจกับนาย { บ้าจังฉันบอกชอบไปแล้วหรอเนี่ย }")
            print("1. ฉันว่างตอนเย็นนะไว้ฉันจะชวนไปหาอะไรทานดีไหมล่ะ ")
            print("2. จริงหรอ...งั้นเย็นนี้เราไปหาอะไรกินร้านที่เธอชอบและคุยกันนะ ")
            print("3. ให้เวลาฉันคิดถึงเย็นนี้ได้ไหม ")
            print("4. งั้น...เธอคิดยังไงกับเดทแรกเย็นนี้ล่ะ ")
            print("1. 2. 3. 4.")
            subchoice = int(input(" "))

            if subchoice == 4:
                scoreCH += 5
                return scoreCH
            elif subchoice == 2  or subchoice == 1:
                scoreCH += 4
                return scoreCH
            elif subchoice == 3:
                scoreCH += 3
                return scoreCH

            #เสร็จตัวเลือก 2
            print("(น้ำขิง) ถ้างั้นเย็นนี้ฉันจะรอคำตอบนะ")
            break
        else:
            print("Error try again")
            continue

def event5():
    #เหตุ 5
    global scoreNK
    global scoreCH
    print("Event 5")
    print("เวลาเย็น // หลังจากที่ทำงานส่งเสร็จ ก็เป็นเวลากลับบ้าน")
    print("ณ เวลา 15.00 – 17.00 น. กำลังเดินทางกลับบ้าน")
    print(" %s เป็นวันเกิดที่ดีจังเลยนะ" %Username)
    print("(ชมพู่) นี่ดีใจอะไรอยู่คนเดียวอะ เห็นยิ้มมาสักพักละ")
    print(" %s เปล่าๆ คือว่าฉันแค่รู้สึกดีอะ"  %Username)
    print("(ชมพู่) วันเกิดทั้งทีฉันไม่มีอะไรจะให้อะ แต่ฉันมีร้านคาเฟ่ดีๆอยู่นะว่างจะไปไหมล่ะ")
    print(" %s ได้สิฉันว่างอยู่พอดีเลย " %Username)
    print("ณ ร้านกาแฟ คาเฟ่ แห่งหนึ่ง เวลา 16.00 ")
    print(" %s ไม่ไกลจากที่โรงเรียนนี่ " %Username)
    print("(ชมพู่)  ใช่แล้วล่ะ ฉันชอบมาที่นี่บ่อยๆน่ะ ")
    print(" %s ฉันคงต้องมาที่นี่บ่อยๆบ่างแล้วล่ะ จะได้เจอเธอไง" %Username)
    print("(ชมพู่) ก็มี IG ฉันแล้วนี่จะยังไงอีก ")
    print(" %s จริงๆฉันดีใจมากๆเลยนะที่ได้มาที่นี่กับเธอ " %Username)
    print("(ชมพู่) แล้วทำไมต้องเป็นฉันด้วยล่ะ ชอบฉันขนาดนั้นเลยหรอ ")
    #ตอนนี้กำลังอยู่ในตัวเลือกที่ 5 แล้ว
    while True:
        print("Please choose")
        print("1 %s แล้วคิดว่านี่ไม่ใช่เดทของเรารึไง" %Username)
        print("2 %s อยากเป็นคนที่ถูกชอบไหมล่ะ" %Username)
        choice = int(input(" "))
        if choice == 1:
            print("(ชมพู่) เธอชอบเดทแรกของเราไหมล่ะ")
            print("1. เป็นเดทแรกที่ดีที่มีเธออยู่ด้วยฉันชอบมากเลยล่ะ ")
            print("2. จริงๆฉันแอบชอบเธอมานานแล้วน่ะ ")
            print("3. นี่เป็นเดทแรกที่ดีมากเลยล่ะสำหรับฉัน ")
            print("4. ไว้เรามาที่นี่บ่อยๆไหมล่ะ ")
            print("1. 2. 3. 4.")
            subchoice = int(input(" "))

            if subchoice == 1:
                scoreCH += 5
                return scoreCH
            elif subchoice == 3  or subchoice == 4:
                scoreCH += 4
                return scoreCH
            elif subchoice == 2:
                scoreCH += 3
                return scoreCH

             




            #เสร็จตัวเลือก 1
            print("(ชมพู่) นี่งั้นดึกๆนี้ก็ทักมาสิ ")
            break
        elif choice == 2:
            print("(ชมพู่) พูดมาขนาดนี้แล้วพูดตรงๆแลยไหม")
            print("1. ไว้ฉันจะให้คำตอมในข้อความดีไหมล่ะ ")
            print("2. นี่ฉันขอ IG เธอเมื่อตอนเช้าไม่ชัดเจดว่าฉันชอบเธอหรอ ")
            print("3. นี้เป็นวันที่ดีที่สุดในการเริ่มต้นที่จะคุยเลยนะ ")
            print("4. แล้วเธอคิดยังไงล่ะถ้านี่คือเดทแรกของเรา ")
            print("1. 2. 3. 4.")
            subchoice = int(input(" "))

            if subchoice == 4:
                scoreCH += 5
                return scoreCH
            elif subchoice == 3  or subchoice == 2:
                scoreCH += 4
                return scoreCH
            elif subchoice == 1:
                scoreCH += 3
                return scoreCH


            #เสร็จตัวเลือก 2
            print("(ชมพู่) นายก็มี IG ฉันแล้วไว งั้นดึกๆนี้ก็ทักมาสิ ")
            break
        else:
            print("Error try again")
            continue



def choosethegirl(): #This one Momo put in this file because having problem with importing scoreNK and scoreCH
    global scoreCH
    global scoreNK
    while True:
        
        print("Choose a cookie 1-9")
        cookie = int(input(" ")) 

        if cookie%2 == 0:
            scoreCH += 10
            return scoreCH
            break

        elif cookie%2 == 1:
            scoreNK +=10
            return scoreNK
            break

        else:
            continue



def event6():
    #เหตุ 6
    print("Event 6")
    print("แชตก่อนนอน // หลังจากที่เดทกันที่ร้านกาแฟ คาเฟ่ ทั้งคู่ก็แยกย้ายกันกลับบ้าน")
    print("ณ เวลา 22.00 น. แชตใน Facebook ")
    print("(น้ำขิง) นี่ใช่ %sไหม ฉันหวังว่าของขวัญนั้นจะเปฌนสื่อกลางระหว่างเรานะ" %Username)
    print(" %s ฉันเอง ฉันชอบของขวัญเธอมากๆเลยนะ" %Username)
    print("(น้ำขิง) แล้วนายล่ะชอบฉันเหมือนของขวัญบ้างไหม")
    print("(ชมพู่) หวัดดี %s เดทแรกของเราก็สนุกดีนะ " %Username)
    print(" %s มีนดีมากๆเลยล่ะ " %Username)
    print("(ชมพู่) ฉันชอบเดทแรกของเรานะ แล้วนายล่ะอยากให้เป็นแบบนี้ต่อไปไหม")
    print("คำเตือนคุณต้องเลือกแล้วว่าคุณชอบใครกันแน่ โปรกจำไว้ว่าการตัดสินใจมีผลต่อคะแนน และความรักของทั้งสองคนฉะนั้นโปรดตอบด้วยใจจริงๆ ")
    #ตอนนี้กำลังอยู่ในตัวเลือกที่ 6 แล้ว

    while True:
        global scoreCH
        global scoreNK
        print("Please choose")
        print("1 %s ฉันชอบ (น้ำขิง) มากกว่าของขวัญอีก " %Username)
        print("2 %s ฉันอยากให้เรามีเดทครั้งต่อไปนะ" %Username)
        print("3 %s ฉันอยากให้ทั้งสองคนนี้อยู่กับฉันต่อไปมินิเกมช่วยฉันด้วย " %Username)

        choice = int(input(" "))
        if choice == 1:
            print("(น้ำขิง) ไว้ฉันจะรอเดทแรกของเรานะ  %s " %Username)
            print("1.%s ได้สิฉันเองก็ตั้งตารอวันนั้นอยู่นะ " %Username)

            subchoice = int(input("1."))
            if subchoice == 1:
                scoreNK += 10
                return scoreNK
            else:
                print("Error")
            #เสร็จตัวเลือก 1
            break

        elif choice == 2:
            print("(ชมพู่) ไว้ฉันจะรอที่ร้านเดิมนะ ")
            print("1.%s แน่นอนฉันจะไปที่นั่นทุกวันเลย " %Username)
            subchoice = int(input("1."))
            if subchoice == 1:
                scoreCH += 10
                return scoreCH

            else:
                print("Error")
            #เสร็จตัวเลือก 2
            break
        elif choice == 3:
            choosethegirl()
            #มินิเกม 6
            break
        else:
            print("Error try again")
            continue

def savescore():
    file = open('score.txt','a')
    file.write(f'{Username},{scoreCH},{scoreNK},{GameplayComproproject.total_score}\n')

start()
GameplayComproproject.Setting()
event1()
print("This is minigame. Kill some time with it")
import hangman
GameplayComproproject.rungame()
print("This is another minigame. Kill some time with it")
import Paw_Ying_Choob
event2()
print("Now another minigame.")
import Opal
GameplayComproproject.contact()
event3()
GameplayComproproject.secret()
event4()
GameplayComproproject.chooserandom()
event5()
event6()
savescore()
print(f"Score Chompoo = {scoreCH}")
print(f"Score Namkhing = {scoreNK}")
print(f"Total score = {GameplayComproproject.total_score}")