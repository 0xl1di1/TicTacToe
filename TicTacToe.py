# Initialisation du tableau de jeu
board = [[' ' for _ in range(3)] for _ in range(3)]

# Demander les noms des joueurs
player1_name = input("Entrez le nom du joueur 1 (X): ")
player2_name = input("Entrez le nom du joueur 2 (O): ")

# Fonction pour afficher le tableau de jeu
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Fonction pour obtenir le mouvement du joueur
def get_player_move(player, player_name):
    while True:
        try:
            row = int(input(f"{player_name} ({player}), entrez la ligne (0, 1, 2): "))
            col = int(input(f"{player_name} ({player}), entrez la colonne (0, 1, 2): "))
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cette case est déjà occupée. Essayez à nouveau.")
        except (ValueError, IndexError):
            print("Entrée invalide. Essayez à nouveau.")

# Fonction pour vérifier si un joueur a gagné
def check_win(board, player):
    # Vérifier les lignes
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Vérifier les colonnes
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Vérifier les diagonales
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Fonction pour jouer le jeu
def play_game():
    current_player = 'X'
    player_names = {
        'X': player1_name,
        'O': player2_name
    }
    for _ in range(9):  # Il y a au maximum 9 tours dans un jeu de Tic-Tac-Toe
        print_board(board)
        row, col = get_player_move(current_player, player_names[current_player])
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"{player_names[current_player]} ({current_player}) a gagné !")
            return
        current_player = 'O' if current_player == 'X' else 'X'
    print_board(board)
    print("Match nul !")

# Démarrer le jeu
play_game()