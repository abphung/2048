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
	return list(filter(lambda x: board[x[0]][x[1]] == 0, list(zip(4*list(range(4)), list(sum(zip(*4*[list(range(4))]), ()))))))

def random_zero(board):
	return __import__('random').choice(zero_locs(board))

def refill_board(board):
	return (lambda x: list(map(lambda j: list(map(lambda i: __import__('random').choice([2, 4]) if (j, i) == (x[0], x[1]) else board[j][i], range(4))), range(4))))(random_zero(board))

def rotate_board(board, count):
	return rotate_board(list(map(list, zip(*board[::-1]))), count - 1) if count > 0 else board

def shift_row(row):
	return list(filter(lambda i: i != 0, row)) + list(filter(lambda i: i == 0, row))

def combine_row(row):
	return row if len(row) <= 1 else [row[0] + row[1]] + combine_row(row[2:]) + [0] if row[0] == row[1] else [row[0]] + combine_row(row[1:])

def myprint(board):
	return (list(map(lambda row: print(row), board)), board)[1]

def myprint2(boards):
	list(map(lambda board: myprint(row), boards))

#how do i add numbers wh
def twentyfourtyeight(board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]):
	if not any(map(any, board)):#good
		board = refill_board(board)#good
	myprint(board)
	rotated_boards = list(map(lambda i: rotate_board(board, i), range(4)))#good
	combined_boards = list(map(lambda board: list(map(lambda row: combine_row(shift_row(row)), board)), rotated_boards))#good
	#myprint2(combined_boards)
	unrotated_boards = list(map(lambda i: rotate_board(combined_boards[i], 4 - i), range(4)))#good
	if unrotated_boards[1:] == unrotated_boards[:-1]:
		print('gameover')
		return
	input_str = input()#__import__('random').choice(['a', 'w', 'd', 's'])#'a'#raw_input()
	input_ind = {'a':0, 's':1, 'd':2, 'w':3}[input_str]
	twentyfourtyeight(refill_board(refill_board(unrotated_boards[input_ind])) if sum(map(lambda x: x.count(0), unrotated_boards[input_ind])) > 1 and __import__('random').choice([True, False]) else refill_board(unrotated_boards[input_ind])) if unrotated_boards[input_ind] != board else twentyfourtyeight(board)
#twentyfourtyeight()


#(lambda boards, input_ind: twentyfourtyeight(refill_board(refill_board(boards[input_ind])) if sum(map(lambda x: x.count(0), boards[input_ind])) > 1 and __import__('random').choice([True, False]) else refill_board(boards[input_ind])) if boards[input_ind] != board else twentyfourtyeight(board))(list(map(lambda i: rotate_board(list(map(lambda board: list(map(lambda row: combine_row(shift_row(row)), board)), list(map(lambda i: rotate_board(refill_board(board) if not any(map(any, board)) else board, i), range(4)))))[i], 4 - i), range(4))), {'a':0, 's':1, 'd':2, 'w':3}[input()])
#list(map(lambda i: rotate_board(list(map(lambda board: list(map(lambda row: combine_row(shift_row(row)), board)), list(map(lambda i: rotate_board(refill_board(board) if not any(map(any, board)) else board, i), range(4)))))[i], 4 - i), range(4)))

#(lambda twentyfourtyeight, board: twentyfourtyeight(twentyfourtyeight, board))(lambda twentyfourtyeight, board: (lambda boards, input_ind: twentyfourtyeight(refill_board(refill_board(boards[input_ind])) if sum(map(lambda x: x.count(0), boards[input_ind])) > 1 and __import__('random').choice([True, False]) else refill_board(boards[input_ind])) if boards[input_ind] != board else twentyfourtyeight(board))(list(map(lambda i: rotate_board(list(map(lambda board: list(map(lambda row: combine_row(shift_row(row)), board)), list(map(lambda i: rotate_board(refill_board(board) if not any(map(any, board)) else board, i), range(4)))))[i], 4 - i), range(4))), {'a':0, 's':1, 'd':2, 'w':3}[input()]), [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])




#print(refill_board([[0, 0, 0, 0]]))
#print(combine_row(shift_row([2,0,4,4])))
board = [[2,0,4,4],[2,8,8,4],[2,0,64,4],[2,0,4,64]]
#print(rotate_board(board, 3))
#twentyfourtyeight()
#print(rotate_board(board, 1))
myprint(board)
# pprint(refill_board(board))
#rotated_boards = [board, list(zip(*board[::-1])), list(zip(*list(zip(*board[::-1]))[::-1])), list(zip(*list(zip(*list(zip(*board[::-1]))[::-1]))[::-1]))]

#myprint2(list(map(lambda board: list(map(lambda row: shift_row(row), board)), rotated_boards)))
#print(refill_board(refill_board(board)) if sum(map(lambda x: x.count(0), board)) > 1 and __import__('random').choice([True, False]) else refill_board(board))

#map(lambda n: (lambda f, *a: f(f, *a))(lambda rec, n: 1 if n == 0 else n*rec(rec, n-1), n), range(10))


#(lambda twentyfourtyeight, input_str: twentyfourtyeight(input_str))(lambda twentyfourtyeight, board: twentyfourtyeight(board) if board != [] else generate_board, raw_input())
