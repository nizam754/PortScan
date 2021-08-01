#TesKill Port scanner
import socket

ip = socket.gethostbyname(socket.gethostname()) #You IP address

for port in range(65535): #All ports are in 0-65535
    try:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.bind((ip, port)) #bind port with your ip address

    except:
        print('[OPEN] Port Open :' ,port) #print port list
    serv.close() #close socket