import random
import copy
 


board = []




#code for building a basic board with "O" as empty places


for i in range(10):
	board.append(["O"]*10)


# assigning ships to dictionary

ships = {"Carrier":4, "Battlehips":3, "Destroyer":2}
print ships.keys()


def place_ships(board, ship):
	for ship in ships.keys():
		# validate positions for the ships, provided by input
		valid = False
		while(not valid):
			print_board("u", board)
			print "placing a/an ship" + ship
			x,y = get_coor()
			ori = v_or_h()
			valid = validate(board, ships[ship],x,y,ori)
			if not valid:
				print "cannot place a ship there/nPlease check location"
				raw_input("Hit ENTER to continue")
		# place ship

		board = place_ship(board, ships[ship], ship[0], ori, x, y)
		print_board("u", board)


def get_coor():
	while (True):
		user_input= raw_input("Please enter coordinates (row, col))")
		try:
			# see if the user entered the two values correct, seperated by a comma
			coor = user_input.split(",")
			if len(coor) != 2:
				raise Exception("Invalid entry, too many/few coordinates")
			#check that 2 values are integers
			coor[0] = int(coor[0])-1
			coor[1] = int(coor[1])-1

			# check that the values are between 1 and 10 for both coordinates
			if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
				raise Exception("Invalid entry, PLease use valies between 1 and 10 only")

			#if eveyrthing is OK, return Coordinates
			return coor

		except ValueError:
			print "Invalid Entry Please enter only numeric values for coordinates"
		except Exception as e:
			print e

def v_or_h():
	# Get ship orientation from user

	while(True):
		user_input=raw_input("Vertical or Horizontal (v,h)")
		if user_input == "v" or user_input=="h":
			return user_input

		else:
			print "Invalid Input. Please only use v(ertical) or h(orizontal)"


def validate(board,ships,x,y,ori):
	#validate the ship can be placed at given coordinates

	if ori == "v" and x+ship > 10:
			return False
	if ori == "h" and y+ship > 10:
		return False
	else:
		if ori == "v":
			for i in range(ship):
				if board[x+i][y] != -1:
					return False
					#if 



















#toying with vertical changes to the board - inserting a carrier
def boardcord(x,y,bl):
	shiple
	x = x-1
	y = y-1
	newboard = []
	#getting the boatlength
	boatend = y-bl
	print boatend
	# checks if the values are within parameters
	if (y-bl) < 0 or (y-bl) > 11:
		raise Exception("not possible value")
	else: #calculates the end coordinates on 'y'
		boatend = y-bl

		#this does two things. first it checks if there is already a boat on the board (s)
		#if not, it will place one.
	for i in range(y, boatend,-1):
		if board[i][x] == "S":
			print "a boat is already here"
		else:
			board[i][x] = "S"
		

#let's fire some shells at them ships!
def fire(x,y):
	x = x-1
	y = y-1
	#checks if there is a ship pressent on the spot. If not, label it anyway.
	if board[y][x]=='C':
		board[y][x]='X'
		print "HIT!!!!"
	else:
		board[y][x]='X'
		print "MISSED!"


def check()


	for line in board:
		print line
boardcord(9,5,4)
boardcord(4,3,2)
fire(4,5)
fire(9,3)
fire(9,4)
fire(9,5)
fire(9,2)