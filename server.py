#!/usr/bin/python

import socket
import subprocess
import Tkinter

s = socket.socket()
host = "127.0.0.1"

port = input("port : ")

s.bind((host,port))

top = Tkinter.Tk()

s.listen(5)

def transfer():
	from tkFileDialog import askopenfilename
	Tkinter.Tk().withdraw()
	filename = askopenfilename()
	c.send('sendack')
	f = open(filename)
        data = f.readlines()
        length = len(data)
        #print length
	sizeHandler = open('size','w+')
	sendHandler = open('sent','w+')
	temp = str(length)
	sizeHandler.write(temp)
	subprocess.call('./g.sh',shell=True)
        for i in range(0,length):
                c.send(data[i])
        print "transfer done"
        c.send("()()()transfer ok")



while True:
	c, addr = s.accept()

	Transfer = Tkinter.Button(top, text =" Browse to send", command = transfer)
	Transfer.pack()
	top.mainloop()

#	f = open('rock.mp3')
#	data = f.readlines()
#	length = len(data)
#	print length
#	for i in range(0,length):
#		c.send(data[i])
#	print "transfer done"
#	c.send("transfer ok")
	c.close()
	
s.close()

