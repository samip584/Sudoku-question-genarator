from os import system
import random


def main():
	system("clear")
	print("SUDOKU QUESTION GENARATOR\n\n")
	print("Your question is :\n\n")
	arr = taken = []
	sudoku = []
	for i in range(9):
		temp = []
		for j in range (9):
			temp.append(0)
		sudoku.append(temp)
	
	make_board(sudoku)

	#erase excess elements from diagonal blocks
	for i in range(3):
		for j in range(3):
			erase_from_block(sudoku, i*3, j*3)
	display(sudoku)


def make_board(sudoku):
	arr = [1,2,3,4,5,6,7,8,9,10]
	direc = random.randint(1,2)
	if(direc == 1):
		for loop in range(9):
			count = 8 - loop
			position = random.randint(0,count)
			sudoku[0][loop] = arr[position]
			for k in range(position,count):
				arr[k], arr[k+1] = arr[k+1], arr[k]
		for loop in [0,3,6]:
			for row in range(loop+1,loop+3):
				for column in range(9):
					sudoku[row][column] = sudoku[row-1][(column + 3)%9]
				if(loop != 6):
					for column in range(9):
						sudoku[loop + 3][column] = sudoku[loop + 2][(column + 1)%9]
	elif(direc == 2):
		for loop in range(9):
			count = 8 - loop
			position = random.randint(0,count)
			sudoku[loop][0] = arr[position]
			for k in range(position,count):
				arr[k], arr[k+1] = arr[k+1], arr[k]
		for loop in [0,3,6]:
			for column in range(loop+1,loop+3):
				for row in range(9):
					sudoku[row][column] = sudoku[(row+3)%9][(column -1)]
				if(loop != 6):
					for row in range(9):
						sudoku[row][loop + 3] = sudoku[(row + 1)%9][loop + 2]


def erase_from_block(sudoku, n, m):
	while(1):
		no_empty_space = 0
		for i in range(n, n + 3):
			for j in range(m, m + 3):
				if(sudoku[i][j] == 0):
					no_empty_space += 1
		if(no_empty_space > 4):
			return
		else:
			count = 8
			position_arr = [0,1,2,3,4,5,6,7,8,9]
			rand_gen_no_spaces = random.randint(4,8) - 3
			while(rand_gen_no_spaces>0):
				randon_no = random.randint(0,count)
				sudoku[int(position_arr[randon_no] / 3) + n][int(position_arr[randon_no] % 3) + m] = 0
				for k in range(randon_no, count):
					position_arr[k], position_arr[k+1] = position_arr[k+1], position_arr[k]
				count -= 1
				rand_gen_no_spaces -= 1

def display(sudoku):
    print("-"*37)
    for index, row in enumerate(sudoku):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if index == 8:
            print("-"*37)
        elif index % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")


if __name__ == "__main__":
	main()