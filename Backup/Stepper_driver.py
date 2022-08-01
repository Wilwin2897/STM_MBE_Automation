import socket
import tkinter as tk
from tkinter import *
HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8090  # Arbitrary non-privileged port

# Socket connection is a three step process - create, bind and connect
# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Following routines are defined to handle button events from the GUI
#First routine handles Initialize button event; creates and binds the socket 
def initialize(event):
	entry1.insert (0,'Socket created')
	
	try:
	   s.bind((HOST, PORT))
	except socket.error as msg:
	   entry1.insert ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + str(msg[1]))
	   sys.exit()
   
	entry1.insert(END,' Socket bind complete')
	print('Socket bind complete')
	print(s.getsockname())

#Second routine handles Connect button event; connects the ESP13 shield to the socket
#and prints out the IP address of the ESP13 shield	
def connect(event):
	global conn	
	entry2.insert(0,'Socket now listening')
	s.listen()
	conn, addr = s.accept()
	connection = 'Connected with ' + addr[0] + ':' + str(addr[1])
	print('connection ',addr)
	entry2.delete(0,tk.END)
	entry2.insert(0,connection)
	print('connect complete')
	
#Third routine handles Send button event; send the contents of the entry dialog to Arduino
#via ESP13 shield and gets the return message and populates the entry dialog box with the return
#message
def send(event):
	data = entry3.get()
	conn.send(data.encode('utf-8'))
	print('send',data)
	data1 = conn.recv(70)
	entry4.delete(0,tk.END)
	entry4.insert(0,data1)
	
#Fourth routine handles LED Update button event; sends the value of the LED brightness slider
#(+ the arbitary header)to the ESP13
#Reads the return message and updates the potentiometer slider. Dont forget the string to integer conversion
def update(event):
	data = '12#$'
	data = data + str(slider2.get())
	print(data)
	conn.send(data.encode('utf-8'))
	data1 = conn.recv(70)
	slider1.set(int(data1))
	print(data1)
	print('Update LED')

#Final routine handles the Exit button; closes the socket, closes the GUI and exits program
def exit(event):
	s.close()
	print('exit')
	window.destroy()

#All below is tkinter programming to create the GUI. Main window contains two frames, one for entry dialog and sliders
#second for buttons
window = tk.Tk()
window.title("ESP13 Communication")

frame1 = tk.Frame(master=window,relief=tk.FLAT,	borderwidth=5)
frame1.pack()
frame2 = tk.Frame(master=window,relief=tk.FLAT,	borderwidth=5)
frame2.pack()

label1 = tk.Label(master=frame1,text="Socket Ready",fg="black",width = 25,height = 2)
label1.grid(row=0,column=0,padx=20,pady=20,sticky="w")

entry1 = tk.Entry(master=frame1,fg="black",bg="white",width=75)
entry1.grid(row=0,column=1,padx=10,pady=10)

label2 = tk.Label(master=frame1,text="Socket Connected",fg="black",width = 25,height = 2)
label2.grid(row=1,column=0,padx=20,pady=20,sticky="w")

entry2 = tk.Entry(master=frame1,fg="black",bg="white",width=75)
entry2.grid(row=1,column=1,padx=10,pady=10)

label3 = tk.Label(master=frame1,text="Message to send",fg="black",width = 25,height = 2)
label3.grid(row=2,column=0,padx=20,pady=20,sticky="w")

entry3 = tk.Entry(master=frame1,fg="black",bg="white",width=75)
entry3.grid(row=2,column=1,padx=10,pady=10)
entry3.bind("<Return>",send)

label4 = tk.Label(master=frame1,text="Message recieved",fg="black",width = 25,height = 2)
label4.grid(row=3,column=0,padx=20,pady=20,sticky="w")

entry4 = tk.Entry(master=frame1,fg="black",bg="white",width=75)
entry4.grid(row=3,column=1,padx=10,pady=10)

label5 = tk.Label(master=frame1,text="Analog Input",fg="black",width = 25,height = 2)
label5.grid(row=4,column=0,padx=20,pady=20,sticky="w")

slider1 = Scale(frame1, from_=0, to=1023, length=600, orient=HORIZONTAL)
slider1.grid(row=4,column=1,padx=10,pady=10)

label6 = tk.Label(master=frame1,text="LED Brightness",fg="black",width = 25,height = 2)
label6.grid(row=5,column=0,padx=20,pady=20,sticky="w")

slider2 = Scale(frame1, from_=0, to=255, length=600, orient=HORIZONTAL)
slider2.grid(row=5,column=1,padx=10,pady=10)

button1 = tk.Button(master=frame2,text="Initialize",width=10,height=2,relief=tk.RAISED,fg="black")
button1.grid(row=0,column=0,padx=20,pady=20)
button1.bind("<Button-1>",initialize)

button2 = tk.Button(master=frame2,text="Connect",width=10,height=2,relief=tk.RAISED,fg="black")
button2.grid(row=0,column=1,padx=20,pady=20)
button2.bind("<Button-1>",connect)

button3 = tk.Button(master=frame2,text="Send",width=10,height=2,relief=tk.RAISED,fg="black")
button3.grid(row=0,column=2,padx=20,pady=20)
button3.bind("<Button-1>",send)

button4 = tk.Button(master=frame2,text="LED Update",width=10,height=2,relief=tk.RAISED,fg="black")
button4.grid(row=0,column=3,padx=20,pady=20)
button4.bind("<Button-1>",update)

button5 = tk.Button(master=frame2,text="Exit",width=10,height=2,relief=tk.RAISED,fg="black")
button5.grid(row=0,column=4,padx=20,pady=20)
button5.bind("<Button-1>",exit)

window.mainloop()
print('Program ended')