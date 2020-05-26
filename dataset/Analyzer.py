
folder = "./May25/"
for i in range(1, 101):
    with open(folder + str(i) + ".txt", 'r') as f:
        s = [l for l in f][-1].strip()
        if not s.startswith("GameStatus"):
            print("Game" + str(i) + ": " + s)



"""
/usr/local/bin/python3.7 "/Users/steven/Desktop/The Only Spring 2020/CS 171/project-AlphaSweeper/AlphaSweeper/dataset/Analyzer.py"
Game22popMove: 57 Action.UNCOVER (6, 6) strategy: PROBABILISTIC frontier: 0.33 random: 0.33 mineleft: 3
Game23popMove: 48 Action.UNCOVER (6, 4) strategy: PROBABILISTIC frontier: 0.33 random: 0.39 mineleft: 7
Game30
Game31popMove: 50 Action.UNCOVER (7, 3) strategy: PROBABILISTIC frontier: 0.17 random: 0.31 mineleft: 5
Game33
Game34
Game37
Game38popMove: 56 Action.UNCOVER (1, 1) strategy: PROBABILISTIC frontier: 0.20 random: 0.40 mineleft: 4
Game40popMove: 48 Action.UNCOVER (2, 1) strategy: PROBABILISTIC frontier: 0.33 random: 0.33 mineleft: 6
Game42
Game51
Game68popMove: 61 Action.UNCOVER (0, 0) strategy: PROBABILISTIC frontier: 0.50 random: 0.40 mineleft: 2
Game71
Game74popMove: 27 Action.UNCOVER (6, 4) strategy: PROBABILISTIC frontier: 0.17 random: 0.21 mineleft: 8
Game80popMove: 25 Action.UNCOVER (4, 4) strategy: PROBABILISTIC frontier: 0.14 random: 0.22 mineleft: 9
Game81
Game84
Game91
Game98

Process finished with exit code 0

"""