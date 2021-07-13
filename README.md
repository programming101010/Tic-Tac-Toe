# Tic-Tac-Toe


#--------------------------------TIC TAC TOE Game with Computer----------------------------
import random
user_moves=[5]
computer_moves=[]#here we remove x and o
rn=[5]#list of random number
Won=['no winner']#for winner board

Computer='Computer Won The Match'
User='User Won The Match'


board=[[1,2,3],[4,'X',6],[7,8,9]]


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
       Temp=[1,2,3,4,6,7,8,9]#creating temp list to print the variable after board
       print("\n\nUser FREE MOVES",Temp,"\nPlease Choose a number from User FREE MOVES\n")



#__________________________________________________________________________________________________________




def user(board):
    un=int(input('user move: '))
    if un in user_moves or un in rn:# preventing user to not select  the number in X and O place
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
    user_moves.append(un)#appending every user move to a list to prevent user to not repeat previous again


#_______________________________________________________________________________________________________________



def list_of_free_fields(board):# this fun removes X's and O's from list and gives crt free moves
    for i in range(len(board[0])):
        if board[0][i] in [1,2,3,4,6,7,8,9]:
            computer_moves.append(board[0][i])
        else:
            continue
    for i in range(len(board[1])):
        if board[1][i] in [1,2,3,4,6,7,8,9]:
            computer_moves.append(board[1][i])
        else:
            continue
    for i in range(len(board[2])):
        if board[2][i] in [1,2,3,4,6,7,8,9]:
            computer_moves.append(board[2][i])
        else:
            continue
    print(computer_moves)


#_______________________________________________________________________________________________________________



def computer(board):
       print("\nFREE MOVES for computer :- ",computer_moves)
       B_1=computer_moves.copy()# making another copy bcz to remove computers move from list to show user what are free moves
       cn=random.choice(computer_moves)
       rn.append(cn)
       computer_moves.clear() # clearing the list to avoid previous values to select by computer again
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
       B_1.remove(cn)#to remove computers move from list to show user what are free moves
       if B_1==[]:
              print("NO MORE MOVES---DRAW MATCH")
       print('\n\nUser FREE MOVES :- ',B_1,)


#________________________________________________________________________________________________________________________________________



def winner(board):
       if Won[-1]!=Computer and Won[-1]!=User:
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

Board(board)
for i in range(20):
       if Won[-1]!=Computer and Won[-1]!=User:# checking if there is any winner or not if there is winner fucntions wont be called
              user(board)
              list_of_free_fields(board)
              computer(board)
              winner(board)
