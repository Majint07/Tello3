#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time
#import tello
#t = telloend
import time
def FormatAngel(sides):
    rotateangel = (round(360 / sides))
    #xmsg = 'cw %d', rotateangel
    xmsg = 'cw {}'.format(rotateangel)
    xmsg = xmsg.encode(encoding="utf-8")
    print(xmsg)


def start(sent):
    xmsg = 'command'
    xmsg = xmsg.encode(encoding="utf-8")
    sent.sendto(xmsg, tello_address)
    print(xmsg)

    time.sleep(4)

    xmsg = 'takeoff'
    xmsg = xmsg.encode(encoding="utf-8")
    sent.sendto(xmsg, tello_address)
    print(xmsg)

    time.sleep(6)

    xmsg = 'back 30 '
    xmsg = xmsg.encode(encoding="utf-8")
    sent.sendto(xmsg, tello_address)
    print(xmsg)

    time.sleep(4)

    xmsg = 'cw 90'
    xmsg = xmsg.encode(encoding="utf-8")
    sent.sendto(xmsg, tello_address)
    print(xmsg)

def fly_polly(sides, sent):
    for s in range (sides):
        #t.forward(150)
        #msg = msg.encode(encoding="utf-8")

        xmsg = 'forward 21'
        xmsg = xmsg.encode(encoding="utf-8")
        sent.sendto(xmsg, tello_address)
        print(xmsg)
        time.sleep(4)


        #xmsg = 'cw 120'
       # xmsg = xmsg.encode(encoding="utf-8")
      #  sent.sendto(xmsg, tello_address)
       # print(xmsg)
        #time.sleep(4)

        rotateangel = (round(360/sides))
        xmsg = 'cw {}'.format(rotateangel)
        xmsg = xmsg.encode(encoding="utf-8")
        sent.sendto(xmsg, tello_address)
        time.sleep(4)

host = ''
port = 8889 #9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')
print ('start -- Misha dron command. start command\r\n')
print ('poly -- Misha dron custom command.\r\n')

print ('end -- quit demo.\r\n')

#FormatAngel(3)



#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 

    try:
        msg = input("");

        if not msg:
            break

        if 'start' in msg:
            start(sock)
            break

        if 'poly' in msg:
            fly_polly(3, sock)
            break
        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
        print(msg)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break




