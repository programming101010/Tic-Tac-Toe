#--------------------------------TIC TAC TOE Game with Computer----------------------------
import random
lum=[]#list of user moves
lcm=[5]#list of computer moves





Won=['no winner']#for winner board

Computer='Computer Won The Match'
User='User Won The Match'
Draw_match="Draw Match"

board=[[1,2,3],[4,'X',6],[7,8,9]]

free_fields=[1,2,3,4,6,7,8,9]

#________________________________________________________________________________________________________


def Board(board):
       print("\n\nRULES OF THE GAME:\n\nComputer chosses ---------> X")
       print("User must have to choose ---> O")
       print("FREE MOVES WILL BE DISPLAYED TO USER\n\n")
       print("computer choose 5")
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
       print("\n\nUser FREE MOVES",free_fields,"\nPlease Choose a number from User FREE MOVES\n")



#__________________________________________________________________________________________________________



def user(board):
  if Won[-1]!=Computer and Won[-1]!=User and Won[-1]!=Draw_match:

    un=int(input('user move: '))
    if un in lum or un in lcm:# preventing user to not select  the number in X and O place
              print('WARNING:--please choose correct number')
              user(board)
    elif un==1:
       board[0][0]='O'
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
    elif un==2:
       board[0][1]='O'
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
    elif un==3:
       board[0][2]='O'
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
    elif un==4:
       board[1][0]='O'
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
    elif un==5:
       board[1][1]='O'
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
    elif un==6:
       board[1][2]='O'
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
    elif un==7:
       board[2][0]='O'
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
    elif un==8:
       board[2][1]='O'
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
    elif un==9:
       board[2][2]='O'
       print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
    else:
       print("please choose correct number")
       user(board)
    lum.append(un)#appending every user move to a list to prevent user to not repeat previous again
    if un in free_fields:
       free_fields.remove(un)# we remove user move from the list to display computer free moves 

#_______________________________________________________________________________________________________________




def computer(board):
    if Won[-1]!=Computer and Won[-1]!=User and Won[-1]!=Draw_match:#checking if there is any winner or not if there is winner fucntions wont be called
       print("\nFREE MOVES for computer :- ",free_fields)
       cn=random.choice(free_fields)
       lcm.append(cn)
       print("\ncomputer move is",cn)
       if cn==1:
              board[0][0]='X'
              print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
       elif cn==2:
              board[0][1]='X'
              print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
       elif cn==3:
              board[0][2]='X'
              print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
       elif cn==4:
              board[1][0]='X'
              print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
       elif cn==6:
              board[1][2]='X'
              print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
       elif cn==7:
              board[2][0]='X'
              print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
       elif cn==8:
              board[2][1]='X'
              print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')
       elif cn==9:
              board[2][2]='X'
              print('''+-------+-------+-------+
|       |       |       |
|   '''+str(board[0][0])+'''   |   '''+str(board[0][1])+'''   |   '''+str(board[0][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[1][0])+'''   |   '''+str(board[1][1])+'''   |   '''+str(board[1][2])+'''   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   '''+str(board[2][0])+'''   |   '''+str(board[2][1])+'''   |   '''+str(board[2][2])+'''   |
|       |       |       |
+-------+-------+-------+''')

       if cn in free_fields:
              free_fields.remove(cn)# we remove computer move from the list to display user free moves 
       print('\n\nUser FREE MOVES :- ',free_fields)


#________________________________________________________________________________________________________________________________________



def winner(board):
       if Won[-1]!=Computer and Won[-1]!=User and Won[-1]!=Draw_match:#checking if there is any winner or not if there is winner fucntions wont be called
       #computer horizontal checking
              if board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X':
                     print('Computer won the match')
                     Won.append('Computer Won The Match')
              elif board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X':
                     print('Computer won the match')
                     Won.append('Computer Won The Match')
              elif board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X':
                     print('Computer won the match')
                     Won.append('Computer Won The Match')
       #computer vertical checking
              elif board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X':
                     print('Computer won the match')
                     Won.append('Computer Won The Match')
              elif board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X':
                     print('Computer won the match')
                     Won.append('Computer Won The Match')
              elif board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X':
                     print('Computer won the match')
                     Won.append('Computer Won The Match')
       #computer diagnoal checking
              elif board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X':
                     print('Computer won the match')
                     Won.append('Computer Won The Match')
              elif board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X':
                     print('Computer won the match')
                     Won.append('Computer Won The Match')
       # user checking horizontal
              elif board[0][0]=='O' and board[0][1]=='O' and board[0][2]=='O':
                     print('User won the match')
                     Won.append('User Won The Match')
              elif board[1][0]=='O' and board[1][1]=='O' and board[1][2]=='O':
                     print('User won the match')
                     Won.append('User Won The Match')
              elif board[2][0]=='O' and board[2][1]=='O' and board[2][2]=='O':
                     print('User won the match')
                     Won.append('User Won The Match')
       #user vertical checking
              elif board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O':
                     print('User won the match')
                     Won.append('User Won The Match')
              elif board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O':
                     print('User won the match')
                     Won.append('User Won The Match')
              elif board[0][2]=='O' and board[1][2]=='O' and board[2][2]=='O':
                     print('User won the match')
                     Won.append('User Won The Match')
       #user diagnoal checking
              elif board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O':
                     print('User won the match')
                     Won.append('User Won The Match')
              elif board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O':
                     print('User won the match')
                     Won.append('User Won The Match')

              if free_fields==[] and Won[-1]!=Computer and Won[-1]!=User:#if the list becomes empty before getting a winner this leads to draw match 
                     print("NO MORE MOVES---DRAW MATCH")
                     Won.append("Draw Match")

Board(board)
for i in range(30):
              user(board)
              winner(board)
              computer(board)
              winner(board)
