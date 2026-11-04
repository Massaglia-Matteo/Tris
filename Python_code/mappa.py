#mappa del tris

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def mappa(board):

    da_mostrare = []

    for i in range(len(board)):
        if board[i] == " ":
            da_mostrare.append(str(i))
        else:
            da_mostrare.append(board[i])
          
    print(f" {da_mostrare[0]} | {da_mostrare[1]} | {da_mostrare[2]} \n"
          "---+---+---\n"
          f" {da_mostrare[3]} | {da_mostrare[4]} | {da_mostrare[5]} \n"
          "---+---+---\n"
          f" {da_mostrare[6]} | {da_mostrare[7]} | {da_mostrare[8]} ")


def mossa_umana(board, simbolo):
    while True:
        
        n = input(f"Inserire la {simbolo}: ")

            
        if n.isdigit() == True:
            n = int(n)

            if not (n<0 or n>8):

                if board[n] == " ":
                    board[n] = simbolo
                    break
                else:
                    print("Lo spazio e gia occupato")

            else:
                print("Numero nn accettato (inserire i numeri nella mappa a schermo)")

        else:
            print("NN e un numero")

def controlla_vittoria(board):

    COMBINAZIONI = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )

    for i in COMBINAZIONI:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[0]] != " ":
            return True
    return False

def controlla_pareggio(board):
    return " " not in board

while True:
        mappa(board)
        mossa_umana(board,"X")
        if controlla_vittoria(board):
            mappa(board)
            print("Ha vinto X")
            break
        if controlla_pareggio(board):
            mappa(board)
            print("Pareggio")
            break
        mappa(board)
        mossa_umana(board,"O")
        if controlla_vittoria(board):
            mappa(board)
            print("Ha vinto O")
            break
        if controlla_pareggio(board):
            mappa(board)
            print("Pareggio")
            break
