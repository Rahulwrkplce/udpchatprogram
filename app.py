import threading
import socket
import time

ip='192.168.43.251'
port=251                        #ip and port of the user system

si=socket.AF_INET   			#we needed the function in some variable si(socket ip)
sp=socket.SOCK_DGRAM			#we needed the function in some variable sp(socket protocol)

s=socket.socket(si, sp)			#we mad the socket here |  above defined functions are needed to be put in socket function of socket module and we keep all that function inside some other variable s


s.bind( (ip, port) )                    	# need to use another function on this socket | we're binding port with the socket | we do not need to put this one into a variable



#function for reveiving the message
def a():
	while True:
		x=s.recvfrom(1024)
		y=x[1][0]
		x=x[0].decode()
		print(ct,':',y,':',x)


#function for sending the message
def b():
	while True:
		txt=input('')
		s.sendto(txt.encode(),('192.168.43.62',62))         #ip and port of the destination system


#adding time
t=time.localtime()
ct=time.strftime('%H:%M:%S',t)

#using multithreading
x1 = threading.Thread(target=a)
x2 = threading.Thread(target=b)


x1.start()
x2.start()
