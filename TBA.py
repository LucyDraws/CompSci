print("Welcome to Battlefront Trenches. \nPress enter to begin.")
input()
print("It is 1940 and you are in Abbeville, France. You are with a platoon of 4 other British soldiers to invade\nGerman trenches and destroy munitions held within them.")
print("Soon after entering the trench, a German grenade wipes out your platoon, sparing you because of a fellow \nsoldier shielding you.")
print("Left alone in enemy territory, you have two options:\n a) go forward \n b) return to no-mans-land and return to friendly trenches \n")

a = input("What will you do?\n")
Error = "Error, option not valid"
Verify = False
Verify1 = False
Verify2 = False
Verify3 = False
Verify4 = False
Verify5 = False
Verify6 = False
Verify7 = False
while Verify == False:
    if a == "a":
        pass
        Verify = True
        print("As you begin to walk forward, you happen upon a split pathway. You can go one of three ways: Forward, Left,\n and Right")
        b = input("What will you do?\na)listen left\nb) listen right\nc) go left\nd) go forward\ne) go right\n")
        Verify1 = False
        while Verify1 == False:
            if b == "a":
                Verify1 = True
                print("While listening to the left path, you hear German soldiers conversing. You can't tell how many there are.")
                b = input("What will you do?\na) listen left\nb) listen right\nc) go left\nd) go forward\ne) go right\n")
                while Verify3 == False:
                    if b == 'a':
                        print("You already listened to the left path")
                        b = input("What will you do?\na)listen left\nb) listen right\nc) go left\nd) go forward\ne) go right\n")
                    elif b == 'b':
                        print("While listening to the right path, you hear nothing but the sounds of the war surrounding you.")
                        b = input("What will you do?\na) listen left\nb) listen right\nc) go left\nd) go forward\ne) go right")
                    elif b == 'c':
                        Verify3 = True
                        print("Having heard the Germans, you draw your pistol and take cover behind the corner. What do you do?")
                        d = input('a) fire at the Germans\n b) attempt to make them surrender\n')
                        #GERMAN FIGHT
                        while Verify4 == False:
                            if d == 'a':
                                Verify4 = True
                                print('You catch the soldiers offguard and successfully take all three out.')
                                #bunker
                            elif d == 'b':
                                Verify4 = True
                                print("The Soldiers fire, killing you\nGAME OVER")
                            else:
                                print(Error)
                                d = input('a) fire at the Germans\n b) attempt to make them surrender\n')
                        


            elif b == 'b':
                print("While listening to the right path, you hear nothing but the sounds of the war surrounding you.")
                b = input("What will you do?\na) listen left\nb) listen right\nc) go left\nd) go forward\ne) go right")
            elif b == 'c':
                Verify1 = True
                print("You take the left path and are confronted by three German soldiers on patrol.")
                #Germans
                c = input("What do you do?\na) grab your pistol and fire\nb) surrender\nc) run away\n d) negotiate\n")
                Verify2 = False
                while Verify2 == False:
                    if c == 'a':
                        Verify2 = True
                        print("You draw your weapon and are able to shoot one soldier before the other two gun you down.\nGAME OVER")
                    elif c == 'b':
                        Verify2 = True
                        print("The Germans take you prisoner and you are thrown into a PoW camp.\nGAME OVER")
                    elif c == 'c':
                        print("You run away, take a left, and hide in a bunker. You hear the Germans going the opposite direction.")
                        e = input('a) search bunker\nb) leave bunker\nc) stay and hide\n')
                        while Verify5 == False:
                            if e == 'a':
                                Verify5 = True
                                print("looking around, you find German munitions and destroy them\n YOU WIN")
                            elif e == 'b':
                                Verify5 = True
                                print("you go back out and are ambushed and captured by the Germans, who looped back around\nGAME OVER")
                            elif e == 'c':
                                Verify5 = True
                                print("You hide behind a table and hear the Germans pass by again.\nWhat do you do?")
                                f = input('a) search bunker\nb)wait til night to leave and run back to friendly territory\n')
                                while Verify6 == False:
                                    if f == 'a':
                                        Verify6 = True
                                        print("looking around, you find German munitions and destroy them\n YOU WIN")
                                    elif f == 'b':
                                        Verify6 == True
                                        print("You run back to friendly territory without completing your mission.\nMISSION FAILED\nGAME OVER")


                            else:
                                print(Error)
                                e = input('a) search bunker\nb) leave bunker\nc) stay and hide\n')
                 
                    elif c == 'd':
                        Verify2 = True
                        print("They do not understand you. They take you prisoner\nGAME OVER")
                    else:
                        print(Error)
                        c = input("What do you do?\na) grab your pistol and fire\nb) surrender\nc) run away\n d) negotiate\n")

                
            elif b == 'd':
                Verify1 = True
                print("Moving forward, you encounter a bunker, what do you do?")
                g = input('a) search bunker\nb)wait til night to leave and run back to friendly territory\n')
                while Verify7 == False:
                    if g == 'a':
                        Verify7 = True
                        print("looking around, you find German munitions and destroy them\n YOU WIN")
                    elif g == 'b':
                        Verify7 == True
                        print("You run back to friendly territory without completing your mission.\nMISSION FAILED\nGAME OVER")
            elif b == 'e':
                print("You take the path to the right, and find a dead end where the trench is being dug out.\nYou return to the intersection.")
                b = input("What will you do?\na)listen left\nb) listen right\nc) go left\nd) go forward\ne) go right")
            else:
                print(Error)
                b = input("What will you do?\na)listen left\nb) listen right\nc) go left\nd) go forward\ne) go right\n")


        
    
        Verify = True
    elif a == 'b':
        print("You climb out of the trenches into no-mans-land. Your allied troops mistake you for a German soldier and fire, killing you\nGAME OVER")
        Verify = True
    else:
        print(Error)
        a = input("What will you do?")
