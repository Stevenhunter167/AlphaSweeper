# ==============================CS-199==================================
# FILE:			MyAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the MyAI class. You will implement your
#				agent in this file. You will write the 'getAction' function,
#				the constructor, and any additional helper functions.
#
# NOTES: 		- MyAI inherits from the abstract AI class in AI.py.
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================

from AI import AI
from Action import Action
from queue import PriorityQueue, Queue

######################################
# Global Var #########################
######################################

DEBUG = False
AlphaSweeper = False
MANUAL = not AlphaSweeper

######################################
# debug console out ##################
######################################
import builtins
from time import time
from inspect import currentframe, getframeinfo

def print(*args, **kwargs):
	builtins.print(*args, **kwargs)

def debug(string):
	previous_frame = currentframe().f_back
	(filename, line_number, function_name, lines, index) = getframeinfo(previous_frame)
	with open("debug.txt", 'a') as f:
		f.write("#############################################################\n")
		f.write("line: " + str(line_number) + "\n")
		f.write(string + "\n")
	# builtins.print("line:", line_number, *args, **kwargs)
######################################


class MyAI( AI ):

	LEAVE = 0
	UNCOVER = 1
	FLAG = 2
	UNFLAG = 3

	gamecount = 0

	class Board:

		FLAG = "F"
		TILE = "."

		def __init__(self, rowDimension, colDimension):
			self.board = [["." for j in range(colDimension)] for i in range(rowDimension)]
			self.colDimension = colDimension
			self.rowDimension = rowDimension

		def isLegalPosition(self, X, Y):
			return 0 <= X < self.colDimension and 0 <= Y < self.rowDimension

		def get(self, X, Y):
			if self.isLegalPosition(X, Y):
				return self.board[Y][X]
			return -1

		def display(self):
			""" display current board """
			print("===" * (self.rowDimension + 1), "[board]")
			for i in range(self.rowDimension - 1, -1, -1):
				print("%2d| " %(i), end="")
				for j in range(self.colDimension):
					print(self.board[i][j], end="  ")
				print()
			print("   ", end="")
			for i in range(self.colDimension):
				print(" - ", end="")
			print()
			print("    ", end="")
			for i in range(self.colDimension):
				print("%-2d" % i, end=" ")
			print()

		def __str__(self):
			result = ""
			result += ("===" * (self.rowDimension + 1) + " [board]\n")
			for i in range(self.rowDimension - 1, -1, -1):
				result += ("%2d|" % (i))
				for j in range(self.colDimension):
					result += (" %s " % str(self.board[i][j]))
				result += "\n"
			result += ("   ")
			for i in range(self.colDimension):
				result += (" - ")
			result += "\n"
			result += ("    ")
			for i in range(self.colDimension):
				result += ("%-2d " % i)
			result += "\n"
			return result

		def displayWithMarkup(self, markUps):
			""" display board with markup map """
			print("===" * (self.rowDimension + 1), "[markup]")
			for i in range(self.rowDimension - 1, -1, -1):
				print("%2d|" % (i), end="")
				for j in range(self.colDimension):
					x = markUps.get((j, i), self.board[i][j])
					if (j, i) in markUps:
						print(x, end="")
					else:
						print(" %s " % str(self.board[i][j]), end="")
				print()
			print("   ", end="")
			for i in range(self.colDimension):
				print(" - ", end="")
			print()
			print("    ", end="")
			for i in range(self.colDimension):
				print("%-2d" % i, end=" ")
			print()

		def toStringMarkup(self, markUps):
			result = ""
			result += ("===" * (self.rowDimension + 1) + " [markup]\n")
			for i in range(self.rowDimension - 1, -1, -1):
				result += ("%2d|" % (i))
				for j in range(self.colDimension):
					x = markUps.get((j, i), self.board[i][j])
					if (j, i) in markUps:
						result += (x)
					else:
						result += (" %s " % str(self.board[i][j]))
				result += "\n"
			result += ("   ")
			for i in range(self.colDimension):
				result += (" - ")
			result += "\n"
			result += ("    ")
			for i in range(self.colDimension):
				result += ("%-2d " % i)
			result += "\n"
			return result

		def set(self, X, Y, char):
			if self.isLegalPosition(X, Y):
				self.board[Y][X] = char
				return True
			return False

	def updateBoard(self, number):
		# routine
		self.moveCount += 1
		# update board: number / flag / unflag
		if number == -1:
			if self.lastMove.getMove() == self.Action(self.UNFLAG) \
					and self.board.get(*self.lastMoveXY) == "F":
				self.board.set(*self.lastMoveXY, self.board.TILE)
			elif self.lastMove.getMove() == self.Action(self.FLAG):
				self.board.set(*self.lastMoveXY, "F")
		else:
			self.board.set(*self.lastMoveXY, number)

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):

		MyAI.gamecount += 1
		# print("Game:", MyAI.gamecount)

		# init Game Variables
		self.board = self.Board(rowDimension, colDimension)
		self.lastMoveXY = (startX, startY)
		self.lastMove = Action(self.Action(self.UNCOVER), startX, startY)
		self.moveCount = 1

		# moves
		self.actionQueue = dict()

		# Heuristic Layer Components
		# frontier
		self.frontier = set()

	####################### making moves ############################

	# class PriorityAction:
	# 	def __init__(self, action, priority):
	# 		self.action = action
	# 		self.priority = priority
	# 	def __lt__(self, other):
	# 		return self.priority < other.priority
	# 	def __eq__(self, other):
	# 		return self.priority == other.priority

	def hasNextMove(self) -> bool:
		return not (len(self.actionQueue) == 0)

	def nextMove(self) -> Action:
		location = next(iter(self.actionQueue))
		action = Action(self.Action(self.actionQueue[location]), *location)
		del self.actionQueue[location]
		return action

	def pushMove(self, actionCode, X, Y, priority=5) -> None:
		# self.actionQueue.put(self.PriorityAction(Action(self.Action(actionCode), X, Y), priority))
		self.actionQueue[(X, Y)] = actionCode

	def popMove(self):
		if len(self.actionQueue) == 0:
			raise Exception("empty action queue")
		action = self.nextMove()
		self.lastMoveXY = (action.getX(), action.getY())
		self.lastMove = action
		return action

	def makeMove(self, actionCode, X, Y) -> Action:
		self.lastMoveXY = (X, Y)
		self.lastMove = Action(self.Action(actionCode), X, Y)
		return self.lastMove

	#################################################################
	# Basic Movements
	#################################################################

	# lookup
	def lookSurround(self, X, Y):
		for dx in range(-1, 2):
			for dy in range(-1, 2):
				if not (dx == 0 and dy == 0):
					if self.board.isLegalPosition(X + dx, Y + dy):
						yield X + dx, Y + dy

	#################################################################
	#          Layer Name						result type
	# Layer 0: Preprocessing Layer				deterministic
	# Layer 1: Heuristic Layer					deterministic
	# Layer 2: CSP Layer						deterministic
	# Layer 3: Probablistic CSP Layer			probabilistic
	# Layer 4: NN Layer							probabilistic
	# Layer 5: Human Overriding Layer			      -
	#################################################################

	def preprocessingLayer(self, number) -> Action:

		# preprocessing a uncovered tile
		if number == 0:
			for x, y in self.lookSurround(*self.lastMoveXY):
				if self.board.get(x, y) == self.board.TILE:
					self.pushMove(self.UNCOVER, x, y, priority=5)

		if number > 0:
			self.frontier.add(self.lastMoveXY)

		if self.hasNextMove():
			return self.popMove()

	#################################################################
	# heuristic Layer ###############################################
	#################################################################

	def heuristicLayer(self, number) -> Action:

		# 1 frontier heuristic

		# 1.1 flag surrounding deterministic tiles
		removeFromFrontier = list()
		for (X, Y) in self.frontier:
			# center:   (X,Y)
			# surround: (x,y)
			surround = [self.board.get(x, y) for x, y in self.lookSurround(X, Y)]

			# if all surrouding are uncoverd or flagged
			if surround.count(self.board.TILE) == 0:
				removeFromFrontier.append((X, Y))

			# if flag + tile = number, flag all tiles
			elif surround.count(self.board.TILE) + surround.count(self.board.FLAG) == self.board.get(X, Y):
				for (x, y) in self.lookSurround(X, Y):
					if self.board.get(x, y) == self.board.TILE:
						self.pushMove(self.FLAG, x, y, priority=4)
				removeFromFrontier.append((X, Y))

			# if flag == number, uncover all tiles
			elif surround.count(self.board.FLAG) == self.board.get(X, Y):
				for (x, y) in self.lookSurround(X, Y):
					if self.board.get(x, y) == self.board.TILE:
						self.pushMove(self.UNCOVER, x, y, priority=4)
				removeFromFrontier.append((X, Y))

		for XYcoordinate in removeFromFrontier:
			self.frontier.remove(XYcoordinate)


		if self.hasNextMove():
			return self.popMove()

	#################################################################
	# CSP Layer #####################################################
	#################################################################

	@staticmethod
	def recursive_backtrack(varset: {'var': None},
							constrains: 'lambda(varset): bool',
							domains: {'var'},
							resultList: list):
		"""
		A recursive backtrack searching algorithm
		perform search in state (domain) space
		return: varset (with assigned value that satisfies constrains)
		"""

		# 1.return varset if every var have assignment
		if all(i is not None for i in varset.values()):
			resultList.append(varset)
			return True

		# 2.select next-unassigned-var
		var = None
		for i in varset:
			if varset[i] == None:
				var = i

		# 3.for each value in domains
		for value in domains:
			# assign next order-domain-value
			varset[var] = value
			# if constraint is satisfied
			if constrains(varset):
				# print(varset)
				result = MyAI.recursive_backtrack(varset.copy(), constrains, domains, resultList)
				# if result is not False:
				# 	return result

				# all childrens of this node is deadend
				# remove assignment
				varset[var] = None
		return False

	def buildConstraint(self):

		# constrainList = list()
		# for (X, Y) in self.frontier:
			# subConstrain for each frontier number

			# constrainList.append(subConstrain)

		# frontier = self.frontier
		def constraints(varset):

			def subConstrain(varset, X, Y):

				currentStatus = [] # current assignment
				for (x, y) in self.lookSurround(X, Y):
					if self.board.get(x, y) == self.board.TILE:
						currentStatus.append(varset[(x, y)])
					elif self.board.get(x, y) == self.board.FLAG:
						currentStatus.append(1)

				# print((X,Y), currentStatus)

				if None in currentStatus:
					return currentStatus.count(1) <= self.board.get(X, Y)
				elif sum(currentStatus) == self.board.get(X, Y):
					return True
				return False
			for (X,Y) in self.frontier:
				if not subConstrain(varset, X, Y):
					return False
			return True

		return constraints

	def buildVarSet(self):
		tiles = dict()
		for (X, Y) in self.frontier:
			for (x, y) in self.lookSurround(X,Y):
				if self.board.get(x, y) == self.board.TILE:
					tiles[(x, y)] = None
		return tiles

	def CSP(self) -> Action:
		print("started CSP")
		startTime = time()
		print(startTime)

		resultList = list()
		varset = self.buildVarSet()
		self.recursive_backtrack(varset=varset,
								 constrains=self.buildConstraint(),
								 domains={0,1},
								 resultList=resultList)

		result = {location:0 for location in varset.keys()}
		for configuration in resultList:
			for location in configuration:
				result[location] += configuration[location]

		# debug
		debug(str(self.board) + "\nlastmove: " + str(self.lastMoveXY))
		for configuration in resultList:
			debug(self.board.toStringMarkup({(x,y): '[m]' if configuration[x,y] else '[x]'
											 for x,y in configuration}))

		print("CSP result:", result)
		print("size:", len(resultList))
		print("CSP finished in:", time() - startTime, "seconds")

	def humanOverridingLayer(self, number) -> Action:
		result = input("Action(x,y): ").split()
		# get input from console
		while len(result) != 3:
			result = input("Action(x,y): ").split()
		self.lastMoveXY = (int(result[1]), int(result[2]))
		action = self.makeMove(eval("self.Action(self." + result[0].upper() + ")"), *self.lastMoveXY)
		self.lastMove = action
		return action

	def winCheck(self):
		for r in range(self.board.rowDimension):
			for c in range(self.board.colDimension):
				if self.board.get(c, r) == self.board.TILE:
					return None
		return Action(self.Action(self.LEAVE), 1, 1)

	#################################################################
	# MAIN ##########################################################
	#################################################################

	def getAction(self, number: int) -> "Action Object":
		""" DO NOT MODIFY self.lastMove OR self.moveCount """
		try:
			# update game status
			self.updateBoard(number)
			print()
			print("---" * (self.board.rowDimension + 1), "Move", self.moveCount, ":", self.lastMoveXY, "status:", number)
			# self.board.display()

			# evaluate action in layers

			# 0 Preprocessing Layer: finish action -> save unable moves to frontier
			preprocessingLayerResult = self.preprocessingLayer(number)
			if preprocessingLayerResult is not None:
				self.board.displayWithMarkup({i: "(%d)" %self.board.get(*i) for i in self.frontier})
				# print("going to move:", preprocessingLayerResult.getMove(), preprocessingLayerResult.getX(), preprocessingLayerResult.getY())
				# print(self.actionQueue)
				return preprocessingLayerResult

			# input("stop preprocessing, start heuristic: ")
			print(self.frontier)

			# 1 Heuristic Layer:
			heuristicLayerResult = self.heuristicLayer(number)
			self.board.displayWithMarkup({i: "(%d)" %self.board.get(*i) for i in self.frontier})
			if heuristicLayerResult is not None:
				return heuristicLayerResult

			# 2 Probability Layer:
			# calculate probability of each tile near frontier
			# generate combinations using constraint satisfaction


			# print(self.buildConstraint()(
			# 	{(0, 4): 0, (1, 4): 0, (2, 4): 0, (3, 4): 0, (4, 4): 1,
			# 	 (7, 0): 0, (7, 1): 0, (7, 2): 0, (5, 4): 0, (6, 4): 0,
			# 	 (7, 3): 0, (7, 4): 0}, self.frontier
			# ))


			# input("start CSP: ")
			self.CSP()
			self.board.display()
			winResult = self.winCheck()
			if winResult is not None:
				return winResult

			# 5 Human Overriding Layer
			humanLayerResult = self.humanOverridingLayer(number)
			return humanLayerResult

			self.board.display()
			return Action(self.Action.LEAVE, 1, 1)

		except Exception as e:
			print(e)
			input()

	#################################################################
