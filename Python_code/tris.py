import random
 
RESET = "\033[0m"
GRIGIO = "\033[90m"
ROSSO = "\033[1;31m"
BLU = "\033[1;34m"
CIANO = "\033[1;36m"
VERDE = "\033[1;32m"
GIALLO = "\033[1;33m"
SFONDO_ULTIMA = "\033[30;43m"
SFONDO_VITTORIA = "\033[30;42m"
 
COMBINAZIONI = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)
 
 
def pulisci():
    print("\033[2J\033[H", end="")
 
 
def cella(board, i, ultima, vincente):
    if board[i] == " ":
        return GRIGIO + f" {i} " + RESET
 
    if board[i] == "X":
        colore = ROSSO
    else:
        colore = BLU
 
    if i in vincente:
        colore = SFONDO_VITTORIA
    elif i == ultima:
        colore = SFONDO_ULTIMA
 
    return colore + f" {board[i]} " + RESET
 
 
def schermata(board, messaggio="", ultima=None, vincente=()):
    c = [cella(board, i, ultima, vincente) for i in range(9)]
 
    pulisci()
    print()
    print(CIANO + "  ╔═══════════════╗" + RESET)
    print(CIANO + "  ║" + RESET + "   T R I S     " + CIANO + "║" + RESET)
    print(CIANO + "  ╚═══════════════╝" + RESET)
    print(f"   Tu: {ROSSO}X{RESET}      PC: {BLU}O{RESET}")
    print()
    print("     ┌───┬───┬───┐")
    print(f"     │{c[0]}│{c[1]}│{c[2]}│")
    print("     ├───┼───┼───┤")
    print(f"     │{c[3]}│{c[4]}│{c[5]}│")
    print("     ├───┼───┼───┤")
    print(f"     │{c[6]}│{c[7]}│{c[8]}│")
    print("     └───┴───┴───┘")
    print()
    if messaggio:
        print("  " + messaggio)
        print()
 
 
def mossa_umana(board, simbolo):
    while True:
        n = input(f"  Scegli una cella per la {simbolo} (0-8): ")
 
        if n.isdigit():
            n = int(n)
 
            if not (n < 0 or n > 8):
                if board[n] == " ":
                    board[n] = simbolo
                    return n
                else:
                    print(f"  {GIALLO}Cella gia occupata{RESET}")
            else:
                print(f"  {GIALLO}Numero fuori intervallo (da 0 a 8){RESET}")
        else:
            print(f"  {GIALLO}Inserisci un numero{RESET}")
 
 
def vincitore(board):
    for i in COMBINAZIONI:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[0]] != " ":
            return board[i[0]]
    return None
 
 
def combinazione_vincente(board):
    for i in COMBINAZIONI:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[0]] != " ":
            return i
    return ()
 
 
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
 
 
def partita():
    board = [" "] * 9
    turno = random.choice(["X", "O"])
    ultima = None
 
    if turno == "X":
        messaggio = f"{VERDE}Inizi tu!{RESET}"
    else:
        messaggio = f"{BLU}Inizia il PC...{RESET}"
 
    while True:
 
        if turno == "X":
            schermata(board, messaggio, ultima)
            ultima = mossa_umana(board, turno)
            messaggio = ""
        else:
            ultima = mossa_minimax(board, turno)
            messaggio = f"Il PC ha giocato in {BLU}{ultima}{RESET}"
 
        v = vincitore(board)
        if v:
            if v == "X":
                esito = f"{VERDE}Hai vinto!{RESET}"
            else:
                esito = f"{BLU}Ha vinto il PC{RESET}"
            schermata(board, esito, ultima, combinazione_vincente(board))
            return
 
        if controlla_pareggio(board):
            schermata(board, f"{GIALLO}Pareggio{RESET}", ultima)
            return
 
        if turno == "X":
            turno = "O"
        else:
            turno = "X"
 
 
while True:
    partita()
    risposta = input("  Giocare ancora? (s/n): ").strip().lower()
    if risposta != "s":
        break
 
