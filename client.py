import socket

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def client_program():
    host = '10.102.232.59'
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        board = client_socket.recv(1024).decode()
        print_board(board)
        move = input("Enter your move (0-8): ")
        client_socket.sendall(move.encode())
        result = client_socket.recv(1024).decode()
        if "wins" in result:
            print(result)
            break

    client_socket.close()

if __name__ == '__main__':
    client_program()