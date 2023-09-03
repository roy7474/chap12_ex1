'''# Exercise 2: Change your socket program so that it counts the number of characters it has received
 and stops displaying any text after it has shown 3000 characters. The program should retrieve the 
 entire document and count the total number of characters and display the count of the number of characters at
 the end of the document.'''

import socket

url = input('Please enter the URL of the website you would like to access: ')
# url    http://data.pr4e.org/romeo.txt

try:
    host = url.split('/')[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    mysock.send('GET ', url, 'HTTP/1.0\n\n')

except:
    print('There was a problem opening this webpage. Please try again!')
    quit()

while True:
    data = sock.recv(3000)
    if len(data) < 1:
        break
    print(data)

mysock.close()