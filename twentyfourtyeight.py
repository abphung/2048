# [0, 1, 2, 3]
# 2 and 3 are the same
# 1 and 3 are the same and 2 is empty
# a = [['a','b','c'],['d','e','f'],['g','h','i']]
# print zip(*zip(*a[::-1])[::-1])
#i = 0
#b = [[2, 4, 0, 4], [2, 4, 4, 4]]
#a = [b, zip(*b[::-1]), zip(*zip(*b[::-1])[::-1]), zip(*zip(*zip(*b[::-1])[::-1])[::-1])][i]
#function should return [0, 2, 4, 8]
#print [_ for _ in [2, 4, 0, 4] if _ != 0]
#print map(lambda row: filter(lambda x: x == 0, row) + filter(lambda x: x != 0, row), a)
#print map(lambda a: [0, a[0], a[1], a[2] + a[3]] if a[2] == a[3] else [0, 0, a[0], a[1] + a[3]] if a[1] == a[3] and a[2] == 0 else [0, 0, 0, a[0] + a[3]] if a[0] == a[3] and a[1] == 0 and a[2] == 0 else a, b)

from pprint import *


#optimizations to make things that should be assigned to a "variable" __import__('random'), unrotated boards?, input_ind
def zero_locs(board):
    return list(filter(lambda x: not board[x[0]][x[1]], list(zip(4*list(range(4)), list(sum(zip(*4*[list(range(4))]), ()))))))

def random_zero(board):
    return __import__('random').choice(zero_locs(board))

def refilled(board):
    return (lambda x: list(map(lambda j: list(map(lambda i: __import__('random').choice(9*[2] + [4]) if (j, i) == (x[0], x[1]) else board[j][i], range(4))), range(4))))(random_zero(board))

def rotated(board, count):
    return rotated(list(map(list, zip(*board[::-1]))), count - 1) if count > 0 else board

def shifted(row):
    return list(filter(lambda i: i, row)) + list(filter(lambda i: not i, row))

def merged(row):
    return row if len(row) <= 1 else [row[0] + row[1]] + merged(row[2:]) + [0] if row[0] == row[1] else [row[0]] + merged(row[1:])

def myprint(board):
    return (list(map(lambda row: print(row), board)), board)[1]

def myprint2(boards):
    list(map(lambda board: myprint(row), boards))

def drawn(board, root):
    return (list(map(lambda i: list(map(lambda j: tk.Label(root, text=str(board[i][j]) if board[i][j] else '', bg='wheat1' if board[i][j] else 'wheat3', relief=tk.RAISED if board[i][j] else tk.GROOVE, height=4, width=5, bd=3).grid(row=i, column=j), range(4))), range(4))) if root.winfo_children() == [] else list(map(lambda i: root.winfo_children()[i].config(text=str(board[int(i/4)][i%4]) if board[int(i/4)][i%4] else '', bg='wheat1' if board[int(i/4)][i%4] else 'wheat3', relief=tk.RAISED if board[int(i/4)][i%4] else tk.GROOVE), range(16))), board)[1]

def mapped(event):
    return {'\uf702':0, '\uf701':1, '\uf703':2, '\uf700':3}[event.char]

def twentyfourtyeight(root, board):
    if not any(map(any, board)):#good
        board = refill_board(board)#good
    draw(board, root)
    rotated_boards = list(map(lambda i: rotate_board(board, i), range(4)))#good
    combined_boards = list(map(lambda board: list(map(lambda row: combine_row(shift_row(row)), board)), rotated_boards))#good
    unrotated_boards = list(map(lambda i: rotate_board(combined_boards[i], 4 - i), range(4)))#good
    if unrotated_boards[1:] == unrotated_boards[:-1]:
        print('gameover')
        return
    else:
        root.bind("<Key>", lambda event: twentyfourtyeight(root, refill_board(unrotated_boards[{'\uf702':0, '\uf701':1, '\uf703':2, '\uf700':3}[event.char]])) if unrotated_boards[{'\uf702':0, '\uf701':1, '\uf703':2, '\uf700':3}[event.char]] != board else twentyfourtyeight(root, board))
    # input_str = input()
    # input_ind = {'a':0, 's':1, 'd':2, 'w':3}[input_str]
    # twentyfourtyeight(refill_board(refill_board(unrotated_boards[input_ind])) if sum(map(lambda x: x.count(0), unrotated_boards[input_ind])) > 1 and __import__('random').choice([True, False]) else refill_board(unrotated_boards[input_ind])) if unrotated_boards[input_ind] != board else twentyfourtyeight(board)

# import tkinter as tk
# import sys
# import random
# root = __import__("tkinter").Tk()
# board = [[2,0,4,4],[2,8,8,4],[2,0,64,4],[2048,0,4,64]]
# tk.Tk()
# __import__("sys").setrecursionlimit(4096)
# root.after(1, twentyfourtyeight, root, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
# __import__("tkinter").mainloop()

# (lambda tk, random, sys: 
#     (lambda root, board: 
#         (lambda refilled, rotated, shifted, merged, drawn, mapped: 
#             (lambda: 
#                 (sys.setrecursionlimit(4096), 
#                 root.after(1, 
#                     lambda func, args: func(func, *args),
#                         lambda twentyfortyeight, root, board: 
#                             (lambda board:
#                                 (lambda boards: 
#                                     print('gameover') if boards[1:] == boards[:-1] else root.bind("<Key>", lambda event: twentyfortyeight(twentyfortyeight, root, refilled(boards[mapped(event)])) if boards[mapped(event)] != board else twentyfortyeight(twentyfortyeight, root, board))
#                                 )(
#                                 list(map(lambda i: rotated(rotated, list(map(lambda board: list(map(lambda row: merged(merged, shifted(row)), board)), list(map(lambda i: rotated(rotated, board, i), range(4)))))[i], 4 - i), range(4)))
#                                 )
#                             )(
#                             drawn(refilled(board) if not any(map(any, board)) else board, root)
#                             ), 
#                         (root, board)
#                 ), 
#                 tk.mainloop()
#                 )
#             )(
#             )
#         )(
#         lambda board: (lambda x: list(map(lambda j: list(map(lambda i: __import__('random').choice([2, 4]) if (j, i) == (x[0], x[1]) else board[j][i], range(4))), range(4))))(__import__('random').choice(list(filter(lambda x: board[x[0]][x[1]] == 0, list(zip(4*list(range(4)), list(sum(zip(*4*[list(range(4))]), ())))))))), 
#         lambda rotate_board, board, count: rotate_board(rotate_board, list(map(list, zip(*board[::-1]))), count - 1) if count > 0 else board, 
#         lambda row: list(filter(lambda i: i != 0, row)) + list(filter(lambda i: i == 0, row)), 
#         lambda combine_row, row: row if len(row) <= 1 else [row[0] + row[1]] + combine_row(combine_row, row[2:]) + [0] if row[0] == row[1] else [row[0]] + combine_row(combine_row, row[1:]), 
#         lambda board, root: (list(map(lambda i: list(map(lambda j: tk.Label(root, text=str(board[i][j]) if board[i][j] else '', bg='wheat1' if board[i][j] else 'wheat3', relief=tk.RAISED if board[i][j] else tk.GROOVE, height=4, width=5, bd=3).grid(row=i, column=j), range(4))), range(4))) if root.winfo_children() == [] else list(map(lambda i: root.winfo_children()[i].config(text=str(board[int(i/4)][i%4]) if board[int(i/4)][i%4] else '', bg='wheat1' if board[int(i/4)][i%4] else 'wheat3', relief=tk.RAISED if board[int(i/4)][i%4] else tk.GROOVE), range(16))), board)[1],
#         lambda event: {'\uf702':0, '\uf701':1, '\uf703':2, '\uf700':3}[event.char]
#         )
#     )(
#     tk.Tk(),
#     [[2,0,4,4],[2,8,8,4],[2,0,64,4],[2048,0,4,64]]
#     )
# )(
# __import__("tkinter"), 
# __import__("random"), 
# __import__("sys")
# )

(lambda tk,random,sys:(lambda root,board:(lambda refilled,rotated,shifted,merged,drawn,mapped:(lambda:(sys.setrecursionlimit(4096),root.after(1,lambda func,args: func(func,*args),lambda twentyfortyeight,root,board: (lambda board:(lambda boards:print('gameover') if boards[1:]==boards[:-1] else root.bind("<Key>",lambda event:twentyfortyeight(twentyfortyeight,root,refilled(boards[mapped(event)])) if boards[mapped(event)]!=board else twentyfortyeight(twentyfortyeight,root,board)))(list(map(lambda i:rotated(rotated, list(map(lambda board:list(map(lambda row:merged(merged,shifted(row)),board)),list(map(lambda i:rotated(rotated,board,i),range(4)))))[i],4-i),range(4)))))(drawn(refilled(board) if not any(map(any,board)) else board,root)),(root, board)),tk.mainloop()))())(lambda board:(lambda x:list(map(lambda j:list(map(lambda i:random.choice([2,4]) if (j,i)==(x[0],x[1]) else board[j][i],range(4))),range(4))))(random.choice(list(filter(lambda x:not board[x[0]][x[1]],list(zip(4*list(range(4)),list(sum(zip(*4*[list(range(4))]),())))))))),lambda rotated,board,count:rotated(rotated, list(map(list,zip(*board[::-1]))),count-1) if count>0 else board,lambda row:list(filter(lambda i:i,row))+list(filter(lambda i:not i,row)),lambda merged,row:row if len(row)<=1 else [row[0]+row[1]]+merged(merged,row[2:])+[0] if row[0]==row[1] else [row[0]]+merged(merged,row[1:]),lambda board,root:(list(map(lambda i:list(map(lambda j:tk.Label(root,text=str(board[i][j]) if board[i][j] else '',bg='wheat1' if board[i][j] else 'wheat3',relief=tk.RAISED if board[i][j] else tk.GROOVE,height=4,width=5,bd=3).grid(row=i,column=j),range(4))),range(4))) if root.winfo_children()==[] else list(map(lambda i:root.winfo_children()[i].config(text=str(board[int(i/4)][i%4]) if board[int(i/4)][i%4] else '',bg='wheat1' if board[int(i/4)][i%4] else 'wheat3',relief=tk.RAISED if board[int(i/4)][i%4] else tk.GROOVE),range(16))),board)[1],lambda event:{'\uf702':0,'\uf701':1,'\uf703':2,'\uf700':3}[event.char]))(tk.Tk(),[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))(__import__("tkinter"),__import__("random"),__import__("sys"))
#twentyfourtyeight(root=root)


#(lambda boards, input_ind: twentyfourtyeight(refill_board(refill_board(boards[input_ind])) if sum(map(lambda x: x.count(0), boards[input_ind])) > 1 and __import__('random').choice([True, False]) else refill_board(boards[input_ind])) if boards[input_ind] != board else twentyfourtyeight(board))(list(map(lambda i: rotate_board(list(map(lambda board: list(map(lambda row: combine_row(shift_row(row)), board)), list(map(lambda i: rotate_board(refill_board(board) if not any(map(any, board)) else board, i), range(4)))))[i], 4 - i), range(4))), {'a':0, 's':1, 'd':2, 'w':3}[input()])
#list(map(lambda i: rotate_board(list(map(lambda board: list(map(lambda row: combine_row(shift_row(row)), board)), list(map(lambda i: rotate_board(refill_board(board) if not any(map(any, board)) else board, i), range(4)))))[i], 4 - i), range(4)))

#(lambda twentyfourtyeight, board: twentyfourtyeight(twentyfourtyeight, board))(lambda twentyfourtyeight, board: (lambda boards, input_ind: twentyfourtyeight(refill_board(refill_board(boards[input_ind])) if sum(map(lambda x: x.count(0), boards[input_ind])) > 1 and __import__('random').choice([True, False]) else refill_board(boards[input_ind])) if boards[input_ind] != board else twentyfourtyeight(board))(list(map(lambda i: rotate_board(list(map(lambda board: list(map(lambda row: combine_row(shift_row(row)), board)), list(map(lambda i: rotate_board(refill_board(board) if not any(map(any, board)) else board, i), range(4)))))[i], 4 - i), range(4))), {'a':0, 's':1, 'd':2, 'w':3}[input()]), [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])




#print(refill_board([[0, 0, 0, 0]]))
#print(combine_row(shift_row([2,0,4,4])))
#board = [[2,0,4,4],[2,8,8,4],[2,0,64,4],[2048,0,4,64]]
#print(rotate_board(board, 3))
#twentyfourtyeight()
#print(rotate_board(board, 1))

#myprint(board)

# pprint(refill_board(board))
#rotated_boards = [board, list(zip(*board[::-1])), list(zip(*list(zip(*board[::-1]))[::-1])), list(zip(*list(zip(*list(zip(*board[::-1]))[::-1]))[::-1]))]

#myprint2(list(map(lambda board: list(map(lambda row: shift_row(row), board)), rotated_boards)))
#print(refill_board(refill_board(board)) if sum(map(lambda x: x.count(0), board)) > 1 and __import__('random').choice([True, False]) else refill_board(board))

#map(lambda n: (lambda f, *a: f(f, *a))(lambda rec, n: 1 if n == 0 else n*rec(rec, n-1), n), range(10))


#(lambda twentyfourtyeight, input_str: twentyfourtyeight(input_str))(lambda twentyfourtyeight, board: twentyfourtyeight(board) if board != [] else generate_board, raw_input())

#list(map(lambda widget: widget.destroy(), root.winfo_children()))
#list(map(lambda i: list(map(lambda j: tk.Label(root, text=str(board[i][j]) if board[i][j] else '', bg='wheat1' if board[i][j] else 'wheat3', relief=tk.RIDGE, height=4, width=5).grid(row=i, column=j), range(4))), range(4))) if root.winfo_children() == [] else list(map(lambda widget: widget.config(text=str(board[i][j])), root.winfo_children()))

#root.bind("<Key>", funky)
# for widget in frame.winfo_children():
#     widget.destroy()

#adding GUI
# import tkinter as tk
# def a(event):
#   print("a")
#   b(root)

# def b(root):
#   print("b")
#   root.bind("<Key>", a)

# root = tk.Tk()
# b(root)
# tk.mainloop()
