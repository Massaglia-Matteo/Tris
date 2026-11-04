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


def mossa_umana(board):
    while True:
        
        n = input("Inserire la X: ")

            
        if n.isdigit() == True:
            n = int(n)

            if not (n<0 or n>8):

                if board[n] == " ":
                    board[n] = "X"
                    break
                else:
                    print("Lo spazio e gia occupato")

            else:
                print("Numero nn accettato (inserire i numeri nella mappa a schermo)")

        else:
            print("NN e un numero")
