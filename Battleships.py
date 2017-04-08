import copy
import random

board = []



#code for building a basic board with "O" as empty places
for i in range(10):
	board.append(["O"]*10)


# assigning ships to dictionary

# def Players(boards, boats):



ships = {"Carrier":4, "Battlehip":3, "Destroyer":2}

#toying with vertical changes to the board - inserting a carrier
def boardcord(x,y,bl):
	shiplen = ships[bl]
	# print shiplen
	x = x-1
	y = y-1
	newboard = []
	#getting the boatlength
	boatend = y-shiplen
	#print boatend
	# checks if the values are within parameters
	if (y-shiplen) < 0 or (y-shiplen) > 11:
		raise Exception("not possible value")
	else: #calculates the end coordinates on 'y'
		boatend = y-shiplen

		#this does two things. first it checks if there is already a boat on the board (s)
		#if not, it will place one.
	for i in range(y, boatend,-1):
		if board[i][x] == "S":
			print "a boat is already here"
		elif bl == "Carrier":
			board[i][x] = "C"
		elif bl == "Destroyer":
			board[i][x] = "D"
		elif bl == "Battleship":
			board[i][x] == "B"

#let's fire some shells at them ships!
def fire(x,y):
	x = x-1
	y = y-1
	#checks if there is a ship pressent on the spot. If not, label it anyway.
	if board[y][x]=='C':
		ships["Carrier"] -=1
		print ships["Carrier"]
		board[y][x]='X'
		print "HIT!!!!"
	else:
		board[y][x]='X'
		print "MISSED!"
	check()


def check():
	for line in ships:
	#	print ships[line]
		if ships[line]==0:
			print "You sunk my Battleship!"
	else:
			print "keep firering!"




boardcord(9,5,"Carrier")
boardcord(4,3,"Destroyer")
#fire(4,5)
#fire(9,4)
#fire(9,3)
#fire(9,5)
#fire(9,2)



for line in board:
	print line
