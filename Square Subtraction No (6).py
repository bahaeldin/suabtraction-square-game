import random
print("                          THE INSTRUCTIONS                    ")
print("_______________________________________________________________________")
print("SUBTRACT SQUARE. This is a two-player mathematical game of strategy")
print("It is played by two people with a pile of coins ")
print("The players take turns removing coins from the pile")
print("Always removing a non-zero square number of coins (1, 4, 9, 16, …)")
print("The player who removes the last coin wins.")
print("_______________________________________________________________________")
print("To Play Against Human Enter 1 ")
print("To Play Against Computer Enter 2 ")
c=[4,9,16,25,1,36,49,64,81]
t=len(c)
x=int(input("Enter Number :" ))

#against human

if x==1:
    print("Enter 1 To Input The Number Of Coins ")
    print("Enter 2  To Input Random Select Coins ")
    a=int(input("Enter Number :"))
    if a==1:
        y=int(input("Eter The Amount Of Coins : ") )
        print("The  Amount Of Coins Is :\n ", y)
        
    else:
        y=random.randint(25,100)
        print("The  Amount Of Coins Is :\n ",y)
    while y!=0 :
     for i in range(t):
         b=int(input(" Player One Enter Square Number:"))
         if b in c:
             if b<=y:
                 y=y-b
                 if y<=0:
                     print("Player One win ")
                     print("game end")
                 else:
                     print("The  Amount Of Coins Is :\n ", y)
                 break
             else:
                 print("The number you have entered is bigger than  coins ")
                 print("Enter Square Number Less or Equal to The coins ")
                 continue
         else:
             print("The number you have entered is not square ")
             continue
     while y!=0:
         b=int(input(" Player Two Enter Square Number:"))
         if b in c:
             if b<=y:
                 y=y-b
                 if y<=0:
                     print("Player Two win ")
                     print("game end")
                     g=int(input())
                     break
                 else:
                     print("The  Amount Of Coins Is :\n ", y)
                 break
             else:
                 print("The number you have entered is bigger than  coins ")
                 print("Enter Square Number Less or Equal to The coins ")
                 continue
         else:
             print("The number you have entered is not square ")
             continue
#against computer       
if x == 2:
    print("Against Comuter")
    print("Enter 1 To Input The Number Of Coins ")
    print("Enter 2  To Input Random Coins ")
    a=int(input("Enter Number :"))
    if a==1:
        y=int(input("Enter The Amount Of Coins : ") )
        print("The  Amount Of Coins Is :\n ", y)
        
    else:
        y=random.randint(25,100)
        print("The  Amount Of Coins Is :\n ",y)
    while y!=0:
     for i in range(t):
         b=int(input(" Player One Enter Square Number:"))
         if b in c :
             if b<=y:
                 y=y-b
                 if y<=0:
                     print("Player One win ")
                     print("game end")
                     break
                 else:
                     print("The  Amount Of Coins Is :\n ", y)
                 break
             else:
                 print("The number you have entered is bigger than  coins ")
                 print("Enter Square Number Less or Equal to The coins ")
                 continue
         else:
             print("The number you have entered is not square ")
             continue
     for k in range (50):
         b=random.choice(c)
         if b <=y :
             print(" The Computer Entered :\n ",b )
             y=y-b
             if y <=0:
                 print("Computer win ")
                 print("game end")
             else:
                 print("The  Amount Of Coins Is :\n ", y)
             break
         else:
             continue
