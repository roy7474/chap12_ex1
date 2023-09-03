''' 
Exercise 1: 
Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
You can use split('/') to break the URL into its component parts so you can extract the host name 
for the socket connect call. 
dAdd error checking using try and except to handle the condition where 
the user enters an improperly formatted or non-existent URL.”

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
'''




import socket
url = input('Please enter the URL of the website you would like to access: ')
try:
    webp = url.split('/')
    HOST = webp[2]
    print('Host: ', HOST)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, 80))
    cmd = ('GET ', url, ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode(), end='')
    mysock.close()

except:
    print('There was a problem opening this webpage. Please try again!')
