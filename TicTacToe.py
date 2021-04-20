import random  #shall be used only as last option by cpu

a=[['.','.','.'],['.','.','.'],['.','.','.']]
#instructions
print("\n\n\n\n\n\n\nPlease note down the instructions for the game:")
print(""" [0][0] | [0][1] | [0][2]
--------|--------|-------
 [1][0] | [1][1] | [1][2]
--------|--------|-------
 [2][0] | [2][1] | [2][2]
while entering a cordinate please enter in format a b
{two numericals separated by a space:}
a:number along vertical
b:number along horizontal
Entering any other format will display an error!
To help the user remember cordinates indexing shall be given every time during the game.
To exit the game press 'Ctrl+Z'  \n\n\n  """)
#The main tabular form output function
def output():
     print('.   0','   ','1','   ','2')
     print('0  ',a[0][0],' | ',a[0][1],' | ',a[0][2])
     print("   ----|-----|----")
     print('1  ',a[1][0],' | ',a[1][1],' | ',a[1][2])
     print("   ----|-----|----")
     print('2  ',a[2][0],' | ',a[2][1],' | ',a[2][2],'\n\n')

#function for player1's input
def player1():
   try:
      i,j=[int(x) for x in input("Player1:Enter cordinates:").split()]
   except ValueError:
      i,j=4,4       #an invalid input so that next if block again calls the function
      print("INVALID FORMAT!")
      print("Input format:a b {a:vertical key||b:borizontal key}")
   if i not in [0,1,2] or j not in [0,1,2]:
       print("Invalid input")
       player1()
   elif a[i][j]=='.':
       a[i][j]=p1
   elif a[i][j]!='.':
       print("CHEAT ALERT!!:do not attemp to overwrite ")
       player1()

#function for player2's input
def player2():
   try:
      i,j=[int(x) for x in input("Player2:Enter cordinates:").split()]
   except ValueError:
      i,j=5,5      #an invalid input so that next if block again calls the function
      print("INVALID FORMAT!")
      print("Input format:a b {a:vertical key||b:borizontal key}")
   if i not in [0,1,2] or j not in [0,1,2]:
       print("Invalid input")
       player2()
   elif a[i][j]=='.':
       a[i][j]=p2
   elif a[i][j]!='.':
       print("CHEAT ALERT!!:do not attemp to overwrite")
       player2()

#######################################################################################
#The auto function will work on the principle that if it finds it's triplet completing
#it will proceed to do so otherwise it will try to ensure that the player does not take
#an easy win
#######################################################################################
def auto():
    switch=0
    if switch==0:
        for r in range(3):               #checks rows for completing triplet
           if a[r][0]==a[r][1]==cpu or a[r][0]==a[r][2]==cpu or a[r][1]==a[r][2]==cpu: 
               for i in range(3):
                   if a[r][i]=='.':
                       a[r][i]=cpu
                       switch=1
           if switch==1: break

    if switch==0:
        for r in range(3):               #checks colomns for completing triplet
           if a[0][r]==a[1][r]==cpu or a[0][r]==a[2][r]==cpu or a[1][r]==a[2][r]==cpu: 
               for i in range(3):
                   if a[i][r]=='.':
                       a[i][r]=cpu
                       switch=1
           if switch==1: break

    if switch==0:                        #completes possible triplets in slant\
        if a[0][0]==a[1][1]==cpu or a[0][0]==a[2][2]==cpu or a[1][1]==a[2][2]==cpu:
            for r in range(3):
                if a[r][r]=='.':
                    a[r][r]=cpu
                    switch=1
    if switch==0:                        #completes possible triplets in slant/
        if a[0][2]==a[1][1]==cpu or a[0][2]==a[2][0]==cpu or a[1][1]==a[2][0]==cpu:
            for r in range(3):
                if a[r][2-r]=='.':
                    a[r][2-r]=cpu
                    switch=1

    if switch==0:
        for r in range(3):               #checks rows for interrupting triplet
           if a[r][0]==a[r][1]==p1 or a[r][0]==a[r][2]==p1 or a[r][1]==a[r][2]==p1: 
               for i in range(3):
                   if a[r][i]=='.':
                       a[r][i]=cpu
                       switch=1
           if switch==1: break

    if switch==0:
        for r in range(3):               #checks colomns for interrupting triplet
           if a[0][r]==a[1][r]==p1 or a[0][r]==a[2][r]==p1 or a[1][r]==a[2][r]==p1: 
               for i in range(3):
                   if a[i][r]=='.':
                       a[i][r]=cpu
                       switch=1
           if switch==1: break

    if switch==0:                        #interrupts possible triplets in slant\
        if a[0][0]==a[1][1]==p1 or a[0][0]==a[2][2]==p1 or a[1][1]==a[2][2]==p1:
            for r in range(3):
                if a[r][r]=='.':
                    a[r][r]=cpu
                    switch=1
    if switch==0:                        #interrupts possible triplets in slant/
        if a[0][2]==a[1][1]==p1 or a[0][2]==a[2][0]==p1 or a[1][1]==a[2][0]==p1:
            for r in range(3):
                if a[r][2-r]=='.':
                    a[r][2-r]=cpu
                    switch=1
    #this block will chose random cordinates if nothing else is possible
    if switch==0:
        hit_n_trial=0
        while hit_n_trial<8:
           trick=([0,0],[1,1],[2,2],[2,0],[0,2])    #these are be chosen in first move
           [i,j]=random.choice(trick)               #as this choice will never let it
           if a[i][j]=='.':                         #loose
              a[i][j]=cpu
              break
           hit_n_trial+=1
        if hit_n_trial==8:
           while True:                              #here it chooses randomly from whatever 
             i=random.choice([0,1,2])               #is available
             j=random.choice([0,1,2])
             if a[i][j]=='.':
                 a[i][j]=cpu
                 break

###################main program############################################################
while True:   #this loop will not let the program exit once a game is finished
   game=int(input("press 1 for single player\npress 2 for 2 player game\nCtrl+Z to exit!\n"))
   choice=int(input("Player 1:\nPress 1 to play as X\nPress 2 to play as O\n"))
   if choice==1:
       p1='X'
       cpu='O'
       p2='O'
   elif choice==2:
       p1='O'
       cpu='X'
       p2='X'
   count=0
   a=[['.','.','.'],['.','.','.'],['.','.','.']]
   output()
   if game==1:print("Computer Plays First!!")
   while True:
      if game==1:
               auto()
               output()
               #checking cpu's win
               flag=0
               for r in range(3):
                  if a[r][0]==a[r][1]==a[r][2]!='.':
                     flag=1
                     break
                  elif a[0][r]==a[1][r]==a[2][r]!='.':
                     flag=1
                     break
               if flag==1:
                   output()
                   print("Computer wins!!!!\n\n")
                   break
               elif a[0][0]==a[1][1]==a[2][2]!='.':
                   output()
                   print("Computer wins!!!!\n\n")
                   break
               elif a[0][2]==a[1][1]==a[2][0]!='.':
                   output()
                   print("Computer wins!!!!\n\n")
                   break
      elif game==2:
               player2()
               output()
               #checkp2()
               flag=0
               for r in range(3):
                 if a[r][0]==a[r][1]==a[r][2]!='.': 
                    flag=1
                    break
                 elif a[0][r]==a[1][r]==a[2][r]!='.':
                    flag=1
                    break
               if flag==1:
                  output()
                  print("Player 2 wins!!!!\n\n")
                  break
               elif a[0][0]==a[1][1]==a[2][2]!='.':
                  output()
                  print("Player 2 wins!!!!\n\n")
                  break
               elif a[0][2]==a[1][1]==a[2][0]!='.':
                  output()
                  print("Player 2 wins!!!!\n\n")
                  break

      player1()
      count+=1
      if game==2:
         output()
      #checkp1
      flag=0
      for r in range(3):
         if a[r][0]==a[r][1]==a[r][2]!='.':
            flag=1
            break
         elif a[0][r]==a[1][r]==a[2][r]!='.':
            flag=1
            break
      if flag==1:
         output()
         print("Player 1 wins!!!!\n\n")
         break
      elif a[0][0]==a[1][1]==a[2][2]!='.':
         output()
         print("Player 1 wins!!!!\n\n")
         break
      elif a[0][2]==a[1][1]==a[2][0]!='.':
         output()
         print("Player 1 wins!!!!\n\n")
         break
      elif count==4:
         print('The game ends in a draw!\n\n\n')
         break