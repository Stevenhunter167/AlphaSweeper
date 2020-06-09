import glob
print()
folder = "./intermediate100_with_subgroup/"
# b: 868 - 882
# i:  87 - 87
# e:

win=0
total=0


games = {
    (8,8) : [0, 0],
    (16, 16) : [0, 0],
    (16, 30) : [0, 0]
} # (x, x): [win, lose]

# print(glob.glob(folder + "*.txt"))
print("calculating from", folder)

fout = open("cleaned.txt", 'w')

for filename in glob.glob(folder + "*.txt"):
    with open(filename, 'r') as f:
        total += 1
        fs = f.read()
        fl = fs.split('\n')
        gamesize = eval(fl[1][fl[1].find("BoardSize:") + 10:].split(')')[0] + ')')


        s = fl[-2].strip()
        # print("line 29", fl[-2])
        board = fs.split("############################################################")[-2]
        if not s.startswith("GameStatus"):
            print("Game", filename, ": " + s)
            fout.write("Game " + filename + " : " + s)
            # print(board)
            fout.write(board)
            games[gamesize][1] += 1
        else:
            games[gamesize][0] += 1
        # input()

fout.close()

for boardsize in games:
    print("Current Win rate on " + str(boardsize) + ": %.2f" %(games[boardsize][0]/sum(games[boardsize]) if sum(games[boardsize]) != 0 else 0.0), str((games[boardsize][0], sum(games[boardsize]))))


# C:\Users\15011\AppData\Local\Programs\Python\Python37\python.exe C:/Users/15011/Desktop/AlphaSweeper/src/Main.py -f ../WorldGenerator/Problems/
# Game: 1, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 0/0 (0.00)]
# WIN, Finished in: 0.9843971729278564(seconds)
# Game: 2, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1/1 (1.00)]
# Game: 3, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1/2 (0.50)]
# Game: 4, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1/3 (0.33)]
# WIN, Finished in: 0.9326474666595459(seconds)
# Game: 5, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 2/4 (0.50)]
# Game: 6, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 2/5 (0.40)]
# Game: 7, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 2/6 (0.33)]
# Game: 8, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 2/7 (0.29)]
# Game: 9, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 2/8 (0.25)]
# WIN, Finished in: 0.9850647449493408(seconds)
# Game: 10, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 3/9 (0.33)]
# Game: 11, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 3/10 (0.30)]
# Game: 12, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 3/11 (0.27)]
# WIN, Finished in: 0.8980262279510498(seconds)
# Game: 13, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 4/12 (0.33)]
# Game: 14, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 4/13 (0.31)]
# Game: 15, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 4/14 (0.29)]
# Game: 16, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 4/15 (0.27)]
# Game: 17, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 4/16 (0.25)]
# WIN, Finished in: 0.8750205039978027(seconds)
# Game: 18, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 5/17 (0.29)]
# Game: 19, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 5/18 (0.28)]
# WIN, Finished in: 19.422722339630127(seconds)
# Game: 20, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 6/19 (0.32)]
# Game: 21, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 6/20 (0.30)]
# Game: 22, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 6/21 (0.29)]
# Game: 23, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 6/22 (0.27)]
# Game: 24, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 6/23 (0.26)]
# Game: 25, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 6/24 (0.25)]
# Game: 26, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 6/25 (0.24)]
# WIN, Finished in: 3.140397787094116(seconds)
# Game: 27, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 7/26 (0.27)]
# WIN, Finished in: 0.937488317489624(seconds)
# Game: 28, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 8/27 (0.30)]
# Game: 29, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 8/28 (0.29)]
# Game: 30, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 8/29 (0.28)]
# Game: 31, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 8/30 (0.27)]
# Game: 32, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 8/31 (0.26)]
# Game: 33, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 8/32 (0.25)]
# WIN, Finished in: 0.8591170310974121(seconds)
# Game: 34, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 9/33 (0.27)]
# WIN, Finished in: 0.93758225440979(seconds)
# Game: 35, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 10/34 (0.29)]
# WIN, Finished in: 75.98464131355286(seconds)
# Game: 36, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 11/35 (0.31)]
# WIN, Finished in: 2.688469886779785(seconds)
# Game: 37, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 12/36 (0.33)]
# Game: 38, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 12/37 (0.32)]
# Game: 39, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 12/38 (0.32)]
# WIN, Finished in: 0.7966001033782959(seconds)
# Game: 40, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 13/39 (0.33)]
# Game: 41, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 13/40 (0.33)]
# Game: 42, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 13/41 (0.32)]
# WIN, Finished in: 0.7190372943878174(seconds)
# Game: 43, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 14/42 (0.33)]
# Game: 44, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 14/43 (0.33)]
# Game: 45, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 14/44 (0.32)]
# Game: 46, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 14/45 (0.31)]
# WIN, Finished in: 9.923165798187256(seconds)
# Game: 47, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 15/46 (0.33)]
# Game: 48, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 15/47 (0.32)]
# WIN, Finished in: 54.31140089035034(seconds)
# Game: 49, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 16/48 (0.33)]
# Game: 50, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 16/49 (0.33)]
# WIN, Finished in: 1.0937848091125488(seconds)
# Game: 51, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 17/50 (0.34)]
# Game: 52, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 17/51 (0.33)]
# Game: 53, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 17/52 (0.33)]
# Game: 54, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 17/53 (0.32)]
# Game: 55, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 17/54 (0.31)]
# WIN, Finished in: 2.560153007507324(seconds)
# Game: 56, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 18/55 (0.33)]
# Game: 57, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 18/56 (0.32)]
# WIN, Finished in: 0.7654519081115723(seconds)
# Game: 58, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 19/57 (0.33)]
# WIN, Finished in: 25.795881032943726(seconds)
# Game: 59, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 20/58 (0.34)]
# Game: 60, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 20/59 (0.34)]
# WIN, Finished in: 9.23693299293518(seconds)
# Game: 61, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 21/60 (0.35)]
# Game: 62, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 21/61 (0.34)]
# Game: 63, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 21/62 (0.34)]
# WIN, Finished in: 4.425701856613159(seconds)
# Game: 64, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 22/63 (0.35)]
# Game: 65, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 22/64 (0.34)]
# Game: 66, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 22/65 (0.34)]
# WIN, Finished in: 0.9532451629638672(seconds)
# Game: 67, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 23/66 (0.35)]
# Game: 68, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 23/67 (0.34)]
# Game: 69, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 23/68 (0.34)]
# WIN, Finished in: 1.6567723751068115(seconds)
# Game: 70, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 24/69 (0.35)]
# Game: 71, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 24/70 (0.34)]
# Game: 72, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 24/71 (0.34)]
# WIN, Finished in: 0.8751275539398193(seconds)
# Game: 73, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 25/72 (0.35)]
# Game: 74, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 25/73 (0.34)]
# Game: 75, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 25/74 (0.34)]
# WIN, Finished in: 18.84451198577881(seconds)
# Game: 76, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 26/75 (0.35)]
# Game: 77, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 26/76 (0.34)]
# WIN, Finished in: 13.313999652862549(seconds)
# Game: 78, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 27/77 (0.35)]
# Game: 79, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 27/78 (0.35)]
# WIN, Finished in: 1.5155236721038818(seconds)
# Game: 80, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 28/79 (0.35)]
# WIN, Finished in: 3.7817089557647705(seconds)
# Game: 81, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 29/80 (0.36)]
# WIN, Finished in: 22.464816093444824(seconds)
# Game: 82, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 30/81 (0.37)]
# Game: 83, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 30/82 (0.37)]
# WIN, Finished in: 0.8751189708709717(seconds)
# Game: 84, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 31/83 (0.37)]
# Game: 85, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 31/84 (0.37)]
# Game: 86, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 31/85 (0.36)]
# Game: 87, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 31/86 (0.36)]
# Game: 88, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 31/87 (0.36)]
# WIN, Finished in: 1.9535913467407227(seconds)
# Game: 89, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 32/88 (0.36)]
# Game: 90, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 32/89 (0.36)]
# Game: 91, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 32/90 (0.36)]
# WIN, Finished in: 47.79119896888733(seconds)
# Game: 92, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 33/91 (0.36)]
# Game: 93, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 33/92 (0.36)]
# WIN, Finished in: 58.01443123817444(seconds)
# Game: 94, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 34/93 (0.37)]
# WIN, Finished in: 34.26672172546387(seconds)
# Game: 95, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 35/94 (0.37)]
# Game: 96, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 35/95 (0.37)]
# Game: 97, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 35/96 (0.36)]
# Game: 98, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 35/97 (0.36)]
# WIN, Finished in: 0.9843916893005371(seconds)
# Game: 99, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 36/98 (0.37)]
# WIN, Finished in: 0.9220192432403564(seconds)
# Game: 100, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 37/99 (0.37)]
# Game: 101, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 37/100 (0.37)]
# WIN, Finished in: 3.3893826007843018(seconds)
# Game: 102, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 38/101 (0.38)]
# Game: 103, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 38/102 (0.37)]
# Game: 104, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 38/103 (0.37)]
# WIN, Finished in: 50.64120268821716(seconds)
# Game: 105, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 39/104 (0.38)]
# Game: 106, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 39/105 (0.37)]
# WIN, Finished in: 5.969592571258545(seconds)
# Game: 107, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 40/106 (0.38)]
# Game: 108, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 40/107 (0.37)]
# WIN, Finished in: 1.8436853885650635(seconds)
# Game: 109, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 41/108 (0.38)]
# WIN, Finished in: 0.8921217918395996(seconds)
# Game: 110, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 42/109 (0.39)]
# Game: 111, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 42/110 (0.38)]
# WIN, Finished in: 8.552758693695068(seconds)
# Game: 112, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 43/111 (0.39)]
# Game: 113, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 43/112 (0.38)]
# Game: 114, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 43/113 (0.38)]
# Game: 115, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 43/114 (0.38)]
# WIN, Finished in: 0.9689037799835205(seconds)
# Game: 116, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 44/115 (0.38)]
# Game: 117, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 44/116 (0.38)]
# Game: 118, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 44/117 (0.38)]
# Game: 119, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 44/118 (0.37)]
# WIN, Finished in: 0.9063634872436523(seconds)
# Game: 120, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 45/119 (0.38)]
# WIN, Finished in: 1.0937776565551758(seconds)
# Game: 121, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 46/120 (0.38)]
# Game: 122, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 46/121 (0.38)]
# Game: 123, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 46/122 (0.38)]
# Game: 124, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 46/123 (0.37)]
# Game: 125, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 46/124 (0.37)]
# Game: 126, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 46/125 (0.37)]
# WIN, Finished in: 1.06260085105896(seconds)
# Game: 127, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 47/126 (0.37)]
# Game: 128, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 47/127 (0.37)]
# WIN, Finished in: 8.626631021499634(seconds)
# Game: 129, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 48/128 (0.38)]
# Game: 130, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 48/129 (0.37)]
# WIN, Finished in: 6.465449571609497(seconds)
# Game: 131, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 49/130 (0.38)]
# Game: 132, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 49/131 (0.37)]
# Game: 133, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 49/132 (0.37)]
# Game: 134, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 49/133 (0.37)]
# Game: 135, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 49/134 (0.37)]
# Game: 136, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 49/135 (0.36)]
# WIN, Finished in: 290.12317967414856(seconds)
# Game: 137, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 50/136 (0.37)]
# Game: 138, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 50/137 (0.36)]
# Game: 139, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 50/138 (0.36)]
# WIN, Finished in: 13.966316223144531(seconds)
# Game: 140, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 51/139 (0.37)]
# Game: 141, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 51/140 (0.36)]
# WIN, Finished in: 0.7341582775115967(seconds)
# Game: 142, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 52/141 (0.37)]
# WIN, Finished in: 0.8675615787506104(seconds)
# Game: 143, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 53/142 (0.37)]
# Game: 144, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 53/143 (0.37)]
# WIN, Finished in: 0.7657618522644043(seconds)
# Game: 145, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 54/144 (0.38)]
# WIN, Finished in: 290.530485868454(seconds)
# Game: 146, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 55/145 (0.38)]
# WIN, Finished in: 1.7504098415374756(seconds)
# Game: 147, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 56/146 (0.38)]
# Game: 148, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 56/147 (0.38)]
# WIN, Finished in: 0.7564635276794434(seconds)
# Game: 149, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 57/148 (0.39)]
# Game: 150, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 57/149 (0.38)]
# Game: 151, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 57/150 (0.38)]
# Game: 152, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 57/151 (0.38)]
# Game: 153, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 57/152 (0.38)]
# WIN, Finished in: 1.0785419940948486(seconds)
# Game: 154, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 58/153 (0.38)]
# WIN, Finished in: 46.38927435874939(seconds)
# Game: 155, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 59/154 (0.38)]
# Game: 156, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 59/155 (0.38)]
# Game: 157, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 59/156 (0.38)]
# WIN, Finished in: 1.0157546997070312(seconds)
# Game: 158, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 60/157 (0.38)]
# Game: 159, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 60/158 (0.38)]
# WIN, Finished in: 0.9681839942932129(seconds)
# Game: 160, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 61/159 (0.38)]
# Game: 161, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 61/160 (0.38)]
# Game: 162, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 61/161 (0.38)]
# Game: 163, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 61/162 (0.38)]
# Game: 164, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 61/163 (0.37)]
# WIN, Finished in: 0.8123109340667725(seconds)
# Game: 165, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 62/164 (0.38)]
# Game: 166, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 62/165 (0.38)]
# Game: 167, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 62/166 (0.37)]
# WIN, Finished in: 0.8439309597015381(seconds)
# Game: 168, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 63/167 (0.38)]
# Game: 169, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 63/168 (0.38)]
# Game: 170, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 63/169 (0.37)]
# Game: 171, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 63/170 (0.37)]
# Game: 172, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 63/171 (0.37)]
# Game: 173, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 63/172 (0.37)]
# WIN, Finished in: 2.2348885536193848(seconds)
# Game: 174, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 64/173 (0.37)]
# WIN, Finished in: 1.3281340599060059(seconds)
# Game: 175, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 65/174 (0.37)]
# Game: 176, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 65/175 (0.37)]
# Game: 177, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 65/176 (0.37)]
# Game: 178, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 65/177 (0.37)]
# Game: 179, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 65/178 (0.37)]
# Game: 180, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 65/179 (0.36)]
# Game: 181, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 65/180 (0.36)]
# WIN, Finished in: 1.0313715934753418(seconds)
# Game: 182, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 66/181 (0.36)]
# Game: 183, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 66/182 (0.36)]
# WIN, Finished in: 0.7185828685760498(seconds)
# Game: 184, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 67/183 (0.37)]
# WIN, Finished in: 1.6096770763397217(seconds)
# Game: 185, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 68/184 (0.37)]
# Game: 186, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 68/185 (0.37)]
# WIN, Finished in: 1.17228364944458(seconds)
# Game: 187, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 69/186 (0.37)]
# Game: 188, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 69/187 (0.37)]
# Game: 189, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 69/188 (0.37)]
# WIN, Finished in: 83.85592770576477(seconds)
# Game: 190, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 70/189 (0.37)]
# Game: 191, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 70/190 (0.37)]
# Game: 192, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 70/191 (0.37)]
# WIN, Finished in: 34.597445011138916(seconds)
# Game: 193, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 71/192 (0.37)]
# Game: 194, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 71/193 (0.37)]
# Game: 195, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 71/194 (0.37)]
# WIN, Finished in: 40.34228873252869(seconds)
# Game: 196, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 72/195 (0.37)]
# Game: 197, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 72/196 (0.37)]
# WIN, Finished in: 19.36217212677002(seconds)
# Game: 198, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 73/197 (0.37)]
# Game: 199, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 73/198 (0.37)]
# Game: 200, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 73/199 (0.37)]
# Game: 201, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 73/200 (0.36)]
# Game: 202, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 73/201 (0.36)]
# Game: 203, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 73/202 (0.36)]
# Game: 204, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 73/203 (0.36)]
# Game: 205, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 73/204 (0.36)]
# WIN, Finished in: 1.1250669956207275(seconds)
# Game: 206, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 74/205 (0.36)]
# Game: 207, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 74/206 (0.36)]
# Game: 208, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 74/207 (0.36)]
# WIN, Finished in: 3.0154716968536377(seconds)
# Game: 209, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 75/208 (0.36)]
# Game: 210, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 75/209 (0.36)]
# Game: 211, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 75/210 (0.36)]
# WIN, Finished in: 1.7030177116394043(seconds)
# Game: 212, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 76/211 (0.36)]
# Game: 213, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 76/212 (0.36)]
# WIN, Finished in: 0.7831301689147949(seconds)
# Game: 214, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 77/213 (0.36)]
# Game: 215, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 77/214 (0.36)]
# Game: 216, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 77/215 (0.36)]
# Game: 217, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 77/216 (0.36)]
# Game: 218, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 77/217 (0.35)]
# Game: 219, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 77/218 (0.35)]
# Game: 220, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 77/219 (0.35)]
# Game: 221, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 77/220 (0.35)]
# WIN, Finished in: 0.9861605167388916(seconds)
# Game: 222, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 78/221 (0.35)]
# WIN, Finished in: 290.29819893836975(seconds)
# Game: 223, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 79/222 (0.36)]
# Game: 224, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 79/223 (0.35)]
# WIN, Finished in: 0.8439116477966309(seconds)
# Game: 225, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 80/224 (0.36)]
# WIN, Finished in: 1.369145154953003(seconds)
# Game: 226, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 81/225 (0.36)]
# WIN, Finished in: 3.5448882579803467(seconds)
# Game: 227, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 82/226 (0.36)]
# WIN, Finished in: 1.8891851902008057(seconds)
# Game: 228, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 83/227 (0.37)]
# Game: 229, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 83/228 (0.36)]
# Game: 230, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 83/229 (0.36)]
# WIN, Finished in: 1.8908064365386963(seconds)
# Game: 231, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 84/230 (0.37)]
# Game: 232, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 84/231 (0.36)]
# WIN, Finished in: 4.469067811965942(seconds)
# Game: 233, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 85/232 (0.37)]
# Game: 234, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 85/233 (0.36)]
# Game: 235, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 85/234 (0.36)]
# Game: 236, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 85/235 (0.36)]
# WIN, Finished in: 0.8666720390319824(seconds)
# Game: 237, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 86/236 (0.36)]
# Game: 238, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 86/237 (0.36)]
# Game: 239, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 86/238 (0.36)]
# WIN, Finished in: 8.15980076789856(seconds)
# Game: 240, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 87/239 (0.36)]
# Game: 241, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 87/240 (0.36)]
# Game: 242, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 87/241 (0.36)]
# Game: 243, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 87/242 (0.36)]
# WIN, Finished in: 0.8283123970031738(seconds)
# Game: 244, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 88/243 (0.36)]
# WIN, Finished in: 4.326608180999756(seconds)
# Game: 245, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 89/244 (0.36)]
# Game: 246, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 89/245 (0.36)]
# Game: 247, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 89/246 (0.36)]
# Game: 248, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 89/247 (0.36)]
# Game: 249, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 89/248 (0.36)]
# Game: 250, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 89/249 (0.36)]
# WIN, Finished in: 14.545530319213867(seconds)
# Game: 251, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 90/250 (0.36)]
# Game: 252, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 90/251 (0.36)]
# Game: 253, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 90/252 (0.36)]
# Game: 254, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 90/253 (0.36)]
# Game: 255, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 90/254 (0.35)]
# Game: 256, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 90/255 (0.35)]
# Game: 257, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 90/256 (0.35)]
# WIN, Finished in: 11.156774044036865(seconds)
# Game: 258, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 91/257 (0.35)]
# WIN, Finished in: 0.8126664161682129(seconds)
# Game: 259, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 92/258 (0.36)]
# WIN, Finished in: 0.9063048362731934(seconds)
# Game: 260, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 93/259 (0.36)]
# Game: 261, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 93/260 (0.36)]
# WIN, Finished in: 1.0325157642364502(seconds)
# Game: 262, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 94/261 (0.36)]
# WIN, Finished in: 30.003034353256226(seconds)
# Game: 263, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 95/262 (0.36)]
# Game: 264, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 95/263 (0.36)]
# Game: 265, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 95/264 (0.36)]
# WIN, Finished in: 35.968672037124634(seconds)
# Game: 266, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 96/265 (0.36)]
# Game: 267, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 96/266 (0.36)]
# WIN, Finished in: 20.84543251991272(seconds)
# Game: 268, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 97/267 (0.36)]
# WIN, Finished in: 0.7502336502075195(seconds)
# Game: 269, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 98/268 (0.37)]
# Game: 270, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 98/269 (0.36)]
# Game: 271, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 98/270 (0.36)]
# Game: 272, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 98/271 (0.36)]
# WIN, Finished in: 1.4378595352172852(seconds)
# Game: 273, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 99/272 (0.36)]
# Game: 274, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 99/273 (0.36)]
# Game: 275, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 99/274 (0.36)]
# Game: 276, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 99/275 (0.36)]
# WIN, Finished in: 290.40824794769287(seconds)
# Game: 277, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 100/276 (0.36)]
# Game: 278, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 100/277 (0.36)]
# Game: 279, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 100/278 (0.36)]
# Game: 280, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 100/279 (0.36)]
# Game: 281, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 100/280 (0.36)]
# WIN, Finished in: 1.0625724792480469(seconds)
# Game: 282, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 101/281 (0.36)]
# Game: 283, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 101/282 (0.36)]
# WIN, Finished in: 0.8907859325408936(seconds)
# Game: 284, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 102/283 (0.36)]
# WIN, Finished in: 22.330889463424683(seconds)
# Game: 285, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 103/284 (0.36)]
# Game: 286, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 103/285 (0.36)]
# Game: 287, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 103/286 (0.36)]
# Game: 288, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 103/287 (0.36)]
# Game: 289, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 103/288 (0.36)]
# Game: 290, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 103/289 (0.36)]
# Game: 291, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 103/290 (0.36)]
# Game: 292, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 103/291 (0.35)]
# Game: 293, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 103/292 (0.35)]
# WIN, Finished in: 7.063424587249756(seconds)
# Game: 294, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 104/293 (0.35)]
# WIN, Finished in: 0.7970283031463623(seconds)
# Game: 295, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 105/294 (0.36)]
# Game: 296, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 105/295 (0.36)]
# WIN, Finished in: 0.890718936920166(seconds)
# Game: 297, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 106/296 (0.36)]
# Game: 298, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 106/297 (0.36)]
# Game: 299, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 106/298 (0.36)]
# WIN, Finished in: 16.09383249282837(seconds)
# Game: 300, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 107/299 (0.36)]
# Game: 301, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 107/300 (0.36)]
# Game: 302, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 107/301 (0.36)]
# Game: 303, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 107/302 (0.35)]
# WIN, Finished in: 0.7654173374176025(seconds)
# Game: 304, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 108/303 (0.36)]
# Game: 305, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 108/304 (0.36)]
# Game: 306, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 108/305 (0.35)]
# WIN, Finished in: 2.5469088554382324(seconds)
# Game: 307, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 109/306 (0.36)]
# Game: 308, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 109/307 (0.36)]
# Game: 309, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 109/308 (0.35)]
# Game: 310, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 109/309 (0.35)]
# Game: 311, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 109/310 (0.35)]
# Game: 312, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 109/311 (0.35)]
# Game: 313, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 109/312 (0.35)]
# WIN, Finished in: 0.7814016342163086(seconds)
# Game: 314, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 110/313 (0.35)]
# Game: 315, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 110/314 (0.35)]
# Game: 316, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 110/315 (0.35)]
# WIN, Finished in: 0.8439393043518066(seconds)
# Game: 317, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 111/316 (0.35)]
# Game: 318, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 111/317 (0.35)]
# WIN, Finished in: 11.563833475112915(seconds)
# Game: 319, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 112/318 (0.35)]
# Game: 320, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 112/319 (0.35)]
# WIN, Finished in: 50.52171754837036(seconds)
# Game: 321, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 113/320 (0.35)]
# Game: 322, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 113/321 (0.35)]
# Game: 323, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 113/322 (0.35)]
# WIN, Finished in: 1.8908562660217285(seconds)
# Game: 324, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 114/323 (0.35)]
# WIN, Finished in: 2.6411004066467285(seconds)
# Game: 325, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 115/324 (0.35)]
# Game: 326, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 115/325 (0.35)]
# WIN, Finished in: 0.8591516017913818(seconds)
# Game: 327, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 116/326 (0.36)]
# Game: 328, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 116/327 (0.35)]
# Game: 329, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 116/328 (0.35)]
# Game: 330, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 116/329 (0.35)]
# Game: 331, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 116/330 (0.35)]
# Game: 332, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 116/331 (0.35)]
# Game: 333, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 116/332 (0.35)]
# WIN, Finished in: 1.8440687656402588(seconds)
# Game: 334, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 117/333 (0.35)]
# Game: 335, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 117/334 (0.35)]
# Game: 336, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 117/335 (0.35)]
# Game: 337, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 117/336 (0.35)]
# WIN, Finished in: 0.8750455379486084(seconds)
# Game: 338, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 118/337 (0.35)]
# WIN, Finished in: 290.1630997657776(seconds)
# Game: 339, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 119/338 (0.35)]
# Game: 340, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 119/339 (0.35)]
# Game: 341, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 119/340 (0.35)]
# WIN, Finished in: 13.126822233200073(seconds)
# Game: 342, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 120/341 (0.35)]
# Game: 343, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 120/342 (0.35)]
# WIN, Finished in: 3.468996524810791(seconds)
# Game: 344, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 121/343 (0.35)]
# Game: 345, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 121/344 (0.35)]
# Game: 346, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 121/345 (0.35)]
# Game: 347, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 121/346 (0.35)]
# WIN, Finished in: 0.7345495223999023(seconds)
# Game: 348, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 122/347 (0.35)]
# WIN, Finished in: 7.750943660736084(seconds)
# Game: 349, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 123/348 (0.35)]
# WIN, Finished in: 2.2118968963623047(seconds)
# Game: 350, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 124/349 (0.36)]
# WIN, Finished in: 10.532779693603516(seconds)
# Game: 351, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 125/350 (0.36)]
# Game: 352, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 125/351 (0.36)]
# Game: 353, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 125/352 (0.36)]
# Game: 354, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 125/353 (0.35)]
# WIN, Finished in: 1.2030246257781982(seconds)
# Game: 355, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 126/354 (0.36)]
# Game: 356, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 126/355 (0.35)]
# Game: 357, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 126/356 (0.35)]
# Game: 358, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 126/357 (0.35)]
# Game: 359, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 126/358 (0.35)]
# Game: 360, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 126/359 (0.35)]
# Game: 361, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 126/360 (0.35)]
# Game: 362, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 126/361 (0.35)]
# WIN, Finished in: 2.9675540924072266(seconds)
# Game: 363, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 127/362 (0.35)]
# Game: 364, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 127/363 (0.35)]
# Game: 365, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 127/364 (0.35)]
# Game: 366, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 127/365 (0.35)]
# WIN, Finished in: 1.2948248386383057(seconds)
# Game: 367, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 128/366 (0.35)]
# WIN, Finished in: 26.234002828598022(seconds)
# Game: 368, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 129/367 (0.35)]
# WIN, Finished in: 0.8906848430633545(seconds)
# Game: 369, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 130/368 (0.35)]
# Game: 370, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 130/369 (0.35)]
# Game: 371, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 130/370 (0.35)]
# Game: 372, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 130/371 (0.35)]
# Game: 373, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 130/372 (0.35)]
# WIN, Finished in: 1.4365370273590088(seconds)
# Game: 374, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 131/373 (0.35)]
# Game: 375, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 131/374 (0.35)]
# Game: 376, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 131/375 (0.35)]
# WIN, Finished in: 4.2523345947265625(seconds)
# Game: 377, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 132/376 (0.35)]
# WIN, Finished in: 29.99783492088318(seconds)
# Game: 378, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 133/377 (0.35)]
# Game: 379, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 133/378 (0.35)]
# WIN, Finished in: 0.7717764377593994(seconds)
# Game: 380, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 134/379 (0.35)]
# Game: 381, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 134/380 (0.35)]
# Game: 382, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 134/381 (0.35)]
# WIN, Finished in: 0.8757579326629639(seconds)
# Game: 383, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 135/382 (0.35)]
# WIN, Finished in: 0.8907313346862793(seconds)
# Game: 384, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 136/383 (0.36)]
# Game: 385, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 136/384 (0.35)]
# Game: 386, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 136/385 (0.35)]
# Game: 387, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 136/386 (0.35)]
# WIN, Finished in: 1.0469038486480713(seconds)
# Game: 388, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 137/387 (0.35)]
# Game: 389, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 137/388 (0.35)]
# WIN, Finished in: 1.0313446521759033(seconds)
# Game: 390, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 138/389 (0.35)]
# Game: 391, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 138/390 (0.35)]
# Game: 392, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 138/391 (0.35)]
# Game: 393, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 138/392 (0.35)]
# WIN, Finished in: 0.8126740455627441(seconds)
# Game: 394, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 139/393 (0.35)]
# WIN, Finished in: 0.8751752376556396(seconds)
# Game: 395, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 140/394 (0.36)]
# Game: 396, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 140/395 (0.35)]
# WIN, Finished in: 28.84160828590393(seconds)
# Game: 397, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 141/396 (0.36)]
# Game: 398, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 141/397 (0.36)]
# Game: 399, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 141/398 (0.35)]
# WIN, Finished in: 4.65464448928833(seconds)
# Game: 400, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 142/399 (0.36)]
# WIN, Finished in: 27.37362790107727(seconds)
# Game: 401, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 143/400 (0.36)]
# Game: 402, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 143/401 (0.36)]
# Game: 403, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 143/402 (0.36)]
# WIN, Finished in: 1.2813217639923096(seconds)
# Game: 404, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 144/403 (0.36)]
# Game: 405, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 144/404 (0.36)]
# WIN, Finished in: 5.7485363483428955(seconds)
# Game: 406, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 145/405 (0.36)]
# Game: 407, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 145/406 (0.36)]
# Game: 408, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 145/407 (0.36)]
# Game: 409, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 145/408 (0.36)]
# WIN, Finished in: 95.58211779594421(seconds)
# Game: 410, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 146/409 (0.36)]
# WIN, Finished in: 0.7658307552337646(seconds)
# Game: 411, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 147/410 (0.36)]
# Game: 412, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 147/411 (0.36)]
# Game: 413, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 147/412 (0.36)]
# WIN, Finished in: 2.5993106365203857(seconds)
# Game: 414, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 148/413 (0.36)]
# Game: 415, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 148/414 (0.36)]
# Game: 416, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 148/415 (0.36)]
# Game: 417, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 148/416 (0.36)]
# WIN, Finished in: 0.7502105236053467(seconds)
# Game: 418, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 149/417 (0.36)]
# Game: 419, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 149/418 (0.36)]
# WIN, Finished in: 0.9375545978546143(seconds)
# Game: 420, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 150/419 (0.36)]
# Game: 421, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 150/420 (0.36)]
# Game: 422, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 150/421 (0.36)]
# Game: 423, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 150/422 (0.36)]
# Game: 424, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 150/423 (0.35)]
# Game: 425, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 150/424 (0.35)]
# WIN, Finished in: 0.8582174777984619(seconds)
# Game: 426, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 151/425 (0.36)]
# WIN, Finished in: 3.1582748889923096(seconds)
# Game: 427, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 152/426 (0.36)]
# Game: 428, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 152/427 (0.36)]
# Game: 429, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 152/428 (0.36)]
# Game: 430, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 152/429 (0.35)]
# WIN, Finished in: 1.8436949253082275(seconds)
# Game: 431, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 153/430 (0.36)]
# Game: 432, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 153/431 (0.35)]
# WIN, Finished in: 0.765833854675293(seconds)
# Game: 433, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 154/432 (0.36)]
# Game: 434, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 154/433 (0.36)]
# Game: 435, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 154/434 (0.35)]
# WIN, Finished in: 7.357122898101807(seconds)
# Game: 436, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 155/435 (0.36)]
# WIN, Finished in: 72.14254546165466(seconds)
# Game: 437, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 156/436 (0.36)]
# Game: 438, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 156/437 (0.36)]
# Game: 439, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 156/438 (0.36)]
# WIN, Finished in: 0.7810587882995605(seconds)
# Game: 440, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 157/439 (0.36)]
# WIN, Finished in: 1.1250133514404297(seconds)
# Game: 441, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 158/440 (0.36)]
# Game: 442, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 158/441 (0.36)]
# Game: 443, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 158/442 (0.36)]
# WIN, Finished in: 2.3726980686187744(seconds)
# Game: 444, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 159/443 (0.36)]
# WIN, Finished in: 0.89082932472229(seconds)
# Game: 445, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 160/444 (0.36)]
# WIN, Finished in: 0.9531891345977783(seconds)
# Game: 446, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 161/445 (0.36)]
# WIN, Finished in: 0.9484691619873047(seconds)
# Game: 447, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 162/446 (0.36)]
# WIN, Finished in: 3.746938943862915(seconds)
# Game: 448, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 163/447 (0.36)]
# Game: 449, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 163/448 (0.36)]
# Game: 450, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 163/449 (0.36)]
# WIN, Finished in: 1.7653567790985107(seconds)
# Game: 451, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 164/450 (0.36)]
# Game: 452, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 164/451 (0.36)]
# WIN, Finished in: 0.9277985095977783(seconds)
# Game: 453, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 165/452 (0.37)]
# Game: 454, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 165/453 (0.36)]
# Game: 455, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 165/454 (0.36)]
# Game: 456, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 165/455 (0.36)]
# Game: 457, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 165/456 (0.36)]
# WIN, Finished in: 290.18794298171997(seconds)
# Game: 458, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 166/457 (0.36)]
# WIN, Finished in: 1.3436930179595947(seconds)
# Game: 459, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 167/458 (0.36)]
# WIN, Finished in: 10.420586109161377(seconds)
# Game: 460, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 168/459 (0.37)]
# Game: 461, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 168/460 (0.37)]
# Game: 462, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 168/461 (0.36)]
# Game: 463, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 168/462 (0.36)]
# Game: 464, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 168/463 (0.36)]
# WIN, Finished in: 3.437579870223999(seconds)
# Game: 465, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 169/464 (0.36)]
# WIN, Finished in: 6.045421600341797(seconds)
# Game: 466, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 170/465 (0.37)]
# WIN, Finished in: 0.7970898151397705(seconds)
# Game: 467, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 171/466 (0.37)]
# Game: 468, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 171/467 (0.37)]
# Game: 469, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 171/468 (0.37)]
# Game: 470, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 171/469 (0.36)]
# Game: 471, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 171/470 (0.36)]
# WIN, Finished in: 0.7653791904449463(seconds)
# Game: 472, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 172/471 (0.37)]
# Game: 473, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 172/472 (0.36)]
# WIN, Finished in: 1.3251359462738037(seconds)
# Game: 474, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 173/473 (0.37)]
# Game: 475, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 173/474 (0.36)]
# Game: 476, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 173/475 (0.36)]
# WIN, Finished in: 0.7657351493835449(seconds)
# Game: 477, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 174/476 (0.37)]
# WIN, Finished in: 0.8907697200775146(seconds)
# Game: 478, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 175/477 (0.37)]
# Game: 479, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 175/478 (0.37)]
# Game: 480, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 175/479 (0.37)]
# Game: 481, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 175/480 (0.36)]
# WIN, Finished in: 5.669163465499878(seconds)
# Game: 482, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 176/481 (0.37)]
# Game: 483, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 176/482 (0.37)]
# Game: 484, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 176/483 (0.36)]
# WIN, Finished in: 1.5472211837768555(seconds)
# Game: 485, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 177/484 (0.37)]
# Game: 486, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 177/485 (0.36)]
# Game: 487, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 177/486 (0.36)]
# WIN, Finished in: 0.8282973766326904(seconds)
# Game: 488, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 178/487 (0.37)]
# Game: 489, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 178/488 (0.36)]
# WIN, Finished in: 7.995747804641724(seconds)
# Game: 490, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 179/489 (0.37)]
# WIN, Finished in: 0.7185986042022705(seconds)
# Game: 491, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 180/490 (0.37)]
# WIN, Finished in: 1.0002765655517578(seconds)
# Game: 492, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 181/491 (0.37)]
# Game: 493, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 181/492 (0.37)]
# WIN, Finished in: 3.7046470642089844(seconds)
# Game: 494, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 182/493 (0.37)]
# Game: 495, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 182/494 (0.37)]
# WIN, Finished in: 19.033079862594604(seconds)
# Game: 496, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 183/495 (0.37)]
# Game: 497, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 183/496 (0.37)]
# WIN, Finished in: 0.8439226150512695(seconds)
# Game: 498, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 184/497 (0.37)]
# Game: 499, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 184/498 (0.37)]
# Game: 500, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 184/499 (0.37)]
# Game: 501, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 184/500 (0.37)]
# Game: 502, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 184/501 (0.37)]
# Game: 503, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 184/502 (0.37)]
# Game: 504, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 184/503 (0.37)]
# WIN, Finished in: 2.4220364093780518(seconds)
# Game: 505, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 185/504 (0.37)]
# Game: 506, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 185/505 (0.37)]
# WIN, Finished in: 3.751934289932251(seconds)
# Game: 507, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 186/506 (0.37)]
# Game: 508, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 186/507 (0.37)]
# Game: 509, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 186/508 (0.37)]
# WIN, Finished in: 0.9532749652862549(seconds)
# Game: 510, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 187/509 (0.37)]
# Game: 511, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 187/510 (0.37)]
# Game: 512, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 187/511 (0.37)]
# Game: 513, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 187/512 (0.37)]
# Game: 514, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 187/513 (0.36)]
# WIN, Finished in: 2.8137705326080322(seconds)
# Game: 515, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 188/514 (0.37)]
# Game: 516, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 188/515 (0.37)]
# WIN, Finished in: 0.7345502376556396(seconds)
# Game: 517, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 189/516 (0.37)]
# WIN, Finished in: 11.779448509216309(seconds)
# Game: 518, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 190/517 (0.37)]
# WIN, Finished in: 2.0313708782196045(seconds)
# Game: 519, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 191/518 (0.37)]
# Game: 520, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 191/519 (0.37)]
# Game: 521, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 191/520 (0.37)]
# Game: 522, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 191/521 (0.37)]
# Game: 523, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 191/522 (0.37)]
# Game: 524, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 191/523 (0.37)]
# WIN, Finished in: 35.140448570251465(seconds)
# Game: 525, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 192/524 (0.37)]
# WIN, Finished in: 4.076623916625977(seconds)
# Game: 526, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 193/525 (0.37)]
# WIN, Finished in: 2.29706072807312(seconds)
# Game: 527, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 194/526 (0.37)]
# WIN, Finished in: 25.913261890411377(seconds)
# Game: 528, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 195/527 (0.37)]
# Game: 529, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 195/528 (0.37)]
# Game: 530, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 195/529 (0.37)]
# Game: 531, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 195/530 (0.37)]
# Game: 532, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 195/531 (0.37)]
# WIN, Finished in: 0.8438096046447754(seconds)
# Game: 533, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 196/532 (0.37)]
# WIN, Finished in: 0.9837918281555176(seconds)
# Game: 534, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 197/533 (0.37)]
# Game: 535, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 197/534 (0.37)]
# Game: 536, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 197/535 (0.37)]
# Game: 537, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 197/536 (0.37)]
# Game: 538, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 197/537 (0.37)]
# Game: 539, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 197/538 (0.37)]
# Game: 540, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 197/539 (0.37)]
# Game: 541, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 197/540 (0.36)]
# WIN, Finished in: 1.078603982925415(seconds)
# Game: 542, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 198/541 (0.37)]
# Game: 543, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 198/542 (0.37)]
# Game: 544, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 198/543 (0.36)]
# WIN, Finished in: 0.843895435333252(seconds)
# Game: 545, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 199/544 (0.37)]
# WIN, Finished in: 290.67320108413696(seconds)
# Game: 546, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 200/545 (0.37)]
# Game: 547, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 200/546 (0.37)]
# WIN, Finished in: 0.9064292907714844(seconds)
# Game: 548, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 201/547 (0.37)]
# WIN, Finished in: 0.8595163822174072(seconds)
# Game: 549, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 202/548 (0.37)]
# WIN, Finished in: 4.785073757171631(seconds)
# Game: 550, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 203/549 (0.37)]
# Game: 551, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 203/550 (0.37)]
# Game: 552, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 203/551 (0.37)]
# WIN, Finished in: 0.9075474739074707(seconds)
# Game: 553, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 204/552 (0.37)]
# WIN, Finished in: 0.8290939331054688(seconds)
# Game: 554, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 205/553 (0.37)]
# Game: 555, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 205/554 (0.37)]
# WIN, Finished in: 4.5650951862335205(seconds)
# Game: 556, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 206/555 (0.37)]
# Game: 557, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 206/556 (0.37)]
# Game: 558, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 206/557 (0.37)]
# Game: 559, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 206/558 (0.37)]
# Game: 560, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 206/559 (0.37)]
# Game: 561, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 206/560 (0.37)]
# WIN, Finished in: 0.8439426422119141(seconds)
# Game: 562, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 207/561 (0.37)]
# Game: 563, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 207/562 (0.37)]
# WIN, Finished in: 0.922067403793335(seconds)
# Game: 564, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 208/563 (0.37)]
# WIN, Finished in: 216.53470659255981(seconds)
# Game: 565, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 209/564 (0.37)]
# Game: 566, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 209/565 (0.37)]
# Game: 567, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 209/566 (0.37)]
# Game: 568, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 209/567 (0.37)]
# Game: 569, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 209/568 (0.37)]
# WIN, Finished in: 1.4687252044677734(seconds)
# Game: 570, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 210/569 (0.37)]
# Game: 571, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 210/570 (0.37)]
# Game: 572, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 210/571 (0.37)]
# Game: 573, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 210/572 (0.37)]
# WIN, Finished in: 1.5936555862426758(seconds)
# Game: 574, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 211/573 (0.37)]
# Game: 575, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 211/574 (0.37)]
# Game: 576, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 211/575 (0.37)]
# Game: 577, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 211/576 (0.37)]
# Game: 578, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 211/577 (0.37)]
# Game: 579, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 211/578 (0.37)]
# WIN, Finished in: 0.9216892719268799(seconds)
# Game: 580, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 212/579 (0.37)]
# Game: 581, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 212/580 (0.37)]
# Game: 582, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 212/581 (0.36)]
# Game: 583, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 212/582 (0.36)]
# WIN, Finished in: 8.313794612884521(seconds)
# Game: 584, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 213/583 (0.37)]
# Game: 585, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 213/584 (0.36)]
# Game: 586, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 213/585 (0.36)]
# Game: 587, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 213/586 (0.36)]
# Game: 588, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 213/587 (0.36)]
# Game: 589, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 213/588 (0.36)]
# WIN, Finished in: 24.218552350997925(seconds)
# Game: 590, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 214/589 (0.36)]
# WIN, Finished in: 128.25150084495544(seconds)
# Game: 591, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 215/590 (0.36)]
# WIN, Finished in: 0.8595378398895264(seconds)
# Game: 592, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 216/591 (0.37)]
# Game: 593, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 216/592 (0.36)]
# Game: 594, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 216/593 (0.36)]
# WIN, Finished in: 9.499932050704956(seconds)
# Game: 595, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 217/594 (0.37)]
# WIN, Finished in: 0.7658431529998779(seconds)
# Game: 596, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 218/595 (0.37)]
# WIN, Finished in: 2.48445200920105(seconds)
# Game: 597, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 219/596 (0.37)]
# Game: 598, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 219/597 (0.37)]
# Game: 599, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 219/598 (0.37)]
# Game: 600, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 219/599 (0.37)]
# Game: 601, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 219/600 (0.36)]
# WIN, Finished in: 0.7345137596130371(seconds)
# Game: 602, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 220/601 (0.37)]
# Game: 603, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 220/602 (0.37)]
# WIN, Finished in: 0.8400490283966064(seconds)
# Game: 604, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 221/603 (0.37)]
# WIN, Finished in: 2.7661147117614746(seconds)
# Game: 605, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 222/604 (0.37)]
# Game: 606, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 222/605 (0.37)]
# Game: 607, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 222/606 (0.37)]
# Game: 608, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 222/607 (0.37)]
# Game: 609, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 222/608 (0.37)]
# WIN, Finished in: 204.8612732887268(seconds)
# Game: 610, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 223/609 (0.37)]
# WIN, Finished in: 1.578014612197876(seconds)
# Game: 611, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 224/610 (0.37)]
# Game: 612, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 224/611 (0.37)]
# Game: 613, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 224/612 (0.37)]
# Game: 614, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 224/613 (0.37)]
# WIN, Finished in: 0.8126659393310547(seconds)
# Game: 615, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 225/614 (0.37)]
# Game: 616, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 225/615 (0.37)]
# Game: 617, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 225/616 (0.37)]
# Game: 618, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 225/617 (0.36)]
# WIN, Finished in: 0.8751134872436523(seconds)
# Game: 619, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 226/618 (0.37)]
# Game: 620, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 226/619 (0.37)]
# WIN, Finished in: 39.37756538391113(seconds)
# Game: 621, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 227/620 (0.37)]
# Game: 622, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 227/621 (0.37)]
# WIN, Finished in: 115.85866093635559(seconds)
# Game: 623, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 228/622 (0.37)]
# Game: 624, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 228/623 (0.37)]
# WIN, Finished in: 0.750190258026123(seconds)
# Game: 625, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 229/624 (0.37)]
# WIN, Finished in: 2.0781383514404297(seconds)
# Game: 626, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 230/625 (0.37)]
# Game: 627, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 230/626 (0.37)]
# Game: 628, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 230/627 (0.37)]
# WIN, Finished in: 3.000196695327759(seconds)
# Game: 629, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 231/628 (0.37)]
# WIN, Finished in: 0.8462822437286377(seconds)
# Game: 630, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 232/629 (0.37)]
# WIN, Finished in: 1.9575154781341553(seconds)
# Game: 631, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 233/630 (0.37)]
# WIN, Finished in: 171.73350620269775(seconds)
# Game: 632, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 234/631 (0.37)]
# Game: 633, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 234/632 (0.37)]
# WIN, Finished in: 0.7970168590545654(seconds)
# Game: 634, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 235/633 (0.37)]
# Game: 635, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 235/634 (0.37)]
# Game: 636, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 235/635 (0.37)]
# Game: 637, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 235/636 (0.37)]
# Game: 638, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 235/637 (0.37)]
# Game: 639, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 235/638 (0.37)]
# WIN, Finished in: 2.1634573936462402(seconds)
# Game: 640, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 236/639 (0.37)]
# Game: 641, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 236/640 (0.37)]
# Game: 642, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 236/641 (0.37)]
# Game: 643, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 236/642 (0.37)]
# Game: 644, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 236/643 (0.37)]
# Game: 645, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 236/644 (0.37)]
# Game: 646, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 236/645 (0.37)]
# Game: 647, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 236/646 (0.37)]
# Game: 648, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 236/647 (0.36)]
# WIN, Finished in: 77.51357054710388(seconds)
# Game: 649, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 237/648 (0.37)]
# Game: 650, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 237/649 (0.37)]
# Game: 651, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 237/650 (0.36)]
# Game: 652, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 237/651 (0.36)]
# Game: 653, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 237/652 (0.36)]
# WIN, Finished in: 0.9531674385070801(seconds)
# Game: 654, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 238/653 (0.36)]
# WIN, Finished in: 1.21242356300354(seconds)
# Game: 655, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 239/654 (0.37)]
# Game: 656, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 239/655 (0.36)]
# WIN, Finished in: 1.6406280994415283(seconds)
# Game: 657, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 240/656 (0.37)]
# Game: 658, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 240/657 (0.37)]
# Game: 659, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 240/658 (0.36)]
# WIN, Finished in: 1.4690866470336914(seconds)
# Game: 660, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 241/659 (0.37)]
# WIN, Finished in: 0.7336330413818359(seconds)
# Game: 661, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 242/660 (0.37)]
# WIN, Finished in: 193.48426842689514(seconds)
# Game: 662, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 243/661 (0.37)]
# WIN, Finished in: 0.8126668930053711(seconds)
# Game: 663, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 244/662 (0.37)]
# WIN, Finished in: 2.9379196166992188(seconds)
# Game: 664, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 245/663 (0.37)]
# Game: 665, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 245/664 (0.37)]
# Game: 666, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 245/665 (0.37)]
# Game: 667, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 245/666 (0.37)]
# WIN, Finished in: 1.5946080684661865(seconds)
# Game: 668, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 246/667 (0.37)]
# Game: 669, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 246/668 (0.37)]
# Game: 670, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 246/669 (0.37)]
# Game: 671, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 246/670 (0.37)]
# WIN, Finished in: 0.7643148899078369(seconds)
# Game: 672, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 247/671 (0.37)]
# WIN, Finished in: 4.5023417472839355(seconds)
# Game: 673, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 248/672 (0.37)]
# WIN, Finished in: 0.9231739044189453(seconds)
# Game: 674, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 249/673 (0.37)]
# Game: 675, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 249/674 (0.37)]
# Game: 676, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 249/675 (0.37)]
# WIN, Finished in: 0.8290832042694092(seconds)
# Game: 677, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 250/676 (0.37)]
# Game: 678, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 250/677 (0.37)]
# Game: 679, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 250/678 (0.37)]
# Game: 680, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 250/679 (0.37)]
# Game: 681, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 250/680 (0.37)]
# Game: 682, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 250/681 (0.37)]
# WIN, Finished in: 0.8751602172851562(seconds)
# Game: 683, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 251/682 (0.37)]
# Game: 684, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 251/683 (0.37)]
# WIN, Finished in: 4.472798109054565(seconds)
# Game: 685, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 252/684 (0.37)]
# WIN, Finished in: 52.74874234199524(seconds)
# Game: 686, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 253/685 (0.37)]
# WIN, Finished in: 0.7813527584075928(seconds)
# Game: 687, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 254/686 (0.37)]
# WIN, Finished in: 3.92057728767395(seconds)
# Game: 688, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 255/687 (0.37)]
# WIN, Finished in: 4.018149375915527(seconds)
# Game: 689, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 256/688 (0.37)]
# WIN, Finished in: 1.2968730926513672(seconds)
# Game: 690, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 257/689 (0.37)]
# WIN, Finished in: 1.8284199237823486(seconds)
# Game: 691, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 258/690 (0.37)]
# WIN, Finished in: 0.794553279876709(seconds)
# Game: 692, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 259/691 (0.37)]
# Game: 693, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 259/692 (0.37)]
# WIN, Finished in: 6.063049554824829(seconds)
# Game: 694, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 260/693 (0.38)]
# WIN, Finished in: 0.7814126014709473(seconds)
# Game: 695, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 261/694 (0.38)]
# Game: 696, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 261/695 (0.38)]
# Game: 697, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 261/696 (0.38)]
# Game: 698, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 261/697 (0.37)]
# Game: 699, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 261/698 (0.37)]
# WIN, Finished in: 2.2846028804779053(seconds)
# Game: 700, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 262/699 (0.37)]
# WIN, Finished in: 0.7501580715179443(seconds)
# Game: 701, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 263/700 (0.38)]
# Game: 702, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 263/701 (0.38)]
# WIN, Finished in: 290.7185344696045(seconds)
# Game: 703, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 264/702 (0.38)]
# Game: 704, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 264/703 (0.38)]
# Game: 705, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 264/704 (0.38)]
# Game: 706, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 264/705 (0.37)]
# Game: 707, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 264/706 (0.37)]
# WIN, Finished in: 172.17424416542053(seconds)
# Game: 708, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 265/707 (0.37)]
# WIN, Finished in: 0.7502200603485107(seconds)
# Game: 709, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 266/708 (0.38)]
# WIN, Finished in: 9.734435319900513(seconds)
# Game: 710, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 267/709 (0.38)]
# WIN, Finished in: 0.7657628059387207(seconds)
# Game: 711, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 268/710 (0.38)]
# Game: 712, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 268/711 (0.38)]
# WIN, Finished in: 0.891169548034668(seconds)
# Game: 713, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 269/712 (0.38)]
# WIN, Finished in: 246.81161999702454(seconds)
# Game: 714, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 270/713 (0.38)]
# Game: 715, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 270/714 (0.38)]
# Game: 716, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 270/715 (0.38)]
# Game: 717, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 270/716 (0.38)]
# Game: 718, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 270/717 (0.38)]
# Game: 719, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 270/718 (0.38)]
# Game: 720, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 270/719 (0.38)]
# Game: 721, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 270/720 (0.38)]
# Game: 722, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 270/721 (0.37)]
# WIN, Finished in: 4.172290563583374(seconds)
# Game: 723, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 271/722 (0.38)]
# WIN, Finished in: 0.79703688621521(seconds)
# Game: 724, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 272/723 (0.38)]
# WIN, Finished in: 11.07841157913208(seconds)
# Game: 725, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 273/724 (0.38)]
# WIN, Finished in: 8.872231006622314(seconds)
# Game: 726, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 274/725 (0.38)]
# Game: 727, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 274/726 (0.38)]
# Game: 728, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 274/727 (0.38)]
# WIN, Finished in: 2.2817492485046387(seconds)
# Game: 729, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 275/728 (0.38)]
# WIN, Finished in: 0.9063303470611572(seconds)
# Game: 730, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 276/729 (0.38)]
# Game: 731, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 276/730 (0.38)]
# WIN, Finished in: 0.8591976165771484(seconds)
# Game: 732, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 277/731 (0.38)]
# Game: 733, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 277/732 (0.38)]
# WIN, Finished in: 27.749838829040527(seconds)
# Game: 734, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 278/733 (0.38)]
# WIN, Finished in: 1.0314173698425293(seconds)
# Game: 735, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 279/734 (0.38)]
# Game: 736, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 279/735 (0.38)]
# Game: 737, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 279/736 (0.38)]
# Game: 738, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 279/737 (0.38)]
# WIN, Finished in: 91.2867066860199(seconds)
# Game: 739, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 280/738 (0.38)]
# WIN, Finished in: 0.7658169269561768(seconds)
# Game: 740, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 281/739 (0.38)]
# Game: 741, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 281/740 (0.38)]
# Game: 742, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 281/741 (0.38)]
# WIN, Finished in: 1.2031958103179932(seconds)
# Game: 743, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 282/742 (0.38)]
# WIN, Finished in: 0.8595459461212158(seconds)
# Game: 744, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 283/743 (0.38)]
# Game: 745, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 283/744 (0.38)]
# Game: 746, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 283/745 (0.38)]
# WIN, Finished in: 1.4864954948425293(seconds)
# Game: 747, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 284/746 (0.38)]
# WIN, Finished in: 6.8096396923065186(seconds)
# Game: 748, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 285/747 (0.38)]
# Game: 749, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 285/748 (0.38)]
# Game: 750, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 285/749 (0.38)]
# Game: 751, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 285/750 (0.38)]
# Game: 752, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 285/751 (0.38)]
# WIN, Finished in: 0.8437728881835938(seconds)
# Game: 753, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 286/752 (0.38)]
# WIN, Finished in: 0.8421750068664551(seconds)
# Game: 754, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 287/753 (0.38)]
# Game: 755, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 287/754 (0.38)]
# WIN, Finished in: 85.06201171875(seconds)
# Game: 756, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 288/755 (0.38)]
# Game: 757, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 288/756 (0.38)]
# WIN, Finished in: 0.7657852172851562(seconds)
# Game: 758, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 289/757 (0.38)]
# WIN, Finished in: 0.9064030647277832(seconds)
# Game: 759, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 290/758 (0.38)]
# WIN, Finished in: 1.0626232624053955(seconds)
# Game: 760, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 291/759 (0.38)]
# Game: 761, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 291/760 (0.38)]
# Game: 762, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 291/761 (0.38)]
# Game: 763, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 291/762 (0.38)]
# WIN, Finished in: 1.5781075954437256(seconds)
# Game: 764, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 292/763 (0.38)]
# WIN, Finished in: 90.31014919281006(seconds)
# Game: 765, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 293/764 (0.38)]
# Game: 766, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 293/765 (0.38)]
# WIN, Finished in: 0.8122222423553467(seconds)
# Game: 767, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 294/766 (0.38)]
# Game: 768, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 294/767 (0.38)]
# Game: 769, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 294/768 (0.38)]
# WIN, Finished in: 0.7657716274261475(seconds)
# Game: 770, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 295/769 (0.38)]
# WIN, Finished in: 0.7966029644012451(seconds)
# Game: 771, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 296/770 (0.38)]
# Game: 772, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 296/771 (0.38)]
# WIN, Finished in: 0.8439924716949463(seconds)
# Game: 773, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 297/772 (0.38)]
# WIN, Finished in: 0.7875010967254639(seconds)
# Game: 774, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 298/773 (0.39)]
# Game: 775, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 298/774 (0.39)]
# Game: 776, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 298/775 (0.38)]
# Game: 777, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 298/776 (0.38)]
# WIN, Finished in: 0.9219276905059814(seconds)
# Game: 778, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 299/777 (0.38)]
# WIN, Finished in: 28.488446712493896(seconds)
# Game: 779, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 300/778 (0.39)]
# Game: 780, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 300/779 (0.39)]
# WIN, Finished in: 6.219792604446411(seconds)
# Game: 781, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 301/780 (0.39)]
# Game: 782, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 301/781 (0.39)]
# WIN, Finished in: 0.8438370227813721(seconds)
# Game: 783, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 302/782 (0.39)]
# WIN, Finished in: 0.8907871246337891(seconds)
# Game: 784, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 303/783 (0.39)]
# WIN, Finished in: 0.9220249652862549(seconds)
# Game: 785, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 304/784 (0.39)]
# Game: 786, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 304/785 (0.39)]
# Game: 787, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 304/786 (0.39)]
# Game: 788, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 304/787 (0.39)]
# WIN, Finished in: 5.377255439758301(seconds)
# Game: 789, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 305/788 (0.39)]
# WIN, Finished in: 3.375562906265259(seconds)
# Game: 790, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 306/789 (0.39)]
# Game: 791, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 306/790 (0.39)]
# Game: 792, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 306/791 (0.39)]
# Game: 793, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 306/792 (0.39)]
# WIN, Finished in: 0.9644510746002197(seconds)
# Game: 794, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 307/793 (0.39)]
# WIN, Finished in: 0.8559169769287109(seconds)
# Game: 795, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 308/794 (0.39)]
# WIN, Finished in: 0.8861796855926514(seconds)
# Game: 796, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 309/795 (0.39)]
# Game: 797, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 309/796 (0.39)]
# WIN, Finished in: 11.126513719558716(seconds)
# Game: 798, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 310/797 (0.39)]
# WIN, Finished in: 1.47613525390625(seconds)
# Game: 799, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 311/798 (0.39)]
# WIN, Finished in: 134.92118048667908(seconds)
# Game: 800, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 312/799 (0.39)]
# WIN, Finished in: 0.8007228374481201(seconds)
# Game: 801, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 313/800 (0.39)]
# WIN, Finished in: 78.92694473266602(seconds)
# Game: 802, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 314/801 (0.39)]
# Game: 803, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 314/802 (0.39)]
# Game: 804, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 314/803 (0.39)]
# WIN, Finished in: 100.49938941001892(seconds)
# Game: 805, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 315/804 (0.39)]
# Game: 806, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 315/805 (0.39)]
# WIN, Finished in: 1.4368319511413574(seconds)
# Game: 807, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 316/806 (0.39)]
# WIN, Finished in: 21.263123273849487(seconds)
# Game: 808, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 317/807 (0.39)]
# Game: 809, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 317/808 (0.39)]
# WIN, Finished in: 290.5456359386444(seconds)
# Game: 810, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 318/809 (0.39)]
# WIN, Finished in: 29.031002283096313(seconds)
# Game: 811, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 319/810 (0.39)]
# Game: 812, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 319/811 (0.39)]
# WIN, Finished in: 0.9376685619354248(seconds)
# Game: 813, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 320/812 (0.39)]
# Game: 814, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 320/813 (0.39)]
# Game: 815, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 320/814 (0.39)]
# Game: 816, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 320/815 (0.39)]
# WIN, Finished in: 0.7810745239257812(seconds)
# Game: 817, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 321/816 (0.39)]
# Game: 818, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 321/817 (0.39)]
# Game: 819, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 321/818 (0.39)]
# WIN, Finished in: 0.8751575946807861(seconds)
# Game: 820, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 322/819 (0.39)]
# Game: 821, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 322/820 (0.39)]
# WIN, Finished in: 0.8595530986785889(seconds)
# Game: 822, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 323/821 (0.39)]
# WIN, Finished in: 1.656599998474121(seconds)
# Game: 823, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 324/822 (0.39)]
# Game: 824, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 324/823 (0.39)]
# Game: 825, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 324/824 (0.39)]
# WIN, Finished in: 88.85683155059814(seconds)
# Game: 826, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 325/825 (0.39)]
# WIN, Finished in: 0.8874750137329102(seconds)
# Game: 827, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 326/826 (0.39)]
# WIN, Finished in: 3.8594813346862793(seconds)
# Game: 828, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 327/827 (0.40)]
# WIN, Finished in: 13.157524585723877(seconds)
# Game: 829, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 328/828 (0.40)]
# WIN, Finished in: 5.470010042190552(seconds)
# Game: 830, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 329/829 (0.40)]
# Game: 831, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 329/830 (0.40)]
# WIN, Finished in: 27.716217756271362(seconds)
# Game: 832, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 330/831 (0.40)]
# WIN, Finished in: 0.7658448219299316(seconds)
# Game: 833, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 331/832 (0.40)]
# Game: 834, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 331/833 (0.40)]
# WIN, Finished in: 1.6919143199920654(seconds)
# Game: 835, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 332/834 (0.40)]
# Game: 836, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 332/835 (0.40)]
# Game: 837, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 332/836 (0.40)]
# WIN, Finished in: 2.3439524173736572(seconds)
# Game: 838, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 333/837 (0.40)]
# WIN, Finished in: 290.34503650665283(seconds)
# Game: 839, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 334/838 (0.40)]
# WIN, Finished in: 0.8559474945068359(seconds)
# Game: 840, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 335/839 (0.40)]
# Game: 841, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 335/840 (0.40)]
# Game: 842, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 335/841 (0.40)]
# WIN, Finished in: 3.361858367919922(seconds)
# Game: 843, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 336/842 (0.40)]
# Game: 844, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 336/843 (0.40)]
# Game: 845, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 336/844 (0.40)]
# Game: 846, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 336/845 (0.40)]
# WIN, Finished in: 0.7497813701629639(seconds)
# Game: 847, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 337/846 (0.40)]
# Game: 848, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 337/847 (0.40)]
# WIN, Finished in: 5.84325385093689(seconds)
# Game: 849, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 338/848 (0.40)]
# WIN, Finished in: 0.9218895435333252(seconds)
# Game: 850, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 339/849 (0.40)]
# Game: 851, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 339/850 (0.40)]
# Game: 852, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 339/851 (0.40)]
# Game: 853, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 339/852 (0.40)]
# Game: 854, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 339/853 (0.40)]
# Game: 855, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 339/854 (0.40)]
# Game: 856, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 339/855 (0.40)]
# WIN, Finished in: 2.1246373653411865(seconds)
# Game: 857, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 340/856 (0.40)]
# WIN, Finished in: 57.70403456687927(seconds)
# Game: 858, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 341/857 (0.40)]
# WIN, Finished in: 0.7963500022888184(seconds)
# Game: 859, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 342/858 (0.40)]
# Game: 860, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 342/859 (0.40)]
# Game: 861, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 342/860 (0.40)]
# Game: 862, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 342/861 (0.40)]
# Game: 863, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 342/862 (0.40)]
# WIN, Finished in: 1.5628118515014648(seconds)
# Game: 864, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 343/863 (0.40)]
# WIN, Finished in: 100.85464000701904(seconds)
# Game: 865, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 344/864 (0.40)]
# Game: 866, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 344/865 (0.40)]
# WIN, Finished in: 0.749798059463501(seconds)
# Game: 867, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 345/866 (0.40)]
# WIN, Finished in: 2.609727144241333(seconds)
# Game: 868, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 346/867 (0.40)]
# WIN, Finished in: 0.9097723960876465(seconds)
# Game: 869, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 347/868 (0.40)]
# WIN, Finished in: 0.8912351131439209(seconds)
# Game: 870, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 348/869 (0.40)]
# WIN, Finished in: 32.56445932388306(seconds)
# Game: 871, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 349/870 (0.40)]
# Game: 872, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 349/871 (0.40)]
# Game: 873, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 349/872 (0.40)]
# WIN, Finished in: 290.2039930820465(seconds)
# Game: 874, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 350/873 (0.40)]
# Game: 875, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 350/874 (0.40)]
# Game: 876, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 350/875 (0.40)]
# Game: 877, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 350/876 (0.40)]
# Game: 878, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 350/877 (0.40)]
# WIN, Finished in: 13.203073263168335(seconds)
# Game: 879, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 351/878 (0.40)]
# Game: 880, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 351/879 (0.40)]
# WIN, Finished in: 0.8436183929443359(seconds)
# Game: 881, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 352/880 (0.40)]
# Game: 882, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 352/881 (0.40)]
# WIN, Finished in: 2.9221174716949463(seconds)
# Game: 883, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 353/882 (0.40)]
# Game: 884, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 353/883 (0.40)]
# WIN, Finished in: 0.98453688621521(seconds)
# Game: 885, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 354/884 (0.40)]
# Game: 886, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 354/885 (0.40)]
# Game: 887, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 354/886 (0.40)]
# WIN, Finished in: 0.9429440498352051(seconds)
# Game: 888, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 355/887 (0.40)]
# Game: 889, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 355/888 (0.40)]
# WIN, Finished in: 290.15633940696716(seconds)
# Game: 890, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 356/889 (0.40)]
# WIN, Finished in: 1.7187354564666748(seconds)
# Game: 891, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 357/890 (0.40)]
# Game: 892, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 357/891 (0.40)]
# Game: 893, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 357/892 (0.40)]
# WIN, Finished in: 3.7970094680786133(seconds)
# Game: 894, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 358/893 (0.40)]
# Game: 895, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 358/894 (0.40)]
# Game: 896, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 358/895 (0.40)]
# Game: 897, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 358/896 (0.40)]
# WIN, Finished in: 2.126328468322754(seconds)
# Game: 898, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 359/897 (0.40)]
# Game: 899, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 359/898 (0.40)]
# WIN, Finished in: 0.8750491142272949(seconds)
# Game: 900, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 360/899 (0.40)]
# WIN, Finished in: 0.8591747283935547(seconds)
# Game: 901, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 361/900 (0.40)]
# WIN, Finished in: 17.266201972961426(seconds)
# Game: 902, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 362/901 (0.40)]
# Game: 903, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 362/902 (0.40)]
# Game: 904, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 362/903 (0.40)]
# Game: 905, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 362/904 (0.40)]
# Game: 906, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 362/905 (0.40)]
# Game: 907, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 362/906 (0.40)]
# WIN, Finished in: 118.99469804763794(seconds)
# Game: 908, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 363/907 (0.40)]
# WIN, Finished in: 0.7654306888580322(seconds)
# Game: 909, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 364/908 (0.40)]
# WIN, Finished in: 3.534788131713867(seconds)
# Game: 910, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 365/909 (0.40)]
# WIN, Finished in: 0.8125746250152588(seconds)
# Game: 911, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 366/910 (0.40)]
# Game: 912, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 366/911 (0.40)]
# Game: 913, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 366/912 (0.40)]
# Game: 914, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 366/913 (0.40)]
# WIN, Finished in: 12.637715101242065(seconds)
# Game: 915, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 367/914 (0.40)]
# WIN, Finished in: 0.8016941547393799(seconds)
# Game: 916, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 368/915 (0.40)]
# Game: 917, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 368/916 (0.40)]
# Game: 918, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 368/917 (0.40)]
# WIN, Finished in: 5.466928482055664(seconds)
# Game: 919, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 369/918 (0.40)]
# Game: 920, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 369/919 (0.40)]
# WIN, Finished in: 4.173744201660156(seconds)
# Game: 921, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 370/920 (0.40)]
# Game: 922, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 370/921 (0.40)]
# Game: 923, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 370/922 (0.40)]
# Game: 924, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 370/923 (0.40)]
# Game: 925, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 370/924 (0.40)]
# WIN, Finished in: 0.8278882503509521(seconds)
# Game: 926, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 371/925 (0.40)]
# Game: 927, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 371/926 (0.40)]
# Game: 928, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 371/927 (0.40)]
# Game: 929, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 371/928 (0.40)]
# WIN, Finished in: 4.4892258644104(seconds)
# Game: 930, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 372/929 (0.40)]
# WIN, Finished in: 2.4107861518859863(seconds)
# Game: 931, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 373/930 (0.40)]
# Game: 932, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 373/931 (0.40)]
# Game: 933, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 373/932 (0.40)]
# WIN, Finished in: 0.7501018047332764(seconds)
# Game: 934, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 374/933 (0.40)]
# Game: 935, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 374/934 (0.40)]
# WIN, Finished in: 1.0628657341003418(seconds)
# Game: 936, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 375/935 (0.40)]
# Game: 937, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 375/936 (0.40)]
# Game: 938, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 375/937 (0.40)]
# WIN, Finished in: 0.7809827327728271(seconds)
# Game: 939, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 376/938 (0.40)]
# Game: 940, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 376/939 (0.40)]
# Game: 941, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 376/940 (0.40)]
# Game: 942, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 376/941 (0.40)]
# Game: 943, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 376/942 (0.40)]
# Game: 944, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 376/943 (0.40)]
# Game: 945, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 376/944 (0.40)]
# Game: 946, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 376/945 (0.40)]
# WIN, Finished in: 1.2501296997070312(seconds)
# Game: 947, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 377/946 (0.40)]
# Game: 948, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 377/947 (0.40)]
# Game: 949, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 377/948 (0.40)]
# Game: 950, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 377/949 (0.40)]
# Game: 951, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 377/950 (0.40)]
# WIN, Finished in: 0.8119375705718994(seconds)
# Game: 952, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 378/951 (0.40)]
# Game: 953, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 378/952 (0.40)]
# WIN, Finished in: 0.9531774520874023(seconds)
# Game: 954, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 379/953 (0.40)]
# Game: 955, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 379/954 (0.40)]
# Game: 956, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 379/955 (0.40)]
# Game: 957, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 379/956 (0.40)]
# Game: 958, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 379/957 (0.40)]
# Game: 959, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 379/958 (0.40)]
# Game: 960, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 379/959 (0.40)]
# Game: 961, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 379/960 (0.39)]
# WIN, Finished in: 0.8663473129272461(seconds)
# Game: 962, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 380/961 (0.40)]
# WIN, Finished in: 11.735456466674805(seconds)
# Game: 963, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 381/962 (0.40)]
# WIN, Finished in: 0.7189624309539795(seconds)
# Game: 964, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 382/963 (0.40)]
# Game: 965, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 382/964 (0.40)]
# Game: 966, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 382/965 (0.40)]
# WIN, Finished in: 0.9688279628753662(seconds)
# Game: 967, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 383/966 (0.40)]
# WIN, Finished in: 0.8907015323638916(seconds)
# Game: 968, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 384/967 (0.40)]
# Game: 969, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 384/968 (0.40)]
# Game: 970, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 384/969 (0.40)]
# Game: 971, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 384/970 (0.40)]
# Game: 972, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 384/971 (0.40)]
# Game: 973, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 384/972 (0.40)]
# Game: 974, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 384/973 (0.39)]
# Game: 975, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 384/974 (0.39)]
# WIN, Finished in: 6.703652381896973(seconds)
# Game: 976, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 385/975 (0.39)]
# WIN, Finished in: 1.6871585845947266(seconds)
# Game: 977, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 386/976 (0.40)]
# Game: 978, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 386/977 (0.40)]
# Game: 979, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 386/978 (0.39)]
# WIN, Finished in: 43.32954788208008(seconds)
# Game: 980, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 387/979 (0.40)]
# Game: 981, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 387/980 (0.39)]
# WIN, Finished in: 10.626593112945557(seconds)
# Game: 982, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 388/981 (0.40)]
# Game: 983, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 388/982 (0.40)]
# Game: 984, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 388/983 (0.39)]
# Game: 985, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 388/984 (0.39)]
# WIN, Finished in: 0.9064171314239502(seconds)
# Game: 986, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 389/985 (0.39)]
# Game: 987, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 389/986 (0.39)]
# Game: 988, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 389/987 (0.39)]
# WIN, Finished in: 1.2965455055236816(seconds)
# Game: 989, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 390/988 (0.39)]
# WIN, Finished in: 39.42281413078308(seconds)
# Game: 990, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 391/989 (0.40)]
# WIN, Finished in: 0.7965996265411377(seconds)
# Game: 991, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 392/990 (0.40)]
# Game: 992, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 392/991 (0.40)]
# Game: 993, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 392/992 (0.40)]
# Game: 994, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 392/993 (0.39)]
# WIN, Finished in: 128.26478910446167(seconds)
# Game: 995, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 393/994 (0.40)]
# Game: 996, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 393/995 (0.39)]
# WIN, Finished in: 0.8752384185791016(seconds)
# Game: 997, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 394/996 (0.40)]
# WIN, Finished in: 1.9376685619354248(seconds)
# Game: 998, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 395/997 (0.40)]
# WIN, Finished in: 58.968125343322754(seconds)
# Game: 999, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 396/998 (0.40)]
# Game: 1000, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 396/999 (0.40)]
# Game: 1001, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 396/1000 (0.40)]
# Game: 1002, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 396/1001 (0.40)]
# WIN, Finished in: 0.9070703983306885(seconds)
# Game: 1003, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 397/1002 (0.40)]
# Game: 1004, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 397/1003 (0.40)]
# Game: 1005, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 397/1004 (0.40)]
# Game: 1006, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 397/1005 (0.40)]
# WIN, Finished in: 1.6558618545532227(seconds)
# Game: 1007, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 398/1006 (0.40)]
# Game: 1008, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 398/1007 (0.40)]
# Game: 1009, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 398/1008 (0.39)]
# WIN, Finished in: 1.2210144996643066(seconds)
# Game: 1010, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 399/1009 (0.40)]
# WIN, Finished in: 3.9688570499420166(seconds)
# Game: 1011, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 400/1010 (0.40)]
# Game: 1012, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 400/1011 (0.40)]
# Game: 1013, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 400/1012 (0.40)]
# WIN, Finished in: 0.7484033107757568(seconds)
# Game: 1014, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 401/1013 (0.40)]
# Game: 1015, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 401/1014 (0.40)]
# WIN, Finished in: 24.207820415496826(seconds)
# Game: 1016, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 402/1015 (0.40)]
# WIN, Finished in: 0.8839435577392578(seconds)
# Game: 1017, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 403/1016 (0.40)]
# Game: 1018, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 403/1017 (0.40)]
# Game: 1019, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 403/1018 (0.40)]
# WIN, Finished in: 0.9063622951507568(seconds)
# Game: 1020, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 404/1019 (0.40)]
# Game: 1021, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 404/1020 (0.40)]
# Game: 1022, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 404/1021 (0.40)]
# Game: 1023, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 404/1022 (0.40)]
# Game: 1024, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 404/1023 (0.39)]
# Game: 1025, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 404/1024 (0.39)]
# WIN, Finished in: 281.5323314666748(seconds)
# Game: 1026, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 405/1025 (0.40)]
# Game: 1027, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 405/1026 (0.39)]
# Game: 1028, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 405/1027 (0.39)]
# Game: 1029, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 405/1028 (0.39)]
# WIN, Finished in: 1.7963223457336426(seconds)
# Game: 1030, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 406/1029 (0.39)]
# Game: 1031, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 406/1030 (0.39)]
# WIN, Finished in: 12.108232736587524(seconds)
# Game: 1032, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 407/1031 (0.39)]
# WIN, Finished in: 0.7341697216033936(seconds)
# Game: 1033, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 408/1032 (0.40)]
# WIN, Finished in: 57.797415256500244(seconds)
# Game: 1034, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 409/1033 (0.40)]
# Game: 1035, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 409/1034 (0.40)]
# Game: 1036, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 409/1035 (0.40)]
# Game: 1037, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 409/1036 (0.39)]
# WIN, Finished in: 163.5467803478241(seconds)
# Game: 1038, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 410/1037 (0.40)]
# Game: 1039, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 410/1038 (0.39)]
# WIN, Finished in: 0.7280480861663818(seconds)
# Game: 1040, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 411/1039 (0.40)]
# WIN, Finished in: 41.76347780227661(seconds)
# Game: 1041, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 412/1040 (0.40)]
# WIN, Finished in: 63.064589977264404(seconds)
# Game: 1042, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 413/1041 (0.40)]
# WIN, Finished in: 3.345707416534424(seconds)
# Game: 1043, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 414/1042 (0.40)]
# Game: 1044, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 414/1043 (0.40)]
# Game: 1045, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 414/1044 (0.40)]
# Game: 1046, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 414/1045 (0.40)]
# Game: 1047, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 414/1046 (0.40)]
# Game: 1048, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 414/1047 (0.40)]
# Game: 1049, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 414/1048 (0.40)]
# WIN, Finished in: 290.46867394447327(seconds)
# Game: 1050, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 415/1049 (0.40)]
# Game: 1051, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 415/1050 (0.40)]
# Game: 1052, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 415/1051 (0.39)]
# WIN, Finished in: 1.004009485244751(seconds)
# Game: 1053, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 416/1052 (0.40)]
# WIN, Finished in: 1.0314044952392578(seconds)
# Game: 1054, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 417/1053 (0.40)]
# WIN, Finished in: 1.062608003616333(seconds)
# Game: 1055, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 418/1054 (0.40)]
# Game: 1056, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 418/1055 (0.40)]
# Game: 1057, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 418/1056 (0.40)]
# WIN, Finished in: 0.8927326202392578(seconds)
# Game: 1058, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 419/1057 (0.40)]
# WIN, Finished in: 1.6843454837799072(seconds)
# Game: 1059, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 420/1058 (0.40)]
# WIN, Finished in: 4.763797044754028(seconds)
# Game: 1060, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 421/1059 (0.40)]
# Game: 1061, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 421/1060 (0.40)]
# WIN, Finished in: 33.15651345252991(seconds)
# Game: 1062, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 422/1061 (0.40)]
# WIN, Finished in: 58.60906720161438(seconds)
# Game: 1063, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 423/1062 (0.40)]
# Game: 1064, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 423/1063 (0.40)]
# Game: 1065, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 423/1064 (0.40)]
# Game: 1066, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 423/1065 (0.40)]
# WIN, Finished in: 0.7341189384460449(seconds)
# Game: 1067, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 424/1066 (0.40)]
# Game: 1068, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 424/1067 (0.40)]
# Game: 1069, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 424/1068 (0.40)]
# WIN, Finished in: 290.53416204452515(seconds)
# Game: 1070, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 425/1069 (0.40)]
# Game: 1071, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 425/1070 (0.40)]
# Game: 1072, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 425/1071 (0.40)]
# Game: 1073, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 425/1072 (0.40)]
# WIN, Finished in: 6.063230991363525(seconds)
# Game: 1074, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 426/1073 (0.40)]
# Game: 1075, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 426/1074 (0.40)]
# Game: 1076, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 426/1075 (0.40)]
# Game: 1077, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 426/1076 (0.40)]
# WIN, Finished in: 126.9063081741333(seconds)
# Game: 1078, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 427/1077 (0.40)]
# WIN, Finished in: 0.7656412124633789(seconds)
# Game: 1079, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 428/1078 (0.40)]
# Game: 1080, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 428/1079 (0.40)]
# Game: 1081, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 428/1080 (0.40)]
# Game: 1082, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 428/1081 (0.40)]
# Game: 1083, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 428/1082 (0.40)]
# Game: 1084, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 428/1083 (0.40)]
# WIN, Finished in: 0.7342145442962646(seconds)
# Game: 1085, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 429/1084 (0.40)]
# WIN, Finished in: 1.031285047531128(seconds)
# Game: 1086, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 430/1085 (0.40)]
# Game: 1087, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 430/1086 (0.40)]
# Game: 1088, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 430/1087 (0.40)]
# WIN, Finished in: 0.7499535083770752(seconds)
# Game: 1089, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 431/1088 (0.40)]
# Game: 1090, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 431/1089 (0.40)]
# WIN, Finished in: 4.124957799911499(seconds)
# Game: 1091, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 432/1090 (0.40)]
# Game: 1092, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 432/1091 (0.40)]
# WIN, Finished in: 3.890730381011963(seconds)
# Game: 1093, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 433/1092 (0.40)]
# WIN, Finished in: 0.8128445148468018(seconds)
# Game: 1094, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 434/1093 (0.40)]
# Game: 1095, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 434/1094 (0.40)]
# WIN, Finished in: 2.171882152557373(seconds)
# Game: 1096, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 435/1095 (0.40)]
# Game: 1097, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 435/1096 (0.40)]
# Game: 1098, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 435/1097 (0.40)]
# WIN, Finished in: 1.218559980392456(seconds)
# Game: 1099, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 436/1098 (0.40)]
# WIN, Finished in: 0.9687936305999756(seconds)
# Game: 1100, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 437/1099 (0.40)]
# Game: 1101, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 437/1100 (0.40)]
# WIN, Finished in: 4.359374523162842(seconds)
# Game: 1102, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 438/1101 (0.40)]
# Game: 1103, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 438/1102 (0.40)]
# Game: 1104, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 438/1103 (0.40)]
# Game: 1105, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 438/1104 (0.40)]
# Game: 1106, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 438/1105 (0.40)]
# Game: 1107, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 438/1106 (0.40)]
# Game: 1108, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 438/1107 (0.40)]
# WIN, Finished in: 0.7659091949462891(seconds)
# Game: 1109, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 439/1108 (0.40)]
# Game: 1110, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 439/1109 (0.40)]
# WIN, Finished in: 5.890683889389038(seconds)
# Game: 1111, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 440/1110 (0.40)]
# WIN, Finished in: 0.8905644416809082(seconds)
# Game: 1112, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 441/1111 (0.40)]
# Game: 1113, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 441/1112 (0.40)]
# Game: 1114, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 441/1113 (0.40)]
# WIN, Finished in: 0.9524927139282227(seconds)
# Game: 1115, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 442/1114 (0.40)]
# WIN, Finished in: 211.14053606987(seconds)
# Game: 1116, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 443/1115 (0.40)]
# Game: 1117, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 443/1116 (0.40)]
# Game: 1118, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 443/1117 (0.40)]
# Game: 1119, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 443/1118 (0.40)]
# Game: 1120, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 443/1119 (0.40)]
# WIN, Finished in: 0.734325647354126(seconds)
# Game: 1121, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 444/1120 (0.40)]
# Game: 1122, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 444/1121 (0.40)]
# Game: 1123, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 444/1122 (0.40)]
# WIN, Finished in: 2.2187652587890625(seconds)
# Game: 1124, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 445/1123 (0.40)]
# WIN, Finished in: 0.9534742832183838(seconds)
# Game: 1125, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 446/1124 (0.40)]
# Game: 1126, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 446/1125 (0.40)]
# WIN, Finished in: 1.171724557876587(seconds)
# Game: 1127, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 447/1126 (0.40)]
# Game: 1128, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 447/1127 (0.40)]
# Game: 1129, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 447/1128 (0.40)]
# WIN, Finished in: 290.32796835899353(seconds)
# Game: 1130, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 448/1129 (0.40)]
# WIN, Finished in: 88.59023857116699(seconds)
# Game: 1131, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 449/1130 (0.40)]
# WIN, Finished in: 10.21206283569336(seconds)
# Game: 1132, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 450/1131 (0.40)]
# WIN, Finished in: 0.796269416809082(seconds)
# Game: 1133, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 451/1132 (0.40)]
# WIN, Finished in: 79.31244945526123(seconds)
# Game: 1134, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 452/1133 (0.40)]
# WIN, Finished in: 4.999881267547607(seconds)
# Game: 1135, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 453/1134 (0.40)]
# Game: 1136, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 453/1135 (0.40)]
# WIN, Finished in: 0.8594341278076172(seconds)
# Game: 1137, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 454/1136 (0.40)]
# WIN, Finished in: 0.922222375869751(seconds)
# Game: 1138, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 455/1137 (0.40)]
# WIN, Finished in: 0.8749678134918213(seconds)
# Game: 1139, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 456/1138 (0.40)]
# Game: 1140, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 456/1139 (0.40)]
# Game: 1141, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 456/1140 (0.40)]
# WIN, Finished in: 0.8592801094055176(seconds)
# Game: 1142, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 457/1141 (0.40)]
# Game: 1143, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 457/1142 (0.40)]
# Game: 1144, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 457/1143 (0.40)]
# WIN, Finished in: 0.9997122287750244(seconds)
# Game: 1145, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 458/1144 (0.40)]
# Game: 1146, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 458/1145 (0.40)]
# WIN, Finished in: 0.9997365474700928(seconds)
# Game: 1147, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 459/1146 (0.40)]
# Game: 1148, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 459/1147 (0.40)]
# Game: 1149, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 459/1148 (0.40)]
# Game: 1150, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 459/1149 (0.40)]
# Game: 1151, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 459/1150 (0.40)]
# WIN, Finished in: 0.7660605907440186(seconds)
# Game: 1152, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 460/1151 (0.40)]
# Game: 1153, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 460/1152 (0.40)]
# WIN, Finished in: 0.7503969669342041(seconds)
# Game: 1154, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 461/1153 (0.40)]
# WIN, Finished in: 0.9214115142822266(seconds)
# Game: 1155, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 462/1154 (0.40)]
# Game: 1156, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 462/1155 (0.40)]
# Game: 1157, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 462/1156 (0.40)]
# Game: 1158, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 462/1157 (0.40)]
# Game: 1159, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 462/1158 (0.40)]
# Game: 1160, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 462/1159 (0.40)]
# WIN, Finished in: 0.7343106269836426(seconds)
# Game: 1161, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 463/1160 (0.40)]
# WIN, Finished in: 5.031334400177002(seconds)
# Game: 1162, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 464/1161 (0.40)]
# WIN, Finished in: 20.59368395805359(seconds)
# Game: 1163, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 465/1162 (0.40)]
# WIN, Finished in: 0.8284614086151123(seconds)
# Game: 1164, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 466/1163 (0.40)]
# Game: 1165, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 466/1164 (0.40)]
# Game: 1166, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 466/1165 (0.40)]
# Game: 1167, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 466/1166 (0.40)]
# WIN, Finished in: 1.859422206878662(seconds)
# Game: 1168, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 467/1167 (0.40)]
# Game: 1169, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 467/1168 (0.40)]
# Game: 1170, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 467/1169 (0.40)]
# WIN, Finished in: 0.9221413135528564(seconds)
# Game: 1171, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 468/1170 (0.40)]
# Game: 1172, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 468/1171 (0.40)]
# Game: 1173, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 468/1172 (0.40)]
# WIN, Finished in: 1.3746514320373535(seconds)
# Game: 1174, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 469/1173 (0.40)]
# WIN, Finished in: 2.4687724113464355(seconds)
# Game: 1175, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 470/1174 (0.40)]
# WIN, Finished in: 0.9866974353790283(seconds)
# Game: 1176, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 471/1175 (0.40)]
# WIN, Finished in: 0.901848316192627(seconds)
# Game: 1177, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 472/1176 (0.40)]
# Game: 1178, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 472/1177 (0.40)]
# Game: 1179, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 472/1178 (0.40)]
# Game: 1180, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 472/1179 (0.40)]
# WIN, Finished in: 57.452996253967285(seconds)
# Game: 1181, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 473/1180 (0.40)]
# Game: 1182, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 473/1181 (0.40)]
# WIN, Finished in: 0.9344546794891357(seconds)
# Game: 1183, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 474/1182 (0.40)]
# WIN, Finished in: 0.9000570774078369(seconds)
# Game: 1184, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 475/1183 (0.40)]
# WIN, Finished in: 1.0626251697540283(seconds)
# Game: 1185, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 476/1184 (0.40)]
# Game: 1186, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 476/1185 (0.40)]
# WIN, Finished in: 0.827660083770752(seconds)
# Game: 1187, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 477/1186 (0.40)]
# Game: 1188, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 477/1187 (0.40)]
# Game: 1189, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 477/1188 (0.40)]
# Game: 1190, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 477/1189 (0.40)]
# Game: 1191, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 477/1190 (0.40)]
# Game: 1192, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 477/1191 (0.40)]
# Game: 1193, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 477/1192 (0.40)]
# Game: 1194, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 477/1193 (0.40)]
# WIN, Finished in: 42.31237006187439(seconds)
# Game: 1195, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 478/1194 (0.40)]
# WIN, Finished in: 0.7655680179595947(seconds)
# Game: 1196, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 479/1195 (0.40)]
# WIN, Finished in: 0.8910810947418213(seconds)
# Game: 1197, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 480/1196 (0.40)]
# Game: 1198, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 480/1197 (0.40)]
# WIN, Finished in: 0.8745594024658203(seconds)
# Game: 1199, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 481/1198 (0.40)]
# WIN, Finished in: 246.77254009246826(seconds)
# Game: 1200, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 482/1199 (0.40)]
# WIN, Finished in: 3.4031457901000977(seconds)
# Game: 1201, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 483/1200 (0.40)]
# Game: 1202, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 483/1201 (0.40)]
# WIN, Finished in: 0.8907015323638916(seconds)
# Game: 1203, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 484/1202 (0.40)]
# Game: 1204, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 484/1203 (0.40)]
# Game: 1205, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 484/1204 (0.40)]
# WIN, Finished in: 3.218662977218628(seconds)
# Game: 1206, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 485/1205 (0.40)]
# Game: 1207, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 485/1206 (0.40)]
# Game: 1208, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 485/1207 (0.40)]
# Game: 1209, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 485/1208 (0.40)]
# Game: 1210, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 485/1209 (0.40)]
# Game: 1211, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 485/1210 (0.40)]
# WIN, Finished in: 0.7402148246765137(seconds)
# Game: 1212, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 486/1211 (0.40)]
# Game: 1213, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 486/1212 (0.40)]
# WIN, Finished in: 1.9531524181365967(seconds)
# Game: 1214, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 487/1213 (0.40)]
# Game: 1215, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 487/1214 (0.40)]
# Game: 1216, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 487/1215 (0.40)]
# Game: 1217, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 487/1216 (0.40)]
# Game: 1218, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 487/1217 (0.40)]
# Game: 1219, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 487/1218 (0.40)]
# Game: 1220, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 487/1219 (0.40)]
# WIN, Finished in: 1.7030577659606934(seconds)
# Game: 1221, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 488/1220 (0.40)]
# WIN, Finished in: 26.70307731628418(seconds)
# Game: 1222, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 489/1221 (0.40)]
# WIN, Finished in: 3.9847474098205566(seconds)
# Game: 1223, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 490/1222 (0.40)]
# WIN, Finished in: 6.608900308609009(seconds)
# Game: 1224, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 491/1223 (0.40)]
# WIN, Finished in: 0.7625799179077148(seconds)
# Game: 1225, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 492/1224 (0.40)]
# WIN, Finished in: 58.160032749176025(seconds)
# Game: 1226, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 493/1225 (0.40)]
# WIN, Finished in: 0.8432855606079102(seconds)
# Game: 1227, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 494/1226 (0.40)]
# WIN, Finished in: 155.65600657463074(seconds)
# Game: 1228, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 495/1227 (0.40)]
# WIN, Finished in: 1.0937657356262207(seconds)
# Game: 1229, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 496/1228 (0.40)]
# Game: 1230, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 496/1229 (0.40)]
# Game: 1231, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 496/1230 (0.40)]
# Game: 1232, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 496/1231 (0.40)]
# WIN, Finished in: 1.8437795639038086(seconds)
# Game: 1233, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 497/1232 (0.40)]
# Game: 1234, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 497/1233 (0.40)]
# Game: 1235, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 497/1234 (0.40)]
# Game: 1236, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 497/1235 (0.40)]
# WIN, Finished in: 1.0001468658447266(seconds)
# Game: 1237, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 498/1236 (0.40)]
# Game: 1238, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 498/1237 (0.40)]
# Game: 1239, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 498/1238 (0.40)]
# WIN, Finished in: 9.609338998794556(seconds)
# Game: 1240, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 499/1239 (0.40)]
# Game: 1241, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 499/1240 (0.40)]
# Game: 1242, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 499/1241 (0.40)]
# WIN, Finished in: 1.1563701629638672(seconds)
# Game: 1243, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 500/1242 (0.40)]
# WIN, Finished in: 0.8592691421508789(seconds)
# Game: 1244, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 501/1243 (0.40)]
# WIN, Finished in: 88.42211532592773(seconds)
# Game: 1245, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 502/1244 (0.40)]
# WIN, Finished in: 58.93768525123596(seconds)
# Game: 1246, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 503/1245 (0.40)]
# Game: 1247, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 503/1246 (0.40)]
# Game: 1248, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 503/1247 (0.40)]
# Game: 1249, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 503/1248 (0.40)]
# Game: 1250, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 503/1249 (0.40)]
# WIN, Finished in: 2.0315754413604736(seconds)
# Game: 1251, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 504/1250 (0.40)]
# Game: 1252, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 504/1251 (0.40)]
# WIN, Finished in: 2.330519199371338(seconds)
# Game: 1253, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 505/1252 (0.40)]
# WIN, Finished in: 71.42583084106445(seconds)
# Game: 1254, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 506/1253 (0.40)]
# WIN, Finished in: 0.7812130451202393(seconds)
# Game: 1255, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 507/1254 (0.40)]
# WIN, Finished in: 3.5157949924468994(seconds)
# Game: 1256, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 508/1255 (0.40)]
# WIN, Finished in: 1.1096487045288086(seconds)
# Game: 1257, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 509/1256 (0.41)]
# Game: 1258, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 509/1257 (0.40)]
# Game: 1259, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 509/1258 (0.40)]
# WIN, Finished in: 22.45348620414734(seconds)
# Game: 1260, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 510/1259 (0.41)]
# Game: 1261, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 510/1260 (0.40)]
# WIN, Finished in: 1.125007152557373(seconds)
# Game: 1262, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 511/1261 (0.41)]
# WIN, Finished in: 2.4062654972076416(seconds)
# Game: 1263, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 512/1262 (0.41)]
# WIN, Finished in: 290.7145993709564(seconds)
# Game: 1264, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 513/1263 (0.41)]
# WIN, Finished in: 1.5264480113983154(seconds)
# Game: 1265, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 514/1264 (0.41)]
# WIN, Finished in: 1.0152816772460938(seconds)
# Game: 1266, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 515/1265 (0.41)]
# WIN, Finished in: 0.8593897819519043(seconds)
# Game: 1267, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 516/1266 (0.41)]
# WIN, Finished in: 1.3284637928009033(seconds)
# Game: 1268, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 517/1267 (0.41)]
# WIN, Finished in: 0.9059226512908936(seconds)
# Game: 1269, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 518/1268 (0.41)]
# Game: 1270, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 518/1269 (0.41)]
# Game: 1271, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 518/1270 (0.41)]
# WIN, Finished in: 54.35931897163391(seconds)
# Game: 1272, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 519/1271 (0.41)]
# Game: 1273, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 519/1272 (0.41)]
# Game: 1274, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 519/1273 (0.41)]
# Game: 1275, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 519/1274 (0.41)]
# WIN, Finished in: 0.8721466064453125(seconds)
# Game: 1276, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 520/1275 (0.41)]
# Game: 1277, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 520/1276 (0.41)]
# Game: 1278, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 520/1277 (0.41)]
# Game: 1279, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 520/1278 (0.41)]
# Game: 1280, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 520/1279 (0.41)]
# Game: 1281, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 520/1280 (0.41)]
# WIN, Finished in: 1.8137407302856445(seconds)
# Game: 1282, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 521/1281 (0.41)]
# Game: 1283, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 521/1282 (0.41)]
# WIN, Finished in: 0.7656304836273193(seconds)
# Game: 1284, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 522/1283 (0.41)]
# Game: 1285, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 522/1284 (0.41)]
# Game: 1286, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 522/1285 (0.41)]
# Game: 1287, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 522/1286 (0.41)]
# Game: 1288, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 522/1287 (0.41)]
# Game: 1289, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 522/1288 (0.41)]
# WIN, Finished in: 13.343640327453613(seconds)
# Game: 1290, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 523/1289 (0.41)]
# Game: 1291, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 523/1290 (0.41)]
# WIN, Finished in: 8.031314373016357(seconds)
# Game: 1292, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 524/1291 (0.41)]
# Game: 1293, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 524/1292 (0.41)]
# Game: 1294, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 524/1293 (0.41)]
# Game: 1295, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 524/1294 (0.40)]
# WIN, Finished in: 3.2498891353607178(seconds)
# Game: 1296, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 525/1295 (0.41)]
# WIN, Finished in: 1.531623125076294(seconds)
# Game: 1297, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 526/1296 (0.41)]
# Game: 1298, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 526/1297 (0.41)]
# WIN, Finished in: 0.8124845027923584(seconds)
# Game: 1299, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 527/1298 (0.41)]
# Game: 1300, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 527/1299 (0.41)]
# Game: 1301, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 527/1300 (0.41)]
# Game: 1302, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 527/1301 (0.41)]
# Game: 1303, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 527/1302 (0.40)]
# WIN, Finished in: 4.156221389770508(seconds)
# Game: 1304, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 528/1303 (0.41)]
# WIN, Finished in: 0.8594598770141602(seconds)
# Game: 1305, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 529/1304 (0.41)]
# Game: 1306, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 529/1305 (0.41)]
# WIN, Finished in: 33.40629434585571(seconds)
# Game: 1307, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 530/1306 (0.41)]
# WIN, Finished in: 0.7499432563781738(seconds)
# Game: 1308, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 531/1307 (0.41)]
# Game: 1309, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 531/1308 (0.41)]
# Game: 1310, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 531/1309 (0.41)]
# Game: 1311, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 531/1310 (0.41)]
# Game: 1312, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 531/1311 (0.41)]
# Game: 1313, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 531/1312 (0.40)]
# Game: 1314, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 531/1313 (0.40)]
# Game: 1315, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 531/1314 (0.40)]
# WIN, Finished in: 2.546830892562866(seconds)
# Game: 1316, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 532/1315 (0.40)]
# Game: 1317, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 532/1316 (0.40)]
# Game: 1318, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 532/1317 (0.40)]
# WIN, Finished in: 6.531174659729004(seconds)
# Game: 1319, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 533/1318 (0.40)]
# Game: 1320, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 533/1319 (0.40)]
# Game: 1321, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 533/1320 (0.40)]
# Game: 1322, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 533/1321 (0.40)]
# Game: 1323, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 533/1322 (0.40)]
# Game: 1324, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 533/1323 (0.40)]
# Game: 1325, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 533/1324 (0.40)]
# Game: 1326, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 533/1325 (0.40)]
# Game: 1327, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 533/1326 (0.40)]
# WIN, Finished in: 4.281086444854736(seconds)
# Game: 1328, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 534/1327 (0.40)]
# Game: 1329, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 534/1328 (0.40)]
# WIN, Finished in: 5.5619635581970215(seconds)
# Game: 1330, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 535/1329 (0.40)]
# Game: 1331, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 535/1330 (0.40)]
# Game: 1332, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 535/1331 (0.40)]
# WIN, Finished in: 119.62499165534973(seconds)
# Game: 1333, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 536/1332 (0.40)]
# Game: 1334, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 536/1333 (0.40)]
# Game: 1335, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 536/1334 (0.40)]
# Game: 1336, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 536/1335 (0.40)]
# WIN, Finished in: 1.0626678466796875(seconds)
# Game: 1337, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 537/1336 (0.40)]
# Game: 1338, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 537/1337 (0.40)]
# WIN, Finished in: 10.750000238418579(seconds)
# Game: 1339, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 538/1338 (0.40)]
# WIN, Finished in: 0.8125584125518799(seconds)
# Game: 1340, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 539/1339 (0.40)]
# Game: 1341, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 539/1340 (0.40)]
# Game: 1342, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 539/1341 (0.40)]
# WIN, Finished in: 0.8749897480010986(seconds)
# Game: 1343, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 540/1342 (0.40)]
# Game: 1344, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 540/1343 (0.40)]
# Game: 1345, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 540/1344 (0.40)]
# Game: 1346, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 540/1345 (0.40)]
# Game: 1347, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 540/1346 (0.40)]
# WIN, Finished in: 1.891024112701416(seconds)
# Game: 1348, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 541/1347 (0.40)]
# WIN, Finished in: 100.68721437454224(seconds)
# Game: 1349, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 542/1348 (0.40)]
# Game: 1350, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 542/1349 (0.40)]
# Game: 1351, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 542/1350 (0.40)]
# WIN, Finished in: 1.0311665534973145(seconds)
# Game: 1352, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 543/1351 (0.40)]
# WIN, Finished in: 4.187839508056641(seconds)
# Game: 1353, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 544/1352 (0.40)]
# Game: 1354, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 544/1353 (0.40)]
# WIN, Finished in: 1.8749780654907227(seconds)
# Game: 1355, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 545/1354 (0.40)]
# Game: 1356, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 545/1355 (0.40)]
# Game: 1357, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 545/1356 (0.40)]
# Game: 1358, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 545/1357 (0.40)]
# WIN, Finished in: 1.0154099464416504(seconds)
# Game: 1359, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 546/1358 (0.40)]
# WIN, Finished in: 0.9842655658721924(seconds)
# Game: 1360, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 547/1359 (0.40)]
# Game: 1361, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 547/1360 (0.40)]
# Game: 1362, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 547/1361 (0.40)]
# WIN, Finished in: 5.312487363815308(seconds)
# Game: 1363, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 548/1362 (0.40)]
# WIN, Finished in: 0.7656550407409668(seconds)
# Game: 1364, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 549/1363 (0.40)]
# Game: 1365, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 549/1364 (0.40)]
# WIN, Finished in: 0.7333412170410156(seconds)
# Game: 1366, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 550/1365 (0.40)]
# Game: 1367, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 550/1366 (0.40)]
# WIN, Finished in: 13.26589322090149(seconds)
# Game: 1368, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 551/1367 (0.40)]
# WIN, Finished in: 0.8280622959136963(seconds)
# Game: 1369, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 552/1368 (0.40)]
# WIN, Finished in: 0.812267541885376(seconds)
# Game: 1370, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 553/1369 (0.40)]
# WIN, Finished in: 0.890557050704956(seconds)
# Game: 1371, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 554/1370 (0.40)]
# Game: 1372, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 554/1371 (0.40)]
# WIN, Finished in: 0.9375414848327637(seconds)
# Game: 1373, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 555/1372 (0.40)]
# Game: 1374, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 555/1373 (0.40)]
# WIN, Finished in: 0.8439846038818359(seconds)
# Game: 1375, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 556/1374 (0.40)]
# Game: 1376, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 556/1375 (0.40)]
# WIN, Finished in: 290.21874022483826(seconds)
# Game: 1377, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 557/1376 (0.40)]
# Game: 1378, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 557/1377 (0.40)]
# Game: 1379, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 557/1378 (0.40)]
# WIN, Finished in: 5.702692270278931(seconds)
# Game: 1380, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 558/1379 (0.40)]
# WIN, Finished in: 1.3124303817749023(seconds)
# Game: 1381, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 559/1380 (0.41)]
# Game: 1382, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 559/1381 (0.40)]
# Game: 1383, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 559/1382 (0.40)]
# Game: 1384, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 559/1383 (0.40)]
# Game: 1385, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 559/1384 (0.40)]
# Game: 1386, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 559/1385 (0.40)]
# Game: 1387, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 559/1386 (0.40)]
# Game: 1388, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 559/1387 (0.40)]
# Game: 1389, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 559/1388 (0.40)]
# WIN, Finished in: 0.765343189239502(seconds)
# Game: 1390, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 560/1389 (0.40)]
# Game: 1391, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 560/1390 (0.40)]
# Game: 1392, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 560/1391 (0.40)]
# WIN, Finished in: 2.703178882598877(seconds)
# Game: 1393, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 561/1392 (0.40)]
# WIN, Finished in: 0.7655131816864014(seconds)
# Game: 1394, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 562/1393 (0.40)]
# Game: 1395, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 562/1394 (0.40)]
# Game: 1396, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 562/1395 (0.40)]
# Game: 1397, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 562/1396 (0.40)]
# Game: 1398, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 562/1397 (0.40)]
# Game: 1399, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 562/1398 (0.40)]
# WIN, Finished in: 3.6093599796295166(seconds)
# Game: 1400, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 563/1399 (0.40)]
# WIN, Finished in: 0.9216735363006592(seconds)
# Game: 1401, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 564/1400 (0.40)]
# WIN, Finished in: 0.8904247283935547(seconds)
# Game: 1402, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 565/1401 (0.40)]
# WIN, Finished in: 11.018656969070435(seconds)
# Game: 1403, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 566/1402 (0.40)]
# Game: 1404, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 566/1403 (0.40)]
# Game: 1405, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 566/1404 (0.40)]
# WIN, Finished in: 0.7474949359893799(seconds)
# Game: 1406, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 567/1405 (0.40)]
# Game: 1407, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 567/1406 (0.40)]
# WIN, Finished in: 1.3437528610229492(seconds)
# Game: 1408, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 568/1407 (0.40)]
# WIN, Finished in: 76.06683778762817(seconds)
# Game: 1409, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 569/1408 (0.40)]
# Game: 1410, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 569/1409 (0.40)]
# Game: 1411, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 569/1410 (0.40)]
# WIN, Finished in: 1.386293649673462(seconds)
# Game: 1412, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 570/1411 (0.40)]
# Game: 1413, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 570/1412 (0.40)]
# WIN, Finished in: 71.94930720329285(seconds)
# Game: 1414, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 571/1413 (0.40)]
# Game: 1415, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 571/1414 (0.40)]
# Game: 1416, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 571/1415 (0.40)]
# Game: 1417, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 571/1416 (0.40)]
# Game: 1418, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 571/1417 (0.40)]
# Game: 1419, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 571/1418 (0.40)]
# WIN, Finished in: 3.375027656555176(seconds)
# Game: 1420, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 572/1419 (0.40)]
# Game: 1421, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 572/1420 (0.40)]
# WIN, Finished in: 1.980130910873413(seconds)
# Game: 1422, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 573/1421 (0.40)]
# Game: 1423, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 573/1422 (0.40)]
# Game: 1424, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 573/1423 (0.40)]
# Game: 1425, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 573/1424 (0.40)]
# WIN, Finished in: 0.9841461181640625(seconds)
# Game: 1426, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 574/1425 (0.40)]
# WIN, Finished in: 187.75645971298218(seconds)
# Game: 1427, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 575/1426 (0.40)]
# WIN, Finished in: 0.7591452598571777(seconds)
# Game: 1428, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 576/1427 (0.40)]
# Game: 1429, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 576/1428 (0.40)]
# Game: 1430, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 576/1429 (0.40)]
# WIN, Finished in: 25.698749542236328(seconds)
# Game: 1431, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 577/1430 (0.40)]
# Game: 1432, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 577/1431 (0.40)]
# WIN, Finished in: 5.781734228134155(seconds)
# Game: 1433, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 578/1432 (0.40)]
# WIN, Finished in: 0.9370479583740234(seconds)
# Game: 1434, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 579/1433 (0.40)]
# WIN, Finished in: 3.3132243156433105(seconds)
# Game: 1435, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 580/1434 (0.40)]
# WIN, Finished in: 10.578032493591309(seconds)
# Game: 1436, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 581/1435 (0.40)]
# Game: 1437, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 581/1436 (0.40)]
# WIN, Finished in: 0.9335341453552246(seconds)
# Game: 1438, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 582/1437 (0.41)]
# Game: 1439, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 582/1438 (0.40)]
# WIN, Finished in: 52.94099426269531(seconds)
# Game: 1440, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 583/1439 (0.41)]
# Game: 1441, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 583/1440 (0.40)]
# Game: 1442, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 583/1441 (0.40)]
# Game: 1443, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 583/1442 (0.40)]
# WIN, Finished in: 1.2308788299560547(seconds)
# Game: 1444, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 584/1443 (0.40)]
# WIN, Finished in: 1.9535787105560303(seconds)
# Game: 1445, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 585/1444 (0.41)]
# Game: 1446, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 585/1445 (0.40)]
# WIN, Finished in: 0.7773470878601074(seconds)
# Game: 1447, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 586/1446 (0.41)]
# Game: 1448, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 586/1447 (0.40)]
# WIN, Finished in: 2.421938419342041(seconds)
# Game: 1449, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 587/1448 (0.41)]
# Game: 1450, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 587/1449 (0.41)]
# Game: 1451, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 587/1450 (0.40)]
# WIN, Finished in: 0.9376099109649658(seconds)
# Game: 1452, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 588/1451 (0.41)]
# Game: 1453, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 588/1452 (0.40)]
# WIN, Finished in: 31.862746953964233(seconds)
# Game: 1454, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 589/1453 (0.41)]
# Game: 1455, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 589/1454 (0.41)]
# Game: 1456, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 589/1455 (0.40)]
# Game: 1457, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 589/1456 (0.40)]
# Game: 1458, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 589/1457 (0.40)]
# WIN, Finished in: 2.1858856678009033(seconds)
# Game: 1459, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 590/1458 (0.40)]
# Game: 1460, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 590/1459 (0.40)]
# Game: 1461, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 590/1460 (0.40)]
# WIN, Finished in: 1.1855463981628418(seconds)
# Game: 1462, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 591/1461 (0.40)]
# Game: 1463, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 591/1462 (0.40)]
# Game: 1464, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 591/1463 (0.40)]
# Game: 1465, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 591/1464 (0.40)]
# WIN, Finished in: 150.84802889823914(seconds)
# Game: 1466, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 592/1465 (0.40)]
# WIN, Finished in: 0.7293522357940674(seconds)
# Game: 1467, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 593/1466 (0.40)]
# WIN, Finished in: 1.656614065170288(seconds)
# Game: 1468, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1467 (0.40)]
# Game: 1469, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1468 (0.40)]
# Game: 1470, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1469 (0.40)]
# Game: 1471, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1470 (0.40)]
# Game: 1472, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1471 (0.40)]
# Game: 1473, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1472 (0.40)]
# Game: 1474, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1473 (0.40)]
# Game: 1475, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1474 (0.40)]
# Game: 1476, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1475 (0.40)]
# Game: 1477, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1476 (0.40)]
# Game: 1478, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 594/1477 (0.40)]
# WIN, Finished in: 1.0319037437438965(seconds)
# Game: 1479, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 595/1478 (0.40)]
# Game: 1480, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 595/1479 (0.40)]
# Game: 1481, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 595/1480 (0.40)]
# Game: 1482, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 595/1481 (0.40)]
# Game: 1483, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 595/1482 (0.40)]
# Game: 1484, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 595/1483 (0.40)]
# WIN, Finished in: 1.1877448558807373(seconds)
# Game: 1485, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 596/1484 (0.40)]
# Game: 1486, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 596/1485 (0.40)]
# Game: 1487, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 596/1486 (0.40)]
# WIN, Finished in: 0.7639868259429932(seconds)
# Game: 1488, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 597/1487 (0.40)]
# WIN, Finished in: 1.734360694885254(seconds)
# Game: 1489, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 598/1488 (0.40)]
# WIN, Finished in: 0.9218978881835938(seconds)
# Game: 1490, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 599/1489 (0.40)]
# WIN, Finished in: 184.69010472297668(seconds)
# Game: 1491, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 600/1490 (0.40)]
# WIN, Finished in: 0.8095884323120117(seconds)
# Game: 1492, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 601/1491 (0.40)]
# WIN, Finished in: 0.9687714576721191(seconds)
# Game: 1493, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 602/1492 (0.40)]
# WIN, Finished in: 1.281214714050293(seconds)
# Game: 1494, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 603/1493 (0.40)]
# WIN, Finished in: 0.8440728187561035(seconds)
# Game: 1495, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 604/1494 (0.40)]
# WIN, Finished in: 2.734708547592163(seconds)
# Game: 1496, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 605/1495 (0.40)]
# Game: 1497, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 605/1496 (0.40)]
# WIN, Finished in: 1.0937976837158203(seconds)
# Game: 1498, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 606/1497 (0.40)]
# WIN, Finished in: 34.04791831970215(seconds)
# Game: 1499, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 607/1498 (0.41)]
# Game: 1500, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 607/1499 (0.40)]
# Game: 1501, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 607/1500 (0.40)]
# WIN, Finished in: 0.8749632835388184(seconds)
# Game: 1502, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 608/1501 (0.41)]
# WIN, Finished in: 2.1255269050598145(seconds)
# Game: 1503, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 609/1502 (0.41)]
# Game: 1504, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 609/1503 (0.41)]
# Game: 1505, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 609/1504 (0.40)]
# WIN, Finished in: 15.657797813415527(seconds)
# Game: 1506, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 610/1505 (0.41)]
# Game: 1507, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 610/1506 (0.41)]
# WIN, Finished in: 1.0312023162841797(seconds)
# Game: 1508, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 611/1507 (0.41)]
# Game: 1509, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 611/1508 (0.41)]
# Game: 1510, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 611/1509 (0.40)]
# Game: 1511, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 611/1510 (0.40)]
# Game: 1512, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 611/1511 (0.40)]
# WIN, Finished in: 0.921931266784668(seconds)
# Game: 1513, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 612/1512 (0.40)]
# Game: 1514, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 612/1513 (0.40)]
# WIN, Finished in: 9.047760009765625(seconds)
# Game: 1515, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 613/1514 (0.40)]
# WIN, Finished in: 0.9989485740661621(seconds)
# Game: 1516, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 614/1515 (0.41)]
# WIN, Finished in: 1.093768835067749(seconds)
# Game: 1517, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 615/1516 (0.41)]
# Game: 1518, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 615/1517 (0.41)]
# Game: 1519, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 615/1518 (0.41)]
# WIN, Finished in: 16.37693476676941(seconds)
# Game: 1520, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 616/1519 (0.41)]
# Game: 1521, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 616/1520 (0.41)]
# Game: 1522, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 616/1521 (0.40)]
# Game: 1523, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 616/1522 (0.40)]
# Game: 1524, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 616/1523 (0.40)]
# Game: 1525, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 616/1524 (0.40)]
# WIN, Finished in: 1.0162036418914795(seconds)
# Game: 1526, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 617/1525 (0.40)]
# Game: 1527, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 617/1526 (0.40)]
# Game: 1528, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 617/1527 (0.40)]
# WIN, Finished in: 37.58427429199219(seconds)
# Game: 1529, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 618/1528 (0.40)]
# Game: 1530, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 618/1529 (0.40)]
# Game: 1531, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 618/1530 (0.40)]
# WIN, Finished in: 2.6405532360076904(seconds)
# Game: 1532, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 619/1531 (0.40)]
# WIN, Finished in: 0.999783992767334(seconds)
# Game: 1533, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 620/1532 (0.40)]
# Game: 1534, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 620/1533 (0.40)]
# Game: 1535, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 620/1534 (0.40)]
# WIN, Finished in: 1.030655860900879(seconds)
# Game: 1536, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 621/1535 (0.40)]
# WIN, Finished in: 0.8280575275421143(seconds)
# Game: 1537, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 622/1536 (0.40)]
# Game: 1538, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 622/1537 (0.40)]
# Game: 1539, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 622/1538 (0.40)]
# Game: 1540, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 622/1539 (0.40)]
# WIN, Finished in: 88.85505962371826(seconds)
# Game: 1541, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 623/1540 (0.40)]
# WIN, Finished in: 0.7380490303039551(seconds)
# Game: 1542, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 624/1541 (0.40)]
# Game: 1543, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 624/1542 (0.40)]
# Game: 1544, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 624/1543 (0.40)]
# Game: 1545, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 624/1544 (0.40)]
# Game: 1546, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 624/1545 (0.40)]
# WIN, Finished in: 0.9374704360961914(seconds)
# Game: 1547, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 625/1546 (0.40)]
# WIN, Finished in: 4.876389741897583(seconds)
# Game: 1548, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 626/1547 (0.40)]
# WIN, Finished in: 1.5144524574279785(seconds)
# Game: 1549, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 627/1548 (0.41)]
# Game: 1550, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 627/1549 (0.40)]
# Game: 1551, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 627/1550 (0.40)]
# WIN, Finished in: 6.078137636184692(seconds)
# Game: 1552, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 628/1551 (0.40)]
# Game: 1553, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 628/1552 (0.40)]
# Game: 1554, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 628/1553 (0.40)]
# WIN, Finished in: 0.968900203704834(seconds)
# Game: 1555, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 629/1554 (0.40)]
# Game: 1556, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 629/1555 (0.40)]
# Game: 1557, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 629/1556 (0.40)]
# WIN, Finished in: 0.8430099487304688(seconds)
# Game: 1558, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 630/1557 (0.40)]
# Game: 1559, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 630/1558 (0.40)]
# Game: 1560, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 630/1559 (0.40)]
# Game: 1561, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 630/1560 (0.40)]
# WIN, Finished in: 0.7313802242279053(seconds)
# Game: 1562, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 631/1561 (0.40)]
# WIN, Finished in: 0.8907251358032227(seconds)
# Game: 1563, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 632/1562 (0.40)]
# WIN, Finished in: 4.203534841537476(seconds)
# Game: 1564, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 633/1563 (0.40)]
# Game: 1565, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 633/1564 (0.40)]
# WIN, Finished in: 0.8594481945037842(seconds)
# Game: 1566, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 634/1565 (0.41)]
# Game: 1567, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 634/1566 (0.40)]
# WIN, Finished in: 0.9211227893829346(seconds)
# Game: 1568, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 635/1567 (0.41)]
# WIN, Finished in: 1.0789971351623535(seconds)
# Game: 1569, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 636/1568 (0.41)]
# Game: 1570, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 636/1569 (0.41)]
# WIN, Finished in: 0.8583359718322754(seconds)
# Game: 1571, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 637/1570 (0.41)]
# Game: 1572, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 637/1571 (0.41)]
# Game: 1573, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 637/1572 (0.41)]
# WIN, Finished in: 290.7223331928253(seconds)
# Game: 1574, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 638/1573 (0.41)]
# Game: 1575, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 638/1574 (0.41)]
# WIN, Finished in: 0.8280701637268066(seconds)
# Game: 1576, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 639/1575 (0.41)]
# Game: 1577, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 639/1576 (0.41)]
# Game: 1578, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 639/1577 (0.41)]
# Game: 1579, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 639/1578 (0.40)]
# WIN, Finished in: 12.76265287399292(seconds)
# Game: 1580, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 640/1579 (0.41)]
# Game: 1581, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 640/1580 (0.41)]
# WIN, Finished in: 0.7968580722808838(seconds)
# Game: 1582, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 641/1581 (0.41)]
# Game: 1583, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 641/1582 (0.41)]
# WIN, Finished in: 290.4278244972229(seconds)
# Game: 1584, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 642/1583 (0.41)]
# Game: 1585, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 642/1584 (0.41)]
# WIN, Finished in: 56.600945234298706(seconds)
# Game: 1586, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 643/1585 (0.41)]
# Game: 1587, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 643/1586 (0.41)]
# Game: 1588, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 643/1587 (0.41)]
# Game: 1589, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 643/1588 (0.40)]
# WIN, Finished in: 1.3633275032043457(seconds)
# Game: 1590, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 644/1589 (0.41)]
# Game: 1591, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 644/1590 (0.41)]
# Game: 1592, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 644/1591 (0.40)]
# Game: 1593, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 644/1592 (0.40)]
# Game: 1594, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 644/1593 (0.40)]
# WIN, Finished in: 0.8438637256622314(seconds)
# Game: 1595, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 645/1594 (0.40)]
# WIN, Finished in: 17.939172744750977(seconds)
# Game: 1596, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 646/1595 (0.41)]
# WIN, Finished in: 1.0291588306427002(seconds)
# Game: 1597, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 647/1596 (0.41)]
# WIN, Finished in: 4.46902871131897(seconds)
# Game: 1598, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 648/1597 (0.41)]
# WIN, Finished in: 3.813910961151123(seconds)
# Game: 1599, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 649/1598 (0.41)]
# WIN, Finished in: 5.170138835906982(seconds)
# Game: 1600, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 650/1599 (0.41)]
# WIN, Finished in: 0.8749294281005859(seconds)
# Game: 1601, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 651/1600 (0.41)]
# WIN, Finished in: 0.7972240447998047(seconds)
# Game: 1602, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 652/1601 (0.41)]
# Game: 1603, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 652/1602 (0.41)]
# WIN, Finished in: 21.516651153564453(seconds)
# Game: 1604, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 653/1603 (0.41)]
# WIN, Finished in: 0.764625072479248(seconds)
# Game: 1605, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 654/1604 (0.41)]
# WIN, Finished in: 4.016143083572388(seconds)
# Game: 1606, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 655/1605 (0.41)]
# Game: 1607, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 655/1606 (0.41)]
# Game: 1608, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 655/1607 (0.41)]
# Game: 1609, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 655/1608 (0.41)]
# Game: 1610, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 655/1609 (0.41)]
# Game: 1611, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 655/1610 (0.41)]
# Game: 1612, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 655/1611 (0.41)]
# WIN, Finished in: 290.6596279144287(seconds)
# Game: 1613, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 656/1612 (0.41)]
# WIN, Finished in: 0.8871574401855469(seconds)
# Game: 1614, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 657/1613 (0.41)]
# Game: 1615, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 657/1614 (0.41)]
# WIN, Finished in: 0.9063985347747803(seconds)
# Game: 1616, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 658/1615 (0.41)]
# Game: 1617, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 658/1616 (0.41)]
# Game: 1618, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 658/1617 (0.41)]
# WIN, Finished in: 0.7950379848480225(seconds)
# Game: 1619, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 659/1618 (0.41)]
# Game: 1620, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 659/1619 (0.41)]
# Game: 1621, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 659/1620 (0.41)]
# Game: 1622, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 659/1621 (0.41)]
# Game: 1623, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 659/1622 (0.41)]
# WIN, Finished in: 290.3466453552246(seconds)
# Game: 1624, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 660/1623 (0.41)]
# WIN, Finished in: 1.5441153049468994(seconds)
# Game: 1625, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 661/1624 (0.41)]
# Game: 1626, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 661/1625 (0.41)]
# Game: 1627, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 661/1626 (0.41)]
# WIN, Finished in: 1.9065282344818115(seconds)
# Game: 1628, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 662/1627 (0.41)]
# WIN, Finished in: 1.109304666519165(seconds)
# Game: 1629, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 663/1628 (0.41)]
# Game: 1630, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 663/1629 (0.41)]
# WIN, Finished in: 290.50140047073364(seconds)
# Game: 1631, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 664/1630 (0.41)]
# Game: 1632, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 664/1631 (0.41)]
# WIN, Finished in: 0.9678566455841064(seconds)
# Game: 1633, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 665/1632 (0.41)]
# Game: 1634, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 665/1633 (0.41)]
# Game: 1635, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 665/1634 (0.41)]
# WIN, Finished in: 4.953598260879517(seconds)
# Game: 1636, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 666/1635 (0.41)]
# Game: 1637, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 666/1636 (0.41)]
# WIN, Finished in: 3.078409194946289(seconds)
# Game: 1638, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 667/1637 (0.41)]
# WIN, Finished in: 0.936943769454956(seconds)
# Game: 1639, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 668/1638 (0.41)]
# WIN, Finished in: 2.249429702758789(seconds)
# Game: 1640, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 669/1639 (0.41)]
# WIN, Finished in: 0.9689986705780029(seconds)
# Game: 1641, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 670/1640 (0.41)]
# Game: 1642, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 670/1641 (0.41)]
# WIN, Finished in: 0.9375667572021484(seconds)
# Game: 1643, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 671/1642 (0.41)]
# Game: 1644, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 671/1643 (0.41)]
# Game: 1645, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 671/1644 (0.41)]
# Game: 1646, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 671/1645 (0.41)]
# Game: 1647, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 671/1646 (0.41)]
# WIN, Finished in: 0.7758028507232666(seconds)
# Game: 1648, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 672/1647 (0.41)]
# Game: 1649, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 672/1648 (0.41)]
# WIN, Finished in: 1.0312762260437012(seconds)
# Game: 1650, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 673/1649 (0.41)]
# WIN, Finished in: 0.859473466873169(seconds)
# Game: 1651, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 674/1650 (0.41)]
# Game: 1652, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 674/1651 (0.41)]
# Game: 1653, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 674/1652 (0.41)]
# Game: 1654, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 674/1653 (0.41)]
# WIN, Finished in: 0.7961616516113281(seconds)
# Game: 1655, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 675/1654 (0.41)]
# Game: 1656, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 675/1655 (0.41)]
# WIN, Finished in: 0.7968361377716064(seconds)
# Game: 1657, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1656 (0.41)]
# Game: 1658, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1657 (0.41)]
# Game: 1659, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1658 (0.41)]
# Game: 1660, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1659 (0.41)]
# Game: 1661, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1660 (0.41)]
# Game: 1662, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1661 (0.41)]
# Game: 1663, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1662 (0.41)]
# Game: 1664, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1663 (0.41)]
# Game: 1665, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1664 (0.41)]
# Game: 1666, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 676/1665 (0.41)]
# WIN, Finished in: 47.50087332725525(seconds)
# Game: 1667, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 677/1666 (0.41)]
# WIN, Finished in: 0.9688222408294678(seconds)
# Game: 1668, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 678/1667 (0.41)]
# Game: 1669, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 678/1668 (0.41)]
# Game: 1670, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 678/1669 (0.41)]
# Game: 1671, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 678/1670 (0.41)]
# Game: 1672, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 678/1671 (0.41)]
# Game: 1673, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 678/1672 (0.41)]
# WIN, Finished in: 106.06786251068115(seconds)
# Game: 1674, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 679/1673 (0.41)]
# Game: 1675, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 679/1674 (0.41)]
# Game: 1676, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 679/1675 (0.41)]
# Game: 1677, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 679/1676 (0.41)]
# Game: 1678, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 679/1677 (0.40)]
# WIN, Finished in: 0.9218001365661621(seconds)
# Game: 1679, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 680/1678 (0.41)]
# WIN, Finished in: 2.9688236713409424(seconds)
# Game: 1680, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 681/1679 (0.41)]
# WIN, Finished in: 18.158427476882935(seconds)
# Game: 1681, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 682/1680 (0.41)]
# WIN, Finished in: 290.6072106361389(seconds)
# Game: 1682, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 683/1681 (0.41)]
# WIN, Finished in: 0.7657899856567383(seconds)
# Game: 1683, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 684/1682 (0.41)]
# Game: 1684, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 684/1683 (0.41)]
# Game: 1685, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 684/1684 (0.41)]
# Game: 1686, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 684/1685 (0.41)]
# Game: 1687, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 684/1686 (0.41)]
# WIN, Finished in: 0.8899490833282471(seconds)
# Game: 1688, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 685/1687 (0.41)]
# Game: 1689, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 685/1688 (0.41)]
# Game: 1690, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 685/1689 (0.41)]
# WIN, Finished in: 2.8740921020507812(seconds)
# Game: 1691, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 686/1690 (0.41)]
# WIN, Finished in: 290.5779857635498(seconds)
# Game: 1692, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 687/1691 (0.41)]
# Game: 1693, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 687/1692 (0.41)]
# Game: 1694, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 687/1693 (0.41)]
# Game: 1695, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 687/1694 (0.41)]
# Game: 1696, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 687/1695 (0.41)]
# Game: 1697, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 687/1696 (0.41)]
# Game: 1698, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 687/1697 (0.40)]
# Game: 1699, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 687/1698 (0.40)]
# Game: 1700, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 687/1699 (0.40)]
# WIN, Finished in: 290.67944049835205(seconds)
# Game: 1701, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 688/1700 (0.40)]
# Game: 1702, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 688/1701 (0.40)]
# Game: 1703, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 688/1702 (0.40)]
# WIN, Finished in: 31.560530424118042(seconds)
# Game: 1704, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 689/1703 (0.40)]
# WIN, Finished in: 0.9211018085479736(seconds)
# Game: 1705, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 690/1704 (0.40)]
# WIN, Finished in: 0.8593292236328125(seconds)
# Game: 1706, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 691/1705 (0.41)]
# Game: 1707, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 691/1706 (0.41)]
# Game: 1708, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 691/1707 (0.40)]
# WIN, Finished in: 1.124924898147583(seconds)
# Game: 1709, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 692/1708 (0.41)]
# WIN, Finished in: 0.8927717208862305(seconds)
# Game: 1710, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 693/1709 (0.41)]
# WIN, Finished in: 1.140638828277588(seconds)
# Game: 1711, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 694/1710 (0.41)]
# Game: 1712, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 694/1711 (0.41)]
# Game: 1713, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 694/1712 (0.41)]
# Game: 1714, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 694/1713 (0.41)]
# Game: 1715, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 694/1714 (0.40)]
# Game: 1716, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 694/1715 (0.40)]
# Game: 1717, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 694/1716 (0.40)]
# WIN, Finished in: 1.1830873489379883(seconds)
# Game: 1718, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 695/1717 (0.40)]
# WIN, Finished in: 290.1888151168823(seconds)
# Game: 1719, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 696/1718 (0.41)]
# WIN, Finished in: 0.8467826843261719(seconds)
# Game: 1720, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 697/1719 (0.41)]
# WIN, Finished in: 3.4219613075256348(seconds)
# Game: 1721, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 698/1720 (0.41)]
# Game: 1722, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 698/1721 (0.41)]
# Game: 1723, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 698/1722 (0.41)]
# WIN, Finished in: 0.9688348770141602(seconds)
# Game: 1724, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 699/1723 (0.41)]
# Game: 1725, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 699/1724 (0.41)]
# WIN, Finished in: 0.8537657260894775(seconds)
# Game: 1726, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 700/1725 (0.41)]
# Game: 1727, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 700/1726 (0.41)]
# Game: 1728, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 700/1727 (0.41)]
# WIN, Finished in: 3.056145191192627(seconds)
# Game: 1729, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 701/1728 (0.41)]
# Game: 1730, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 701/1729 (0.41)]
# Game: 1731, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 701/1730 (0.41)]
# WIN, Finished in: 26.795748949050903(seconds)
# Game: 1732, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 702/1731 (0.41)]
# Game: 1733, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 702/1732 (0.41)]
# WIN, Finished in: 1.623558521270752(seconds)
# Game: 1734, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 703/1733 (0.41)]
# Game: 1735, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 703/1734 (0.41)]
# WIN, Finished in: 1.5398285388946533(seconds)
# Game: 1736, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 704/1735 (0.41)]
# WIN, Finished in: 4.165830135345459(seconds)
# Game: 1737, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 705/1736 (0.41)]
# Game: 1738, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 705/1737 (0.41)]
# WIN, Finished in: 4.791866779327393(seconds)
# Game: 1739, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 706/1738 (0.41)]
# WIN, Finished in: 2.801941394805908(seconds)
# Game: 1740, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 707/1739 (0.41)]
# Game: 1741, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 707/1740 (0.41)]
# Game: 1742, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 707/1741 (0.41)]
# Game: 1743, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 707/1742 (0.41)]
# Game: 1744, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 707/1743 (0.41)]
# Game: 1745, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 707/1744 (0.41)]
# Game: 1746, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 707/1745 (0.41)]
# WIN, Finished in: 1.7224383354187012(seconds)
# Game: 1747, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 708/1746 (0.41)]
# Game: 1748, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 708/1747 (0.41)]
# Game: 1749, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 708/1748 (0.41)]
# WIN, Finished in: 1.550281286239624(seconds)
# Game: 1750, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 709/1749 (0.41)]
# Game: 1751, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 709/1750 (0.41)]
# Game: 1752, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 709/1751 (0.40)]
# WIN, Finished in: 1.6896953582763672(seconds)
# Game: 1753, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 710/1752 (0.41)]
# WIN, Finished in: 1.6992628574371338(seconds)
# Game: 1754, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 711/1753 (0.41)]
# WIN, Finished in: 1.6889541149139404(seconds)
# Game: 1755, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 712/1754 (0.41)]
# Game: 1756, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 712/1755 (0.41)]
# Game: 1757, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 712/1756 (0.41)]
# WIN, Finished in: 1.7358291149139404(seconds)
# Game: 1758, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 713/1757 (0.41)]
# WIN, Finished in: 1.6055569648742676(seconds)
# Game: 1759, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 714/1758 (0.41)]
# WIN, Finished in: 16.7839138507843(seconds)
# Game: 1760, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 715/1759 (0.41)]
# Game: 1761, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 715/1760 (0.41)]
# WIN, Finished in: 2.27126407623291(seconds)
# Game: 1762, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 716/1761 (0.41)]
# WIN, Finished in: 46.67643976211548(seconds)
# Game: 1763, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 717/1762 (0.41)]
# Game: 1764, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 717/1763 (0.41)]
# Game: 1765, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 717/1764 (0.41)]
# WIN, Finished in: 1.9699018001556396(seconds)
# Game: 1766, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 718/1765 (0.41)]
# Game: 1767, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 718/1766 (0.41)]
# Game: 1768, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 718/1767 (0.41)]
# Game: 1769, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 718/1768 (0.41)]
# WIN, Finished in: 0.8280720710754395(seconds)
# Game: 1770, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 719/1769 (0.41)]
# Game: 1771, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 719/1770 (0.41)]
# WIN, Finished in: 2.0001468658447266(seconds)
# Game: 1772, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 720/1771 (0.41)]
# Game: 1773, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 720/1772 (0.41)]
# WIN, Finished in: 1.5002272129058838(seconds)
# Game: 1774, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 721/1773 (0.41)]
# Game: 1775, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 721/1774 (0.41)]
# Game: 1776, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 721/1775 (0.41)]
# WIN, Finished in: 2.3272457122802734(seconds)
# Game: 1777, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 722/1776 (0.41)]
# WIN, Finished in: 2.7036526203155518(seconds)
# Game: 1778, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 723/1777 (0.41)]
# WIN, Finished in: 1.406341552734375(seconds)
# Game: 1779, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 724/1778 (0.41)]
# WIN, Finished in: 2.453028440475464(seconds)
# Game: 1780, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 725/1779 (0.41)]
# WIN, Finished in: 0.9689602851867676(seconds)
# Game: 1781, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 726/1780 (0.41)]
# Game: 1782, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 726/1781 (0.41)]
# WIN, Finished in: 0.8281240463256836(seconds)
# Game: 1783, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 727/1782 (0.41)]
# WIN, Finished in: 0.8908886909484863(seconds)
# Game: 1784, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 728/1783 (0.41)]
# Game: 1785, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 728/1784 (0.41)]
# Game: 1786, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 728/1785 (0.41)]
# WIN, Finished in: 4.817357778549194(seconds)
# Game: 1787, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 729/1786 (0.41)]
# Game: 1788, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 729/1787 (0.41)]
# Game: 1789, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 729/1788 (0.41)]
# Game: 1790, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 729/1789 (0.41)]
# Game: 1791, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 729/1790 (0.41)]
# Game: 1792, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 729/1791 (0.41)]
# WIN, Finished in: 4.562440633773804(seconds)
# Game: 1793, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 730/1792 (0.41)]
# WIN, Finished in: 290.6407346725464(seconds)
# Game: 1794, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 731/1793 (0.41)]
# Game: 1795, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 731/1794 (0.41)]
# WIN, Finished in: 0.9376702308654785(seconds)
# Game: 1796, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 732/1795 (0.41)]
# WIN, Finished in: 0.8593273162841797(seconds)
# Game: 1797, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 733/1796 (0.41)]
# WIN, Finished in: 0.8748714923858643(seconds)
# Game: 1798, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 734/1797 (0.41)]
# Game: 1799, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 734/1798 (0.41)]
# WIN, Finished in: 7.625283479690552(seconds)
# Game: 1800, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 735/1799 (0.41)]
# WIN, Finished in: 0.9215352535247803(seconds)
# Game: 1801, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 736/1800 (0.41)]
# Game: 1802, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 736/1801 (0.41)]
# WIN, Finished in: 0.9352855682373047(seconds)
# Game: 1803, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 737/1802 (0.41)]
# Game: 1804, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 737/1803 (0.41)]
# Game: 1805, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 737/1804 (0.41)]
# WIN, Finished in: 45.9999315738678(seconds)
# Game: 1806, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 738/1805 (0.41)]
# WIN, Finished in: 1.2501206398010254(seconds)
# Game: 1807, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 739/1806 (0.41)]
# Game: 1808, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 739/1807 (0.41)]
# WIN, Finished in: 11.031280040740967(seconds)
# Game: 1809, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 740/1808 (0.41)]
# Game: 1810, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 740/1809 (0.41)]
# WIN, Finished in: 8.875405311584473(seconds)
# Game: 1811, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 741/1810 (0.41)]
# WIN, Finished in: 0.7338087558746338(seconds)
# Game: 1812, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 742/1811 (0.41)]
# Game: 1813, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 742/1812 (0.41)]
# WIN, Finished in: 1.1401793956756592(seconds)
# Game: 1814, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 743/1813 (0.41)]
# WIN, Finished in: 0.8906304836273193(seconds)
# Game: 1815, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 744/1814 (0.41)]
# Game: 1816, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 744/1815 (0.41)]
# WIN, Finished in: 14.015881061553955(seconds)
# Game: 1817, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 745/1816 (0.41)]
# Game: 1818, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 745/1817 (0.41)]
# Game: 1819, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 745/1818 (0.41)]
# Game: 1820, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 745/1819 (0.41)]
# Game: 1821, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 745/1820 (0.41)]
# WIN, Finished in: 0.9019496440887451(seconds)
# Game: 1822, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 746/1821 (0.41)]
# Game: 1823, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 746/1822 (0.41)]
# Game: 1824, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 746/1823 (0.41)]
# Game: 1825, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 746/1824 (0.41)]
# Game: 1826, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 746/1825 (0.41)]
# WIN, Finished in: 0.9225935935974121(seconds)
# Game: 1827, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 747/1826 (0.41)]
# WIN, Finished in: 18.06183624267578(seconds)
# Game: 1828, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 748/1827 (0.41)]
# WIN, Finished in: 3.0780367851257324(seconds)
# Game: 1829, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 749/1828 (0.41)]
# WIN, Finished in: 290.1719591617584(seconds)
# Game: 1830, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 750/1829 (0.41)]
# Game: 1831, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 750/1830 (0.41)]
# WIN, Finished in: 1.3280997276306152(seconds)
# Game: 1832, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 751/1831 (0.41)]
# Game: 1833, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 751/1832 (0.41)]
# WIN, Finished in: 0.890648365020752(seconds)
# Game: 1834, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 752/1833 (0.41)]
# WIN, Finished in: 0.8905868530273438(seconds)
# Game: 1835, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 753/1834 (0.41)]
# WIN, Finished in: 5.250152349472046(seconds)
# Game: 1836, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 754/1835 (0.41)]
# Game: 1837, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 754/1836 (0.41)]
# Game: 1838, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 754/1837 (0.41)]
# Game: 1839, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 754/1838 (0.41)]
# Game: 1840, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 754/1839 (0.41)]
# WIN, Finished in: 5.718310356140137(seconds)
# Game: 1841, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 755/1840 (0.41)]
# Game: 1842, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 755/1841 (0.41)]
# WIN, Finished in: 0.7827639579772949(seconds)
# Game: 1843, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 756/1842 (0.41)]
# Game: 1844, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 756/1843 (0.41)]
# WIN, Finished in: 0.9622604846954346(seconds)
# Game: 1845, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 757/1844 (0.41)]
# Game: 1846, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 757/1845 (0.41)]
# Game: 1847, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 757/1846 (0.41)]
# Game: 1848, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 757/1847 (0.41)]
# Game: 1849, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 757/1848 (0.41)]
# WIN, Finished in: 0.9485628604888916(seconds)
# Game: 1850, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 758/1849 (0.41)]
# Game: 1851, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 758/1850 (0.41)]
# WIN, Finished in: 0.8753941059112549(seconds)
# Game: 1852, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 759/1851 (0.41)]
# WIN, Finished in: 0.8590590953826904(seconds)
# Game: 1853, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 760/1852 (0.41)]
# Game: 1854, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 760/1853 (0.41)]
# Game: 1855, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 760/1854 (0.41)]
# WIN, Finished in: 7.71855092048645(seconds)
# Game: 1856, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 761/1855 (0.41)]
# Game: 1857, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 761/1856 (0.41)]
# WIN, Finished in: 290.65515875816345(seconds)
# Game: 1858, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 762/1857 (0.41)]
# Game: 1859, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 762/1858 (0.41)]
# WIN, Finished in: 1.0304558277130127(seconds)
# Game: 1860, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 763/1859 (0.41)]
# Game: 1861, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 763/1860 (0.41)]
# WIN, Finished in: 0.9996397495269775(seconds)
# Game: 1862, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 764/1861 (0.41)]
# Game: 1863, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 764/1862 (0.41)]
# Game: 1864, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 764/1863 (0.41)]
# WIN, Finished in: 0.9062943458557129(seconds)
# Game: 1865, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 765/1864 (0.41)]
# Game: 1866, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 765/1865 (0.41)]
# WIN, Finished in: 22.515669584274292(seconds)
# Game: 1867, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 766/1866 (0.41)]
# WIN, Finished in: 0.9530034065246582(seconds)
# Game: 1868, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1867 (0.41)]
# Game: 1869, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1868 (0.41)]
# Game: 1870, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1869 (0.41)]
# Game: 1871, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1870 (0.41)]
# Game: 1872, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1871 (0.41)]
# Game: 1873, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1872 (0.41)]
# Game: 1874, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1873 (0.41)]
# Game: 1875, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1874 (0.41)]
# Game: 1876, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1875 (0.41)]
# Game: 1877, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 767/1876 (0.41)]
# WIN, Finished in: 17.046524047851562(seconds)
# Game: 1878, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 768/1877 (0.41)]
# Game: 1879, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 768/1878 (0.41)]
# Game: 1880, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 768/1879 (0.41)]
# Game: 1881, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 768/1880 (0.41)]
# Game: 1882, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 768/1881 (0.41)]
# WIN, Finished in: 1.9530375003814697(seconds)
# Game: 1883, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 769/1882 (0.41)]
# Game: 1884, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 769/1883 (0.41)]
# Game: 1885, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 769/1884 (0.41)]
# Game: 1886, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 769/1885 (0.41)]
# WIN, Finished in: 0.7274906635284424(seconds)
# Game: 1887, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 770/1886 (0.41)]
# Game: 1888, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 770/1887 (0.41)]
# Game: 1889, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 770/1888 (0.41)]
# WIN, Finished in: 0.8909134864807129(seconds)
# Game: 1890, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 771/1889 (0.41)]
# WIN, Finished in: 1.1091043949127197(seconds)
# Game: 1891, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 772/1890 (0.41)]
# Game: 1892, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 772/1891 (0.41)]
# WIN, Finished in: 0.9802286624908447(seconds)
# Game: 1893, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 773/1892 (0.41)]
# WIN, Finished in: 25.62471103668213(seconds)
# Game: 1894, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 774/1893 (0.41)]
# WIN, Finished in: 33.96876525878906(seconds)
# Game: 1895, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 775/1894 (0.41)]
# WIN, Finished in: 24.666160106658936(seconds)
# Game: 1896, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 776/1895 (0.41)]
# Game: 1897, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 776/1896 (0.41)]
# WIN, Finished in: 1.0311496257781982(seconds)
# Game: 1898, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 777/1897 (0.41)]
# WIN, Finished in: 7.7031519412994385(seconds)
# Game: 1899, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 778/1898 (0.41)]
# Game: 1900, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 778/1899 (0.41)]
# WIN, Finished in: 0.8122305870056152(seconds)
# Game: 1901, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 779/1900 (0.41)]
# WIN, Finished in: 0.9374470710754395(seconds)
# Game: 1902, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 780/1901 (0.41)]
# Game: 1903, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 780/1902 (0.41)]
# WIN, Finished in: 0.7343041896820068(seconds)
# Game: 1904, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 781/1903 (0.41)]
# WIN, Finished in: 2.609449863433838(seconds)
# Game: 1905, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 782/1904 (0.41)]
# WIN, Finished in: 0.8124561309814453(seconds)
# Game: 1906, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 783/1905 (0.41)]
# WIN, Finished in: 0.9222550392150879(seconds)
# Game: 1907, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 784/1906 (0.41)]
# WIN, Finished in: 0.9215278625488281(seconds)
# Game: 1908, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 785/1907 (0.41)]
# Game: 1909, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 785/1908 (0.41)]
# WIN, Finished in: 0.8629074096679688(seconds)
# Game: 1910, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 786/1909 (0.41)]
# WIN, Finished in: 6.390092849731445(seconds)
# Game: 1911, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 787/1910 (0.41)]
# WIN, Finished in: 0.8127336502075195(seconds)
# Game: 1912, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 788/1911 (0.41)]
# Game: 1913, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 788/1912 (0.41)]
# Game: 1914, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 788/1913 (0.41)]
# WIN, Finished in: 118.27361941337585(seconds)
# Game: 1915, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 789/1914 (0.41)]
# WIN, Finished in: 2.906028985977173(seconds)
# Game: 1916, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 790/1915 (0.41)]
# Game: 1917, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 790/1916 (0.41)]
# WIN, Finished in: 0.8599579334259033(seconds)
# Game: 1918, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 791/1917 (0.41)]
# WIN, Finished in: 1.3429739475250244(seconds)
# Game: 1919, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 792/1918 (0.41)]
# Game: 1920, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 792/1919 (0.41)]
# WIN, Finished in: 0.8903565406799316(seconds)
# Game: 1921, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 793/1920 (0.41)]
# Game: 1922, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 793/1921 (0.41)]
# Game: 1923, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 793/1922 (0.41)]
# WIN, Finished in: 0.9216797351837158(seconds)
# Game: 1924, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 794/1923 (0.41)]
# WIN, Finished in: 1.547304630279541(seconds)
# Game: 1925, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 795/1924 (0.41)]
# Game: 1926, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 795/1925 (0.41)]
# WIN, Finished in: 290.6874921321869(seconds)
# Game: 1927, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 796/1926 (0.41)]
# Game: 1928, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 796/1927 (0.41)]
# Game: 1929, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 796/1928 (0.41)]
# WIN, Finished in: 0.7655313014984131(seconds)
# Game: 1930, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 797/1929 (0.41)]
# WIN, Finished in: 1.1561920642852783(seconds)
# Game: 1931, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 798/1930 (0.41)]
# WIN, Finished in: 0.8910038471221924(seconds)
# Game: 1932, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 799/1931 (0.41)]
# Game: 1933, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 799/1932 (0.41)]
# WIN, Finished in: 1.0630450248718262(seconds)
# Game: 1934, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 800/1933 (0.41)]
# Game: 1935, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 800/1934 (0.41)]
# Game: 1936, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 800/1935 (0.41)]
# Game: 1937, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 800/1936 (0.41)]
# Game: 1938, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 800/1937 (0.41)]
# Game: 1939, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 800/1938 (0.41)]
# Game: 1940, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 800/1939 (0.41)]
# Game: 1941, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 800/1940 (0.41)]
# WIN, Finished in: 0.7813291549682617(seconds)
# Game: 1942, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 801/1941 (0.41)]
# Game: 1943, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 801/1942 (0.41)]
# WIN, Finished in: 3.2656893730163574(seconds)
# Game: 1944, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 802/1943 (0.41)]
# Game: 1945, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 802/1944 (0.41)]
# Game: 1946, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 802/1945 (0.41)]
# WIN, Finished in: 0.7648487091064453(seconds)
# Game: 1947, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 803/1946 (0.41)]
# WIN, Finished in: 0.8907639980316162(seconds)
# Game: 1948, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 804/1947 (0.41)]
# Game: 1949, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 804/1948 (0.41)]
# WIN, Finished in: 1.2343463897705078(seconds)
# Game: 1950, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 805/1949 (0.41)]
# Game: 1951, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 805/1950 (0.41)]
# WIN, Finished in: 23.06248164176941(seconds)
# Game: 1952, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 806/1951 (0.41)]
# Game: 1953, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 806/1952 (0.41)]
# Game: 1954, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 806/1953 (0.41)]
# WIN, Finished in: 0.9223306179046631(seconds)
# Game: 1955, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 807/1954 (0.41)]
# Game: 1956, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 807/1955 (0.41)]
# WIN, Finished in: 1.234776496887207(seconds)
# Game: 1957, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 808/1956 (0.41)]
# Game: 1958, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 808/1957 (0.41)]
# WIN, Finished in: 4.0312676429748535(seconds)
# Game: 1959, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 809/1958 (0.41)]
# Game: 1960, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 809/1959 (0.41)]
# Game: 1961, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 809/1960 (0.41)]
# WIN, Finished in: 290.57842922210693(seconds)
# Game: 1962, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 810/1961 (0.41)]
# Game: 1963, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 810/1962 (0.41)]
# Game: 1964, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 810/1963 (0.41)]
# WIN, Finished in: 3.671823263168335(seconds)
# Game: 1965, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 811/1964 (0.41)]
# WIN, Finished in: 23.56246781349182(seconds)
# Game: 1966, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 812/1965 (0.41)]
# WIN, Finished in: 1.7344279289245605(seconds)
# Game: 1967, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 813/1966 (0.41)]
# Game: 1968, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 813/1967 (0.41)]
# Game: 1969, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 813/1968 (0.41)]
# Game: 1970, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 813/1969 (0.41)]
# Game: 1971, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 813/1970 (0.41)]
# Game: 1972, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 813/1971 (0.41)]
# WIN, Finished in: 8.593478202819824(seconds)
# Game: 1973, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 814/1972 (0.41)]
# Game: 1974, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 814/1973 (0.41)]
# Game: 1975, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 814/1974 (0.41)]
# Game: 1976, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 814/1975 (0.41)]
# Game: 1977, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 814/1976 (0.41)]
# Game: 1978, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 814/1977 (0.41)]
# WIN, Finished in: 0.9064655303955078(seconds)
# Game: 1979, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 815/1978 (0.41)]
# WIN, Finished in: 1.2364981174468994(seconds)
# Game: 1980, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 816/1979 (0.41)]
# Game: 1981, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 816/1980 (0.41)]
# WIN, Finished in: 21.71879744529724(seconds)
# Game: 1982, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 817/1981 (0.41)]
# Game: 1983, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 817/1982 (0.41)]
# WIN, Finished in: 1.45332670211792(seconds)
# Game: 1984, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 818/1983 (0.41)]
# Game: 1985, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 818/1984 (0.41)]
# Game: 1986, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 818/1985 (0.41)]
# WIN, Finished in: 1.2656919956207275(seconds)
# Game: 1987, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 819/1986 (0.41)]
# Game: 1988, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 819/1987 (0.41)]
# Game: 1989, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 819/1988 (0.41)]
# Game: 1990, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 819/1989 (0.41)]
# Game: 1991, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 819/1990 (0.41)]
# WIN, Finished in: 0.8905825614929199(seconds)
# Game: 1992, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 820/1991 (0.41)]
# Game: 1993, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 820/1992 (0.41)]
# Game: 1994, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 820/1993 (0.41)]
# WIN, Finished in: 1.6163763999938965(seconds)
# Game: 1995, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 821/1994 (0.41)]
# WIN, Finished in: 0.8126220703125(seconds)
# Game: 1996, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 822/1995 (0.41)]
# WIN, Finished in: 0.9563572406768799(seconds)
# Game: 1997, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 823/1996 (0.41)]
# Game: 1998, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 823/1997 (0.41)]
# Game: 1999, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 823/1998 (0.41)]
# WIN, Finished in: 0.9376137256622314(seconds)
# Game: 2000, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 824/1999 (0.41)]
# WIN, Finished in: 1.0014333724975586(seconds)
# Game: 2001, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 825/2000 (0.41)]
# Game: 2002, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 825/2001 (0.41)]
# Game: 2003, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 825/2002 (0.41)]
# Game: 2004, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 825/2003 (0.41)]
# WIN, Finished in: 0.9922952651977539(seconds)
# Game: 2005, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 826/2004 (0.41)]
# Game: 2006, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 826/2005 (0.41)]
# WIN, Finished in: 0.8805563449859619(seconds)
# Game: 2007, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 827/2006 (0.41)]
# Game: 2008, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 827/2007 (0.41)]
# Game: 2009, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 827/2008 (0.41)]
# Game: 2010, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 827/2009 (0.41)]
# Game: 2011, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 827/2010 (0.41)]
# Game: 2012, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 827/2011 (0.41)]
# Game: 2013, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 827/2012 (0.41)]
# Game: 2014, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 827/2013 (0.41)]
# WIN, Finished in: 13.60895848274231(seconds)
# Game: 2015, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 828/2014 (0.41)]
# Game: 2016, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 828/2015 (0.41)]
# Game: 2017, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 828/2016 (0.41)]
# WIN, Finished in: 0.8412761688232422(seconds)
# Game: 2018, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 829/2017 (0.41)]
# WIN, Finished in: 2.108795166015625(seconds)
# Game: 2019, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 830/2018 (0.41)]
# Game: 2020, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 830/2019 (0.41)]
# Game: 2021, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 830/2020 (0.41)]
# WIN, Finished in: 0.8726940155029297(seconds)
# Game: 2022, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 831/2021 (0.41)]
# Game: 2023, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 831/2022 (0.41)]
# WIN, Finished in: 0.8906333446502686(seconds)
# Game: 2024, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 832/2023 (0.41)]
# WIN, Finished in: 5.140880107879639(seconds)
# Game: 2025, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 833/2024 (0.41)]
# WIN, Finished in: 1.1561706066131592(seconds)
# Game: 2026, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 834/2025 (0.41)]
# Game: 2027, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 834/2026 (0.41)]
# Game: 2028, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 834/2027 (0.41)]
# Game: 2029, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 834/2028 (0.41)]
# Game: 2030, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 834/2029 (0.41)]
# WIN, Finished in: 14.562601089477539(seconds)
# Game: 2031, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 835/2030 (0.41)]
# Game: 2032, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 835/2031 (0.41)]
# Game: 2033, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 835/2032 (0.41)]
# Game: 2034, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 835/2033 (0.41)]
# WIN, Finished in: 8.937865018844604(seconds)
# Game: 2035, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 836/2034 (0.41)]
# Game: 2036, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 836/2035 (0.41)]
# Game: 2037, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 836/2036 (0.41)]
# Game: 2038, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 836/2037 (0.41)]
# WIN, Finished in: 1.0000782012939453(seconds)
# Game: 2039, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 837/2038 (0.41)]
# Game: 2040, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 837/2039 (0.41)]
# Game: 2041, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 837/2040 (0.41)]
# Game: 2042, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 837/2041 (0.41)]
# Game: 2043, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 837/2042 (0.41)]
# Game: 2044, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 837/2043 (0.41)]
# Game: 2045, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 837/2044 (0.41)]
# WIN, Finished in: 0.8124120235443115(seconds)
# Game: 2046, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 838/2045 (0.41)]
# WIN, Finished in: 5.71823525428772(seconds)
# Game: 2047, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 839/2046 (0.41)]
# Game: 2048, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 839/2047 (0.41)]
# Game: 2049, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 839/2048 (0.41)]
# Game: 2050, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 839/2049 (0.41)]
# WIN, Finished in: 20.531123638153076(seconds)
# Game: 2051, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 840/2050 (0.41)]
# Game: 2052, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 840/2051 (0.41)]
# Game: 2053, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 840/2052 (0.41)]
# WIN, Finished in: 185.0311963558197(seconds)
# Game: 2054, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 841/2053 (0.41)]
# Game: 2055, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 841/2054 (0.41)]
# WIN, Finished in: 1.1089308261871338(seconds)
# Game: 2056, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 842/2055 (0.41)]
# WIN, Finished in: 4.203530311584473(seconds)
# Game: 2057, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 843/2056 (0.41)]
# WIN, Finished in: 5.10980224609375(seconds)
# Game: 2058, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 844/2057 (0.41)]
# WIN, Finished in: 290.56223154067993(seconds)
# Game: 2059, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 845/2058 (0.41)]
# Game: 2060, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 845/2059 (0.41)]
# WIN, Finished in: 2.8906824588775635(seconds)
# Game: 2061, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 846/2060 (0.41)]
# WIN, Finished in: 1.1873993873596191(seconds)
# Game: 2062, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 847/2061 (0.41)]
# Game: 2063, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 847/2062 (0.41)]
# WIN, Finished in: 1.187544345855713(seconds)
# Game: 2064, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 848/2063 (0.41)]
# Game: 2065, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 848/2064 (0.41)]
# Game: 2066, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 848/2065 (0.41)]
# WIN, Finished in: 5.265651702880859(seconds)
# Game: 2067, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 849/2066 (0.41)]
# WIN, Finished in: 0.8906211853027344(seconds)
# Game: 2068, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 850/2067 (0.41)]
# WIN, Finished in: 15.906413316726685(seconds)
# Game: 2069, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 851/2068 (0.41)]
# WIN, Finished in: 0.7343058586120605(seconds)
# Game: 2070, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 852/2069 (0.41)]
# WIN, Finished in: 0.9833080768585205(seconds)
# Game: 2071, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 853/2070 (0.41)]
# Game: 2072, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 853/2071 (0.41)]
# Game: 2073, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 853/2072 (0.41)]
# Game: 2074, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 853/2073 (0.41)]
# WIN, Finished in: 0.9218697547912598(seconds)
# Game: 2075, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 854/2074 (0.41)]
# Game: 2076, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 854/2075 (0.41)]
# WIN, Finished in: 0.968311071395874(seconds)
# Game: 2077, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 855/2076 (0.41)]
# Game: 2078, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 855/2077 (0.41)]
# Game: 2079, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 855/2078 (0.41)]
# Game: 2080, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 855/2079 (0.41)]
# WIN, Finished in: 8.89057469367981(seconds)
# Game: 2081, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 856/2080 (0.41)]
# WIN, Finished in: 7.828096151351929(seconds)
# Game: 2082, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 857/2081 (0.41)]
# Game: 2083, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 857/2082 (0.41)]
# Game: 2084, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 857/2083 (0.41)]
# Game: 2085, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 857/2084 (0.41)]
# WIN, Finished in: 278.9530622959137(seconds)
# Game: 2086, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 858/2085 (0.41)]
# Game: 2087, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 858/2086 (0.41)]
# Game: 2088, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 858/2087 (0.41)]
# WIN, Finished in: 1.109248161315918(seconds)
# Game: 2089, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 859/2088 (0.41)]
# WIN, Finished in: 0.7656605243682861(seconds)
# Game: 2090, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 860/2089 (0.41)]
# Game: 2091, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 860/2090 (0.41)]
# WIN, Finished in: 0.9687185287475586(seconds)
# Game: 2092, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 861/2091 (0.41)]
# Game: 2093, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 861/2092 (0.41)]
# WIN, Finished in: 0.9529266357421875(seconds)
# Game: 2094, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 862/2093 (0.41)]
# WIN, Finished in: 290.547278881073(seconds)
# Game: 2095, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 863/2094 (0.41)]
# Game: 2096, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 863/2095 (0.41)]
# Game: 2097, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 863/2096 (0.41)]
# Game: 2098, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 863/2097 (0.41)]
# Game: 2099, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 863/2098 (0.41)]
# Game: 2100, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 863/2099 (0.41)]
# WIN, Finished in: 2.078017234802246(seconds)
# Game: 2101, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 864/2100 (0.41)]
# WIN, Finished in: 4.1719069480896(seconds)
# Game: 2102, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 865/2101 (0.41)]
# Game: 2103, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 865/2102 (0.41)]
# Game: 2104, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 865/2103 (0.41)]
# Game: 2105, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 865/2104 (0.41)]
# WIN, Finished in: 0.828824520111084(seconds)
# Game: 2106, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 866/2105 (0.41)]
# Game: 2107, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 866/2106 (0.41)]
# WIN, Finished in: 0.7342836856842041(seconds)
# Game: 2108, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 867/2107 (0.41)]
# WIN, Finished in: 52.640647172927856(seconds)
# Game: 2109, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 868/2108 (0.41)]
# Game: 2110, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 868/2109 (0.41)]
# WIN, Finished in: 2.390700578689575(seconds)
# Game: 2111, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 869/2110 (0.41)]
# Game: 2112, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 869/2111 (0.41)]
# Game: 2113, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 869/2112 (0.41)]
# WIN, Finished in: 0.8121886253356934(seconds)
# Game: 2114, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 870/2113 (0.41)]
# Game: 2115, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 870/2114 (0.41)]
# Game: 2116, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 870/2115 (0.41)]
# Game: 2117, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 870/2116 (0.41)]
# Game: 2118, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 870/2117 (0.41)]
# Game: 2119, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 870/2118 (0.41)]
# Game: 2120, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 870/2119 (0.41)]
# WIN, Finished in: 0.9070422649383545(seconds)
# Game: 2121, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 871/2120 (0.41)]
# Game: 2122, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 871/2121 (0.41)]
# Game: 2123, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 871/2122 (0.41)]
# Game: 2124, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 871/2123 (0.41)]
# Game: 2125, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 871/2124 (0.41)]
# Game: 2126, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 871/2125 (0.41)]
# WIN, Finished in: 16.702985048294067(seconds)
# Game: 2127, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 872/2126 (0.41)]
# WIN, Finished in: 0.765869140625(seconds)
# Game: 2128, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 873/2127 (0.41)]
# Game: 2129, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 873/2128 (0.41)]
# WIN, Finished in: 0.9216697216033936(seconds)
# Game: 2130, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 874/2129 (0.41)]
# Game: 2131, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 874/2130 (0.41)]
# Game: 2132, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 874/2131 (0.41)]
# WIN, Finished in: 0.8900182247161865(seconds)
# Game: 2133, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 875/2132 (0.41)]
# WIN, Finished in: 0.9850590229034424(seconds)
# Game: 2134, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 876/2133 (0.41)]
# WIN, Finished in: 31.42184567451477(seconds)
# Game: 2135, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 877/2134 (0.41)]
# WIN, Finished in: 3.9536240100860596(seconds)
# Game: 2136, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 878/2135 (0.41)]
# Game: 2137, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 878/2136 (0.41)]
# WIN, Finished in: 0.7968275547027588(seconds)
# Game: 2138, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 879/2137 (0.41)]
# Game: 2139, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 879/2138 (0.41)]
# Game: 2140, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 879/2139 (0.41)]
# WIN, Finished in: 290.6365604400635(seconds)
# Game: 2141, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 880/2140 (0.41)]
# Game: 2142, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 880/2141 (0.41)]
# Game: 2143, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 880/2142 (0.41)]
# Game: 2144, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 880/2143 (0.41)]
# WIN, Finished in: 16.149195432662964(seconds)
# Game: 2145, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 881/2144 (0.41)]
# Game: 2146, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 881/2145 (0.41)]
# WIN, Finished in: 4.4721903800964355(seconds)
# Game: 2147, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 882/2146 (0.41)]
# Game: 2148, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 882/2147 (0.41)]
# WIN, Finished in: 0.8123879432678223(seconds)
# Game: 2149, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 883/2148 (0.41)]
# Game: 2150, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 883/2149 (0.41)]
# Game: 2151, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 883/2150 (0.41)]
# WIN, Finished in: 64.18742156028748(seconds)
# Game: 2152, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 884/2151 (0.41)]
# Game: 2153, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 884/2152 (0.41)]
# Game: 2154, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 884/2153 (0.41)]
# Game: 2155, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 884/2154 (0.41)]
# WIN, Finished in: 1.0291249752044678(seconds)
# Game: 2156, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 885/2155 (0.41)]
# Game: 2157, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 885/2156 (0.41)]
# WIN, Finished in: 2.5776774883270264(seconds)
# Game: 2158, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 886/2157 (0.41)]
# Game: 2159, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 886/2158 (0.41)]
# WIN, Finished in: 0.8436036109924316(seconds)
# Game: 2160, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 887/2159 (0.41)]
# WIN, Finished in: 1.1562533378601074(seconds)
# Game: 2161, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 888/2160 (0.41)]
# WIN, Finished in: 0.9535400867462158(seconds)
# Game: 2162, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 889/2161 (0.41)]
# WIN, Finished in: 0.8901963233947754(seconds)
# Game: 2163, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 890/2162 (0.41)]
# Game: 2164, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 890/2163 (0.41)]
# Game: 2165, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 890/2164 (0.41)]
# Game: 2166, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 890/2165 (0.41)]
# WIN, Finished in: 0.9065098762512207(seconds)
# Game: 2167, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 891/2166 (0.41)]
# WIN, Finished in: 1.046462059020996(seconds)
# Game: 2168, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 892/2167 (0.41)]
# Game: 2169, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 892/2168 (0.41)]
# WIN, Finished in: 10.56156611442566(seconds)
# Game: 2170, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 893/2169 (0.41)]
# Game: 2171, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 893/2170 (0.41)]
# Game: 2172, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 893/2171 (0.41)]
# Game: 2173, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 893/2172 (0.41)]
# WIN, Finished in: 0.766221284866333(seconds)
# Game: 2174, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 894/2173 (0.41)]
# Game: 2175, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 894/2174 (0.41)]
# Game: 2176, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 894/2175 (0.41)]
# WIN, Finished in: 0.9227302074432373(seconds)
# Game: 2177, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 895/2176 (0.41)]
# Game: 2178, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 895/2177 (0.41)]
# Game: 2179, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 895/2178 (0.41)]
# WIN, Finished in: 0.9064204692840576(seconds)
# Game: 2180, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 896/2179 (0.41)]
# WIN, Finished in: 46.58397030830383(seconds)
# Game: 2181, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 897/2180 (0.41)]
# Game: 2182, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 897/2181 (0.41)]
# Game: 2183, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 897/2182 (0.41)]
# Game: 2184, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 897/2183 (0.41)]
# WIN, Finished in: 2.2195799350738525(seconds)
# Game: 2185, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 898/2184 (0.41)]
# WIN, Finished in: 6.574297666549683(seconds)
# Game: 2186, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 899/2185 (0.41)]
# Game: 2187, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 899/2186 (0.41)]
# Game: 2188, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 899/2187 (0.41)]
# WIN, Finished in: 1.1473381519317627(seconds)
# Game: 2189, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 900/2188 (0.41)]
# Game: 2190, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 900/2189 (0.41)]
# Game: 2191, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 900/2190 (0.41)]
# Game: 2192, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 900/2191 (0.41)]
# Game: 2193, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 900/2192 (0.41)]
# WIN, Finished in: 36.98433876037598(seconds)
# Game: 2194, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 901/2193 (0.41)]
# Game: 2195, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 901/2194 (0.41)]
# WIN, Finished in: 0.9524626731872559(seconds)
# Game: 2196, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 902/2195 (0.41)]
# Game: 2197, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 902/2196 (0.41)]
# Game: 2198, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 902/2197 (0.41)]
# WIN, Finished in: 12.812039613723755(seconds)
# Game: 2199, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 903/2198 (0.41)]
# WIN, Finished in: 1.5000064373016357(seconds)
# Game: 2200, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 904/2199 (0.41)]
# Game: 2201, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 904/2200 (0.41)]
# Game: 2202, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 904/2201 (0.41)]
# WIN, Finished in: 3.781428575515747(seconds)
# Game: 2203, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 905/2202 (0.41)]
# Game: 2204, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 905/2203 (0.41)]
# Game: 2205, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 905/2204 (0.41)]
# Game: 2206, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 905/2205 (0.41)]
# Game: 2207, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 905/2206 (0.41)]
# WIN, Finished in: 0.9345831871032715(seconds)
# Game: 2208, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 906/2207 (0.41)]
# WIN, Finished in: 2.687453508377075(seconds)
# Game: 2209, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 907/2208 (0.41)]
# Game: 2210, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 907/2209 (0.41)]
# Game: 2211, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 907/2210 (0.41)]
# Game: 2212, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 907/2211 (0.41)]
# WIN, Finished in: 2.8282363414764404(seconds)
# Game: 2213, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 908/2212 (0.41)]
# Game: 2214, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 908/2213 (0.41)]
# WIN, Finished in: 1.9844872951507568(seconds)
# Game: 2215, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 909/2214 (0.41)]
# WIN, Finished in: 40.890514612197876(seconds)
# Game: 2216, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 910/2215 (0.41)]
# WIN, Finished in: 15.96874713897705(seconds)
# Game: 2217, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 911/2216 (0.41)]
# Game: 2218, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 911/2217 (0.41)]
# Game: 2219, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 911/2218 (0.41)]
# WIN, Finished in: 1.0779953002929688(seconds)
# Game: 2220, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 912/2219 (0.41)]
# WIN, Finished in: 0.8750147819519043(seconds)
# Game: 2221, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 913/2220 (0.41)]
# Game: 2222, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 913/2221 (0.41)]
# Game: 2223, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 913/2222 (0.41)]
# Game: 2224, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 913/2223 (0.41)]
# Game: 2225, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 913/2224 (0.41)]
# Game: 2226, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 913/2225 (0.41)]
# WIN, Finished in: 0.7969276905059814(seconds)
# Game: 2227, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 914/2226 (0.41)]
# Game: 2228, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 914/2227 (0.41)]
# Game: 2229, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 914/2228 (0.41)]
# WIN, Finished in: 1.625089168548584(seconds)
# Game: 2230, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 915/2229 (0.41)]
# Game: 2231, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 915/2230 (0.41)]
# WIN, Finished in: 1.7822141647338867(seconds)
# Game: 2232, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 916/2231 (0.41)]
# WIN, Finished in: 0.8276090621948242(seconds)
# Game: 2233, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 917/2232 (0.41)]
# WIN, Finished in: 1.218440294265747(seconds)
# Game: 2234, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 918/2233 (0.41)]
# WIN, Finished in: 1.2501118183135986(seconds)
# Game: 2235, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 919/2234 (0.41)]
# WIN, Finished in: 1.4192934036254883(seconds)
# Game: 2236, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 920/2235 (0.41)]
# WIN, Finished in: 1.5155246257781982(seconds)
# Game: 2237, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 921/2236 (0.41)]
# Game: 2238, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 921/2237 (0.41)]
# WIN, Finished in: 1.9527347087860107(seconds)
# Game: 2239, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 922/2238 (0.41)]
# Game: 2240, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 922/2239 (0.41)]
# Game: 2241, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 922/2240 (0.41)]
# WIN, Finished in: 0.9843277931213379(seconds)
# Game: 2242, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 923/2241 (0.41)]
# WIN, Finished in: 0.8433985710144043(seconds)
# Game: 2243, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 924/2242 (0.41)]
# Game: 2244, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 924/2243 (0.41)]
# Game: 2245, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 924/2244 (0.41)]
# Game: 2246, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 924/2245 (0.41)]
# WIN, Finished in: 0.8430583477020264(seconds)
# Game: 2247, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 925/2246 (0.41)]
# Game: 2248, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 925/2247 (0.41)]
# Game: 2249, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 925/2248 (0.41)]
# Game: 2250, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 925/2249 (0.41)]
# Game: 2251, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 925/2250 (0.41)]
# WIN, Finished in: 32.51609444618225(seconds)
# Game: 2252, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 926/2251 (0.41)]
# Game: 2253, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 926/2252 (0.41)]
# Game: 2254, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 926/2253 (0.41)]
# WIN, Finished in: 0.7968647480010986(seconds)
# Game: 2255, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 927/2254 (0.41)]
# Game: 2256, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 927/2255 (0.41)]
# Game: 2257, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 927/2256 (0.41)]
# Game: 2258, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 927/2257 (0.41)]
# Game: 2259, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 927/2258 (0.41)]
# Game: 2260, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 927/2259 (0.41)]
# WIN, Finished in: 0.8303916454315186(seconds)
# Game: 2261, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 928/2260 (0.41)]
# Game: 2262, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 928/2261 (0.41)]
# Game: 2263, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 928/2262 (0.41)]
# WIN, Finished in: 16.355587005615234(seconds)
# Game: 2264, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 929/2263 (0.41)]
# Game: 2265, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 929/2264 (0.41)]
# Game: 2266, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 929/2265 (0.41)]
# Game: 2267, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 929/2266 (0.41)]
# Game: 2268, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 929/2267 (0.41)]
# Game: 2269, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 929/2268 (0.41)]
# WIN, Finished in: 0.7809300422668457(seconds)
# Game: 2270, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 930/2269 (0.41)]
# WIN, Finished in: 0.927299976348877(seconds)
# Game: 2271, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 931/2270 (0.41)]
# WIN, Finished in: 3.6627438068389893(seconds)
# Game: 2272, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 932/2271 (0.41)]
# Game: 2273, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 932/2272 (0.41)]
# Game: 2274, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 932/2273 (0.41)]
# WIN, Finished in: 1.2030436992645264(seconds)
# Game: 2275, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 933/2274 (0.41)]
# WIN, Finished in: 1.0471525192260742(seconds)
# Game: 2276, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 934/2275 (0.41)]
# WIN, Finished in: 290.7185447216034(seconds)
# Game: 2277, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 935/2276 (0.41)]
# Game: 2278, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 935/2277 (0.41)]
# Game: 2279, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 935/2278 (0.41)]
# Game: 2280, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 935/2279 (0.41)]
# WIN, Finished in: 9.406622886657715(seconds)
# Game: 2281, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 936/2280 (0.41)]
# Game: 2282, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 936/2281 (0.41)]
# Game: 2283, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 936/2282 (0.41)]
# WIN, Finished in: 47.98404145240784(seconds)
# Game: 2284, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 937/2283 (0.41)]
# Game: 2285, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 937/2284 (0.41)]
# Game: 2286, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 937/2285 (0.41)]
# WIN, Finished in: 0.9216117858886719(seconds)
# Game: 2287, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 938/2286 (0.41)]
# Game: 2288, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 938/2287 (0.41)]
# Game: 2289, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 938/2288 (0.41)]
# Game: 2290, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 938/2289 (0.41)]
# Game: 2291, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 938/2290 (0.41)]
# WIN, Finished in: 290.64689779281616(seconds)
# Game: 2292, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 939/2291 (0.41)]
# Game: 2293, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 939/2292 (0.41)]
# Game: 2294, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 939/2293 (0.41)]
# Game: 2295, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 939/2294 (0.41)]
# WIN, Finished in: 1.302393913269043(seconds)
# Game: 2296, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 940/2295 (0.41)]
# Game: 2297, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 940/2296 (0.41)]
# WIN, Finished in: 0.8283345699310303(seconds)
# Game: 2298, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 941/2297 (0.41)]
# WIN, Finished in: 19.98427653312683(seconds)
# Game: 2299, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 942/2298 (0.41)]
# WIN, Finished in: 0.7654657363891602(seconds)
# Game: 2300, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 943/2299 (0.41)]
# Game: 2301, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 943/2300 (0.41)]
# Game: 2302, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 943/2301 (0.41)]
# WIN, Finished in: 0.8904669284820557(seconds)
# Game: 2303, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 944/2302 (0.41)]
# WIN, Finished in: 3.1720592975616455(seconds)
# Game: 2304, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 945/2303 (0.41)]
# Game: 2305, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 945/2304 (0.41)]
# Game: 2306, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 945/2305 (0.41)]
# Game: 2307, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 945/2306 (0.41)]
# Game: 2308, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 945/2307 (0.41)]
# WIN, Finished in: 0.9533283710479736(seconds)
# Game: 2309, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 946/2308 (0.41)]
# Game: 2310, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 946/2309 (0.41)]
# WIN, Finished in: 0.890143871307373(seconds)
# Game: 2311, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 947/2310 (0.41)]
# WIN, Finished in: 290.7187879085541(seconds)
# Game: 2312, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 948/2311 (0.41)]
# Game: 2313, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 948/2312 (0.41)]
# WIN, Finished in: 0.8021824359893799(seconds)
# Game: 2314, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 949/2313 (0.41)]
# Game: 2315, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 949/2314 (0.41)]
# Game: 2316, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 949/2315 (0.41)]
# Game: 2317, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 949/2316 (0.41)]
# Game: 2318, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 949/2317 (0.41)]
# WIN, Finished in: 0.7812769412994385(seconds)
# Game: 2319, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 950/2318 (0.41)]
# Game: 2320, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 950/2319 (0.41)]
# Game: 2321, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 950/2320 (0.41)]
# WIN, Finished in: 35.249972105026245(seconds)
# Game: 2322, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 951/2321 (0.41)]
# Game: 2323, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 951/2322 (0.41)]
# WIN, Finished in: 0.922025203704834(seconds)
# Game: 2324, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 952/2323 (0.41)]
# WIN, Finished in: 1.1402814388275146(seconds)
# Game: 2325, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 953/2324 (0.41)]
# WIN, Finished in: 0.9062433242797852(seconds)
# Game: 2326, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 954/2325 (0.41)]
# Game: 2327, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 954/2326 (0.41)]
# Game: 2328, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 954/2327 (0.41)]
# Game: 2329, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 954/2328 (0.41)]
# Game: 2330, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 954/2329 (0.41)]
# WIN, Finished in: 0.9218590259552002(seconds)
# Game: 2331, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 955/2330 (0.41)]
# Game: 2332, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 955/2331 (0.41)]
# Game: 2333, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 955/2332 (0.41)]
# WIN, Finished in: 130.17163348197937(seconds)
# Game: 2334, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 956/2333 (0.41)]
# Game: 2335, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 956/2334 (0.41)]
# Game: 2336, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 956/2335 (0.41)]
# WIN, Finished in: 24.92142391204834(seconds)
# Game: 2337, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 957/2336 (0.41)]
# WIN, Finished in: 13.753948211669922(seconds)
# Game: 2338, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 958/2337 (0.41)]
# Game: 2339, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 958/2338 (0.41)]
# Game: 2340, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 958/2339 (0.41)]
# Game: 2341, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 958/2340 (0.41)]
# WIN, Finished in: 0.8438074588775635(seconds)
# Game: 2342, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 959/2341 (0.41)]
# WIN, Finished in: 0.9374630451202393(seconds)
# Game: 2343, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 960/2342 (0.41)]
# Game: 2344, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 960/2343 (0.41)]
# WIN, Finished in: 1.5157880783081055(seconds)
# Game: 2345, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 961/2344 (0.41)]
# WIN, Finished in: 0.780987024307251(seconds)
# Game: 2346, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 962/2345 (0.41)]
# Game: 2347, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 962/2346 (0.41)]
# Game: 2348, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 962/2347 (0.41)]
# Game: 2349, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 962/2348 (0.41)]
# Game: 2350, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 962/2349 (0.41)]
# Game: 2351, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 962/2350 (0.41)]
# WIN, Finished in: 0.8584747314453125(seconds)
# Game: 2352, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 963/2351 (0.41)]
# Game: 2353, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 963/2352 (0.41)]
# WIN, Finished in: 6.875037431716919(seconds)
# Game: 2354, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 964/2353 (0.41)]
# Game: 2355, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 964/2354 (0.41)]
# Game: 2356, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 964/2355 (0.41)]
# Game: 2357, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 964/2356 (0.41)]
# Game: 2358, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 964/2357 (0.41)]
# WIN, Finished in: 2.2811951637268066(seconds)
# Game: 2359, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 965/2358 (0.41)]
# WIN, Finished in: 8.784329175949097(seconds)
# Game: 2360, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 966/2359 (0.41)]
# Game: 2361, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 966/2360 (0.41)]
# WIN, Finished in: 5.8912341594696045(seconds)
# Game: 2362, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 967/2361 (0.41)]
# Game: 2363, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 967/2362 (0.41)]
# WIN, Finished in: 5.01496434211731(seconds)
# Game: 2364, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 968/2363 (0.41)]
# Game: 2365, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 968/2364 (0.41)]
# Game: 2366, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 968/2365 (0.41)]
# WIN, Finished in: 0.961315393447876(seconds)
# Game: 2367, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 969/2366 (0.41)]
# Game: 2368, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 969/2367 (0.41)]
# WIN, Finished in: 0.7814548015594482(seconds)
# Game: 2369, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 970/2368 (0.41)]
# WIN, Finished in: 3.5467615127563477(seconds)
# Game: 2370, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 971/2369 (0.41)]
# Game: 2371, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 971/2370 (0.41)]
# WIN, Finished in: 4.281231880187988(seconds)
# Game: 2372, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 972/2371 (0.41)]
# Game: 2373, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 972/2372 (0.41)]
# Game: 2374, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 972/2373 (0.41)]
# WIN, Finished in: 0.7806296348571777(seconds)
# Game: 2375, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 973/2374 (0.41)]
# Game: 2376, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 973/2375 (0.41)]
# Game: 2377, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 973/2376 (0.41)]
# Game: 2378, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 973/2377 (0.41)]
# WIN, Finished in: 1.0151851177215576(seconds)
# Game: 2379, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 974/2378 (0.41)]
# WIN, Finished in: 58.62501049041748(seconds)
# Game: 2380, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 975/2379 (0.41)]
# Game: 2381, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 975/2380 (0.41)]
# Game: 2382, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 975/2381 (0.41)]
# WIN, Finished in: 11.328281879425049(seconds)
# Game: 2383, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 976/2382 (0.41)]
# WIN, Finished in: 0.7655470371246338(seconds)
# Game: 2384, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 977/2383 (0.41)]
# Game: 2385, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 977/2384 (0.41)]
# WIN, Finished in: 1.781175136566162(seconds)
# Game: 2386, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 978/2385 (0.41)]
# Game: 2387, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 978/2386 (0.41)]
# WIN, Finished in: 0.7499914169311523(seconds)
# Game: 2388, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 979/2387 (0.41)]
# Game: 2389, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 979/2388 (0.41)]
# Game: 2390, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 979/2389 (0.41)]
# Game: 2391, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 979/2390 (0.41)]
# WIN, Finished in: 0.9531095027923584(seconds)
# Game: 2392, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 980/2391 (0.41)]
# WIN, Finished in: 0.8905987739562988(seconds)
# Game: 2393, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 981/2392 (0.41)]
# Game: 2394, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 981/2393 (0.41)]
# Game: 2395, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 981/2394 (0.41)]
# Game: 2396, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 981/2395 (0.41)]
# Game: 2397, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 981/2396 (0.41)]
# Game: 2398, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 981/2397 (0.41)]
# Game: 2399, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 981/2398 (0.41)]
# WIN, Finished in: 290.5935790538788(seconds)
# Game: 2400, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 982/2399 (0.41)]
# Game: 2401, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 982/2400 (0.41)]
# WIN, Finished in: 1.0312464237213135(seconds)
# Game: 2402, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 983/2401 (0.41)]
# Game: 2403, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 983/2402 (0.41)]
# WIN, Finished in: 1.217923879623413(seconds)
# Game: 2404, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 984/2403 (0.41)]
# WIN, Finished in: 10.312562704086304(seconds)
# Game: 2405, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 985/2404 (0.41)]
# Game: 2406, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 985/2405 (0.41)]
# Game: 2407, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 985/2406 (0.41)]
# Game: 2408, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 985/2407 (0.41)]
# WIN, Finished in: 3.3906362056732178(seconds)
# Game: 2409, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 986/2408 (0.41)]
# WIN, Finished in: 7.563018321990967(seconds)
# Game: 2410, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 987/2409 (0.41)]
# WIN, Finished in: 4.4843738079071045(seconds)
# Game: 2411, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 988/2410 (0.41)]
# WIN, Finished in: 0.9371600151062012(seconds)
# Game: 2412, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 989/2411 (0.41)]
# Game: 2413, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 989/2412 (0.41)]
# WIN, Finished in: 4.28156590461731(seconds)
# Game: 2414, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 990/2413 (0.41)]
# Game: 2415, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 990/2414 (0.41)]
# Game: 2416, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 990/2415 (0.41)]
# WIN, Finished in: 75.57769846916199(seconds)
# Game: 2417, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 991/2416 (0.41)]
# Game: 2418, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 991/2417 (0.41)]
# Game: 2419, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 991/2418 (0.41)]
# WIN, Finished in: 7.218654155731201(seconds)
# Game: 2420, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 992/2419 (0.41)]
# WIN, Finished in: 290.3436198234558(seconds)
# Game: 2421, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 993/2420 (0.41)]
# WIN, Finished in: 59.23479223251343(seconds)
# Game: 2422, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 994/2421 (0.41)]
# Game: 2423, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 994/2422 (0.41)]
# Game: 2424, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 994/2423 (0.41)]
# WIN, Finished in: 4.844085693359375(seconds)
# Game: 2425, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 995/2424 (0.41)]
# WIN, Finished in: 17.99571919441223(seconds)
# Game: 2426, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 996/2425 (0.41)]
# WIN, Finished in: 27.12497329711914(seconds)
# Game: 2427, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 997/2426 (0.41)]
# Game: 2428, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 997/2427 (0.41)]
# WIN, Finished in: 24.437403917312622(seconds)
# Game: 2429, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 998/2428 (0.41)]
# WIN, Finished in: 1.171844244003296(seconds)
# Game: 2430, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 999/2429 (0.41)]
# WIN, Finished in: 210.21868658065796(seconds)
# Game: 2431, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1000/2430 (0.41)]
# Game: 2432, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1000/2431 (0.41)]
# Game: 2433, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1000/2432 (0.41)]
# WIN, Finished in: 2.39018177986145(seconds)
# Game: 2434, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1001/2433 (0.41)]
# Game: 2435, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1001/2434 (0.41)]
# WIN, Finished in: 7.468642711639404(seconds)
# Game: 2436, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1002/2435 (0.41)]
# WIN, Finished in: 3.7959165573120117(seconds)
# Game: 2437, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1003/2436 (0.41)]
# Game: 2438, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1003/2437 (0.41)]
# Game: 2439, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1003/2438 (0.41)]
# WIN, Finished in: 1.8281548023223877(seconds)
# Game: 2440, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1004/2439 (0.41)]
# Game: 2441, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1004/2440 (0.41)]
# Game: 2442, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1004/2441 (0.41)]
# Game: 2443, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1004/2442 (0.41)]
# WIN, Finished in: 1.468440055847168(seconds)
# Game: 2444, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1005/2443 (0.41)]
# WIN, Finished in: 1.9997467994689941(seconds)
# Game: 2445, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1006/2444 (0.41)]
# Game: 2446, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1006/2445 (0.41)]
# Game: 2447, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1006/2446 (0.41)]
# Game: 2448, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1006/2447 (0.41)]
# Game: 2449, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1006/2448 (0.41)]
# WIN, Finished in: 1.2499759197235107(seconds)
# Game: 2450, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1007/2449 (0.41)]
# WIN, Finished in: 2.4062271118164062(seconds)
# Game: 2451, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1008/2450 (0.41)]
# Game: 2452, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1008/2451 (0.41)]
# Game: 2453, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1008/2452 (0.41)]
# WIN, Finished in: 1.171886682510376(seconds)
# Game: 2454, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1009/2453 (0.41)]
# Game: 2455, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1009/2454 (0.41)]
# WIN, Finished in: 290.0338819026947(seconds)
# Game: 2456, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1010/2455 (0.41)]
# WIN, Finished in: 0.7684707641601562(seconds)
# Game: 2457, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1011/2456 (0.41)]
# Game: 2458, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1011/2457 (0.41)]
# WIN, Finished in: 0.984391450881958(seconds)
# Game: 2459, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1012/2458 (0.41)]
# Game: 2460, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1012/2459 (0.41)]
# WIN, Finished in: 0.9374842643737793(seconds)
# Game: 2461, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1013/2460 (0.41)]
# Game: 2462, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1013/2461 (0.41)]
# Game: 2463, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1013/2462 (0.41)]
# WIN, Finished in: 22.591214656829834(seconds)
# Game: 2464, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1014/2463 (0.41)]
# Game: 2465, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1014/2464 (0.41)]
# WIN, Finished in: 3.1405997276306152(seconds)
# Game: 2466, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1015/2465 (0.41)]
# Game: 2467, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1015/2466 (0.41)]
# Game: 2468, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1015/2467 (0.41)]
# WIN, Finished in: 35.90641212463379(seconds)
# Game: 2469, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1016/2468 (0.41)]
# Game: 2470, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1016/2469 (0.41)]
# Game: 2471, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1016/2470 (0.41)]
# Game: 2472, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1016/2471 (0.41)]
# WIN, Finished in: 0.8902699947357178(seconds)
# Game: 2473, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1017/2472 (0.41)]
# WIN, Finished in: 24.31248927116394(seconds)
# Game: 2474, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1018/2473 (0.41)]
# WIN, Finished in: 0.8281028270721436(seconds)
# Game: 2475, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1019/2474 (0.41)]
# WIN, Finished in: 0.9063100814819336(seconds)
# Game: 2476, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1020/2475 (0.41)]
# WIN, Finished in: 7.766463041305542(seconds)
# Game: 2477, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1021/2476 (0.41)]
# WIN, Finished in: 1.061563491821289(seconds)
# Game: 2478, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1022/2477 (0.41)]
# Game: 2479, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1022/2478 (0.41)]
# Game: 2480, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1022/2479 (0.41)]
# WIN, Finished in: 175.76530504226685(seconds)
# Game: 2481, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1023/2480 (0.41)]
# WIN, Finished in: 4.8748860359191895(seconds)
# Game: 2482, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1024/2481 (0.41)]
# Game: 2483, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1024/2482 (0.41)]
# Game: 2484, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1024/2483 (0.41)]
# WIN, Finished in: 0.7811965942382812(seconds)
# Game: 2485, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1025/2484 (0.41)]
# WIN, Finished in: 0.9532103538513184(seconds)
# Game: 2486, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1026/2485 (0.41)]
# WIN, Finished in: 34.812416553497314(seconds)
# Game: 2487, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1027/2486 (0.41)]
# Game: 2488, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1027/2487 (0.41)]
# Game: 2489, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1027/2488 (0.41)]
# Game: 2490, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1027/2489 (0.41)]
# Game: 2491, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1027/2490 (0.41)]
# WIN, Finished in: 1.1558480262756348(seconds)
# Game: 2492, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1028/2491 (0.41)]
# Game: 2493, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1028/2492 (0.41)]
# WIN, Finished in: 1.280634880065918(seconds)
# Game: 2494, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1029/2493 (0.41)]
# WIN, Finished in: 2.506086587905884(seconds)
# Game: 2495, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1030/2494 (0.41)]
# Game: 2496, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1030/2495 (0.41)]
# Game: 2497, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1030/2496 (0.41)]
# WIN, Finished in: 5.812612056732178(seconds)
# Game: 2498, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1031/2497 (0.41)]
# Game: 2499, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1031/2498 (0.41)]
# Game: 2500, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1031/2499 (0.41)]
# WIN, Finished in: 2.2968311309814453(seconds)
# Game: 2501, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1032/2500 (0.41)]
# WIN, Finished in: 0.9218010902404785(seconds)
# Game: 2502, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1033/2501 (0.41)]
# Game: 2503, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1033/2502 (0.41)]
# Game: 2504, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1033/2503 (0.41)]
# Game: 2505, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1033/2504 (0.41)]
# Game: 2506, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1033/2505 (0.41)]
# Game: 2507, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1033/2506 (0.41)]
# WIN, Finished in: 290.90513730049133(seconds)
# Game: 2508, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1034/2507 (0.41)]
# Game: 2509, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1034/2508 (0.41)]
# Game: 2510, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1034/2509 (0.41)]
# Game: 2511, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1034/2510 (0.41)]
# WIN, Finished in: 0.9057679176330566(seconds)
# Game: 2512, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1035/2511 (0.41)]
# WIN, Finished in: 5.734715700149536(seconds)
# Game: 2513, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1036/2512 (0.41)]
# Game: 2514, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1036/2513 (0.41)]
# WIN, Finished in: 0.8106732368469238(seconds)
# Game: 2515, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1037/2514 (0.41)]
# WIN, Finished in: 2.2889132499694824(seconds)
# Game: 2516, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1038/2515 (0.41)]
# WIN, Finished in: 7.31250524520874(seconds)
# Game: 2517, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1039/2516 (0.41)]
# WIN, Finished in: 21.406171560287476(seconds)
# Game: 2518, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1040/2517 (0.41)]
# Game: 2519, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1040/2518 (0.41)]
# Game: 2520, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1040/2519 (0.41)]
# WIN, Finished in: 1.031484603881836(seconds)
# Game: 2521, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1041/2520 (0.41)]
# Game: 2522, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1041/2521 (0.41)]
# Game: 2523, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1041/2522 (0.41)]
# Game: 2524, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1041/2523 (0.41)]
# WIN, Finished in: 1.218778133392334(seconds)
# Game: 2525, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1042/2524 (0.41)]
# Game: 2526, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1042/2525 (0.41)]
# Game: 2527, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1042/2526 (0.41)]
# Game: 2528, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1042/2527 (0.41)]
# Game: 2529, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1042/2528 (0.41)]
# WIN, Finished in: 243.37499594688416(seconds)
# Game: 2530, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1043/2529 (0.41)]
# WIN, Finished in: 290.64051389694214(seconds)
# Game: 2531, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1044/2530 (0.41)]
# Game: 2532, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1044/2531 (0.41)]
# WIN, Finished in: 52.26533317565918(seconds)
# Game: 2533, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1045/2532 (0.41)]
# Game: 2534, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1045/2533 (0.41)]
# Game: 2535, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1045/2534 (0.41)]
# WIN, Finished in: 0.8127520084381104(seconds)
# Game: 2536, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1046/2535 (0.41)]
# Game: 2537, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1046/2536 (0.41)]
# Game: 2538, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1046/2537 (0.41)]
# WIN, Finished in: 0.7810084819793701(seconds)
# Game: 2539, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1047/2538 (0.41)]
# Game: 2540, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1047/2539 (0.41)]
# Game: 2541, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1047/2540 (0.41)]
# WIN, Finished in: 1.1379098892211914(seconds)
# Game: 2542, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1048/2541 (0.41)]
# Game: 2543, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1048/2542 (0.41)]
# Game: 2544, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1048/2543 (0.41)]
# WIN, Finished in: 1.9063644409179688(seconds)
# Game: 2545, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1049/2544 (0.41)]
# Game: 2546, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1049/2545 (0.41)]
# WIN, Finished in: 17.84335422515869(seconds)
# Game: 2547, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1050/2546 (0.41)]
# WIN, Finished in: 1.2837817668914795(seconds)
# Game: 2548, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1051/2547 (0.41)]
# WIN, Finished in: 0.9718999862670898(seconds)
# Game: 2549, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1052/2548 (0.41)]
# WIN, Finished in: 289.46893882751465(seconds)
# Game: 2550, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1053/2549 (0.41)]
# Game: 2551, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1053/2550 (0.41)]
# WIN, Finished in: 2.968773126602173(seconds)
# Game: 2552, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1054/2551 (0.41)]
# WIN, Finished in: 0.7893581390380859(seconds)
# Game: 2553, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1055/2552 (0.41)]
# Game: 2554, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1055/2553 (0.41)]
# WIN, Finished in: 1.9061639308929443(seconds)
# Game: 2555, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1056/2554 (0.41)]
# WIN, Finished in: 2.859459161758423(seconds)
# Game: 2556, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1057/2555 (0.41)]
# WIN, Finished in: 0.8440356254577637(seconds)
# Game: 2557, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1058/2556 (0.41)]
# WIN, Finished in: 0.9526948928833008(seconds)
# Game: 2558, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1059/2557 (0.41)]
# WIN, Finished in: 3.5147547721862793(seconds)
# Game: 2559, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1060/2558 (0.41)]
# Game: 2560, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1060/2559 (0.41)]
# Game: 2561, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1060/2560 (0.41)]
# Game: 2562, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1060/2561 (0.41)]
# Game: 2563, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1060/2562 (0.41)]
# Game: 2564, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1060/2563 (0.41)]
# Game: 2565, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1060/2564 (0.41)]
# Game: 2566, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1060/2565 (0.41)]
# WIN, Finished in: 55.13997220993042(seconds)
# Game: 2567, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1061/2566 (0.41)]
# Game: 2568, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1061/2567 (0.41)]
# Game: 2569, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1061/2568 (0.41)]
# Game: 2570, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1061/2569 (0.41)]
# WIN, Finished in: 3.2031986713409424(seconds)
# Game: 2571, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1062/2570 (0.41)]
# WIN, Finished in: 1.0623669624328613(seconds)
# Game: 2572, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1063/2571 (0.41)]
# WIN, Finished in: 2.279017925262451(seconds)
# Game: 2573, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1064/2572 (0.41)]
# WIN, Finished in: 0.92983078956604(seconds)
# Game: 2574, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1065/2573 (0.41)]
# WIN, Finished in: 1.562490463256836(seconds)
# Game: 2575, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1066/2574 (0.41)]
# Game: 2576, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1066/2575 (0.41)]
# Game: 2577, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1066/2576 (0.41)]
# Game: 2578, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1066/2577 (0.41)]
# WIN, Finished in: 290.14045572280884(seconds)
# Game: 2579, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1067/2578 (0.41)]
# Game: 2580, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1067/2579 (0.41)]
# WIN, Finished in: 1.062330961227417(seconds)
# Game: 2581, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1068/2580 (0.41)]
# Game: 2582, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1068/2581 (0.41)]
# Game: 2583, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1068/2582 (0.41)]
# Game: 2584, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1068/2583 (0.41)]
# Game: 2585, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1068/2584 (0.41)]
# WIN, Finished in: 36.218364000320435(seconds)
# Game: 2586, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1069/2585 (0.41)]
# Game: 2587, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1069/2586 (0.41)]
# WIN, Finished in: 0.8128907680511475(seconds)
# Game: 2588, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1070/2587 (0.41)]
# WIN, Finished in: 0.9058194160461426(seconds)
# Game: 2589, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1071/2588 (0.41)]
# WIN, Finished in: 0.9062473773956299(seconds)
# Game: 2590, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1072/2589 (0.41)]
# WIN, Finished in: 11.062851905822754(seconds)
# Game: 2591, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1073/2590 (0.41)]
# Game: 2592, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1073/2591 (0.41)]
# Game: 2593, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1073/2592 (0.41)]
# WIN, Finished in: 5.844027519226074(seconds)
# Game: 2594, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1074/2593 (0.41)]
# Game: 2595, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1074/2594 (0.41)]
# Game: 2596, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1074/2595 (0.41)]
# Game: 2597, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1074/2596 (0.41)]
# Game: 2598, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1074/2597 (0.41)]
# WIN, Finished in: 5.1402740478515625(seconds)
# Game: 2599, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1075/2598 (0.41)]
# Game: 2600, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1075/2599 (0.41)]
# WIN, Finished in: 45.484028816223145(seconds)
# Game: 2601, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1076/2600 (0.41)]
# WIN, Finished in: 0.7344009876251221(seconds)
# Game: 2602, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1077/2601 (0.41)]
# Game: 2603, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1077/2602 (0.41)]
# Game: 2604, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1077/2603 (0.41)]
# Game: 2605, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1077/2604 (0.41)]
# Game: 2606, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1077/2605 (0.41)]
# Game: 2607, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1077/2606 (0.41)]
# Game: 2608, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1077/2607 (0.41)]
# WIN, Finished in: 2.51568865776062(seconds)
# Game: 2609, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1078/2608 (0.41)]
# Game: 2610, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1078/2609 (0.41)]
# WIN, Finished in: 0.8743681907653809(seconds)
# Game: 2611, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1079/2610 (0.41)]
# Game: 2612, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1079/2611 (0.41)]
# Game: 2613, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1079/2612 (0.41)]
# Game: 2614, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1079/2613 (0.41)]
# Game: 2615, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1079/2614 (0.41)]
# Game: 2616, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1079/2615 (0.41)]
# WIN, Finished in: 290.29699087142944(seconds)
# Game: 2617, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1080/2616 (0.41)]
# WIN, Finished in: 0.8124334812164307(seconds)
# Game: 2618, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1081/2617 (0.41)]
# Game: 2619, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1081/2618 (0.41)]
# Game: 2620, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1081/2619 (0.41)]
# Game: 2621, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1081/2620 (0.41)]
# Game: 2622, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1081/2621 (0.41)]
# WIN, Finished in: 0.9686856269836426(seconds)
# Game: 2623, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1082/2622 (0.41)]
# Game: 2624, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1082/2623 (0.41)]
# WIN, Finished in: 0.9375357627868652(seconds)
# Game: 2625, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1083/2624 (0.41)]
# Game: 2626, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1083/2625 (0.41)]
# Game: 2627, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1083/2626 (0.41)]
# Game: 2628, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1083/2627 (0.41)]
# Game: 2629, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1083/2628 (0.41)]
# WIN, Finished in: 0.9861578941345215(seconds)
# Game: 2630, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1084/2629 (0.41)]
# Game: 2631, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1084/2630 (0.41)]
# Game: 2632, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1084/2631 (0.41)]
# Game: 2633, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1084/2632 (0.41)]
# Game: 2634, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1084/2633 (0.41)]
# WIN, Finished in: 24.828328132629395(seconds)
# Game: 2635, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1085/2634 (0.41)]
# WIN, Finished in: 1.281022071838379(seconds)
# Game: 2636, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1086/2635 (0.41)]
# Game: 2637, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1086/2636 (0.41)]
# Game: 2638, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1086/2637 (0.41)]
# Game: 2639, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1086/2638 (0.41)]
# Game: 2640, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1086/2639 (0.41)]
# Game: 2641, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1086/2640 (0.41)]
# WIN, Finished in: 0.7657124996185303(seconds)
# Game: 2642, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1087/2641 (0.41)]
# Game: 2643, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1087/2642 (0.41)]
# WIN, Finished in: 1.0958061218261719(seconds)
# Game: 2644, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1088/2643 (0.41)]
# Game: 2645, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1088/2644 (0.41)]
# Game: 2646, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1088/2645 (0.41)]
# Game: 2647, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1088/2646 (0.41)]
# WIN, Finished in: 3.234574317932129(seconds)
# Game: 2648, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1089/2647 (0.41)]
# WIN, Finished in: 290.5002341270447(seconds)
# Game: 2649, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1090/2648 (0.41)]
# Game: 2650, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1090/2649 (0.41)]
# Game: 2651, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1090/2650 (0.41)]
# WIN, Finished in: 0.8905696868896484(seconds)
# Game: 2652, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1091/2651 (0.41)]
# Game: 2653, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1091/2652 (0.41)]
# WIN, Finished in: 290.5937683582306(seconds)
# Game: 2654, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1092/2653 (0.41)]
# WIN, Finished in: 9.093679904937744(seconds)
# Game: 2655, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1093/2654 (0.41)]
# WIN, Finished in: 3.015580177307129(seconds)
# Game: 2656, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1094/2655 (0.41)]
# WIN, Finished in: 0.7656562328338623(seconds)
# Game: 2657, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1095/2656 (0.41)]
# Game: 2658, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1095/2657 (0.41)]
# WIN, Finished in: 0.9687609672546387(seconds)
# Game: 2659, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1096/2658 (0.41)]
# WIN, Finished in: 222.06247758865356(seconds)
# Game: 2660, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1097/2659 (0.41)]
# Game: 2661, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1097/2660 (0.41)]
# Game: 2662, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1097/2661 (0.41)]
# Game: 2663, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1097/2662 (0.41)]
# Game: 2664, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1097/2663 (0.41)]
# Game: 2665, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1097/2664 (0.41)]
# Game: 2666, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1097/2665 (0.41)]
# WIN, Finished in: 165.51542615890503(seconds)
# Game: 2667, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2666 (0.41)]
# Game: 2668, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2667 (0.41)]
# Game: 2669, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2668 (0.41)]
# Game: 2670, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2669 (0.41)]
# Game: 2671, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2670 (0.41)]
# Game: 2672, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2671 (0.41)]
# Game: 2673, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2672 (0.41)]
# Game: 2674, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2673 (0.41)]
# Game: 2675, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2674 (0.41)]
# Game: 2676, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2675 (0.41)]
# Game: 2677, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2676 (0.41)]
# Game: 2678, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1098/2677 (0.41)]
# WIN, Finished in: 3.7346034049987793(seconds)
# Game: 2679, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1099/2678 (0.41)]
# Game: 2680, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1099/2679 (0.41)]
# Game: 2681, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1099/2680 (0.41)]
# WIN, Finished in: 98.59399795532227(seconds)
# Game: 2682, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1100/2681 (0.41)]
# WIN, Finished in: 1.163712501525879(seconds)
# Game: 2683, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1101/2682 (0.41)]
# WIN, Finished in: 1.107285499572754(seconds)
# Game: 2684, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1102/2683 (0.41)]
# WIN, Finished in: 0.9687144756317139(seconds)
# Game: 2685, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1103/2684 (0.41)]
# Game: 2686, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1103/2685 (0.41)]
# Game: 2687, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1103/2686 (0.41)]
# WIN, Finished in: 1.0112371444702148(seconds)
# Game: 2688, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1104/2687 (0.41)]
# Game: 2689, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1104/2688 (0.41)]
# WIN, Finished in: 1.1877174377441406(seconds)
# Game: 2690, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1105/2689 (0.41)]
# Game: 2691, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1105/2690 (0.41)]
# Game: 2692, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1105/2691 (0.41)]
# WIN, Finished in: 0.8276855945587158(seconds)
# Game: 2693, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1106/2692 (0.41)]
# WIN, Finished in: 0.8906550407409668(seconds)
# Game: 2694, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1107/2693 (0.41)]
# WIN, Finished in: 0.9374179840087891(seconds)
# Game: 2695, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1108/2694 (0.41)]
# WIN, Finished in: 2.703091621398926(seconds)
# Game: 2696, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1109/2695 (0.41)]
# Game: 2697, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1109/2696 (0.41)]
# WIN, Finished in: 60.281548738479614(seconds)
# Game: 2698, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1110/2697 (0.41)]
# Game: 2699, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1110/2698 (0.41)]
# WIN, Finished in: 0.8594117164611816(seconds)
# Game: 2700, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1111/2699 (0.41)]
# WIN, Finished in: 0.7815420627593994(seconds)
# Game: 2701, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1112/2700 (0.41)]
# Game: 2702, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1112/2701 (0.41)]
# Game: 2703, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1112/2702 (0.41)]
# WIN, Finished in: 18.5642671585083(seconds)
# Game: 2704, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1113/2703 (0.41)]
# Game: 2705, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1113/2704 (0.41)]
# Game: 2706, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1113/2705 (0.41)]
# WIN, Finished in: 96.64162349700928(seconds)
# Game: 2707, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1114/2706 (0.41)]
# Game: 2708, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1114/2707 (0.41)]
# WIN, Finished in: 30.697077989578247(seconds)
# Game: 2709, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1115/2708 (0.41)]
# Game: 2710, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1115/2709 (0.41)]
# Game: 2711, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1115/2710 (0.41)]
# Game: 2712, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1115/2711 (0.41)]
# Game: 2713, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1115/2712 (0.41)]
# Game: 2714, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1115/2713 (0.41)]
# WIN, Finished in: 4.359819412231445(seconds)
# Game: 2715, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1116/2714 (0.41)]
# WIN, Finished in: 0.7808308601379395(seconds)
# Game: 2716, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1117/2715 (0.41)]
# Game: 2717, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1117/2716 (0.41)]
# Game: 2718, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1117/2717 (0.41)]
# WIN, Finished in: 141.35938358306885(seconds)
# Game: 2719, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1118/2718 (0.41)]
# WIN, Finished in: 0.7657194137573242(seconds)
# Game: 2720, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1119/2719 (0.41)]
# Game: 2721, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1119/2720 (0.41)]
# Game: 2722, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1119/2721 (0.41)]
# Game: 2723, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1119/2722 (0.41)]
# WIN, Finished in: 1.0155704021453857(seconds)
# Game: 2724, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1120/2723 (0.41)]
# Game: 2725, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1120/2724 (0.41)]
# Game: 2726, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1120/2725 (0.41)]
# Game: 2727, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1120/2726 (0.41)]
# Game: 2728, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1120/2727 (0.41)]
# Game: 2729, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1120/2728 (0.41)]
# WIN, Finished in: 0.8749279975891113(seconds)
# Game: 2730, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1121/2729 (0.41)]
# Game: 2731, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1121/2730 (0.41)]
# Game: 2732, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1121/2731 (0.41)]
# Game: 2733, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1121/2732 (0.41)]
# WIN, Finished in: 0.8908824920654297(seconds)
# Game: 2734, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1122/2733 (0.41)]
# Game: 2735, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1122/2734 (0.41)]
# Game: 2736, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1122/2735 (0.41)]
# Game: 2737, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1122/2736 (0.41)]
# Game: 2738, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1122/2737 (0.41)]
# Game: 2739, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1122/2738 (0.41)]
# Game: 2740, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1122/2739 (0.41)]
# WIN, Finished in: 1.4377470016479492(seconds)
# Game: 2741, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1123/2740 (0.41)]
# Game: 2742, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1123/2741 (0.41)]
# WIN, Finished in: 0.8281168937683105(seconds)
# Game: 2743, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1124/2742 (0.41)]
# Game: 2744, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1124/2743 (0.41)]
# WIN, Finished in: 1.5624797344207764(seconds)
# Game: 2745, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2744 (0.41)]
# Game: 2746, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2745 (0.41)]
# Game: 2747, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2746 (0.41)]
# Game: 2748, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2747 (0.41)]
# Game: 2749, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2748 (0.41)]
# Game: 2750, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2749 (0.41)]
# Game: 2751, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2750 (0.41)]
# Game: 2752, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2751 (0.41)]
# Game: 2753, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2752 (0.41)]
# Game: 2754, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1125/2753 (0.41)]
# WIN, Finished in: 0.7501859664916992(seconds)
# Game: 2755, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1126/2754 (0.41)]
# WIN, Finished in: 1.515425205230713(seconds)
# Game: 2756, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1127/2755 (0.41)]
# WIN, Finished in: 0.9131205081939697(seconds)
# Game: 2757, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1128/2756 (0.41)]
# Game: 2758, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1128/2757 (0.41)]
# Game: 2759, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1128/2758 (0.41)]
# Game: 2760, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1128/2759 (0.41)]
# WIN, Finished in: 5.140809774398804(seconds)
# Game: 2761, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1129/2760 (0.41)]
# Game: 2762, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1129/2761 (0.41)]
# Game: 2763, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1129/2762 (0.41)]
# WIN, Finished in: 114.46864247322083(seconds)
# Game: 2764, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1130/2763 (0.41)]
# Game: 2765, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1130/2764 (0.41)]
# WIN, Finished in: 0.7656359672546387(seconds)
# Game: 2766, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1131/2765 (0.41)]
# WIN, Finished in: 0.8437502384185791(seconds)
# Game: 2767, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1132/2766 (0.41)]
# Game: 2768, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1132/2767 (0.41)]
# Game: 2769, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1132/2768 (0.41)]
# Game: 2770, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1132/2769 (0.41)]
# Game: 2771, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1132/2770 (0.41)]
# Game: 2772, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1132/2771 (0.41)]
# WIN, Finished in: 0.9202685356140137(seconds)
# Game: 2773, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1133/2772 (0.41)]
# Game: 2774, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1133/2773 (0.41)]
# Game: 2775, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1133/2774 (0.41)]
# WIN, Finished in: 10.218682765960693(seconds)
# Game: 2776, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1134/2775 (0.41)]
# WIN, Finished in: 1.6298885345458984(seconds)
# Game: 2777, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1135/2776 (0.41)]
# WIN, Finished in: 0.92276930809021(seconds)
# Game: 2778, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1136/2777 (0.41)]
# Game: 2779, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1136/2778 (0.41)]
# WIN, Finished in: 6.953583717346191(seconds)
# Game: 2780, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1137/2779 (0.41)]
# Game: 2781, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1137/2780 (0.41)]
# Game: 2782, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1137/2781 (0.41)]
# Game: 2783, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1137/2782 (0.41)]
# WIN, Finished in: 147.7187783718109(seconds)
# Game: 2784, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1138/2783 (0.41)]
# Game: 2785, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1138/2784 (0.41)]
# WIN, Finished in: 0.7967841625213623(seconds)
# Game: 2786, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1139/2785 (0.41)]
# Game: 2787, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1139/2786 (0.41)]
# WIN, Finished in: 4.374646186828613(seconds)
# Game: 2788, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1140/2787 (0.41)]
# Game: 2789, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1140/2788 (0.41)]
# Game: 2790, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1140/2789 (0.41)]
# Game: 2791, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1140/2790 (0.41)]
# Game: 2792, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1140/2791 (0.41)]
# Game: 2793, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1140/2792 (0.41)]
# WIN, Finished in: 0.8901181221008301(seconds)
# Game: 2794, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1141/2793 (0.41)]
# Game: 2795, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1141/2794 (0.41)]
# WIN, Finished in: 1.0172145366668701(seconds)
# Game: 2796, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1142/2795 (0.41)]
# Game: 2797, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1142/2796 (0.41)]
# Game: 2798, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1142/2797 (0.41)]
# WIN, Finished in: 1.8280370235443115(seconds)
# Game: 2799, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1143/2798 (0.41)]
# Game: 2800, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1143/2799 (0.41)]
# Game: 2801, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1143/2800 (0.41)]
# WIN, Finished in: 30.10942268371582(seconds)
# Game: 2802, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1144/2801 (0.41)]
# WIN, Finished in: 28.203107118606567(seconds)
# Game: 2803, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1145/2802 (0.41)]
# Game: 2804, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1145/2803 (0.41)]
# Game: 2805, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1145/2804 (0.41)]
# WIN, Finished in: 2.7813096046447754(seconds)
# Game: 2806, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1146/2805 (0.41)]
# Game: 2807, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1146/2806 (0.41)]
# WIN, Finished in: 31.687005281448364(seconds)
# Game: 2808, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1147/2807 (0.41)]
# Game: 2809, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1147/2808 (0.41)]
# WIN, Finished in: 26.171751499176025(seconds)
# Game: 2810, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1148/2809 (0.41)]
# Game: 2811, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1148/2810 (0.41)]
# Game: 2812, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1148/2811 (0.41)]
# Game: 2813, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1148/2812 (0.41)]
# WIN, Finished in: 0.7655370235443115(seconds)
# Game: 2814, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1149/2813 (0.41)]
# WIN, Finished in: 2.8281874656677246(seconds)
# Game: 2815, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1150/2814 (0.41)]
# Game: 2816, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1150/2815 (0.41)]
# WIN, Finished in: 0.9477503299713135(seconds)
# Game: 2817, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1151/2816 (0.41)]
# Game: 2818, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1151/2817 (0.41)]
# WIN, Finished in: 1.3750100135803223(seconds)
# Game: 2819, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1152/2818 (0.41)]
# Game: 2820, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1152/2819 (0.41)]
# Game: 2821, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1152/2820 (0.41)]
# WIN, Finished in: 1.12495756149292(seconds)
# Game: 2822, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1153/2821 (0.41)]
# Game: 2823, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1153/2822 (0.41)]
# Game: 2824, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1153/2823 (0.41)]
# Game: 2825, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1153/2824 (0.41)]
# WIN, Finished in: 13.859567165374756(seconds)
# Game: 2826, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1154/2825 (0.41)]
# Game: 2827, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1154/2826 (0.41)]
# Game: 2828, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1154/2827 (0.41)]
# WIN, Finished in: 36.32811188697815(seconds)
# Game: 2829, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1155/2828 (0.41)]
# WIN, Finished in: 2.3595130443573(seconds)
# Game: 2830, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1156/2829 (0.41)]
# Game: 2831, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1156/2830 (0.41)]
# Game: 2832, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1156/2831 (0.41)]
# Game: 2833, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1156/2832 (0.41)]
# WIN, Finished in: 0.8546738624572754(seconds)
# Game: 2834, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1157/2833 (0.41)]
# WIN, Finished in: 0.9222116470336914(seconds)
# Game: 2835, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1158/2834 (0.41)]
# Game: 2836, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1158/2835 (0.41)]
# Game: 2837, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1158/2836 (0.41)]
# Game: 2838, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1158/2837 (0.41)]
# Game: 2839, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1158/2838 (0.41)]
# WIN, Finished in: 0.9065902233123779(seconds)
# Game: 2840, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1159/2839 (0.41)]
# WIN, Finished in: 0.999697208404541(seconds)
# Game: 2841, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1160/2840 (0.41)]
# WIN, Finished in: 0.8596622943878174(seconds)
# Game: 2842, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1161/2841 (0.41)]
# WIN, Finished in: 20.616195917129517(seconds)
# Game: 2843, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1162/2842 (0.41)]
# Game: 2844, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1162/2843 (0.41)]
# WIN, Finished in: 8.093584299087524(seconds)
# Game: 2845, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1163/2844 (0.41)]
# Game: 2846, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1163/2845 (0.41)]
# WIN, Finished in: 1.7342979907989502(seconds)
# Game: 2847, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1164/2846 (0.41)]
# WIN, Finished in: 0.9687261581420898(seconds)
# Game: 2848, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1165/2847 (0.41)]
# Game: 2849, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1165/2848 (0.41)]
# Game: 2850, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1165/2849 (0.41)]
# Game: 2851, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1165/2850 (0.41)]
# WIN, Finished in: 8.296629190444946(seconds)
# Game: 2852, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1166/2851 (0.41)]
# Game: 2853, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1166/2852 (0.41)]
# Game: 2854, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1166/2853 (0.41)]
# Game: 2855, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1166/2854 (0.41)]
# WIN, Finished in: 290.34365153312683(seconds)
# Game: 2856, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1167/2855 (0.41)]
# Game: 2857, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1167/2856 (0.41)]
# Game: 2858, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1167/2857 (0.41)]
# Game: 2859, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1167/2858 (0.41)]
# WIN, Finished in: 1.2189991474151611(seconds)
# Game: 2860, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2859 (0.41)]
# Game: 2861, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2860 (0.41)]
# Game: 2862, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2861 (0.41)]
# Game: 2863, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2862 (0.41)]
# Game: 2864, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2863 (0.41)]
# Game: 2865, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2864 (0.41)]
# Game: 2866, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2865 (0.41)]
# Game: 2867, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2866 (0.41)]
# Game: 2868, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2867 (0.41)]
# Game: 2869, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1168/2868 (0.41)]
# WIN, Finished in: 177.95217299461365(seconds)
# Game: 2870, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1169/2869 (0.41)]
# WIN, Finished in: 18.84374761581421(seconds)
# Game: 2871, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1170/2870 (0.41)]
# Game: 2872, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1170/2871 (0.41)]
# Game: 2873, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1170/2872 (0.41)]
# WIN, Finished in: 22.272751331329346(seconds)
# Game: 2874, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1171/2873 (0.41)]
# Game: 2875, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1171/2874 (0.41)]
# Game: 2876, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1171/2875 (0.41)]
# Game: 2877, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1171/2876 (0.41)]
# Game: 2878, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1171/2877 (0.41)]
# WIN, Finished in: 1.5319106578826904(seconds)
# Game: 2879, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1172/2878 (0.41)]
# WIN, Finished in: 0.8744940757751465(seconds)
# Game: 2880, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1173/2879 (0.41)]
# Game: 2881, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1173/2880 (0.41)]
# Game: 2882, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1173/2881 (0.41)]
# Game: 2883, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1173/2882 (0.41)]
# WIN, Finished in: 2.0158917903900146(seconds)
# Game: 2884, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1174/2883 (0.41)]
# WIN, Finished in: 0.8902685642242432(seconds)
# Game: 2885, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1175/2884 (0.41)]
# WIN, Finished in: 0.9065701961517334(seconds)
# Game: 2886, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1176/2885 (0.41)]
# Game: 2887, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1176/2886 (0.41)]
# Game: 2888, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1176/2887 (0.41)]
# WIN, Finished in: 0.921576738357544(seconds)
# Game: 2889, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1177/2888 (0.41)]
# Game: 2890, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1177/2889 (0.41)]
# WIN, Finished in: 11.687510251998901(seconds)
# Game: 2891, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1178/2890 (0.41)]
# Game: 2892, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1178/2891 (0.41)]
# WIN, Finished in: 0.85929274559021(seconds)
# Game: 2893, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1179/2892 (0.41)]
# Game: 2894, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1179/2893 (0.41)]
# Game: 2895, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1179/2894 (0.41)]
# Game: 2896, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1179/2895 (0.41)]
# Game: 2897, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1179/2896 (0.41)]
# WIN, Finished in: 0.765430212020874(seconds)
# Game: 2898, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1180/2897 (0.41)]
# Game: 2899, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1180/2898 (0.41)]
# WIN, Finished in: 51.23408484458923(seconds)
# Game: 2900, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1181/2899 (0.41)]
# WIN, Finished in: 0.765934944152832(seconds)
# Game: 2901, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1182/2900 (0.41)]
# WIN, Finished in: 0.9998874664306641(seconds)
# Game: 2902, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1183/2901 (0.41)]
# WIN, Finished in: 2.703080415725708(seconds)
# Game: 2903, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1184/2902 (0.41)]
# Game: 2904, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1184/2903 (0.41)]
# WIN, Finished in: 0.9383230209350586(seconds)
# Game: 2905, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1185/2904 (0.41)]
# Game: 2906, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1185/2905 (0.41)]
# WIN, Finished in: 290.7656388282776(seconds)
# Game: 2907, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1186/2906 (0.41)]
# Game: 2908, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1186/2907 (0.41)]
# WIN, Finished in: 254.29595589637756(seconds)
# Game: 2909, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1187/2908 (0.41)]
# Game: 2910, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1187/2909 (0.41)]
# Game: 2911, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1187/2910 (0.41)]
# Game: 2912, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1187/2911 (0.41)]
# Game: 2913, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1187/2912 (0.41)]
# Game: 2914, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1187/2913 (0.41)]
# Game: 2915, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1187/2914 (0.41)]
# Game: 2916, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1187/2915 (0.41)]
# WIN, Finished in: 290.51549005508423(seconds)
# Game: 2917, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1188/2916 (0.41)]
# Game: 2918, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1188/2917 (0.41)]
# Game: 2919, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1188/2918 (0.41)]
# Game: 2920, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1188/2919 (0.41)]
# Game: 2921, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1188/2920 (0.41)]
# Game: 2922, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1188/2921 (0.41)]
# WIN, Finished in: 1.3905844688415527(seconds)
# Game: 2923, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1189/2922 (0.41)]
# Game: 2924, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1189/2923 (0.41)]
# Game: 2925, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1189/2924 (0.41)]
# Game: 2926, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1189/2925 (0.41)]
# Game: 2927, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1189/2926 (0.41)]
# Game: 2928, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1189/2927 (0.41)]
# Game: 2929, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1189/2928 (0.41)]
# WIN, Finished in: 0.8122107982635498(seconds)
# Game: 2930, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1190/2929 (0.41)]
# WIN, Finished in: 12.953100204467773(seconds)
# Game: 2931, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1191/2930 (0.41)]
# Game: 2932, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1191/2931 (0.41)]
# WIN, Finished in: 0.7815225124359131(seconds)
# Game: 2933, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1192/2932 (0.41)]
# WIN, Finished in: 1.0309500694274902(seconds)
# Game: 2934, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1193/2933 (0.41)]
# WIN, Finished in: 0.8905901908874512(seconds)
# Game: 2935, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1194/2934 (0.41)]
# WIN, Finished in: 8.609378814697266(seconds)
# Game: 2936, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1195/2935 (0.41)]
# Game: 2937, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1195/2936 (0.41)]
# Game: 2938, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1195/2937 (0.41)]
# WIN, Finished in: 95.82811284065247(seconds)
# Game: 2939, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1196/2938 (0.41)]
# Game: 2940, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1196/2939 (0.41)]
# WIN, Finished in: 2.9686553478240967(seconds)
# Game: 2941, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1197/2940 (0.41)]
# Game: 2942, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1197/2941 (0.41)]
# WIN, Finished in: 270.00548338890076(seconds)
# Game: 2943, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1198/2942 (0.41)]
# Game: 2944, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1198/2943 (0.41)]
# Game: 2945, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1198/2944 (0.41)]
# Game: 2946, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1198/2945 (0.41)]
# WIN, Finished in: 1.9841220378875732(seconds)
# Game: 2947, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1199/2946 (0.41)]
# WIN, Finished in: 2.0168354511260986(seconds)
# Game: 2948, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1200/2947 (0.41)]
# WIN, Finished in: 11.577808380126953(seconds)
# Game: 2949, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1201/2948 (0.41)]
# WIN, Finished in: 25.75033736228943(seconds)
# Game: 2950, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1202/2949 (0.41)]
# WIN, Finished in: 112.71845650672913(seconds)
# Game: 2951, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1203/2950 (0.41)]
# Game: 2952, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1203/2951 (0.41)]
# WIN, Finished in: 240.8120527267456(seconds)
# Game: 2953, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1204/2952 (0.41)]
# Game: 2954, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1204/2953 (0.41)]
# Game: 2955, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1204/2954 (0.41)]
# Game: 2956, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1204/2955 (0.41)]
# WIN, Finished in: 6.2811644077301025(seconds)
# Game: 2957, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1205/2956 (0.41)]
# Game: 2958, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1205/2957 (0.41)]
# WIN, Finished in: 1.8748786449432373(seconds)
# Game: 2959, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1206/2958 (0.41)]
# WIN, Finished in: 209.37509846687317(seconds)
# Game: 2960, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1207/2959 (0.41)]
# WIN, Finished in: 0.9844095706939697(seconds)
# Game: 2961, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1208/2960 (0.41)]
# Game: 2962, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1208/2961 (0.41)]
# Game: 2963, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1208/2962 (0.41)]
# Game: 2964, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1208/2963 (0.41)]
# Game: 2965, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1208/2964 (0.41)]
# Game: 2966, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1208/2965 (0.41)]
# Game: 2967, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1208/2966 (0.41)]
# WIN, Finished in: 0.9221389293670654(seconds)
# Game: 2968, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1209/2967 (0.41)]
# Game: 2969, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1209/2968 (0.41)]
# Game: 2970, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1209/2969 (0.41)]
# WIN, Finished in: 1.2344563007354736(seconds)
# Game: 2971, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1210/2970 (0.41)]
# WIN, Finished in: 0.9220564365386963(seconds)
# Game: 2972, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1211/2971 (0.41)]
# Game: 2973, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1211/2972 (0.41)]
# Game: 2974, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1211/2973 (0.41)]
# WIN, Finished in: 1.0313193798065186(seconds)
# Game: 2975, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1212/2974 (0.41)]
# WIN, Finished in: 3.156162738800049(seconds)
# Game: 2976, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1213/2975 (0.41)]
# WIN, Finished in: 3.093791961669922(seconds)
# Game: 2977, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1214/2976 (0.41)]
# WIN, Finished in: 61.46909308433533(seconds)
# Game: 2978, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1215/2977 (0.41)]
# Game: 2979, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1215/2978 (0.41)]
# Game: 2980, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1215/2979 (0.41)]
# Game: 2981, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1215/2980 (0.41)]
# Game: 2982, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1215/2981 (0.41)]
# Game: 2983, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1215/2982 (0.41)]
# Game: 2984, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1215/2983 (0.41)]
# WIN, Finished in: 41.75044274330139(seconds)
# Game: 2985, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1216/2984 (0.41)]
# Game: 2986, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1216/2985 (0.41)]
# WIN, Finished in: 1.140669822692871(seconds)
# Game: 2987, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1217/2986 (0.41)]
# Game: 2988, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1217/2987 (0.41)]
# WIN, Finished in: 0.8901865482330322(seconds)
# Game: 2989, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1218/2988 (0.41)]
# Game: 2990, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1218/2989 (0.41)]
# Game: 2991, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1218/2990 (0.41)]
# Game: 2992, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1218/2991 (0.41)]
# Game: 2993, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1218/2992 (0.41)]
# Game: 2994, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1218/2993 (0.41)]
# Game: 2995, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1218/2994 (0.41)]
# Game: 2996, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1218/2995 (0.41)]
# Game: 2997, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1218/2996 (0.41)]
# WIN, Finished in: 1.4999780654907227(seconds)
# Game: 2998, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1219/2997 (0.41)]
# WIN, Finished in: 17.906779050827026(seconds)
# Game: 2999, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1220/2998 (0.41)]
# WIN, Finished in: 1.9845268726348877(seconds)
# Game: 3000, BoardSize: (16,30), TotalMines: 99 | Current Win [B: (0/-1) I: (0/-1) E: 1221/2999 (0.41)]
# ---------------Your agent's results:---------------
# Beginner: 0 	Intermediate: 0 	Expert: 1232
# Cumulative Score: 3696
#
# Process finished with exit code 0