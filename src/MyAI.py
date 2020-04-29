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

AlphaSweeper = False
MANUAL = not AlphaSweeper
############ import ############
# if MANUAL:
# from tkinter import *
################################


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
				print(i, end=" | ")
				for j in range(self.colDimension):
					print(self.board[i][j], end="  ")
				print()
			print("   ", end="")
			for i in range(self.colDimension):
				print(" - ", end="")
			print()
			print("    ", end="")
			for i in range(self.colDimension):
				print(i, end="  ")
			print()

		def displayWithMarkup(self, markUps):
			""" display board with markup map """
			print("===" * (self.rowDimension + 1), "[markup]")
			for i in range(self.rowDimension - 1, -1, -1):
				print(i, end=" | ")
				for j in range(self.colDimension):
					print(markUps.get((j, i), self.board[i][j]), end="  ")
				print()
			print("   ", end="")
			for i in range(self.colDimension):
				print(" - ", end="")
			print()
			print("    ", end="")
			for i in range(self.colDimension):
				print(i, end="  ")
			print()

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
		print("Game:", MyAI.gamecount)

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
	# Layer 0: Preprocessing Layer
	# Layer 1: Heuristic Layer
	# Layer 2: Probability Layer
	# Layer 3: NN Layer
	# Layer 4: Human Overriding Layer
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

	def humanOverridingLayer(self, number) -> Action:
		result = input("Action(x,y): ").split()
		self.lastMoveXY = (int(result[1]), int(result[2]))
		action = self.makeMove(eval("self.Action(self." + result[0].upper() + ")"), *self.lastMoveXY)
		self.lastMove = action
		return action

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
			self.board.display()

			# evaluate action in layers

			# 1 Preprocessing Layer: finish action -> save unable moves to frontier
			preprocessingLayerResult = self.preprocessingLayer(number)
			if preprocessingLayerResult is not None:
				self.board.displayWithMarkup({i: "+" for i in self.frontier})
				# print("going to move:", preprocessingLayerResult.getMove(), preprocessingLayerResult.getX(), preprocessingLayerResult.getY())
				# print(self.actionQueue)
				return preprocessingLayerResult

			input("stop preprocessing, start heuristic: ")

			print(self.frontier)

			# 2 Heuristic Layer:
			heuristicLayerResult = self.heuristicLayer(number)
			self.board.displayWithMarkup({i: "+" for i in self.frontier})
			if heuristicLayerResult is not None:
				return heuristicLayerResult

			# 5 Human Overriding Layer
			humanLayerResult = self.humanOverridingLayer(number)
			return humanLayerResult

			self.board.display()
			return Action(self.Action.LEAVE, 1, 1)

		except Exception as e:
			print(e)
			input()

	#################################################################
