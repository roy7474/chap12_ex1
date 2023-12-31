'''# Exercise 2: Change your socket program so that it counts the number of characters it has received
 and stops displaying any text after it has shown 3000 characters. The program should retrieve the 
 entire document and count the total number of characters and display the count of the number of characters at
 the end of the document.'''

# URLs for testing: 
# http://data.pr4e.org/romeo.txt 
# http://data.pr4e.org/mbox.txt
# http://data.pr4e.org/romeo-full.txt
# http://data.pr4e.org/mbox-short.txt
# http://data.pr4e.org/intro.txt


import socket
url = input('Please enter the URL of the website you would like to access: ')
count = 0
try:
    webp = url.split('/')
    HOST = webp[2]
    print('Host: ', HOST)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, 80))
    cmd = ('GET '+ url+ ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(500)
        for text in data:
            count +=1
        if len(data) < 1 or count >= 3000:
            break
        print(data.decode())#, end='')
    print('The total number of characters is: ', count)    
    mysock.close()
    


except:
    print('There was a problem opening this webpage. Please try again!')
