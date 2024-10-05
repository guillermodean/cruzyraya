import socket

def create_board():
    return [' ' for _ in range(9)]

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def server_program():
    host = '10.102.232.90'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print(f"Connection from: {address}")

    board = create_board()
    current_player = 'X'

    while True:
        print_board(board)
        conn.sendall(''.join(board).encode())
        move = conn.recv(1024).decode()
        if not move:
            break
        board[int(move)] = current_player
        if check_winner(board, current_player):
            conn.sendall(f"Player {current_player} wins!".encode())
            break
        current_player = 'O' if current_player == 'X' else 'X'

    conn.close()

if __name__ == '__main__':
    server_program()
