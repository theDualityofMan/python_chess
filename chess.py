import tkinter as tk
import os
import shutil
from tkinter import *

try:
    import playsound
except ModuleNotFoundError:
    subprocess.call(['pip', 'install', "playsound"])
    import playsound

try:
    import PIL
except ModuleNotFoundError:
    subprocess.call(['pip', 'install', "pillow"])
    import PIL

    
from playsound import playsound
from PIL import Image, ImageTk

class App:
    pass

global app

app = App()

app.cur_player = 'white'

app.opp_player = 'black'

app.last_piece = {
    
    'black': '',
    'white': ''
    
              }


pieces = {
    'black':{
        
        'pawn_1':{'place': [1,0], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_2':{'place': [1,1], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_3':{'place': [1,2], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_4':{'place': [1,3], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_5':{'place': [1,4], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_6':{'place': [1,5], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_7':{'place': [1,6], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_8':{'place': [1,7], 'dead': False, 'kind': 'pawn', 'jump': True},
        'rook_1':{'place': [0,0], 'dead': False, 'kind': 'rook'},
        'rook_2':{'place': [0,7], 'dead': False, 'kind': 'rook'},
        'knight_1':{'place': [0,1], 'dead': False, 'kind': 'knight'},
        'knight_2':{'place': [0,6], 'dead': False, 'kind': 'knight'},
        'bishop_1':{'place': [0,2], 'dead': False, 'kind': 'bishop'},
        'bishop_2':{'place': [0,5], 'dead': False, 'kind': 'bishop'},
        'king':{'place': [0,4], 'dead': False, 'kind': 'king'},
        'queen':{'place': [0,3], 'dead': False, 'kind': 'queen'}
        
        },
    'white':{
        
        'pawn_1':{'place': [6,0], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_2':{'place': [6,1], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_3':{'place': [6,2], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_4':{'place': [6,3], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_5':{'place': [6,4], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_6':{'place': [6,5], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_7':{'place': [6,6], 'dead': False, 'kind': 'pawn', 'jump': True},
        'pawn_8':{'place': [6,7], 'dead': False, 'kind': 'pawn', 'jump': True},
        'rook_1':{'place': [7,0], 'dead': False, 'kind': 'rook'},
        'rook_2':{'place': [7,7], 'dead': False, 'kind': 'rook'},
        'knight_1':{'place': [7,1], 'dead': False, 'kind': 'knight'},
        'knight_2':{'place': [7,6], 'dead': False, 'kind': 'knight'},
        'bishop_1':{'place':[7,2], 'dead': False, 'kind': 'bishop'},
        'bishop_2':{'place': [7,5], 'dead': False, 'kind': 'bishop'},
        'king':{'place': [7,4], 'dead': False, 'kind': 'king'},
        'queen':{'place': [7,3], 'dead': False, 'kind': 'queen'}

        }


    }


app.disp_text = ''

root= tk.Tk()

img_root = os.getcwd()
def get_img_path(filename: str) -> str:
    return os.path.join(img_root, filename)

img_board = get_img_path("WoodBoard.png")
img_path = get_img_path("BishopBlack.png")
img_path2 = get_img_path("BishopBlack.png")
img_path3 = get_img_path("WhiteKnight.png")
img_path4 = get_img_path("KnightBlack.png")
img_path5 = get_img_path("WhitePawn.png")
img_path6 = get_img_path("PawnBlack.png")
img_path7 = get_img_path("KingBlack.png")
img_path8 = get_img_path("WhiteKing.png")
img_path9 = get_img_path("QueenBlack.png")
img_path10 = get_img_path("WhiteQueen.png")
img_path11= get_img_path("WhiteBishop.png")
img_path12= get_img_path("WhiteRook.png")
img_path13= get_img_path("RookBlack.png")

img = PhotoImage(file=img_board)
img1 = PhotoImage(file=img_path)
img2 = PhotoImage(file=img_path2)
img3 = PhotoImage(file=img_path3)
img4 = PhotoImage(file=img_path4)
img5 = PhotoImage(file=img_path5)
img6 = PhotoImage(file=img_path6)
img7 = PhotoImage(file=img_path7)
img8 = PhotoImage(file=img_path8)
img9 = PhotoImage(file=img_path9)
img10= PhotoImage(file=img_path10)
img11 = PhotoImage(file=img_path11)
img12 = PhotoImage(file=img_path12)
img13 = PhotoImage(file=img_path13)

app.state = '1click'


def click(event):

    """ Checks whether the user clicks, and inputs the mouse coordinates for the piece coordinates """

    global app

    if (86 <= event.x <= 657) and (88 <= event.y <= 653):
        
        x = event.x - 86
        y = event.y - 88

        odd_black = ((y // 70) % 2) and not ((x // 70) % 2)
        even_black = not ((y // 70) % 2) and ((x // 70) % 2)

        if app.state == '1click':

            app.o_coords = [(event.y-88)//71, (event.x-86)//71]

            for piece in pieces[app.cur_player]:

                if pieces[app.cur_player][piece]['place'][0] == int(app.o_coords[0]) and pieces[app.cur_player][piece]['place'][1] == int(app.o_coords[1]) and pieces[app.cur_player][piece]['dead'] == False:
                    
                    app.state = '2click'

                    app.disp_text = app.cur_player + ' ' + pieces[app.cur_player][piece]['kind'] + ' at (' + str(app.o_coords[1]) + ', ' + str(app.o_coords[0]) + ')'

                    break

                elif pieces[app.cur_player][piece]['place'][0] != int(app.o_coords[0]) and pieces[app.cur_player][piece]['place'][1] != int(app.o_coords[1]) and piece == 'queen':

                    app.disp_text = ' You have either selected         \nan enemy piece or an         \nempty point. Please try again.    '

                    break

            draw_board()

        elif app.state == '2click':

            app.t_coords = [(event.y-88)//71, (event.x-86)//71]

            app.state = '1click'

            move()

            draw_board()

            

def move():

    """ Updates the pieces' coordinates on the board """

    global app
        
    cmd_select = app.o_coords

    cmd_move = app.t_coords

    if app.cur_player == 'white':
                
        app.opp_player = 'black'
                
    else:
                
        app.opp_player = 'white'


    data = move_piece(int(cmd_select[0]), int(cmd_select[1]), int(cmd_move[0]), int(cmd_move[1]), app.cur_player)

    if data != 0 and data != None and data != 'no':

        playsound('C:/Users/dmmah_qwkdxlj/Documents/compsci_scripts/monke/Test/351518__mh2o__chess-move-on-alabaster.wav')

        app.disp_text += '\nmoved to (' + str(data[2]) + ', ' + str(data[1]) + ')          '

        app.disp_text += '\n' +  f'{app.opp_player}\'s turn !          '

        if check():

            app.disp_text = app.opp_player + ' is in check!  '

        if checkmate():

            app.disp_text = app.opp_player + ' is in \n checkmate! Game over, ' + app.cur_player + ' wins! '

            app.game_won = True

        app.cur_player = app.opp_player

    elif data == 'no':

            app.disp_text = ' Your king is in check! Try again. '


    else:

        app.disp_text = '    Invalid move. Try again! \n                    \n                    '




canvas = tk.Canvas(root, width = 1000, height = 800)
canvas.pack()

def draw_board():

    """ Draws the board with all the pieces and text """
    
    global app
    
    canvas.create_image(22, 22, anchor = NW, image=img)

    label = Label(root, text = app.disp_text, font='impact', width = 800, height = 800,anchor = NW).place(x=730,y=400)


    

    for i in range (0,8):

        canvas.create_text(60, 115 + i * 73, text=str(i), font='impact')

        canvas.create_text(115 + i * 73, 60, text=str(i), font='impact')

        



    

    for players in pieces:
        
        for piece in pieces[players]:

            if not pieces[players][piece]['dead']:

                if players == 'white':

                    if piece == 'pawn_1':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img5)
                    
                    if piece == 'pawn_2':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img5)

                    if piece == 'pawn_3':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img5)

                    if piece == 'pawn_4':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img5)

                    if piece == 'pawn_5':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img5)

                    if piece == 'pawn_6':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img5)

                    if piece == 'pawn_7':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img5)

                    if piece == 'pawn_8':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img5)

                    if piece == 'rook_1':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img12)

                    if piece == 'rook_2':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img12)

                    if piece == 'knight_1':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img3)

                    if piece == 'knight_2':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img3)

                    if piece == 'bishop_1':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img11)

                    if piece == 'bishop_2':

                         canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img11)
                    
                    if piece == 'queen':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img10)

                    if piece == 'king':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img8)


                if players == 'black':

                    if piece == 'pawn_1':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img6)
                    
                    if piece == 'pawn_2':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img6)

                    if piece == 'pawn_3':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img6)

                    if piece == 'pawn_4':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img6)

                    if piece == 'pawn_5':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img6)

                    if piece == 'pawn_6':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img6)

                    if piece == 'pawn_7':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img6)

                    if piece == 'pawn_8':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img6)

                    if piece == 'rook_1':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img13)

                    if piece == 'rook_2':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img13)

                    if piece == 'knight_1':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img4)

                    if piece == 'knight_2':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img4)

                    if piece == 'bishop_1':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img2)

                    if piece == 'bishop_2':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img2)
                    
                    if piece == 'queen':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img9)

                    if piece == 'king':

                        canvas.create_image((pieces[players][piece]['place'][1] * 70) + 95, (pieces[players][piece]['place'][0] * 70) + 95, anchor=NW, image=img7)


        
    root.bind('<Button-1>', click) 

    root.mainloop()




def on_opp(new_y: int, new_x: int) -> str:

    """ Return the piece that is being attacked """


    for piece in pieces[app.cur_player]:

        for o_piece in pieces[app.opp_player]:

            if [new_y, new_x] == pieces[app.opp_player][o_piece]['place']:

                return o_piece


def attack(piece: str, prev_y: int, prev_x: int, new_y: int, new_x: int) -> bool:

    """ Checks whether a piece attacks another piece """

    for thing in pieces[app.opp_player]:

        if new_y == pieces[app.opp_player][thing]['place'][0] and new_x == pieces[app.opp_player][thing]['place'][1]:

            if piece != 'pawn':

                return True

            else:

                if app.cur_player == 'black':

                    if new_y - prev_y == 1 and abs(new_x - prev_x) == 1:

                        return True
                    
                    else:

                        return False


                elif app.cur_player == 'white':

                    if new_y - prev_y == -1 and abs(new_x - prev_x) == 1:

                        return True
                    
                    else:

                        return False

                    

        elif thing == 'queen':

            return False




def does_collide(player: str, piece: str, prev_y: int, prev_x: int, new_y: int, new_x: int) -> bool:

    """ Checks collisions between both colors of pieces """

    global app

    if player == 'white':

        opp_player = 'black'

    else:

        opp_player = 'white'

    for color in pieces:

        for candidate in pieces[color]:

            if color == player:

                if pieces[color][candidate]['dead'] == False:

                    if piece == 'pawn':

                        if pieces[color][candidate]['place'][0] == new_y and pieces[color][candidate]['place'][1] == new_x:

                            return True

                    elif piece == 'rook':

                        if    ((new_x >= pieces[color][candidate]['place'][1] and prev_x < pieces[color][candidate]['place'][1] and new_y == pieces[color][candidate]['place'][0])
                                    or (new_x <= pieces[color][candidate]['place'][1] and prev_x > pieces[color][candidate]['place'][1] and new_y == pieces[color][candidate]['place'][0])
                                    or (new_y >= pieces[color][candidate]['place'][0] and prev_y < pieces[color][candidate]['place'][0] and new_x == pieces[color][candidate]['place'][1])
                                    or (new_y <= pieces[color][candidate]['place'][0] and prev_y > pieces[color][candidate]['place'][0] and new_x == pieces[color][candidate]['place'][1])):


                            return True

                    elif piece == 'knight':

                        if pieces[color][candidate]['place'][0] == new_y and pieces[color][candidate]['place'][1] == new_x:

                            return True

                    elif piece == 'bishop':

                        for i in range(abs(new_y - prev_y)):

                            if prev_y < new_y and prev_x < new_x:
                                
                                if (new_y - i == pieces[color][candidate]['place'][0] and new_x - i == pieces[color][candidate]['place'][1]):
                                    
                                    return True

                            elif prev_y < new_y and prev_x > new_x:

                                if (new_y - i == pieces[color][candidate]['place'][0] and new_x + i == pieces[color][candidate]['place'][1]):

                                    return True
                                
                            elif prev_y > new_y and prev_x < new_x:

                                if (new_y + i == pieces[color][candidate]['place'][0] and new_x - i == pieces[color][candidate]['place'][1]):

                                    return True

                            elif prev_y > new_y and prev_x > new_x:

                                if (new_y + i == pieces[color][candidate]['place'][0] and new_x + i == pieces[color][candidate]['place'][1]):

                                    return True
   

                    elif piece == 'queen':

                        for i in range(abs(new_y - prev_y)):

                            if prev_y < new_y and prev_x < new_x:
                                
                                if (new_y - i == pieces[color][candidate]['place'][0] and new_x - i == pieces[color][candidate]['place'][1]):
                                    
                                    return True



                            elif prev_y < new_y and prev_x > new_x:
                                
                                if (new_y - i == pieces[color][candidate]['place'][0] and new_x + i == pieces[color][candidate]['place'][1]):

                                    return True

                                
                            elif prev_y > new_y and prev_x < new_x:
                                
                                if (new_y + i == pieces[color][candidate]['place'][0] and new_x - i == pieces[color][candidate]['place'][1]):

                                    return True

                            elif prev_y > new_y and prev_x > new_x:

                                if (new_y + i == pieces[color][candidate]['place'][0] and new_x + i == pieces[color][candidate]['place'][1]):

                                    return True
                                


                        if    ((new_x >= pieces[color][candidate]['place'][1] and prev_x < pieces[color][candidate]['place'][1] and new_y == prev_y and new_y == pieces[color][candidate]['place'][0])
                                    or (new_x <= pieces[color][candidate]['place'][1] and prev_x > pieces[color][candidate]['place'][1] and new_y == prev_y and new_y == pieces[color][candidate]['place'][0])
                                    or (new_y >= pieces[color][candidate]['place'][0] and prev_y < pieces[color][candidate]['place'][0] and new_x == prev_x and new_x == pieces[color][candidate]['place'][1])
                                    or (new_y <= pieces[color][candidate]['place'][0] and prev_y > pieces[color][candidate]['place'][0] and new_x == prev_x and new_x == pieces[color][candidate]['place'][1])):

                            return True
                        

                            
                        

                    elif piece == 'king':

                        if pieces[color][candidate]['place'][0] == new_y and pieces[color][candidate]['place'][1] == new_x:

                            return True





                        

            if color == opp_player:

                if pieces[color][candidate]['dead'] == False:

                    if piece == 'pawn' and new_y != prev_y and prev_x == prev_x and new_y == pieces[color][candidate]['place'][0] and new_x == pieces[color][candidate]['place'][1] :

                        return True

                    if piece == 'rook':

                        if    ((new_x > pieces[color][candidate]['place'][1] and prev_x < pieces[color][candidate]['place'][1] and new_y == pieces[color][candidate]['place'][0])
                                    or (new_x < pieces[color][candidate]['place'][1] and prev_x > pieces[color][candidate]['place'][1] and new_y == pieces[color][candidate]['place'][0])
                                    or (new_y > pieces[color][candidate]['place'][0] and prev_y < pieces[color][candidate]['place'][0] and new_x == pieces[color][candidate]['place'][1])
                                    or (new_y < pieces[color][candidate]['place'][0] and prev_y > pieces[color][candidate]['place'][0] and new_x == pieces[color][candidate]['place'][1])):


                            return True

                    elif piece == 'bishop':

                        for i in range(abs(new_y - prev_y-1)):

                            if prev_y < new_y and prev_x < new_x:

                                if (new_y - i - 1 == pieces[color][candidate]['place'][0] and new_x - i - 1  == pieces[color][candidate]['place'][1]):
                                    
                                    return True

                            elif prev_y < new_y and prev_x > new_x:

                                if (new_y - i - 1 == pieces[color][candidate]['place'][0] and new_x + i + 1 == pieces[color][candidate]['place'][1]):

                                    return True
                                
                            elif prev_y > new_y and prev_x < new_x:

                                if (new_y + i + 1  == pieces[color][candidate]['place'][0] and new_x - i - 1 == pieces[color][candidate]['place'][1]):
                                    
                                    return True

                            elif prev_y > new_y and prev_x > new_x:

                                if (new_y + i + 1 == pieces[color][candidate]['place'][0] and new_x + i + 1 == pieces[color][candidate]['place'][1]):

                                    return True

                        

                    elif piece == 'queen':

                        for i in range(abs(new_y - prev_y)):

                            if prev_y < new_y and prev_x < new_x:
                                
                                if (new_y - i - 1 == pieces[color][candidate]['place'][0] and new_x - i - 1  == pieces[color][candidate]['place'][1]):
                                    
                                    return True

                            elif prev_y < new_y and prev_x > new_x:

                                if (new_y - i - 1 == pieces[color][candidate]['place'][0] and new_x + i + 1 == pieces[color][candidate]['place'][1]):

                                    return True
                                
                            elif prev_y > new_y and prev_x < new_x:

                                if (new_y + i + 1  == pieces[color][candidate]['place'][0] and new_x - i - 1 == pieces[color][candidate]['place'][1]):

                                    return True

                            elif prev_y > new_y and prev_x > new_x:

                                if (new_y + i + 1 == pieces[color][candidate]['place'][0] and new_x + i + 1 == pieces[color][candidate]['place'][1]):

                                    return True

                        if    ((new_x > pieces[color][candidate]['place'][1] and prev_x < pieces[color][candidate]['place'][1] and new_y == prev_y and new_y == pieces[color][candidate]['place'][0])
                                    or (new_x < pieces[color][candidate]['place'][1] and prev_x > pieces[color][candidate]['place'][1] and new_y == prev_y and new_y == pieces[color][candidate]['place'][0])
                                    or (new_y > pieces[color][candidate]['place'][0] and prev_y < pieces[color][candidate]['place'][0] and new_x == prev_x and new_x == pieces[color][candidate]['place'][1])
                                    or (new_y < pieces[color][candidate]['place'][0] and prev_y > pieces[color][candidate]['place'][0] and new_x == prev_x and new_x == pieces[color][candidate]['place'][1])):

                            return True


    return False



                
    

    
def piece_limits(player: str, piece: str, prev_y: int, prev_x: int, new_y: int, new_x: int) -> bool:

    """ Defines the pieces' limits and checks whether they are being met """

    global app

    if new_x > 7 or new_y > 7 or new_x < 0 or new_y < 0:

        return False

    elif piece == 'pawn':

        for thing in pieces[player]:

            if pieces[player][thing]['kind'] == piece:

                if pieces[player][thing]['place'][0] == prev_y and pieces[player][thing]['place'][1] == prev_x:

                    if pieces[player][thing]['jump']:

                        if app.cur_player == 'black':

                            if (new_y - prev_y) == 2 and (new_y - prev_y) > 0  and new_x == prev_x:
                            
                                pieces[player][thing]['jump'] = False

                                return True

                            elif (new_y - prev_y) == 1 and (new_y - prev_y) > 0  and new_x == prev_x:

                                return True

                            else:

                                return False

                        elif app.cur_player == 'white':

                            if (new_y - prev_y) == -2 and (new_y - prev_y) < 0  and new_x == prev_x:
                            
                                pieces[player][thing]['jump'] = False

                                return True

                            elif (new_y - prev_y) == -1 and (new_y - prev_y) < 0  and new_x == prev_x:

                                return True

                            else:

                                return False
                        
                    elif pieces[player][thing]['jump'] == False:

                        if app.cur_player == 'black':

                            if (new_y - prev_y) == 1 and (new_y - prev_y) > 0  and new_x == prev_x:

                                return True

                            else:

                                return False

                        elif app.cur_player == 'white':

                            if (new_y - prev_y) == -1 and (new_y - prev_y) < 0  and new_x == prev_x:

                                return True

                            else:

                                return False             

                    else:

                        for o_piece in pieces[app.opp_player]:
                            

                            if (app.cur_player == 'black' and (new_y - prev_y) == 1 and new_x == prev_x and new_y == pieces[app.opp_player][o_piece]['place'][0] and
                            new_x == pieces[app.opp_player][o_piece]['place'][1]):
                                
                                return True

                            elif (app.cur_player == 'black' and (new_y - prev_y) == -1 and new_x == prev_x and new_y == pieces[app.opp_player][o_piece]['place'][0] and
                            new_x == pieces[app.opp_player][o_piece]['place'][1]):
                                
                                return True

                        return False
        
        

    elif piece == 'rook':

        if prev_x == new_x or prev_y == new_y:

            return True

        else:

            return False

    elif piece == 'knight':

        if ((abs(new_x - prev_x) == 2) and (abs(new_y - prev_y) == 1)) or ((abs(new_y - prev_y) == 2) and (abs(new_x - prev_x) == 1)):

            return True

        else:

            return False

    elif piece == 'bishop':

        if abs(new_y - prev_y) == abs(new_x - prev_x):

            return True

        else:

            return False

    elif piece == 'queen':

        if abs(new_y - prev_y) == abs(new_x - prev_x):

            return True

        elif prev_x == new_x or prev_y == new_y:

            return True

        else:

            return False

    elif piece == 'king':

        if ((abs(new_x - prev_x) == 1 and abs(new_y - prev_y) == 1)) or (abs(new_y - prev_y) == 1 and abs(new_x - prev_x) == 0) or (abs(new_x - prev_x) == 1 and abs(new_y - prev_y) == 0):

            return True
                
        else:

            return False


            
    
def move_piece(place_y: int, place_x: int, new_y: int, new_x: int, player: str) -> int:

    """ Updates the dictionary based on collisions and piece limits """

    global app
    
    for piece in pieces[player]:
        
        if pieces[player][piece]['place'][0] == place_y and pieces[player][piece]['place'][1] == place_x and pieces[player][piece]['dead'] == False:
                
                if piece_limits(player, pieces[player][piece]['kind'], place_y, place_x, new_y, new_x) or (pieces[player][piece]['kind'] == 'pawn' and attack('pawn', place_y, place_x, new_y, new_x)):

                    if pieces[player][piece]['kind'] != 'pawn' and attack(pieces[player][piece]['kind'], place_y, place_x, new_y, new_x) == False and does_collide(app.cur_player,pieces[player][piece]['kind'], place_y, place_x, new_y, new_x) == False:

                        pieces[player][piece]['place'][0] = new_y
                
                        pieces[player][piece]['place'][1] = new_x

                        if move_into_check():

                            pieces[player][piece]['place'][0] = place_y
                
                            pieces[player][piece]['place'][1] = place_x

                            return 'no'

                        app.last_piece[player] = piece

                        return pieces[player][piece]['kind'], pieces[player][piece]['place'][0], pieces[player][piece]['place'][1]
                    
                    if (pieces[player][piece]['kind'] == 'pawn' and attack(pieces[player][piece]['kind'], place_y, place_x, new_y, new_x) == False
                        
                        and does_collide(app.cur_player,pieces[player][piece]['kind'], place_y, place_x, new_y, new_x) == False):

                        pieces[player][piece]['place'][0] = new_y
                
                        pieces[player][piece]['place'][1] = new_x

                        if move_into_check():

                            pieces[player][piece]['place'][0] = place_y
                
                            pieces[player][piece]['place'][1] = place_x

                            return 'no'

                        app.last_piece[player] = piece

                        return pieces[player][piece]['kind'], pieces[player][piece]['place'][0], pieces[player][piece]['place'][1]

                    elif pieces[player][piece]['kind'] == 'pawn' and attack('pawn', place_y, place_x, new_y, new_x):

                        pieces[app.opp_player][on_opp(new_y, new_x)]['dead'] = True

                        pieces[player][piece]['place'][0] = new_y
                
                        pieces[player][piece]['place'][1] = new_x

                        if move_into_check():

                            pieces[player][piece]['place'][0] = place_y
                
                            pieces[player][piece]['place'][1] = place_x

                            return 'no'

                        app.last_piece[player] = piece

                        return pieces[player][piece]['kind'], pieces[player][piece]['place'][0], pieces[player][piece]['place'][1]

                    elif attack(pieces[player][piece]['kind'], place_y, place_x, new_y, new_x) and does_collide(app.cur_player,pieces[player][piece]['kind'], place_y, place_x, new_y, new_x) == False:

                        pieces[app.opp_player][on_opp(new_y, new_x)]['dead'] = True

                        pieces[player][piece]['place'][0] = new_y
                
                        pieces[player][piece]['place'][1] = new_x

                        if move_into_check():

                            pieces[player][piece]['place'][0] = place_y
                
                            pieces[player][piece]['place'][1] = place_x

                            return 'no'

                        app.last_piece[player] = piece

                        return pieces[player][piece]['kind'], pieces[player][piece]['place'][0], pieces[player][piece]['place'][1]

                    else:

                        return 0

                else:

                        return 0


app.check_piece = {

    'black': '',
    'white': ''

    }


def move_into_check() -> bool:

    global app

    for piece in pieces[app.opp_player]:


        if ((does_collide(app.opp_player, pieces[app.opp_player][piece]['kind'], pieces[app.opp_player][piece]['place'][0],
                          
            pieces[app.opp_player][piece]['place'][1], pieces[app.cur_player]['king']['place'][0],
                          
            pieces[app.cur_player]['king']['place'][1]) == False)
            
            and piece_limits(app.opp_player,pieces[app.opp_player][piece]['kind'], pieces[app.opp_player][piece]['place'][0],
                             
            pieces[app.opp_player][piece]['place'][1],
                             
            pieces[app.cur_player]['king']['place'][0], pieces[app.cur_player]['king']['place'][1])

            and pieces[app.opp_player][piece]['dead'] == False):

            return True

    return False


def check() -> bool:

    global app

    """ Determines whether king is in check or not """

    for piece in pieces[app.cur_player]:

        if ((does_collide(app.cur_player,pieces[app.cur_player][piece]['kind'], pieces[app.cur_player][piece]['place'][0],
                          
            pieces[app.cur_player][piece]['place'][1], pieces[app.opp_player]['king']['place'][0],
                          
            pieces[app.opp_player]['king']['place'][1]) == False)
            
            and piece_limits(app.cur_player,pieces[app.cur_player][piece]['kind'], pieces[app.cur_player][piece]['place'][0],
                             
            pieces[app.cur_player][piece]['place'][1],
                             
            pieces[app.opp_player]['king']['place'][0], pieces[app.opp_player]['king']['place'][1])

            and pieces[app.cur_player][piece]['dead'] == False):
            

            app.check_piece[app.cur_player] = [piece]
            

            if pieces[app.cur_player][piece]['kind'] == 'rook':

                if pieces[app.opp_player]['king']['place'][1] != pieces[app.cur_player][piece]['place'][1]:

                    app.check_piece[app.cur_player] = [piece, 'y']

                elif pieces[app.opp_player]['king']['place'][0] != pieces[app.cur_player][piece]['place'][0]:

                    app.check_piece[app.cur_player] = [piece, 'x']
                    

            if pieces[app.cur_player][piece]['kind'] == 'bishop':

                if (pieces[app.cur_player][piece]['place'][0] < pieces[app.opp_player]['king']['place'][0] and
                    pieces[app.cur_player][piece]['place'][1] < pieces[app.opp_player]['king']['place'][1]):

                    app.check_piece[app.cur_player] = [piece, 't_l']

                elif (pieces[app.cur_player][piece]['place'][0] < pieces[app.opp_player]['king']['place'][0] and
                    pieces[app.cur_player][piece]['place'][1] > pieces[app.opp_player]['king']['place'][1]):

                    app.check_piece[app.cur_player] = [piece, 't_r']

                                
                elif (pieces[app.cur_player][piece]['place'][0] > pieces[app.opp_player]['king']['place'][0] and
                    pieces[app.cur_player][piece]['place'][1] < pieces[app.opp_player]['king']['place'][1]):

                    app.check_piece[app.cur_player] = [piece, 'b_l']


                elif (pieces[app.cur_player][piece]['place'][0] > pieces[app.opp_player]['king']['place'][0] and
                    pieces[app.cur_player][piece]['place'][1] > pieces[app.opp_player]['king']['place'][1]):

                    app.check_piece[app.cur_player] = [piece, 'b_r']


            if pieces[app.cur_player][piece]['kind'] == 'queen':

                if (pieces[app.opp_player]['king']['place'][1] != pieces[app.cur_player][piece]['place'][1] and
                pieces[app.opp_player]['king']['place'][0] == pieces[app.cur_player][piece]['place'][0]):

                    app.check_piece[app.cur_player] = [piece, 'y']

                elif (pieces[app.opp_player]['king']['place'][0] != pieces[app.cur_player][piece]['place'][0] and
                      pieces[app.opp_player]['king']['place'][1] == pieces[app.cur_player][piece]['place'][1]):

                    app.check_piece[app.cur_player] = [piece, 'x']

                elif (pieces[app.cur_player][piece]['place'][0] < pieces[app.opp_player]['king']['place'][0] and
                    pieces[app.cur_player][piece]['place'][1] < pieces[app.opp_player]['king']['place'][1]):

                    app.check_piece[app.cur_player] = [piece, 't_l']

                elif (pieces[app.cur_player][piece]['place'][0] < pieces[app.opp_player]['king']['place'][0] and
                    pieces[app.cur_player][piece]['place'][1] > pieces[app.opp_player]['king']['place'][1]):

                    app.check_piece[app.cur_player] = [piece, 't_r']

                                
                elif (pieces[app.cur_player][piece]['place'][0] > pieces[app.opp_player]['king']['place'][0] and
                    pieces[app.cur_player][piece]['place'][1] < pieces[app.opp_player]['king']['place'][1]):

                    app.check_piece[app.cur_player] = [piece, 'b_l']


                elif (pieces[app.cur_player][piece]['place'][0] > pieces[app.opp_player]['king']['place'][0] and
                    pieces[app.cur_player][piece]['place'][1] > pieces[app.opp_player]['king']['place'][1]):

                    app.check_piece[app.cur_player] = [piece, 'b_r']

                

                
            return True   

    return False
        

def get_piece_at_place(row: int, col: int)-> str:
    for player in pieces:
        for piece in pieces[player]:
            if pieces[player][piece]['place'] == [row, col]:
                return piece

def check_piece_out() -> bool:

    global app

    for o_piece in pieces[app.opp_player]:

        if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'], pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],
                         
        pieces[app.cur_player][app.last_piece[app.cur_player]]['place'][0], pieces[app.cur_player][app.last_piece[app.cur_player]]['place'][1]) == False
            
        and piece_limits(app.opp_player,pieces[app.opp_player][o_piece]['kind'], pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],
                         
        pieces[app.cur_player][app.last_piece[app.cur_player]]['place'][0], pieces[app.cur_player][app.last_piece[app.cur_player]]['place'][1])
            
        and pieces[app.opp_player][o_piece]['dead'] == False):

            return True

    return False


def block_check() -> bool:

    global app

    for o_piece in pieces[app.opp_player]:
    
        if pieces[app.cur_player][app.check_piece[app.cur_player][0]]['kind'] == 'rook':

            if app.check_piece[app.cur_player][1] == 'y':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][0] - pieces[app.opp_player]['king']['place'][0])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1], i,

                    pieces[app.cur_player][app.check_piece[app.cur_player]]['place'][1]) == False and piece_limits(app.opp_player,pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1], i, pieces[app.cur_player][app.check_piece[app.cur_player]]['place'][1])):

                        return True

            elif app.check_piece[app.cur_player][1] == 'x':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.cur_player][app.check_piece[app.cur_player]]['place'][0], i) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1], pieces[app.cur_player][app.check_piece[app.cur_player]]['place'][0], i)):

                        return True
                    
                                

        elif pieces[app.cur_player][app.check_piece[app.cur_player][0]]['kind'] == 'bishop':

            if app.check_piece[app.cur_player][1] == 't_l':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.opp_player]['king']['place'][0] - i, pieces[app.opp_player]['king']['place'][1] - i ) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],pieces[app.opp_player]['king']['place'][0] - i,

                    pieces[app.opp_player]['king']['place'][1] - i )):

                        return True

            elif app.check_piece[app.cur_player][1] == 't_r':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.opp_player]['king']['place'][0] - i, pieces[app.opp_player]['king']['place'][1] + i ) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],pieces[app.opp_player]['king']['place'][0] - i,

                    pieces[app.opp_player]['king']['place'][1] + i )):

                        return True

            elif app.check_piece[app.cur_player][1] == 'b_l':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.opp_player]['king']['place'][0] + i, pieces[app.opp_player]['king']['place'][1] - i ) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],pieces[app.opp_player]['king']['place'][0] + i,

                    pieces[app.opp_player]['king']['place'][1] - i )):

                        return True

            elif app.check_piece[app.cur_player][1] == 'b_r':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.opp_player]['king']['place'][0] + i, pieces[app.opp_player]['king']['place'][1] + i ) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],pieces[app.opp_player]['king']['place'][0] + i,

                    pieces[app.opp_player]['king']['place'][1] + i )):

                        return True


            
        elif pieces[app.cur_player][app.check_piece[app.cur_player][0]]['kind'] == 'queen':

            if app.check_piece[app.cur_player][1] == 'y':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][0] - pieces[app.opp_player]['king']['place'][0])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1], i,

                    pieces[app.cur_player][app.check_piece[app.cur_player]]['place'][1]) == False and piece_limits(app.opp_player,pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1], i, pieces[app.cur_player][app.check_piece[app.cur_player]]['place'][1])):

                        return True

            elif app.check_piece[app.cur_player][1] == 'x':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.cur_player][app.check_piece[app.cur_player]]['place'][0], i) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1], pieces[app.cur_player][app.check_piece[app.cur_player]]['place'][0], i)):

                        return True

            elif app.check_piece[app.cur_player][1] == 't_l':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.opp_player]['king']['place'][0] - i, pieces[app.opp_player]['king']['place'][1] - i ) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],pieces[app.opp_player]['king']['place'][0] - i,

                    pieces[app.opp_player]['king']['place'][1] - i )):

                        return True

            elif app.check_piece[app.cur_player][1] == 't_r':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.opp_player]['king']['place'][0] - i, pieces[app.opp_player]['king']['place'][1] + i ) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],pieces[app.opp_player]['king']['place'][0] - i,

                    pieces[app.opp_player]['king']['place'][1] + i )):

                        return True

            elif app.check_piece[app.cur_player][1] == 'b_l':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.opp_player]['king']['place'][0] + i, pieces[app.opp_player]['king']['place'][1] - i ) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],pieces[app.opp_player]['king']['place'][0] + i,

                    pieces[app.opp_player]['king']['place'][1] - i )):

                        return True

            elif app.check_piece[app.cur_player][1] == 'b_r':

                for i in range(abs(pieces[app.cur_player][app.check_piece[app.cur_player][0]]['place'][1] - pieces[app.opp_player]['king']['place'][1])):

                    if (does_collide(app.opp_player, pieces[app.opp_player][o_piece]['kind'],pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],

                    pieces[app.opp_player]['king']['place'][0] + i, pieces[app.opp_player]['king']['place'][1] + i ) == False and piece_limits(app.opp_player, pieces[app.opp_player][o_piece]['kind'],

                    pieces[app.opp_player][o_piece]['place'][0], pieces[app.opp_player][o_piece]['place'][1],pieces[app.opp_player]['king']['place'][0] + i,

                    pieces[app.opp_player]['king']['place'][1] + i )):

                        return True

    return False
            
def checkmate() -> bool:

    """ Determines whether the king is in checkmate or not """

    checkm_pieces = {}

    if check() and not block_check():

        if not check_piece_out():

            for j in range(pieces[app.opp_player]['king']['place'][0] - 1, pieces[app.opp_player]['king']['place'][0] + 2):

                    for i in range(pieces[app.opp_player]['king']['place'][1] - 1, pieces[app.opp_player]['king']['place'][1] + 2):

                        if 0 <= j <= 7 and 0 <= i <= 7:
                            
                            piece = get_piece_at_place(j, i)

                            if not piece:
                    
                                for c_piece in pieces[app.cur_player]:

                                    if (does_collide(app.cur_player, pieces[app.cur_player][c_piece]['kind'], pieces[app.cur_player][c_piece]['place'][0], pieces[app.cur_player][c_piece]['place'][1], j, i) == False
                                        and piece_limits(app.cur_player,pieces[app.cur_player][c_piece]['kind'], pieces[app.cur_player][c_piece]['place'][0],
                                        pieces[app.cur_player][c_piece]['place'][1], j, i)
                                        and pieces[app.cur_player][c_piece]['dead'] == False): 

                                        checkm_pieces[(j,i)] = True

                                        break

                                    elif (pieces[app.cur_player][c_piece]['kind'] == 'pawn' and attack('pawn',
                                        pieces[app.cur_player][c_piece]['place'][0],pieces[app.cur_player][piece]['place'][1], j, i)
                                        and pieces[app.cur_player][c_piece]['dead'] == False):

                                        checkm_pieces[(j,i)] = True

                                        break

                                    else:

                                        checkm_pieces[(j,i)] = False

    for spaces in checkm_pieces:

        if checkm_pieces[spaces] == False:

            return False

    if len(checkm_pieces) > 0:
        
        return True

            
                                    
        

app.game_won = False

draw_board()



