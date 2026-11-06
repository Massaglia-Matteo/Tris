import random
 
ROSSO = "\033[31m"
BLU = "\033[34m"
EVIDENZIA = "\033[1;30;43m"
RESET = "\033[0m"
 
COMBINAZIONI = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)
 
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
 
 
def mappa(board, ultima=None):
    da_mostrare = []
 
    for i in range(len(board)):
        if board[i] == " ":
            da_mostrare.append(str(i))
        else:
            if i == ultima:
                colore = EVIDENZIA
            elif board[i] == "X":
                colore = ROSSO
            else:
                colore = BLU
            da_mostrare.append(colore + board[i] + RESET)
 
    print(f"\n {da_mostrare[0]} | {da_mostrare[1]} | {da_mostrare[2]} \n"
          "---+---+---\n"
          f" {da_mostrare[3]} | {da_mostrare[4]} | {da_mostrare[5]} \n"
          "---+---+---\n"
          f" {da_mostrare[6]} | {da_mostrare[7]} | {da_mostrare[8]} ")
 
 
def mossa_umana(board, simbolo):
    while True:
        n = input(f"Inserire la {simbolo}: ")
 
        if n.isdigit():
            n = int(n)
 
            if not (n < 0 or n > 8):
                if board[n] == " ":
                    board[n] = simbolo
                    return n
                else:
                    print("Lo spazio e gia occupato")
            else:
                print("Numero fuori intervallo (da 0 a 8)")
        else:
            print("NN e un numero")
 
 
def vincitore(board):
    for i in COMBINAZIONI:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[0]] != " ":
            return board[i[0]]
    return None
 
 
def controlla_pareggio(board):
    return " " not in board
 
 
def minimax(board, turno):
    v = vincitore(board)
 
    if v == "O":
        return 1
    if v == "X":
        return -1
    if controlla_pareggio(board):
        return 0
 
    if turno == "O":
        migliore = -2
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                valore = minimax(board, "X")
                board[i] = " "
                if valore > migliore:
                    migliore = valore
        return migliore
 
    else:
        migliore = 2
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                valore = minimax(board, "O")
                board[i] = " "
                if valore < migliore:
                    migliore = valore
        return migliore
 
 
def mossa_minimax(board, simbolo):
    if board.count(" ") == 9:
        scelta = random.choice(range(9))
        board[scelta] = simbolo
        return scelta
 
    migliore = -2
    mosse_migliori = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            valore = minimax(board, "X")
            board[i] = " "
            if valore > migliore:
                migliore = valore
                mosse_migliori = [i]
            elif valore == migliore:
                mosse_migliori.append(i)
    scelta = random.choice(mosse_migliori)
    board[scelta] = simbolo
    return scelta
 
 
turno = random.choice(["X", "O"])
print("Inizia:", turno)
ultima = None
 
while True:
 
    if turno == "X":
        mappa(board, ultima)
        ultima = mossa_umana(board, turno)
    else:
        ultima = mossa_minimax(board, turno)
 
    v = vincitore(board)
    if v:
        mappa(board, ultima)
        print(f"Ha vinto {v}")
        break
 
    if controlla_pareggio(board):
        mappa(board, ultima)
        print("Pareggio")
        break
 
    if turno == "X":
        turno = "O"
    else:
        turno = "X"
