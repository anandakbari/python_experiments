import socket           
s = socket.socket()     
port = 3000         
s.connect(('127.0.0.1', port))
s.send(input("Enter candidate to vote for:").encode())
s.close()