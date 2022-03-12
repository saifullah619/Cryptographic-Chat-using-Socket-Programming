import socket

# Select an appropriate port number. 
PORT = 65432  
# Set The Server's IP Address
SERVER_IP = '127.0.0.1'
# Set up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

# Add code to initialize the Socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Write Code that will allow the Client (Agent) to send messages to the server. The Function accepts the message as a String (msg) and sends that message to the Server through a connection established.
def send(msg):
    client.send(msg.encode(FORMAT))

# Write code to Prompts the Agent to enter their connection code and returns the code given.
def getConCode():
    return input("Enter the connection code: ")

# Write code to Prompts the Agent to enter an answer and returns the answer given.
def getAnswer(question):
    return input('Answer: ')

# Get Connection Code.
connCode = getConCode()


# Send Connection Code to Server.
send(connCode)

# Recive question from server.
question = client.recv(1024).decode()

# Get Answer from Agent.
print(question)

if question!="Invalid Connection Code":
    answer = getAnswer(question)
    # Send Answer to Server.
    send(answer)

    # Recive and print response from the server.
    response = client.recv(1024).decode()
    print(response)
    
client.close()

