import glob
print()
folder = "./May29/"

win=0
total=0


games = {
    (8,8) : [0, 0],
    (16, 16) : [0, 0],
    (16, 30) : [0, 0]
} # (x, x): [win, lose]

# print(glob.glob(folder + "*.txt"))
print("calculating from", folder)
for filename in glob.glob(folder + "*.txt"):
    with open(filename, 'r') as f:
        total += 1
        fl = [l for l in f]
        gamesize = eval(fl[1][fl[1].find("BoardSize:") + 10:].split(')')[0] + ')')
        # print(filename)
        # print(gamesize)
        s = fl[-1].strip()
        if not s.startswith("GameStatus"):
            print("Game", filename, ": " + s)
            games[gamesize][1] += 1
        else:
            games[gamesize][0] += 1
for boardsize in games:
    print("Current Win rate on " + str(boardsize) + ": %.2f" %(games[boardsize][0]/sum(games[boardsize]) if sum(games[boardsize]) != 0 else 0.0), str((games[boardsize][0], sum(games[boardsize]))))