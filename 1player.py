#prototype
import random


a=[['.','.','.'],['.','.','.'],['.','.','.']]

print("\n\n\nPlease note down the instructions for the game:")            #instru$
print(""" [0][0] | [0][1] | [0][2]
--------|--------|-------
 [1][0] | [1][1] | [1][2]
--------|--------|-------
 [2][0] | [2][1] | [2][2]
while entering a cordinate please enter in format a b
{two numericals separated by a space:}
You can access the cordinates' naming anytime if you enter 'k'

      """)

def Help():
   print("""    [0][0] | [0][1] | [0][2]
   --------|--------|-------
    [1][0] | [1][1] | [1][2]
   --------|--------|-------
    [2][0] | [2][1] | [2][2]
         """)

def output():                                                                                                                               #function to give out$
   print(a[0][0],' | ',a[0][1],' | ',a[0][2])                                                                                               #cordinates

   print("---|-----|---")

   print(a[1][0],' | ',a[1][1],' | ',a[1][2])

   print("---|-----|---")

   print(a[2][0],' | ',a[2][1],' | ',a[2][2])


def player1():
   i,j=4,4
   try:
      i,j=[int(x) for x in input("Player1:Enter cordinates:").split()]
   except ValueError:
      print("INVALID FORMAT")
   if i not in [0,1,2] or j not in [0,1,2]:
       print("Invalid input")
       player1()
   elif a[i][j]=='.':
       a[i][j]='X'
   elif a[i][j]!='.':
       print("CHEAT ALERT!!:do not attemp to overwrite ")
       player1()


def auto():
  i=random.choice([0,1,2])
  j=random.choice([0,1,2])
  if a[i][j]=='.':
     a[i][j]='O'
  else:
     auto()

output()
while True:
    player1()
   #checkp1()
    for r in range(3):
        flag=0
        if a[r][0]==a[r][1]==a[r][2]!='.':                     #same row condition
           flag=1
           break
        elif a[0][r]==a[1][r]==a[2][r]!='.':
           flag=1
           break
    if flag==1:
        print("Player 1 wins!!!!")
        break
    elif a[0][0]==a[1][1]==a[2][2]!='.':
        print("Player 1 wins!!!!")
        break
    elif a[0][2]==a[1][1]==a[2][0]!='.':
        print("Player 1 wins!!!!")
        break

    auto()
    output()
   #check computer's win
    for r in range(3):
        flag=0
        if a[r][0]==a[r][1]==a[r][2]!='.':                     #same row condition
           flag=1
           break
        elif a[0][r]==a[1][r]==a[2][r]!='.':                   #same colomn condition
           flag=1
           break
    if flag==1:                                                #considering condi$
        print("Computer wins!!!!")
        break
    elif a[0][0]==a[1][1]==a[2][2]!='.':                       #slant line condit$
        print("Computer wins!!!!")
        break
    elif a[0][2]==a[1][1]==a[2][0]!='.':                       #slant line condit$
        print("Computer wins!!!!")
        break

