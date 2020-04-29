# class Window:
# 	def __init__(self, rowDim, colDim):
# 		self.board = MyAI.Board(rowDim, colDim)
# 		self.clickedAction = None
# 		self.clickedLocation = None
# 		self.clicked = False
# 		self.root = Tk()
#
# 		def left_click(window, X, Y):
# 			def action(event):
# 				event.widget.configure(bg="green")
# 				window.clicked = True
# 				window.clickedAction = AI.Action.UNCOVER
# 				window.clickedLocation = (X, Y)
# 			return action
#
# 		def right_click(window, X, Y):
# 			def action(event):
# 				event.widget.configure(bg="green")
# 				window.clicked = True
# 				window.clickedAction = AI.Action.UNCOVER
# 				window.clickedLocation = (X, Y)
# 			return action
#
# 		# init buttons
# 		self.buttons = [[Button(self.root, text="#") for c in range(rowDim)] for r in range(colDim)]
# 		for row in range(rowDim):
# 			for col in range(colDim):
# 				self.buttons[row][col].bind("<Button-1>", left_click(self, row + 1, col + 1))
# 				self.buttons[row][col].bind("<Button-2>", right_click(self, row + 1, col + 1))
# 				self.buttons[row][col].grid(row=row, column=col)
#
# 		self.root.mainloop()
#
# 	def update(self, X, Y, char):
# 		self.board.set(X, Y, char)
# 		self.buttons[X - 1][Y - 1].config(text=str(char))
# 		self.buttons[X - 1][Y - 1].grid(X - 1, Y - 1)
# 		print("update finished")
#
# 	def getAction(self):
# 		while not self.clicked:
# 			pass
# 		return Action(self.clickedAction, *self.clickedLocation)