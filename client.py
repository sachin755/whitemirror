#/bin/usr/python

import socket
import subprocess
import Tkinter

s = socket.socket()

host = "127.0.0.1"

port = input("port : ")


s.connect((host,port))
flag = 0
filename = ""
def accept():
	print "accepted"
	print filename
while True:
#	print s.recv(1024)
	def h():
                print "into h function "
	        print filename

	data = ""
	data = s.recv(1024)
	if data == "sendack":
		data = ""	
		print " 	Server has transfered a file 		"
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


