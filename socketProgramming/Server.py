import socket
import datetime as dt
import threading
import Verify as av

# Select an appropriate port number. 
PORT = 65432
# Set The Server's IP Address
SERVER_IP = '127.0.0.1'
# Set up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

# Add code to initialize the socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Write Code to bind Address to the server socket.
server.bind(ADDR)



# This function processes messages that are read through the Socket.
def clientHandler(conn, addr): 
    # Write Code that allows the Server to receive a connection code from an Agent. 
    connCode = conn.recv(1024).decode()

    # Write Code that allows the Server to check if the connection code received is valid. 
    agentCheck = av.check_conn_codes(connCode)
    
    

    # Write Code that allows the Server to retrieve a random secret question.
    question = av.getSecretQuestion()

    # Write Code that allows the Server to send the random secret question to the Client.
    
    if agentCheck == -1:
        conn.send("Invalid Connection Code".encode(FORMAT))
    else:
        conn.send(question[0].encode(FORMAT))

        # Write Code that allows the Server to receive an answer from the Client.
        answer = conn.recv(1024).decode()

        # Write Code that allows the Server to check if the answer received is correct.
        answerCheck = False
        if answer == question[1]:
            answerCheck = True

        # Write Code that allows the Server to Send Welcome message to agent -> "Welcome Agent X" 
        if answerCheck:
            now = dt.datetime.now()
            welcome = "Welcome " + agentCheck + " Time Logged " + now.strftime("%Y-%m-%d %H:%M:%S")
            conn.send(welcome.encode(FORMAT))
        else:
            conn.send("Invalid Answer".encode(FORMAT))

def runServer():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=clientHandler, args=(conn,addr) )
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")

print("[STRTING] The Server is Starting...")
runServer()