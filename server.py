import socket   
a, b, n = 0, 0, 0   
s = socket.socket()     
print ("Socket successfully created")
port = 3000         
s.bind(('', port))      
print ("socket binded to %s" %(port))
s.listen(5) 
print ("socket is listening")       
while n!=5:
    c, addr = s.accept()    
    data = c.recv(1024).decode()
    if data.strip() == 'A':
      a += 1
    elif data.strip() == 'B':
      b += 1
    else:
       print("Invalid vote!")
    print ('Recieved vote from', addr)
    c.send('Thank you for voting'.encode())
    c.close()
    n += 1
s.close()
if a > b:
   print("Candidate A won with no. of votes = " + str(a))
elif a < b:
   print("Candidate B won with no. of votes = " + str(b))
else:
   print("Tie!")