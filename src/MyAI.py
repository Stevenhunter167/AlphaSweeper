# ==========CS-171=============
# FILE:			MyAI.py
#
# AUTHOR: 		Litian Liang
# TEAM:			AlphaSweeper
#
# =============================

from AI import AI
from Action import Action
from itertools import combinations

######################################
# Global Var #########################
######################################

LOG = True
DEBUG = False
AlphaSweeper = False
MANUAL = not AlphaSweeper
OUTFOLDER = "../dataset/intermediate100_with_subgroup/"

######################################
# debug console out ##################
######################################
import builtins
import traceback
from time import time, sleep
from inspect import currentframe, getframeinfo
from pprint import pformat


def line():
	previous_frame = currentframe().f_back
	(filename, line_number, function_name, lines, index) = getframeinfo(previous_frame)
	return "line: " + str(line_number)

def print(*args, **kwargs):
	# builtins.print(*args, **kwargs)
	pass

def print2(*args, **kwargs):
	builtins.print(*args, **kwargs)
	pass

def debug(*args, **kwargs):
	builtins.print("[debug" + line() + "]", *args, **kwargs)

def log(filename, string):
	global OUTFOLDER
	with open(OUTFOLDER + str(filename) + ".txt", 'a') as f:
		f.write(("#" * 60) + "\n")
		f.write(string + "\n")
	pass

def logCSP(filename, string):
	global OUTFOLDER
	with open(OUTFOLDER + str(filename) + ".txt", 'a') as f:
		f.write(("#" * 60) + "\n")
		f.write(string + "\n")
	pass
######################################


class MyAI( AI ):

	# action code
	LEAVE = 0
	UNCOVER = 1
	FLAG = 2
	UNFLAG = 3

	# statistics
	gamecount = 0
	beginnerStats = [0, -1]
	intermediateStats = [0, -1]
	expertStats = [0, -1]
	stats = {
		( 8, 8) : beginnerStats,
		(16,16) : intermediateStats,
		(16,30) : expertStats
	}

	# parameters
	THREASH_TIME = 4 # time left for stoping all time consuming heuristics
	THREASH_SUBGROUP = 5

	class Board:

		FLAG = "F"
		TILE = "."

		def __init__(self, rowDimension, colDimension):
			self.board = [["." for j in range(colDimension)] for i in range(rowDimension)]
			self.colDimension = colDimension
			self.rowDimension = rowDimension

		def isLegalPosition(self, X, Y):
			return 0 <= X < self.colDimension and 0 <= Y < self.rowDimension

		def set(self, X, Y, char):
			if self.isLegalPosition(X, Y):
				self.board[Y][X] = char
				return True
			return False

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



	class Equivalence:
		def __init__(self):
			self.parent = {}

		def add(self, a, b):
			self.addSingleton(a)
			self.addSingleton(b)
			self.merge(a, b)

		def addSingleton(self, a):
			if a not in self.parent:
				self.parent[a] = a

		def merge(self, a, b):
			self.parent[self.root(a)] = self.root(b)

		def check(self, a, b):
			return self.root(a) == self.root(b)

		def root(self, a):
			while True:
				pa = self.parent[a]
				if pa == a:
					break
				a = pa
			return a

		def classes(self):
			res = {}
			for element in self.parent:
				res.setdefault(self.root(element), set())
				res[self.root(element)].add(element)
				res[self.root(element)].add(self.root(element))
			return res

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

	def log(self, string):
		log(MyAI.gamecount, string)

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):

		MyAI.gamecount += 1
		# 1 more game at this difficulty level
		self.stats[(rowDimension, colDimension)][1] += 1

		# init Game Variables
		self.totalMines = totalMines
		self.totalFlags = 0
		self.tileLeft = rowDimension * colDimension
		self.board = self.Board(rowDimension, colDimension)
		self.lastMoveXY = (startX, startY)
		self.lastMove = Action(self.Action(self.UNCOVER), startX, startY)
		self.moveCount = 1

		print2("Game: %d, BoardSize: (%d,%d), TotalMines: %d"
				 %(MyAI.gamecount,
				   rowDimension,
				   colDimension,
				   totalMines), end=" | ")
		print2("Current Win [B: %d/%d (%.2f) I: %d/%d (%.2f) E: %d/%d (%.2f)]"
			   %(self.beginnerStats[0],
				 self.beginnerStats[1],
				 self.beginnerStats[0] / self.beginnerStats[1] if self.beginnerStats[1] != 0 else 0,
				 self.intermediateStats[0],
				 self.intermediateStats[1],
				 self.intermediateStats[0] / self.intermediateStats[1] if self.intermediateStats[1] != 0 else 0,
				 self.expertStats[0],
				 self.expertStats[1],
				 self.expertStats[0] / self.expertStats[1] if self.expertStats[1] != 0 else 0))
		self.log("Game: %d, BoardSize: (%d,%d), TotalMines: %d"
				 %(MyAI.gamecount,
				   rowDimension,
				   colDimension,
				   totalMines)
		)

		self.BEGINTIME = time()

		# moves
		self.actionQueue = dict()
		# corresponding heuristic map
		self.heuristicQueue = dict()

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

	def pushMove(self, actionCode, X, Y, heuristic="NOT PROVIDED") -> None:
		# self.actionQueue.put(self.PriorityAction(Action(self.Action(actionCode), X, Y), priority))
		self.actionQueue[(X, Y)] = actionCode
		self.heuristicQueue[(X, Y)] = heuristic

	def popMove(self):
		if len(self.actionQueue) == 0:
			return None
		action = self.nextMove()
		self.lastMoveXY = (action.getX(), action.getY())
		self.lastMove = action

		self.log("popMove: " + str(self.moveCount) + " " + str(self.lastMove.getMove()) + " " + str(self.lastMoveXY)
				 + " strategy: " + str(self.heuristicQueue[self.lastMoveXY])
				 + " mineleft: " + str(self.totalMines - self.totalFlags))
		# print2("popMove: " + str(self.moveCount) + " " + str(self.lastMove.getMove()) + " " + str(self.lastMoveXY)
		# 		 + " strategy: " + str(self.heuristicQueue[self.lastMoveXY])
		# 		 + " mineleft: " + str(self.totalMines - self.totalFlags))

		if self.lastMove.getMove() == AI.Action.FLAG:
			self.totalFlags += 1
			self.tileLeft -= 1
		elif self.lastMove.getMove() == AI.Action.UNCOVER:
			self.tileLeft -= 1
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
	# Layer 1: Basic Layer						deterministic
	# Layer 2: Grouping							deterministic
	# Layer 3: CSP Layer						deterministic
	# Layer 4: PSEQ Layer						probabilistic
	# Layer 5: Probablistic CSP Layer			probabilistic
	# Layer 6: Human Overriding Layer			      -
	#################################################################

	#################################################################
	# preprocessing Layer ###########################################
	#################################################################

	def allCells(self):
		for y in range(self.board.rowDimension):
			for x in range(self.board.colDimension):
				yield (x, y)


	def preprocessingLayer(self, number) -> Action:
		hName = "PREPROCESS"

		allCellResult = [self.board.get(x, y) for x, y in self.allCells()]

		# discoverd all mines
		if self.totalFlags == self.totalMines:
			for (x, y) in self.allCells():
				if self.board.get(x, y) == self.board.TILE:
					self.pushMove(self.UNCOVER, x, y, heuristic=hName)
			return self.popMove()

		# all rest tiles are mines
		if self.totalFlags + self.tileLeft == self.totalMines:
			for (x, y) in self.allCells():
				if self.board.get(x, y) == self.board.TILE:
					self.pushMove(self.FLAG, x, y, heuristic=hName)
			return self.popMove()

		# preprocessing a uncovered tile
		if number == 0:
			for x, y in self.lookSurround(*self.lastMoveXY):
				if self.board.get(x, y) == self.board.TILE:
					self.pushMove(self.UNCOVER, x, y, heuristic=hName)

		# there are some mines around, add to frontier
		if number > 0:
			self.frontier.add(self.lastMoveXY)

		# finish any move in queue
		if self.hasNextMove():
			return self.popMove()

	#################################################################
	# heuristic Layer ###############################################
	#################################################################

	def basicLayer(self, number) -> Action:

		# 1 frontier heuristic
		hName = "BASIC"

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
						self.pushMove(self.FLAG, x, y, heuristic=hName)
				removeFromFrontier.append((X, Y))

			# if flag == number, uncover all tiles
			elif surround.count(self.board.FLAG) == self.board.get(X, Y):
				for (x, y) in self.lookSurround(X, Y):
					if self.board.get(x, y) == self.board.TILE:
						self.pushMove(self.UNCOVER, x, y, heuristic=hName)
				removeFromFrontier.append((X, Y))

		for XYcoordinate in removeFromFrontier:
			self.frontier.remove(XYcoordinate)


		if self.hasNextMove():
			return self.popMove()

	#################################################################
	# Grouping ######################################################
	#################################################################

	def buildGroup(self, frontier):
		groups = list()
		for (X,Y) in frontier:
			thisGroup = set()
			minecount = self.board.get(X,Y)
			for location in self.lookSurround(X,Y):
				if self.board.get(*location) == self.board.TILE:
					thisGroup.add(location)
				elif self.board.get(*location) == self.board.FLAG:
					minecount -= 1
			groups.append((thisGroup, minecount))
		return groups

	def groupof(self, group, count):
		return [set(i) for i in combinations(group, count)]

	def subgrouping(self, groups):

		hName = "SUBGROUP"

		ge = {}
		le = {}
		for group, mine_count in groups:

			if mine_count >= self.THREASH_SUBGROUP:
				continue

			# print2(group, mine_count)

			# greater or equals
			safe_count = len(group) - mine_count
			for x in range(1, mine_count):
				for subgroup in self.groupof(group, safe_count + x):
					ge[tuple(sorted(subgroup))] = (x, group, mine_count)
					# print2(subgroup, x)

			# less or equals
			for y in range(len(group)-1, mine_count, -1):
				for subgroup in self.groupof(group, y):
					le[tuple(sorted(subgroup))] = (mine_count, group, mine_count)
					# print2(subgroup, y)

		# print2(ge)
		# print2(le)
		# input(line())
		subgroupAction = False

		for sub1 in ge:
			for sub2 in le:
				count1, group1, mc1 = ge[sub1]
				count2, group2, mc2 = le[sub2]
				if sub1 == sub2 and count1 == count2:
					subgroup = set(sub1)
					# check its 2 relevent groups for deduction

					# M(group) == M(subgroup), all rest are safe
					if subgroup.issubset(group1) and mc1 - count1 == 0:
						subgroupAction = True
						difference1 = group1 - subgroup
						for location in difference1:
							self.pushMove(self.UNCOVER, *location, heuristic=hName)
					# M(group) - M(subgroup) = len(group - subgroup), all rest are mines
					if subgroup.issubset(group1) and mc1 - count1 == len(group1) - len(subgroup):
						subgroupAction = True
						difference1 = group1 - subgroup
						for location in difference1:
							self.pushMove(self.FLAG, *location, heuristic=hName)

					# same logic for group2
					if subgroup.issubset(group2) and mc2 - count2 == 0:
						subgroupAction = True
						difference2 = group2 - subgroup
						for location in difference2:
							self.pushMove(self.UNCOVER, *location, heuristic=hName)
					if subgroup.issubset(group2) and mc2 - count2 == len(group2) - len(subgroup):
						subgroupAction = True
						difference2 = group2 - subgroup
						for location in difference2:
							self.pushMove(self.FLAG, *location, heuristic=hName)



		if subgroupAction == True:
			return self.popMove()
		else:
			return None

	def grouping(self):
		hName = "GROUPING"
		groups = self.buildGroup(self.frontier)

		groupingAction = False
		for pivotLocations, pivotMine in groups:
			for locations, locMine in groups:
				# check every pair in group

				if locations != pivotLocations and locations.issubset(pivotLocations):
					# if not same set and locations is subset of pivot

					difference = pivotLocations - locations
					if len(difference) == pivotMine - locMine:
						# flag the difference, make move
						groupingAction = True
						for (x,y) in difference:
							self.pushMove(self.FLAG, x, y, heuristic=hName)
					if (pivotMine - locMine) == 0:
						# difference are safe, make move
						groupingAction = True
						for (x,y) in difference:
							self.pushMove(self.UNCOVER, x, y, heuristic=hName)

		if groupingAction:
			return self.popMove()
		else:
			return self.subgrouping(groups)

	#################################################################
	# CSP Layer #####################################################
	#################################################################


	def recursive_backtrack(self,
							varset: {'var': None},
							constrains: 'lambda(varset): bool',
							domains: {'var'},
							resultList: list):
		"""
		A recursive backtrack searching algorithm
		perform search in state (domain) space
		return: varset (with assigned value that satisfies constrains)
		"""

		if self.timeLeft() < self.THREASH_TIME:
			return False

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
				result = self.recursive_backtrack(varset.copy(), constrains, domains, resultList)
				# if result is not False:
				# 	return result

				# all childrens of this node is deadend
				# remove assignment
				varset[var] = None
				if result == False:
					return False

	def buildConstraint(self, frontier):
		def constraints(varset) -> bool:
			def subConstrain(varset, X, Y): # varset satisfies mine constrain at X,Y
				currentStatus = []  # current assignment
				for (x, y) in self.lookSurround(X, Y):
					if self.board.get(x, y) == self.board.TILE:
						currentStatus.append(varset[(x, y)])
					elif self.board.get(x, y) == self.board.FLAG:
						currentStatus.append(1)
				if None in currentStatus:
					return currentStatus.count(1) <= self.board.get(X, Y)
				elif sum(currentStatus) == self.board.get(X, Y):
					return True
				return False
			# print("constrain on:", sorted(varset))
			# print(frontier)
			for (X,Y) in frontier:
				if not subConstrain(varset, X, Y):
					return False
			return True
		# print(line(), "finished buildConstrain")
		return constraints

	def buildVarSet(self):
		tiles = dict()
		for (X, Y) in self.frontier:
			for (x, y) in self.lookSurround(X,Y):
				if self.board.get(x, y) == self.board.TILE:
					tiles[(x, y)] = None
		return tiles

	# def buildVarSet(self, tiles):
	# 	res = dict()
	# 	for (x, y) in tiles:
	# 		res[(x, y)] = None
	# 	return res

	def splitFrontiers(self) -> (set, dict):

		""" set: frontier, dict: varset """

		# eq class of tiles, if t1 and t2 are eq, they are in the same frontier
		e = self.Equivalence()

		# if a and b share 1 uncoverd tile, they are in the same frontier
		for coord in self.frontier:
			tiles = []
			for neighbour in self.lookSurround(*coord):
				if self.board.get(*neighbour) == self.Board.TILE:
					tiles.append(neighbour)
			first = tiles.pop(0)
			for t in tiles:
				e.add(first, t)

		# build frontier and result list
		res = []
		for tiles in e.classes().values():
			frontier = set()
			for t in tiles:
				for location in self.lookSurround(*t):
					if type(self.board.get(*location)) == int\
						and self.board.get(*location) > 0:
						frontier.add(location)
			varset = {i: None for i in tiles}
			res.append((frontier, varset))

		return res

	def CSP(self, frontier, varset) -> (dict, Action):

		# CSP Layer
		hName = "CSP"

		print("started CSP on", frontier)
		startTime = time()

		resultList = list()
		#debug
		markup = {}
		markup.update({i: '[%d]' %(self.board.get(*i)) for i in frontier})
		markup.update({j: '(.)' for j in varset})
		self.board.displayWithMarkup(markup)
		# hName += "\n" + self.board.toStringMarkup(markup) + "\n"
		#end
		constrains = self.buildConstraint(frontier)
		res = self.recursive_backtrack(varset=varset,
								 constrains=constrains,
								 domains={0, 1},
								 resultList=resultList)

		print("CSP finished in:", time() - startTime, "seconds")
		logCSPdata = {
			'finished': res,
			'time': time() - startTime,
			'frontier_size': len(frontier),
			'varset_size': len(varset)
		}
		logCSP("CSP"+str(self.gamecount), str(logCSPdata))

		if res == False:
			return ({}, self.chooseRandom())

		result = {location: 0 for location in varset.keys()}

		# count all possible results
		for configuration in resultList:
			for location in configuration:
				result[location] += configuration[location]

		# hName += pformat(resultList)

		print(line(), result)
		print("possible results:", len(resultList))
		minMine = min(result.values())
		maxMine = max(result.values())

		# input("leastMine:"+str(leastMine))
		if minMine == 0:  # There is somewhere that cannot be mine
			for location in result:
				if result[location] == 0:
					self.pushMove(self.UNCOVER, *location, heuristic=hName)
			return (result, self.popMove())
		elif maxMine == len(resultList):
			for location in result:
				if result[location] == maxMine:
					print("CSP flagged", location)
					self.pushMove(self.FLAG, *location, heuristic=hName)
			return (result, self.popMove())
		else:
			# construct probability distribution
			for location in result:
				result[location] = result[location] / len(resultList)
			return (result, None)

	def cspEval(self) -> (dict, Action):
		results = {}
		# calculate p for all frontiers
		for frontier, varset in sorted(self.splitFrontiers(), key=lambda f_v: len(f_v[1])): # sort frontier from small to large
			res, action = self.CSP(frontier, varset)
			if action is not None:
				return res, action
			results.update(res)
		return results, None


	def probEval(self, varset: {(int,int):float}) -> Action:

		hName = "PROBABILISTIC"

		# minimum prob on frontier
		minimum = 1
		(X, Y) = (None, None)
		for (x, y), p in varset.items():
			if p < minimum:
				X, Y = x, y
				minimum = p

		# minimum random click prob = (safe tile) / (total uncovered tile)
		minimum_random = (self.totalMines - self.totalFlags) / self.tileLeft

		hName += " frontier: %.2f random: %.2f" %(minimum, minimum_random)

		if minimum <= minimum_random: # safer clicking on frontier
			self.pushMove(self.UNCOVER, X, Y, heuristic=hName)
			return self.popMove()
		elif minimum_random < minimum:# safer clicking on a random cell
			varset = self.buildVarSet()
			for location in self.allCells():
				if self.board.get(
						*location) == self.board.TILE and location not in varset:
					self.pushMove(self.UNCOVER, *location, heuristic=hName)
					return self.popMove()



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
		for (x, y) in self.allCells():
			if self.board.get(x, y) == self.board.TILE:
				return None
		self.log("GameStatus: WIN, Finished in: "+ str(time() - self.BEGINTIME) + "(seconds)")
		print2("WIN, Finished in: "+ str(time() - self.BEGINTIME) + "(seconds)")

		# world win count += 1
		self.stats[(self.board.rowDimension, self.board.colDimension)][0] += 1
		return Action(self.Action(self.LEAVE), 1, 1)

	#################################################################
	# MAIN ##########################################################
	#################################################################

	def timeLeft(self):
		return 300 - (time() - self.BEGINTIME)

	def chooseRandom(self):

		# random
		hName = "RANDOM"

		varset = self.buildVarSet()
		for location in self.allCells():
			if self.board.get(*location) == self.board.TILE and location not in varset:
				self.pushMove(self.UNCOVER, *location, heuristic=hName)
				return self.popMove()
		else:
			for location in self.allCells():
				if self.board.get(*location) == self.board.TILE:
					self.pushMove(self.UNCOVER, *location, heuristic=hName)
					return self.popMove()


	def getAction(self, number: int) -> "Action Object":
		""" DO NOT MODIFY self.lastMove OR self.moveCount """

		try:
			# update game status
			self.updateBoard(number)
			print()
			print("---" * (self.board.rowDimension + 1), "Move", self.moveCount, ":", self.lastMoveXY, "status:", number, "timeleft:", self.timeLeft())

			self.log("timeleft:" + str(self.timeLeft()) + "\n" + self.board.toStringMarkup({i: "(%d)" % self.board.get(*i) for i in self.frontier}))

			# self.board.display()

			# evaluate action in layers
			winResult = self.winCheck()
			if winResult is not None:
				return winResult

			# 0 Preprocessing Layer: finish action -> save unable moves to frontier
			preprocessingLayerResult = self.preprocessingLayer(number)
			if preprocessingLayerResult is not None:
				# self.board.displayWithMarkup({i: "(%d)" %self.board.get(*i) for i in self.frontier})
				# print("going to move:", preprocessingLayerResult.getMove(), preprocessingLayerResult.getX(), preprocessingLayerResult.getY())
				# print(self.actionQueue)
				return preprocessingLayerResult

			# input("stop preprocessing, start heuristic: ")
			# print(self.frontier)

			# sleep(1)

			# 1 Basic Layer:
			basicLayerResult = self.basicLayer(number)
			if basicLayerResult is not None:
				return basicLayerResult

			self.board.displayWithMarkup({i: "(%d)" %self.board.get(*i) for i in self.frontier})

			# 2 Grouping
			groupingResult = self.grouping()
			if groupingResult is not None:
				return groupingResult

			# 3 CSP Layer: result, weight_vector
			# calculate probability of each tile near frontier
			# generate combinations using constraint satisfaction

			if len(self.frontier) > 0: # not all tiles are surrounded by mines
				print(self.frontier)
				print("start splitfrontier")
				fs = list(self.splitFrontiers())
				print("frontier split:", len(fs), fs)
				print("end splitfrontier")

				cspResult, cspAction = self.cspEval()
				if cspAction is not None:
					return cspAction

				print("cspResult:", cspResult)
				# self.log("CSPresult" + str(cspResult))


				# Probablity Evaluation Layer
				evalResult = self.probEval(cspResult)
				# self.log(line()+str(evalResult.getMove() if evalResult is not None else None))
				if evalResult is not None:
					return evalResult
				else:
					return self.chooseRandom()

			else: # all tiles are surrounded by mines
				return self.chooseRandom()


			# 5 Human Overriding Layer
			# self.board.displayWithMarkup(
			# 	{i: "(%d)" % self.board.get(*i) for i in self.frontier})
			# humanLayerResult = self.humanOverridingLayer(number)
			# return humanLayerResult


			# builtins.print(self.gamecount)
			return Action(self.Action.LEAVE, 1, 1)

		except Exception as e:
			print("EXCEPTION:")
			print2(traceback.format_exc())
			input()

	#################################################################
		# Add frontier splitting