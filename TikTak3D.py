import os

#wwwww

game={'A7': "a7 ", 'A8': "a8 ", 'A9': "a9 ", 
    'A4': "a4 ", 'A5': "a5 ", 'A6': "a6 ",
    'A1': "a1 ", 'A2': "a2 ", 'A3': "a3 ",
    
    'B7': "b7 ", 'B8': "b8 ", 'B9': "b9 ", 
    'B4': "b4 ", 'B5': "b5 ", 'B6': "b6 ",
    'B1': "b1 ", 'B2': "b2 ", 'B3': "b3 ",
    
    'C7': "c7 ", 'C8': "c8 ", 'C9': "c9 ", 
    'C4': "c4 ", 'C5': "c5 ", 'C6': "c6 ",
    'C1': "c1 ", 'C2': "c2 ", 'C3': "c3 "
    }

now_move_player = 1

def print_board(game):

    os.system ("clear")

    print(game.get('A7')+'|', game.get('A8')+'|', game.get('A9'))
    print("___|____|___")
    print(game.get('A4')+'|', game.get('A5')+'|', game.get('A6'))
    print("___|____|___")
    print(game.get('A1')+'|', game.get('A2')+'|', game.get('A3'))
    print("   |    |   ")

    print('           ', game.get('B7')+'|', game.get('B8')+'|', game.get('B9'))
    print('           ', "___|____|___")
    print('           ', game.get('B4')+'|', game.get('B5')+'|', game.get('B6'))
    print('           ', "___|____|___")
    print('           ', game.get('B1')+'|', game.get('B2')+'|', game.get('B3'))
    print('           ',"   |    |   ")

    print('                       ', game.get('C7')+'|', game.get('C8')+'|', game.get('C9'))
    print('                       ', "___|____|___")
    print('                       ', game.get('C4')+'|', game.get('C5')+'|', game.get('C6'))
    print('                       ', "___|____|___")
    print('                       ', game.get('C1')+'|', game.get('C2')+'|', game.get('C3'))
    print('                       ',"   |    |   ")


def player_1_move(game):
    move_p1 = 0

    print("____________             ")
    print('|          |             ')
    print('| Player 1 | Player 2    ')
    print('|__________|             ')

    while move_p1 == 0:
        move_p1 = input('could you select field:')
        
        if move_p1 in game:
            if game[move_p1] == ' X ' or game[move_p1] == ' O ':
                move_p1 = 0
                print("Wrong move")
        else:
            move_p1 = 0
            print('NO')


    game[move_p1]=' X '
    return game

def player_2_move(game):
    move_p1 = 0

    print("           ____________  ")
    print('           |          |  ')
    print('  Player 1 | Player 2 |  ')
    print('           |__________|  ')

    while move_p1 == 0:
        move_p1 = input('could you select field:')
        if game[move_p1] == ' X ' or game[move_p1] == ' O ':
            move_p1 = 0
            print("Wrong move, try again")
    game[move_p1]=' O '
    return game


while True:
    print_board(game)
    if now_move_player == 1:
        player_1_move(game)
        now_move_player = 2
    elif now_move_player == 2:
        player_2_move(game)
        now_move_player = 1
 