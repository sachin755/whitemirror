#/bin/usr/python

import socket
import subprocess
import Tkinter

s = socket.socket()

host = "192.168.0.101"

port = input("port : ")

top = Tkinter.Tk()

s.connect((host,port))
flag = 0
filename = ""
def accept():
	print "accepted"
	filename = Path.get("1.0","200.0")
	print filename
while True:
#	print s.recv(1024)
	def h():
                print "into h function "
		filename = Path.get("1.0","200.0")
	        print filename

	data = ""
	data = s.recv(1024)
	Accept = Tkinter.Button(top,text=" Accept file ",command=h)
	Path = Tkinter.Text(top)
	if data == "sendack":
		data = ""	
		print " 	Server has transfered a file 		"
		Accept.pack()
		Path.pack()
		#top.mainloop()
		
		filename = raw_input("Enter file name with path to recieve, eg (/home/user/abc.pdf : )\n")
	try:
		print " WYSIWYG : %s " % filename
		if filename == "":
			print "---- No filename -----"
		else:
			subprocess.call("touch "+filename,shell=True)
			f = open(filename,'a+')
		        f.write(data)
			if data == "":
				print " Stored Successfully"
	except Exception as e:
		print " Error occurred while storing the file : %s" % e

	if data == "transfer ok":
		print "Transfer successful"
		data = ""
		break
	#f = open(filename,'a+')
	#f.write(data)
#	if s.recv(1024) == "":
#		break
print "-- "
s.close()


